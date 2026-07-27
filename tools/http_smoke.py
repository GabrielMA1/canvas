#!/usr/bin/env python3
"""HTTP smoke crawl for a locally served RielArt build.

This standard-library check complements ``site_audit.py`` by confirming that
deployable routes can be requested through an actual static server.
"""

from __future__ import annotations

import argparse
import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlsplit
from urllib.request import Request, urlopen
from xml.etree import ElementTree


EXTRA_ROUTES = (
    "/404.html",
    "/privacy-policy.html",
    "/terms.html",
    "/packages/",
    "/robots.txt",
    "/sitemap.xml",
)
MISSING_ROUTE = "/audit-check-this-route-should-not-exist/"
DEFAULT_BUDGETS = {
    "html_per_route": 60 * 1024,
    "css_total": 65 * 1024,
    "javascript_total": 20 * 1024,
    "image_library": 650 * 1024,
    "logo": 10 * 1024,
}
IMAGE_SUFFIXES = {".gif", ".ico", ".jpeg", ".jpg", ".png", ".svg", ".webp"}


class HtmlSummaryParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.h1_count = 0
        self.title_count = 0
        self.canonical_count = 0

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        values = {name.lower(): value or "" for name, value in attrs}
        if tag.lower() == "h1":
            self.h1_count += 1
        elif tag.lower() == "title":
            self.title_count += 1
        elif tag.lower() == "link":
            rel = {token.lower() for token in values.get("rel", "").split()}
            if "canonical" in rel:
                self.canonical_count += 1


def sitemap_routes(path: Path) -> list[str]:
    root = ElementTree.parse(path).getroot()
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    routes: list[str] = []
    for node in root.findall("sm:url/sm:loc", namespace):
        if node.text:
            routes.append(urlsplit(node.text.strip()).path or "/")
    return routes


def fetch(url: str, timeout: float) -> tuple[int, str, bytes]:
    request = Request(url, headers={"User-Agent": "RielArt-local-audit/1.0"})
    try:
        with urlopen(request, timeout=timeout) as response:
            return (
                response.status,
                response.headers.get("Content-Type", ""),
                response.read(),
            )
    except HTTPError as error:
        return (
            error.code,
            error.headers.get("Content-Type", ""),
            error.read(),
        )


def main() -> int:
    parser = argparse.ArgumentParser(description="Crawl a locally served RielArt build.")
    parser.add_argument(
        "--base-url",
        default="http://127.0.0.1:4173/",
        help="Local static-server origin (default: %(default)s)",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Site root containing sitemap.xml.",
    )
    parser.add_argument("--timeout", type=float, default=8.0)
    parser.add_argument("--json-output", type=Path)
    parser.add_argument(
        "--max-html-bytes",
        type=int,
        default=DEFAULT_BUDGETS["html_per_route"],
        help="Maximum raw bytes for one HTML response (default: %(default)s)",
    )
    parser.add_argument(
        "--max-css-bytes",
        type=int,
        default=DEFAULT_BUDGETS["css_total"],
        help="Maximum raw bytes across local CSS files (default: %(default)s)",
    )
    parser.add_argument(
        "--max-js-bytes",
        type=int,
        default=DEFAULT_BUDGETS["javascript_total"],
        help="Maximum raw bytes across local JavaScript files (default: %(default)s)",
    )
    parser.add_argument(
        "--max-image-bytes",
        type=int,
        default=DEFAULT_BUDGETS["image_library"],
        help="Maximum raw bytes across the local image library (default: %(default)s)",
    )
    parser.add_argument(
        "--max-logo-bytes",
        type=int,
        default=DEFAULT_BUDGETS["logo"],
        help="Maximum raw bytes for images/logo.png (default: %(default)s)",
    )
    args = parser.parse_args()

    base_url = args.base_url.rstrip("/") + "/"
    routes = list(dict.fromkeys([*sitemap_routes(args.root / "sitemap.xml"), *EXTRA_ROUTES]))
    results: list[dict[str, object]] = []
    failures: list[str] = []

    for route in [*routes, MISSING_ROUTE]:
        url = urljoin(base_url, route.lstrip("/"))
        try:
            status, content_type, body = fetch(url, args.timeout)
        except (URLError, TimeoutError, OSError) as error:
            failures.append(f"{route}: request failed: {error}")
            results.append({"route": route, "error": str(error)})
            continue

        expected_status = 404 if route == MISSING_ROUTE else 200
        result: dict[str, object] = {
            "route": route,
            "status": status,
            "bytes": len(body),
            "content_type": content_type,
        }
        if status != expected_status:
            failures.append(f"{route}: HTTP {status}; expected {expected_status}")

        if status == 200 and "text/html" in content_type.lower():
            html_parser = HtmlSummaryParser()
            html_parser.feed(body.decode("utf-8", errors="replace"))
            result.update(
                {
                    "h1_count": html_parser.h1_count,
                    "title_count": html_parser.title_count,
                    "canonical_count": html_parser.canonical_count,
                }
            )
            if route not in {"/privacy-policy.html", "/terms.html", "/packages/"}:
                if html_parser.h1_count != 1:
                    failures.append(
                        f"{route}: expected one H1, found {html_parser.h1_count}"
                    )
                if html_parser.title_count != 1:
                    failures.append(
                        f"{route}: expected one title, found {html_parser.title_count}"
                    )
                if html_parser.canonical_count != 1:
                    failures.append(
                        f"{route}: expected one canonical, found "
                        f"{html_parser.canonical_count}"
                    )
                if len(body) > args.max_html_bytes:
                    failures.append(
                        f"{route}: {len(body)} HTML bytes exceed the "
                        f"{args.max_html_bytes}-byte budget"
                    )
        results.append(result)

    css_bytes = sum(
        path.stat().st_size for path in (args.root / "assets" / "css").rglob("*.css")
    )
    javascript_bytes = sum(
        path.stat().st_size for path in (args.root / "assets" / "js").rglob("*.js")
    )
    image_bytes = sum(
        path.stat().st_size
        for path in (args.root / "images").rglob("*")
        if path.is_file() and path.suffix.lower() in IMAGE_SUFFIXES
    )
    logo_bytes = (args.root / "images" / "logo.png").stat().st_size
    performance_budgets = {
        "html_per_route_bytes": args.max_html_bytes,
        "css": {"actual": css_bytes, "maximum": args.max_css_bytes},
        "javascript": {
            "actual": javascript_bytes,
            "maximum": args.max_js_bytes,
        },
        "image_library": {
            "actual": image_bytes,
            "maximum": args.max_image_bytes,
        },
        "logo": {"actual": logo_bytes, "maximum": args.max_logo_bytes},
    }

    for label, actual, maximum in (
        ("CSS", css_bytes, args.max_css_bytes),
        ("JavaScript", javascript_bytes, args.max_js_bytes),
        ("Image library", image_bytes, args.max_image_bytes),
        ("Logo", logo_bytes, args.max_logo_bytes),
    ):
        if actual > maximum:
            failures.append(
                f"{label}: {actual} bytes exceed the {maximum}-byte budget"
            )

    successful = [item for item in results if item.get("status") == 200]
    html_results = [
        item for item in successful if "text/html" in str(item.get("content_type", "")).lower()
    ]
    summary = {
        "base_url": base_url,
        "routes_checked": len(results),
        "successful_200_routes": len(successful),
        "html_routes": len(html_results),
        "html_bytes": sum(int(item.get("bytes", 0)) for item in html_results),
        "performance_budgets": performance_budgets,
        "failures": failures,
        "results": results,
    }

    print("RielArt local HTTP smoke crawl")
    print("==============================")
    print(f"Routes checked: {summary['routes_checked']}")
    print(f"Successful HTTP 200 routes: {summary['successful_200_routes']}")
    print(f"HTML routes: {summary['html_routes']}")
    print(f"HTML response bytes: {summary['html_bytes']}")
    print(
        "Performance budgets: "
        f"HTML <= {args.max_html_bytes}/route; "
        f"CSS {css_bytes}/{args.max_css_bytes}; "
        f"JS {javascript_bytes}/{args.max_js_bytes}; "
        f"images {image_bytes}/{args.max_image_bytes}; "
        f"logo {logo_bytes}/{args.max_logo_bytes}"
    )
    print(f"Failures: {len(failures)}")
    for failure in failures:
        print(f"- {failure}")

    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(
            json.dumps(summary, indent=2) + "\n", encoding="utf-8"
        )

    return 1 if failures else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ElementTree.ParseError as error:
        print(f"Could not parse sitemap.xml: {error}", file=sys.stderr)
        raise SystemExit(2)
