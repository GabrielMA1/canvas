#!/usr/bin/env python3
"""Static quality checks for the RielArt marketing site.

The script uses only the Python standard library. It is a local QA tool and is
not required for deployment.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree


SITE_ORIGIN = "https://rielart.com"
LOCAL_HOSTS = {"rielart.com", "www.rielart.com"}
PORTAL_URL = "https://portal.rielart.com"
FORMSPREE_URL = "https://formspree.io/f/xojrdoel"
EXPECTED_STRIPE_URLS = {
    "https://buy.stripe.com/8x25kvbsKcKF6M2gYqfw400",
    "https://buy.stripe.com/dRm00b9kC5id6M29vYfw401",
    "https://buy.stripe.com/bJe14f54m11Xc6mdMefw402",
    "https://buy.stripe.com/7sYbIT0O64e95HYfUmfw403",
    "https://buy.stripe.com/14A5kv9kCh0Vb2igYqfw404",
    "https://buy.stripe.com/5kQ6oz2WefWRgmCfUmfw405",
}
FORBIDDEN_COMPETITOR_TOKEN = "brand" + "vm"
TEXT_EXTENSIONS = {
    ".css",
    ".html",
    ".js",
    ".json",
    ".md",
    ".txt",
    ".xml",
}
IGNORED_DIRECTORIES = {".git", "node_modules", "__pycache__"}


@dataclass(frozen=True)
class Anchor:
    href: str
    target: str
    rel: frozenset[str]
    line: int


@dataclass
class Page:
    path: Path
    title: str = ""
    description: str = ""
    canonical: str = ""
    robots: str = ""
    h1_text: list[str] = field(default_factory=list)
    ids: list[tuple[str, int]] = field(default_factory=list)
    images_without_alt: list[int] = field(default_factory=list)
    anchors: list[Anchor] = field(default_factory=list)

    @property
    def indexable(self) -> bool:
        return "noindex" not in {
            token.strip().lower()
            for token in re.split(r"[\s,]+", self.robots)
            if token.strip()
        }


class PageParser(HTMLParser):
    def __init__(self, path: Path) -> None:
        super().__init__(convert_charrefs=True)
        self.page = Page(path=path)
        self._title_depth = 0
        self._title_parts: list[str] = []
        self._h1_depth = 0
        self._h1_parts: list[str] = []

    @staticmethod
    def _attrs(attrs: list[tuple[str, str | None]]) -> dict[str, str]:
        return {name.lower(): value or "" for name, value in attrs}

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        tag = tag.lower()
        values = self._attrs(attrs)
        line, _ = self.getpos()

        element_id = values.get("id")
        if element_id:
            self.page.ids.append((element_id, line))

        if tag == "title":
            self._title_depth += 1
        elif tag == "h1":
            self._h1_depth += 1
            self._h1_parts = []
        elif tag == "meta":
            name = values.get("name", "").lower()
            if name == "description":
                self.page.description = values.get("content", "").strip()
            elif name == "robots":
                self.page.robots = values.get("content", "").strip()
        elif tag == "link":
            rel = {
                token.lower() for token in values.get("rel", "").split() if token
            }
            if "canonical" in rel:
                self.page.canonical = values.get("href", "").strip()
        elif tag == "img":
            if "alt" not in values:
                self.page.images_without_alt.append(line)
        elif tag == "a":
            href = values.get("href", "").strip()
            if href:
                self.page.anchors.append(
                    Anchor(
                        href=href,
                        target=values.get("target", "").lower(),
                        rel=frozenset(
                            token.lower()
                            for token in values.get("rel", "").split()
                            if token
                        ),
                        line=line,
                    )
                )

    def handle_startendtag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title" and self._title_depth:
            self._title_depth -= 1
            if not self._title_depth:
                self.page.title = normalize_text("".join(self._title_parts))
        elif tag == "h1" and self._h1_depth:
            self._h1_depth -= 1
            if not self._h1_depth:
                self.page.h1_text.append(normalize_text("".join(self._h1_parts)))

    def handle_data(self, data: str) -> None:
        if self._title_depth:
            self._title_parts.append(data)
        if self._h1_depth:
            self._h1_parts.append(data)


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def iter_files(root: Path, extensions: set[str] | None = None) -> Iterable[Path]:
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in IGNORED_DIRECTORIES for part in path.relative_to(root).parts):
            continue
        if extensions is None or path.suffix.lower() in extensions:
            yield path


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def parse_page(path: Path) -> Page:
    parser = PageParser(path)
    parser.feed(read_text(path))
    parser.close()
    return parser.page


def route_file(root: Path, url_path: str) -> Path | None:
    decoded = unquote(url_path or "/").replace("\\", "/")
    relative = decoded.lstrip("/")
    candidate = root / relative

    candidates: list[Path] = []
    if not relative:
        candidates.append(root / "index.html")
    elif decoded.endswith("/"):
        candidates.append(candidate / "index.html")
    else:
        candidates.append(candidate)
        if candidate.suffix == "":
            candidates.append(candidate / "index.html")
            candidates.append(candidate.with_suffix(".html"))

    root_resolved = root.resolve()
    for item in candidates:
        try:
            resolved = item.resolve()
            resolved.relative_to(root_resolved)
        except (OSError, ValueError):
            continue
        if resolved.is_file():
            return resolved
    return None


def resolve_local_href(root: Path, source: Path, href: str) -> tuple[Path, str] | None:
    parsed = urlsplit(href)
    scheme = parsed.scheme.lower()

    if scheme in {"mailto", "tel", "javascript", "data"}:
        return None
    if scheme and scheme not in {"http", "https"}:
        return None
    if parsed.netloc and (parsed.hostname or "").lower() not in LOCAL_HOSTS:
        return None

    fragment = unquote(parsed.fragment)
    if parsed.path.startswith("/") or parsed.netloc:
        target = route_file(root, parsed.path)
    elif not parsed.path:
        target = source
    else:
        relative_candidate = source.parent / unquote(parsed.path)
        try:
            relative_candidate.resolve().relative_to(root.resolve())
        except (OSError, ValueError):
            return Path(), fragment

        if parsed.path.endswith("/"):
            target = route_file(
                root,
                "/" + relative_candidate.resolve().relative_to(root.resolve()).as_posix() + "/",
            )
        elif relative_candidate.is_file():
            target = relative_candidate.resolve()
        elif relative_candidate.suffix == "":
            index_candidate = relative_candidate / "index.html"
            html_candidate = relative_candidate.with_suffix(".html")
            target = (
                index_candidate.resolve()
                if index_candidate.is_file()
                else html_candidate.resolve()
                if html_candidate.is_file()
                else None
            )
        else:
            target = None

    return (target if target is not None else Path(), fragment)


def canonical_for_file(root: Path, path: Path) -> str:
    relative = path.resolve().relative_to(root.resolve()).as_posix()
    if relative == "index.html":
        route = "/"
    elif relative.endswith("/index.html"):
        route = "/" + relative[: -len("index.html")]
    else:
        route = "/" + relative
    return SITE_ORIGIN + route


def main() -> int:
    argument_parser = argparse.ArgumentParser(
        description="Audit the static RielArt website."
    )
    argument_parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Site root (defaults to the parent of tools/).",
    )
    argument_parser.add_argument(
        "--output",
        type=Path,
        help="Optionally save the readable report to this path.",
    )
    args = argument_parser.parse_args()
    root = args.root.resolve()

    critical: list[str] = []
    warnings: list[str] = []
    notes: list[str] = []

    if not root.is_dir():
        print(f"CRITICAL: site root does not exist: {root}", file=sys.stderr)
        return 2

    html_paths = sorted(iter_files(root, {".html"}))
    pages = {path.resolve(): parse_page(path) for path in html_paths}
    indexable_pages = [page for page in pages.values() if page.indexable]

    for page in pages.values():
        relative = page.path.relative_to(root).as_posix()
        id_lines: dict[str, list[int]] = defaultdict(list)
        for element_id, line in page.ids:
            id_lines[element_id].append(line)
        for element_id, lines in id_lines.items():
            if len(lines) > 1:
                critical.append(
                    f"{relative}: duplicate id {element_id!r} on lines "
                    + ", ".join(map(str, lines))
                )

        for line in page.images_without_alt:
            critical.append(f"{relative}:{line}: image is missing an alt attribute")

        if page.indexable:
            if not page.title:
                critical.append(f"{relative}: indexable page is missing a title")
            if not page.description:
                critical.append(
                    f"{relative}: indexable page is missing a meta description"
                )
            if not page.canonical:
                critical.append(f"{relative}: indexable page is missing a canonical")
            if len(page.h1_text) != 1:
                critical.append(
                    f"{relative}: expected exactly one H1, found {len(page.h1_text)}"
                )
            expected_canonical = canonical_for_file(root, page.path)
            if page.canonical and page.canonical != expected_canonical:
                critical.append(
                    f"{relative}: canonical is {page.canonical!r}; "
                    f"expected {expected_canonical!r}"
                )

        known_ids = {element_id for element_id, _ in page.ids}
        for anchor in page.anchors:
            safe_blank = bool({"noopener", "noreferrer"} & set(anchor.rel))
            if anchor.target == "_blank" and not safe_blank:
                critical.append(
                    f"{relative}:{anchor.line}: target=\"_blank\" lacks "
                    f"rel=\"noopener\" or rel=\"noreferrer\" ({anchor.href})"
                )

            if anchor.href.rstrip("/") == PORTAL_URL.rstrip("/"):
                if anchor.target != "_blank" or not safe_blank:
                    critical.append(
                        f"{relative}:{anchor.line}: Client Portal must open in a "
                        f"safe new tab"
                    )

            resolved = resolve_local_href(root, page.path.resolve(), anchor.href)
            if resolved is None:
                continue
            target, fragment = resolved
            if not target or not target.is_file():
                critical.append(
                    f"{relative}:{anchor.line}: local href target does not exist "
                    f"({anchor.href})"
                )
                continue
            if fragment:
                target_page = pages.get(target.resolve())
                if target_page is None and target.suffix.lower() == ".html":
                    target_page = parse_page(target)
                    pages[target.resolve()] = target_page
                target_ids = (
                    {element_id for element_id, _ in target_page.ids}
                    if target_page
                    else known_ids
                    if target.resolve() == page.path.resolve()
                    else set()
                )
                if fragment not in target_ids:
                    critical.append(
                        f"{relative}:{anchor.line}: fragment #{fragment} does not "
                        f"exist in {target.relative_to(root).as_posix()}"
                    )

    titles: dict[str, list[str]] = defaultdict(list)
    canonicals: dict[str, list[str]] = defaultdict(list)
    for page in indexable_pages:
        relative = page.path.relative_to(root).as_posix()
        if page.title:
            titles[page.title.casefold()].append(relative)
        if page.canonical:
            canonicals[page.canonical].append(relative)
    for files in titles.values():
        if len(files) > 1:
            critical.append("duplicate page title: " + ", ".join(files))
    for canonical, files in canonicals.items():
        if len(files) > 1:
            critical.append(
                f"duplicate canonical {canonical!r}: " + ", ".join(files)
            )

    sitemap_path = root / "sitemap.xml"
    sitemap_urls: list[str] = []
    if not sitemap_path.is_file():
        critical.append("sitemap.xml is missing")
    else:
        try:
            sitemap_root = ElementTree.parse(sitemap_path).getroot()
            namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            sitemap_urls = [
                node.text.strip()
                for node in sitemap_root.findall("sm:url/sm:loc", namespace)
                if node.text and node.text.strip()
            ]
        except (ElementTree.ParseError, OSError) as error:
            critical.append(f"sitemap.xml could not be parsed: {error}")

    sitemap_duplicates = {
        url for url in sitemap_urls if sitemap_urls.count(url) > 1
    }
    for url in sorted(sitemap_duplicates):
        critical.append(f"sitemap contains duplicate URL: {url}")

    expected_indexable_urls = {
        page.canonical for page in indexable_pages if page.canonical
    }
    sitemap_url_set = set(sitemap_urls)
    for url in sorted(expected_indexable_urls - sitemap_url_set):
        critical.append(f"sitemap is missing indexable page: {url}")
    for url in sorted(sitemap_url_set - expected_indexable_urls):
        parsed = urlsplit(url)
        target = (
            route_file(root, parsed.path)
            if (parsed.hostname or "").lower() in LOCAL_HOSTS
            else None
        )
        if target is None:
            critical.append(f"sitemap URL has no local page: {url}")
        else:
            page = pages.get(target.resolve()) or parse_page(target)
            if not page.indexable:
                critical.append(f"sitemap includes a noindex page: {url}")
            else:
                critical.append(
                    f"sitemap URL is not represented by an indexable canonical: {url}"
                )

    text_files = sorted(iter_files(root, TEXT_EXTENSIONS))
    forbidden_lower = FORBIDDEN_COMPETITOR_TOKEN.casefold()
    localhost_pattern = re.compile(
        r"(?i)(?:https?://)?(?:localhost|127\.0\.0\.1|0\.0\.0\.0|\[?::1\]?)"
    )
    for path in text_files:
        relative = path.relative_to(root).as_posix()
        text = read_text(path)
        lowered = text.casefold()
        if forbidden_lower in lowered:
            critical.append(
                f"{relative}: forbidden competitor token appears in public source"
            )
        if "lorem ipsum" in lowered:
            critical.append(f"{relative}: placeholder text 'Lorem ipsum' found")
        if localhost_pattern.search(text):
            critical.append(f"{relative}: localhost URL or address found")
        if forbidden_lower in relative.casefold():
            critical.append(
                f"{relative}: forbidden competitor token appears in a filename"
            )

    production_html = "\n".join(read_text(path) for path in html_paths)
    portal_count = production_html.count(PORTAL_URL)
    formspree_count = production_html.count(FORMSPREE_URL)
    if portal_count == 0:
        critical.append(f"required Client Portal URL is missing: {PORTAL_URL}")
    if formspree_count == 0:
        critical.append(f"required Formspree endpoint is missing: {FORMSPREE_URL}")

    found_stripe_urls = set(
        re.findall(r"https://buy\.stripe\.com/[A-Za-z0-9]+", production_html)
    )
    for url in sorted(EXPECTED_STRIPE_URLS - found_stripe_urls):
        critical.append(f"required Stripe Payment Link is missing: {url}")
    for url in sorted(found_stripe_urls - EXPECTED_STRIPE_URLS):
        critical.append(f"unexpected Stripe Payment Link found: {url}")

    notes.extend(
        [
            f"HTML files checked: {len(html_paths)}",
            f"Indexable pages checked: {len(indexable_pages)}",
            f"Sitemap URLs checked: {len(sitemap_urls)}",
            f"Client Portal URL occurrences: {portal_count}",
            f"Formspree endpoint occurrences: {formspree_count}",
            f"Approved Stripe Payment Links found: "
            f"{len(found_stripe_urls & EXPECTED_STRIPE_URLS)}/6",
        ]
    )
    if not warnings:
        notes.append("Warnings: none")

    report_lines = [
        "RielArt static site audit",
        "=" * 25,
        f"Root: {root}",
        "",
        "Summary",
        "-------",
        *[f"- {note}" for note in notes],
        f"- Critical failures: {len(critical)}",
    ]
    if critical:
        report_lines.extend(
            [
                "",
                "Critical failures",
                "-----------------",
                *[
                    f"{number}. {message}"
                    for number, message in enumerate(critical, start=1)
                ],
            ]
        )
    else:
        report_lines.extend(
            [
                "",
                "PASS: no critical static-site failures were found.",
            ]
        )
    if warnings:
        report_lines.extend(
            [
                "",
                "Warnings",
                "--------",
                *[
                    f"{number}. {message}"
                    for number, message in enumerate(warnings, start=1)
                ],
            ]
        )

    report = "\n".join(report_lines) + "\n"
    print(report, end="")
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")

    return 1 if critical else 0


if __name__ == "__main__":
    raise SystemExit(main())
