#!/usr/bin/env python3
"""Static quality checks for the RielArt marketing site.

The script uses only the Python standard library. It is a local QA tool and is
not required for deployment.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date, datetime
from fnmatch import fnmatch
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree


SITE_ORIGIN = "https://rielart.com"
LOCAL_HOSTS = {"rielart.com", "www.rielart.com"}
PORTAL_URL = "https://portal.rielart.com"
FORMSPREE_URL = "https://formspree.io/f/xojrdoel"
CALENDLY_URL = (
    "https://calendly.com/gabrielmacovei001/15min?hide_gdpr_banner=1"
)
EMAIL_URL = "mailto:hello@rielart.com"
LINKEDIN_URL = "https://www.linkedin.com/in/gabrielmacovei/"
EXPECTED_STRIPE_URLS = {
    "https://buy.stripe.com/8x25kvbsKcKF6M2gYqfw400",
    "https://buy.stripe.com/dRm00b9kC5id6M29vYfw401",
    "https://buy.stripe.com/bJe14f54m11Xc6mdMefw402",
    "https://buy.stripe.com/7sYbIT0O64e95HYfUmfw403",
    "https://buy.stripe.com/14A5kv9kCh0Vb2igYqfw404",
    "https://buy.stripe.com/5kQ6oz2WefWRgmCfUmfw405",
}
EXPECTED_ONE_TIME_PRICES = {"$497", "$247"}
EXPECTED_MONTHLY_PRICES = {"$149", "$249", "$399", "$699"}
FORBIDDEN_COMPETITOR_TOKEN = "brand" + "vm"
IGNORED_DIRECTORIES = {".git", "node_modules", "__pycache__"}
PAGE_SCHEMA_TYPES = {
    "AboutPage",
    "Article",
    "Blog",
    "BlogPosting",
    "CollectionPage",
    "ContactPage",
    "FAQPage",
    "Service",
    "WebPage",
}
SCHEMA_IMAGE_KEYS = {
    "contentUrl",
    "image",
    "logo",
    "primaryImageOfPage",
    "thumbnail",
    "thumbnailUrl",
}
REQUIRED_OPEN_GRAPH = {
    "og:type",
    "og:title",
    "og:description",
    "og:url",
    "og:image",
}
REQUIRED_TWITTER = {
    "twitter:card",
    "twitter:title",
    "twitter:description",
    "twitter:image",
}
BUILD_ARTIFACT_DIRECTORIES = {
    "__pycache__",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    "coverage",
    "node_modules",
    "tools",
}
BUILD_ARTIFACT_NAMES = {
    ".DS_Store",
    ".env",
    ".env.local",
    ".env.production",
    ".gitattributes",
    ".gitignore",
    "desktop.ini",
    "Thumbs.db",
}
BUILD_ARTIFACT_SUFFIXES = {
    ".bak",
    ".log",
    ".orig",
    ".pyo",
    ".pyc",
    ".swp",
    ".tmp",
}
ROOT_INTERNAL_DOCUMENT_PATTERNS = {
    "*AUDIT*.json",
    "*AUDIT*.md",
    "*AUDIT*.txt",
    "*PLAN*.md",
    "*QA*.md",
    "*QA*.txt",
    "*REVIEW*.md",
    "*NOTES*.md",
    "CHANGELOG*.md",
    "README.md",
}


@dataclass(frozen=True)
class Anchor:
    href: str
    target: str
    rel: frozenset[str]
    line: int


@dataclass(frozen=True)
class AssetReference:
    url: str
    kind: str
    line: int


@dataclass(frozen=True)
class Heading:
    level: int
    text: str
    line: int


@dataclass(frozen=True)
class Image:
    src: str
    alt: str
    has_alt: bool
    width: str
    height: str
    aria_hidden: bool
    line: int


@dataclass(frozen=True)
class Control:
    tag: str
    control_type: str
    name: str
    element_id: str
    aria_label: str
    aria_labelledby: str
    value: str
    required: bool
    wrapped_label: bool
    line: int


@dataclass
class Form:
    action: str
    method: str
    line: int
    controls: list[Control] = field(default_factory=list)
    links: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class JsonLdBlock:
    text: str
    line: int


@dataclass(frozen=True)
class Redirect:
    source: str
    target: str
    status: int
    line: int


@dataclass
class Page:
    path: Path
    title: str = ""
    description: str = ""
    canonical: str = ""
    robots: str = ""
    h1_text: list[str] = field(default_factory=list)
    headings: list[Heading] = field(default_factory=list)
    ids: list[tuple[str, int]] = field(default_factory=list)
    images: list[Image] = field(default_factory=list)
    anchors: list[Anchor] = field(default_factory=list)
    assets: list[AssetReference] = field(default_factory=list)
    visible_text_parts: list[str] = field(default_factory=list)
    meta_values: dict[str, list[tuple[str, int]]] = field(
        default_factory=lambda: defaultdict(list)
    )
    canonical_values: list[tuple[str, int]] = field(default_factory=list)
    labels_for: set[str] = field(default_factory=set)
    forms: list[Form] = field(default_factory=list)
    json_ld: list[JsonLdBlock] = field(default_factory=list)
    refresh_values: list[tuple[str, int]] = field(default_factory=list)
    title_count: int = 0

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
        self._heading_level = 0
        self._heading_line = 0
        self._heading_parts: list[str] = []
        self._label_depth = 0
        self._current_form: Form | None = None
        self._json_ld_depth = 0
        self._json_ld_line = 0
        self._json_ld_parts: list[str] = []
        self._hidden_text_depth = 0

    @staticmethod
    def _attrs(attrs: list[tuple[str, str | None]]) -> dict[str, str]:
        return {name.lower(): value or "" for name, value in attrs}

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        tag = tag.lower()
        values = self._attrs(attrs)
        line, _ = self.getpos()

        if tag in {"script", "style", "template"}:
            self._hidden_text_depth += 1

        element_id = values.get("id")
        if element_id:
            self.page.ids.append((element_id, line))

        if tag == "title":
            self._title_depth += 1
            self.page.title_count += 1
        elif tag == "h1":
            self._h1_depth += 1
            self._h1_parts = []
        if re.fullmatch(r"h[1-6]", tag):
            self._heading_level = int(tag[1])
            self._heading_line = line
            self._heading_parts = []
        if tag == "label":
            self._label_depth += 1
            label_for = values.get("for", "").strip()
            if label_for:
                self.page.labels_for.add(label_for)
        if tag == "form":
            form = Form(
                action=values.get("action", "").strip(),
                method=values.get("method", "get").strip().lower() or "get",
                line=line,
            )
            self.page.forms.append(form)
            self._current_form = form
        if tag in {"input", "select", "textarea"} and self._current_form:
            self._current_form.controls.append(
                Control(
                    tag=tag,
                    control_type=values.get("type", "text").strip().lower(),
                    name=values.get("name", "").strip(),
                    element_id=values.get("id", "").strip(),
                    aria_label=values.get("aria-label", "").strip(),
                    aria_labelledby=values.get("aria-labelledby", "").strip(),
                    value=values.get("value", "").strip(),
                    required="required" in values,
                    wrapped_label=bool(self._label_depth),
                    line=line,
                )
            )
        if tag == "script" and values.get("type", "").strip().lower() == "application/ld+json":
            self._json_ld_depth += 1
            self._json_ld_line = line
            self._json_ld_parts = []
        if tag == "script" and values.get("src", "").strip():
            self.page.assets.append(
                AssetReference(values["src"].strip(), "script", line)
            )
        elif tag == "meta":
            name = values.get("name", "").lower()
            property_name = values.get("property", "").lower()
            meta_key = property_name or name
            content = values.get("content", "").strip()
            if meta_key:
                self.page.meta_values[meta_key].append((content, line))
            if name == "description":
                self.page.description = content
            elif name == "robots":
                self.page.robots = content
            if values.get("http-equiv", "").lower() == "refresh":
                self.page.refresh_values.append((content, line))
            if meta_key in {"og:image", "twitter:image"} and content:
                self.page.assets.append(
                    AssetReference(content, meta_key, line)
                )
        elif tag == "link":
            rel = {
                token.lower() for token in values.get("rel", "").split() if token
            }
            if "canonical" in rel:
                self.page.canonical = values.get("href", "").strip()
                self.page.canonical_values.append((self.page.canonical, line))
            if rel & {
                "apple-touch-icon",
                "icon",
                "manifest",
                "modulepreload",
                "preload",
                "stylesheet",
            }:
                href = values.get("href", "").strip()
                if href:
                    self.page.assets.append(
                        AssetReference(href, "link", line)
                    )
        elif tag == "img":
            source = values.get("src", "").strip()
            self.page.images.append(
                Image(
                    src=source,
                    alt=values.get("alt", "").strip(),
                    has_alt="alt" in values,
                    width=values.get("width", "").strip(),
                    height=values.get("height", "").strip(),
                    aria_hidden=values.get("aria-hidden", "").strip().lower()
                    == "true",
                    line=line,
                )
            )
            if source:
                self.page.assets.append(AssetReference(source, "image", line))
            self._append_srcset(values.get("srcset", ""), line)
        elif tag in {"audio", "iframe", "source", "video"}:
            source = values.get("src", "").strip()
            if source:
                self.page.assets.append(
                    AssetReference(source, tag, line)
                )
            poster = values.get("poster", "").strip()
            if poster:
                self.page.assets.append(
                    AssetReference(poster, "video poster", line)
                )
            self._append_srcset(values.get("srcset", ""), line)
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
                if self._current_form:
                    self._current_form.links.append(href)

    def _append_srcset(self, srcset: str, line: int) -> None:
        for candidate in srcset.split(","):
            url = candidate.strip().split(maxsplit=1)[0] if candidate.strip() else ""
            if url:
                self.page.assets.append(
                    AssetReference(url, "srcset", line)
                )

    def handle_startendtag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in {"script", "style", "template"} and self._hidden_text_depth:
            self._hidden_text_depth -= 1
        if tag == "title" and self._title_depth:
            self._title_depth -= 1
            if not self._title_depth:
                self.page.title = normalize_text("".join(self._title_parts))
        elif tag == "h1" and self._h1_depth:
            self._h1_depth -= 1
            if not self._h1_depth:
                self.page.h1_text.append(normalize_text("".join(self._h1_parts)))
        if re.fullmatch(r"h[1-6]", tag) and self._heading_level == int(tag[1]):
            self.page.headings.append(
                Heading(
                    level=self._heading_level,
                    text=normalize_text("".join(self._heading_parts)),
                    line=self._heading_line,
                )
            )
            self._heading_level = 0
            self._heading_parts = []
        if tag == "label" and self._label_depth:
            self._label_depth -= 1
        if tag == "form":
            self._current_form = None
        if tag == "script" and self._json_ld_depth:
            self._json_ld_depth -= 1
            if not self._json_ld_depth:
                self.page.json_ld.append(
                    JsonLdBlock(
                        text="".join(self._json_ld_parts).strip(),
                        line=self._json_ld_line,
                    )
                )
                self._json_ld_parts = []

    def handle_data(self, data: str) -> None:
        if not self._hidden_text_depth and normalize_text(data):
            self.page.visible_text_parts.append(data)
        if self._title_depth:
            self._title_parts.append(data)
        if self._h1_depth:
            self._h1_parts.append(data)
        if self._heading_level:
            self._heading_parts.append(data)
        if self._json_ld_depth:
            self._json_ld_parts.append(data)


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


def resolve_local_resource(
    root: Path, source: Path, value: str
) -> tuple[bool, Path | None]:
    """Return whether a URL is local and, when local, its resolved file."""
    parsed = urlsplit(value.strip())
    scheme = parsed.scheme.lower()
    if scheme in {"data", "mailto", "tel", "javascript"}:
        return False, None
    if scheme and scheme not in {"http", "https"}:
        return False, None
    if parsed.netloc and (parsed.hostname or "").lower() not in LOCAL_HOSTS:
        return False, None
    if not parsed.path:
        return False, None

    if parsed.path.startswith("/") or parsed.netloc:
        candidate = root / unquote(parsed.path).lstrip("/")
    else:
        candidate = source.parent / unquote(parsed.path)

    try:
        resolved = candidate.resolve()
        resolved.relative_to(root.resolve())
    except (OSError, ValueError):
        return True, None
    return True, resolved if resolved.is_file() else None


def local_url_problem(value: str) -> str | None:
    parsed = urlsplit(value.strip())
    if (parsed.hostname or "").lower() not in LOCAL_HOSTS:
        return None
    if parsed.scheme.lower() != "https":
        return "must use https"
    if (parsed.hostname or "").lower() != "rielart.com":
        return "must use the canonical rielart.com host"
    return None


def extract_refresh_url(value: str) -> str:
    match = re.search(r"(?i)\burl\s*=\s*['\"]?([^'\"]+)", value)
    return match.group(1).strip() if match else ""


def parse_sitemap_date(value: str) -> date | None:
    cleaned = value.strip()
    try:
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", cleaned):
            return date.fromisoformat(cleaned)
        return datetime.fromisoformat(cleaned.replace("Z", "+00:00")).date()
    except ValueError:
        return None


def parse_redirects(path: Path) -> tuple[list[Redirect], list[str]]:
    redirects: list[Redirect] = []
    errors: list[str] = []
    for line_number, raw_line in enumerate(read_text(path).splitlines(), start=1):
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        parts = stripped.split()
        if len(parts) not in {2, 3}:
            errors.append(
                f"_redirects:{line_number}: expected source, target, and optional status"
            )
            continue
        source, target = parts[:2]
        status_text = parts[2] if len(parts) == 3 else "301"
        try:
            status = int(status_text.rstrip("!"))
        except ValueError:
            errors.append(
                f"_redirects:{line_number}: invalid redirect status {status_text!r}"
            )
            continue
        if status not in {200, 301, 302, 303, 307, 308}:
            errors.append(
                f"_redirects:{line_number}: unsupported redirect status {status}"
            )
            continue
        if not source.startswith("/"):
            errors.append(
                f"_redirects:{line_number}: local redirect source must start with /"
            )
        redirects.append(
            Redirect(source=source, target=target, status=status, line=line_number)
        )
    return redirects, errors


def normalize_deploy_path(value: str) -> str:
    normalized = value.strip().replace("\\", "/")
    while normalized.startswith("./"):
        normalized = normalized[2:]
    return normalized.strip("/")


def parse_github_pages_excludes(path: Path) -> tuple[set[str], list[str]]:
    """Parse the simple top-level Jekyll `exclude` list without PyYAML."""
    excludes: set[str] = set()
    errors: list[str] = []
    found_exclude = False
    in_exclude = False

    for line_number, raw_line in enumerate(read_text(path).splitlines(), start=1):
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        top_level = len(raw_line) == len(raw_line.lstrip())
        if top_level:
            match = re.fullmatch(r"exclude\s*:\s*(.*)", raw_line.strip())
            if not match:
                in_exclude = False
                continue
            found_exclude = True
            remainder = match.group(1).strip()
            in_exclude = not remainder
            if remainder:
                if not (remainder.startswith("[") and remainder.endswith("]")):
                    errors.append(
                        f"_config.yml:{line_number}: exclude must be a YAML "
                        f"list"
                    )
                    continue
                for item in remainder[1:-1].split(","):
                    normalized = normalize_deploy_path(
                        item.strip().strip("'\"")
                    )
                    if normalized:
                        excludes.add(normalized)
            continue

        if not in_exclude:
            continue
        match = re.fullmatch(r"\s*-\s+(.+?)\s*", raw_line)
        if not match:
            errors.append(
                f"_config.yml:{line_number}: invalid exclude list entry"
            )
            continue
        scalar = match.group(1).strip()
        if " #" in scalar:
            scalar = scalar.split(" #", 1)[0].rstrip()
        normalized = normalize_deploy_path(scalar.strip("'\""))
        if not normalized:
            errors.append(
                f"_config.yml:{line_number}: empty exclude list entry"
            )
        elif normalized == ".." or normalized.startswith("../"):
            errors.append(
                f"_config.yml:{line_number}: exclude escapes the site root "
                f"({scalar})"
            )
        else:
            excludes.add(normalized)

    if not found_exclude:
        errors.append("_config.yml: top-level exclude list is missing")
    return excludes, errors


def deploy_path_is_excluded(relative: str, excludes: set[str]) -> bool:
    candidate = normalize_deploy_path(relative)
    for excluded in excludes:
        normalized = normalize_deploy_path(excluded)
        if not normalized:
            continue
        if any(character in normalized for character in "*?["):
            if fnmatch(candidate, normalized):
                return True
            continue
        if candidate == normalized or candidate.startswith(normalized + "/"):
            return True
    return False


def collapse_artifact_paths(paths: set[str]) -> list[str]:
    """Report an artifact directory once instead of repeating every child."""
    collapsed: list[str] = []
    for path in sorted(paths, key=lambda item: (item.count("/"), item.casefold())):
        normalized = normalize_deploy_path(path)
        if any(
            normalized == parent
            or normalized.startswith(parent.rstrip("/") + "/")
            for parent in collapsed
        ):
            continue
        collapsed.append(normalized)
    return collapsed


def redirect_match(rule: Redirect, source_path: str) -> tuple[bool, str]:
    pattern = re.escape(rule.source).replace(r"\*", "(.*)")
    match = re.fullmatch(pattern, source_path)
    if not match:
        return False, ""
    splat = match.group(1) if match.groups() else ""
    target = rule.target.replace(":splat", splat)
    return True, target


def schema_types(value: Any) -> set[str]:
    if isinstance(value, str):
        return {value.rsplit("/", 1)[-1]}
    if isinstance(value, list):
        return {
            item.rsplit("/", 1)[-1]
            for item in value
            if isinstance(item, str)
        }
    return set()


def iter_primary_schema_objects(value: Any) -> Iterable[dict[str, Any]]:
    """Yield document-level entities, excluding nested collection members."""
    if isinstance(value, list):
        for child in value:
            if isinstance(child, dict):
                yield child
        return
    if not isinstance(value, dict):
        return
    yield value
    graph = value.get("@graph")
    if isinstance(graph, list):
        for child in graph:
            if isinstance(child, dict):
                yield child


def iter_schema_strings(
    value: Any, key: str = "", image_context: bool = False
) -> Iterable[tuple[str, str, bool]]:
    if isinstance(value, dict):
        object_is_image = "ImageObject" in schema_types(value.get("@type"))
        for child_key, child in value.items():
            next_image_context = (
                image_context
                or object_is_image
                or child_key in SCHEMA_IMAGE_KEYS
            )
            yield from iter_schema_strings(
                child, child_key, next_image_context
            )
    elif isinstance(value, list):
        for child in value:
            yield from iter_schema_strings(child, key, image_context)
    elif isinstance(value, str):
        yield key, value.strip(), image_context


def strip_html(value: str) -> str:
    return normalize_text(unescape(re.sub(r"<[^>]+>", " ", value)))


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
    asset_reference_count = 0
    image_count = 0
    json_ld_block_count = 0
    form_count = 0
    deploy_excludes: set[str] = set()
    excluded_artifact_count = 0

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

        for image in page.images:
            image_count += 1
            if not image.has_alt:
                critical.append(
                    f"{relative}:{image.line}: image is missing an alt attribute"
                )
            elif not image.alt:
                image_name = Path(
                    unquote(urlsplit(image.src).path)
                ).name.casefold()
                if image_name != "logo.png" and not image.aria_hidden:
                    warnings.append(
                        f"{relative}:{image.line}: non-logo image has an empty "
                        f"alt and may be informative ({image.src or 'missing src'})"
                    )
            for dimension_name, dimension_value in (
                ("width", image.width),
                ("height", image.height),
            ):
                if not re.fullmatch(r"[1-9]\d*", dimension_value):
                    critical.append(
                        f"{relative}:{image.line}: image {dimension_name} must "
                        f"be a nonempty positive integer "
                        f"({dimension_value or 'missing'})"
                    )

        if page.title_count > 1:
            critical.append(
                f"{relative}: multiple title elements found ({page.title_count})"
            )
        if len(page.canonical_values) > 1:
            lines = ", ".join(str(line) for _, line in page.canonical_values)
            critical.append(
                f"{relative}: multiple canonical links found on lines {lines}"
            )
        descriptions_on_page = page.meta_values.get("description", [])
        if len(descriptions_on_page) > 1:
            lines = ", ".join(str(line) for _, line in descriptions_on_page)
            critical.append(
                f"{relative}: multiple meta descriptions found on lines {lines}"
            )

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

            for meta_key in sorted(REQUIRED_OPEN_GRAPH | REQUIRED_TWITTER):
                values = page.meta_values.get(meta_key, [])
                if not values or not values[0][0]:
                    critical.append(
                        f"{relative}: indexable page is missing {meta_key}"
                    )
                elif len(values) > 1:
                    lines = ", ".join(str(line) for _, line in values)
                    critical.append(
                        f"{relative}: duplicate {meta_key} metadata on lines {lines}"
                    )

            og_url_values = page.meta_values.get("og:url", [])
            if page.canonical and og_url_values:
                og_url, line = og_url_values[0]
                if og_url != page.canonical:
                    critical.append(
                        f"{relative}:{line}: og:url is {og_url!r}; "
                        f"expected canonical {page.canonical!r}"
                    )
            twitter_card_values = page.meta_values.get("twitter:card", [])
            if twitter_card_values and twitter_card_values[0][0] not in {
                "summary",
                "summary_large_image",
            }:
                value, line = twitter_card_values[0]
                critical.append(
                    f"{relative}:{line}: unsupported twitter:card {value!r}"
                )

        previous_heading: Heading | None = None
        for heading in page.headings:
            if not heading.text:
                warnings.append(
                    f"{relative}:{heading.line}: empty H{heading.level}"
                )
            if (
                previous_heading is not None
                and heading.level > previous_heading.level + 1
            ):
                warnings.append(
                    f"{relative}:{heading.line}: heading level skips from "
                    f"H{previous_heading.level} to H{heading.level}"
                )
            previous_heading = heading
        if page.headings and page.headings[0].level != 1:
            warnings.append(
                f"{relative}:{page.headings[0].line}: first heading is "
                f"H{page.headings[0].level}, not H1"
            )

        for asset in page.assets:
            asset_reference_count += 1
            parsed_asset = urlsplit(asset.url)
            if parsed_asset.scheme.lower() == "http":
                critical.append(
                    f"{relative}:{asset.line}: insecure {asset.kind} URL "
                    f"({asset.url})"
                )
            url_problem = local_url_problem(asset.url)
            if url_problem:
                critical.append(
                    f"{relative}:{asset.line}: local {asset.kind} URL "
                    f"{url_problem} ({asset.url})"
                )
            is_local, target = resolve_local_resource(
                root, page.path.resolve(), asset.url
            )
            if is_local and target is None:
                critical.append(
                    f"{relative}:{asset.line}: local {asset.kind} asset does "
                    f"not exist ({asset.url})"
                )

        form_count += len(page.forms)
        known_ids = {element_id for element_id, _ in page.ids}
        for label_target in sorted(page.labels_for - known_ids):
            critical.append(
                f"{relative}: label references missing id {label_target!r}"
            )
        for form in page.forms:
            if form.method != "post":
                critical.append(
                    f"{relative}:{form.line}: form method must be POST"
                )
            parsed_action = urlsplit(form.action)
            if not form.action:
                critical.append(
                    f"{relative}:{form.line}: form action is missing"
                )
            elif parsed_action.scheme.lower() != "https":
                critical.append(
                    f"{relative}:{form.line}: form action must use HTTPS "
                    f"({form.action})"
                )
            elif form.action.rstrip("/") != FORMSPREE_URL.rstrip("/"):
                critical.append(
                    f"{relative}:{form.line}: unexpected form action "
                    f"({form.action})"
                )

            for control in form.controls:
                if not control.name:
                    critical.append(
                        f"{relative}:{control.line}: {control.tag} control "
                        f"is missing a name"
                    )
                label_required = control.control_type not in {
                    "hidden",
                    "button",
                    "submit",
                    "reset",
                    "image",
                }
                has_label = (
                    control.wrapped_label
                    or bool(control.aria_label)
                    or (
                        bool(control.element_id)
                        and control.element_id in page.labels_for
                    )
                )
                if control.aria_labelledby:
                    labelled_ids = control.aria_labelledby.split()
                    has_label = has_label or all(
                        item in known_ids for item in labelled_ids
                    )
                    missing_label_ids = [
                        item for item in labelled_ids if item not in known_ids
                    ]
                    if missing_label_ids:
                        critical.append(
                            f"{relative}:{control.line}: aria-labelledby "
                            f"references missing id(s): "
                            + ", ".join(missing_label_ids)
                        )
                if label_required and not has_label:
                    critical.append(
                        f"{relative}:{control.line}: {control.tag} control "
                        f"{control.name!r} has no associated label"
                    )

            next_controls = [
                control
                for control in form.controls
                if control.name == "_next"
            ]
            if len(next_controls) != 1:
                critical.append(
                    f"{relative}:{form.line}: form must contain exactly one "
                    f"_next success destination"
                )
            else:
                next_control = next_controls[0]
                parsed_next = urlsplit(next_control.value)
                if (
                    parsed_next.scheme.lower() != "https"
                    or (parsed_next.hostname or "").lower() not in LOCAL_HOSTS
                ):
                    critical.append(
                        f"{relative}:{next_control.line}: _next must be an "
                        f"HTTPS RielArt URL ({next_control.value})"
                    )
                elif route_file(root, parsed_next.path) is None:
                    critical.append(
                        f"{relative}:{next_control.line}: _next destination "
                        f"does not exist ({next_control.value})"
                    )

            privacy_controls = [
                control
                for control in form.controls
                if control.control_type == "checkbox"
                and re.search(r"privacy|consent", control.name, re.I)
            ]
            if not privacy_controls:
                critical.append(
                    f"{relative}:{form.line}: form is missing a privacy "
                    f"consent checkbox"
                )
            elif not any(control.required for control in privacy_controls):
                critical.append(
                    f"{relative}:{form.line}: privacy consent checkbox must "
                    f"be required"
                )
            if not any(
                urlsplit(href).path.rstrip("/") == "/privacy-policy"
                for href in form.links
            ):
                critical.append(
                    f"{relative}:{form.line}: form is missing a link to the "
                    f"privacy policy"
                )

        for block in page.json_ld:
            json_ld_block_count += 1
            if not block.text:
                critical.append(
                    f"{relative}:{block.line}: empty JSON-LD block"
                )
                continue
            try:
                schema_data = json.loads(block.text)
            except json.JSONDecodeError as error:
                critical.append(
                    f"{relative}:{block.line}: invalid JSON-LD "
                    f"({error.msg} at line {error.lineno}, column {error.colno})"
                )
                continue

            for _key, value, image_context in iter_schema_strings(schema_data):
                if not value.startswith(("http://", "https://", "/")):
                    continue
                if image_context:
                    asset_reference_count += 1
                parsed_value = urlsplit(value)
                if image_context and parsed_value.scheme.lower() == "http":
                    critical.append(
                        f"{relative}:{block.line}: insecure schema image "
                        f"URL ({value})"
                    )
                problem = local_url_problem(value)
                if problem:
                    critical.append(
                        f"{relative}:{block.line}: local schema URL {problem} "
                        f"({value})"
                    )
                host = (parsed_value.hostname or "").lower()
                is_local_value = (
                    value.startswith("/") or host in LOCAL_HOSTS
                )
                if not is_local_value:
                    continue
                if image_context:
                    is_local, image_path = resolve_local_resource(
                        root, page.path.resolve(), value
                    )
                    if is_local and image_path is None:
                        critical.append(
                            f"{relative}:{block.line}: schema image does not "
                            f"exist ({value})"
                        )
                else:
                    schema_target = route_file(root, parsed_value.path)
                    if schema_target is None:
                        critical.append(
                            f"{relative}:{block.line}: schema URL has no "
                            f"local page ({value})"
                        )

            canonical_base = page.canonical.split("#", 1)[0]
            primary_schema_objects = list(
                iter_primary_schema_objects(schema_data)
            )
            service_entity_count = sum(
                "Service" in schema_types(item.get("@type"))
                for item in primary_schema_objects
            )
            for schema_object in primary_schema_objects:
                object_types = schema_types(schema_object.get("@type"))
                is_page_entity = bool(
                    object_types & (PAGE_SCHEMA_TYPES - {"Service"})
                )
                is_single_service_entity = (
                    "Service" in object_types and service_entity_count == 1
                )
                if not (is_page_entity or is_single_service_entity):
                    continue
                candidates: list[str] = []
                for key in ("url", "@id"):
                    if isinstance(schema_object.get(key), str):
                        candidates.append(schema_object[key])
                main_entity = schema_object.get("mainEntityOfPage")
                if isinstance(main_entity, str):
                    candidates.append(main_entity)
                elif isinstance(main_entity, dict):
                    for key in ("url", "@id"):
                        if isinstance(main_entity.get(key), str):
                            candidates.append(main_entity[key])
                for candidate in candidates:
                    parsed_candidate = urlsplit(candidate)
                    if (
                        (parsed_candidate.hostname or "").lower()
                        in LOCAL_HOSTS
                        and candidate.split("#", 1)[0] != canonical_base
                    ):
                        critical.append(
                            f"{relative}:{block.line}: page schema URL "
                            f"{candidate!r} does not match canonical "
                            f"{page.canonical!r}"
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

    indexable_paths = {page.path.resolve() for page in indexable_pages}
    incoming_indexable_links: dict[Path, set[Path]] = defaultdict(set)
    for source_page in indexable_pages:
        source_path = source_page.path.resolve()
        for anchor in source_page.anchors:
            resolved = resolve_local_href(
                root, source_path, anchor.href
            )
            if resolved is None:
                continue
            target, _fragment = resolved
            if not target or not target.is_file():
                continue
            target_path = target.resolve()
            if target_path in indexable_paths and target_path != source_path:
                incoming_indexable_links[target_path].add(source_path)

    home_path = (root / "index.html").resolve()
    orphan_pages = [
        page
        for page in indexable_pages
        if page.path.resolve() != home_path
        and not incoming_indexable_links[page.path.resolve()]
    ]
    for page in orphan_pages:
        critical.append(
            f"{page.path.relative_to(root).as_posix()}: indexable page has no "
            f"incoming resolved link from another indexable HTML page"
        )

    titles: dict[str, list[str]] = defaultdict(list)
    descriptions: dict[str, list[str]] = defaultdict(list)
    canonicals: dict[str, list[str]] = defaultdict(list)
    for page in indexable_pages:
        relative = page.path.relative_to(root).as_posix()
        if page.title:
            titles[page.title.casefold()].append(relative)
        if page.description:
            descriptions[normalize_text(page.description).casefold()].append(relative)
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
    for files in descriptions.values():
        if len(files) > 1:
            critical.append(
                "duplicate meta description: " + ", ".join(files)
            )

    sitemap_path = root / "sitemap.xml"
    sitemap_urls: list[str] = []
    sitemap_lastmods: dict[str, str] = {}
    if not sitemap_path.is_file():
        critical.append("sitemap.xml is missing")
    else:
        try:
            sitemap_root = ElementTree.parse(sitemap_path).getroot()
            namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            for url_node in sitemap_root.findall("sm:url", namespace):
                loc_node = url_node.find("sm:loc", namespace)
                lastmod_node = url_node.find("sm:lastmod", namespace)
                if loc_node is None or not loc_node.text or not loc_node.text.strip():
                    critical.append("sitemap contains a URL entry without loc")
                    continue
                loc = loc_node.text.strip()
                sitemap_urls.append(loc)
                if (
                    lastmod_node is None
                    or not lastmod_node.text
                    or not lastmod_node.text.strip()
                ):
                    warnings.append(f"sitemap URL is missing lastmod: {loc}")
                    continue
                lastmod = lastmod_node.text.strip()
                sitemap_lastmods[loc] = lastmod
                parsed_lastmod = parse_sitemap_date(lastmod)
                if parsed_lastmod is None:
                    critical.append(
                        f"sitemap URL has invalid lastmod {lastmod!r}: {loc}"
                    )
                elif parsed_lastmod > date.today():
                    critical.append(
                        f"sitemap URL has future lastmod {lastmod!r}: {loc}"
                    )
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

    redirects_path = root / "_redirects"
    redirects: list[Redirect] = []
    if not redirects_path.is_file():
        critical.append("_redirects is missing")
    else:
        redirects, redirect_errors = parse_redirects(redirects_path)
        critical.extend(redirect_errors)
        redirect_sources: dict[str, list[Redirect]] = defaultdict(list)
        for redirect in redirects:
            redirect_sources[redirect.source].append(redirect)
            parsed_target = urlsplit(redirect.target)
            if parsed_target.scheme.lower() == "http":
                critical.append(
                    f"_redirects:{redirect.line}: redirect target must use "
                    f"HTTPS ({redirect.target})"
                )
            if parsed_target.netloc:
                if (parsed_target.hostname or "").lower() in LOCAL_HOSTS:
                    problem = local_url_problem(redirect.target)
                    if problem:
                        critical.append(
                            f"_redirects:{redirect.line}: local redirect "
                            f"target {problem} ({redirect.target})"
                        )
                continue
            if not redirect.target.startswith("/"):
                critical.append(
                    f"_redirects:{redirect.line}: redirect target must be "
                    f"an absolute path or URL ({redirect.target})"
                )
                continue
            target_prefix = re.split(r"[:*]", parsed_target.path, maxsplit=1)[0]
            if target_prefix and route_file(root, target_prefix) is None:
                critical.append(
                    f"_redirects:{redirect.line}: local redirect target does "
                    f"not resolve ({redirect.target})"
                )

            if "*" not in redirect.source and ":" not in redirect.source:
                source_page_path = route_file(root, urlsplit(redirect.source).path)
                if source_page_path is not None:
                    source_page = pages.get(source_page_path.resolve())
                    if source_page and source_page.indexable:
                        source_route = urlsplit(
                            canonical_for_file(root, source_page.path)
                        ).path
                        if source_route.rstrip("/") == redirect.source.rstrip("/"):
                            critical.append(
                                f"_redirects:{redirect.line}: redirect source "
                                f"collides with indexable page {redirect.source}"
                            )

        for source, rules in redirect_sources.items():
            destinations = {(rule.target, rule.status) for rule in rules}
            if len(destinations) > 1:
                critical.append(
                    f"_redirects has conflicting rules for {source}: "
                    + ", ".join(
                        f"{target} ({status})"
                        for target, status in sorted(destinations)
                    )
                )
            elif len(rules) > 1:
                warnings.append(
                    f"_redirects repeats the same rule for {source}"
                )

        exact_sources = {
            rule.source: rule
            for rule in redirects
            if "*" not in rule.source and ":" not in rule.source
        }
        for source, rule in exact_sources.items():
            target_path = urlsplit(rule.target).path
            if target_path in exact_sources:
                critical.append(
                    f"_redirects:{rule.line}: redirect chain detected "
                    f"({source} -> {target_path})"
                )
            if target_path.rstrip("/") == source.rstrip("/"):
                critical.append(
                    f"_redirects:{rule.line}: redirect loop detected "
                    f"({source} -> {target_path})"
                )

        for page in pages.values():
            if not page.canonical:
                continue
            public_url = canonical_for_file(root, page.path)
            if page.canonical == public_url:
                continue
            public_path = urlsplit(public_url).path
            canonical_path = urlsplit(page.canonical).path
            matching_rules = []
            for rule in redirects:
                matches, target = redirect_match(rule, public_path)
                if matches:
                    matching_rules.append((rule, urlsplit(target).path))
            correct_rules = [
                (rule, target)
                for rule, target in matching_rules
                if target.rstrip("/") == canonical_path.rstrip("/")
            ]
            relative = page.path.relative_to(root).as_posix()
            if not correct_rules:
                critical.append(
                    f"{relative}: legacy URL {public_path} lacks a redirect "
                    f"to canonical {canonical_path}"
                )
            elif not any(rule.status in {301, 308} for rule, _ in correct_rules):
                critical.append(
                    f"{relative}: legacy redirect to {canonical_path} must "
                    f"be permanent"
                )
            for refresh, line in page.refresh_values:
                refresh_url = extract_refresh_url(refresh)
                if (
                    refresh_url
                    and urlsplit(refresh_url).path.rstrip("/")
                    != canonical_path.rstrip("/")
                ):
                    critical.append(
                        f"{relative}:{line}: meta refresh destination "
                        f"{refresh_url!r} does not match canonical "
                        f"{page.canonical!r}"
                    )

    for stylesheet in sorted(iter_files(root, {".css"})):
        text = read_text(stylesheet)
        relative = stylesheet.relative_to(root).as_posix()
        for match in re.finditer(
            r"""(?i)url\(\s*(?P<quote>['"]?)(?P<url>.*?)(?P=quote)\s*\)""",
            text,
        ):
            value = match.group("url").strip()
            if not value or value.startswith("#"):
                continue
            line = text.count("\n", 0, match.start()) + 1
            asset_reference_count += 1
            if urlsplit(value).scheme.lower() == "http":
                critical.append(
                    f"{relative}:{line}: insecure CSS asset URL ({value})"
                )
            problem = local_url_problem(value)
            if problem:
                critical.append(
                    f"{relative}:{line}: local CSS asset URL {problem} "
                    f"({value})"
                )
            is_local, target = resolve_local_resource(
                root, stylesheet.resolve(), value
            )
            if is_local and target is None:
                critical.append(
                    f"{relative}:{line}: local CSS asset does not exist "
                    f"({value})"
                )

    unfinished_pattern = re.compile(
        r"(?i)\b(?:TODO|TBD|FIXME|CHANGEME)\b|"
        r"(?:https?://)?example\.com|test@example\.(?:com|org|net)"
    )
    public_source_extensions = {".css", ".html", ".js", ".json", ".xml"}
    for path in sorted(iter_files(root, public_source_extensions)):
        relative = path.relative_to(root).as_posix()
        for line_number, line in enumerate(read_text(path).splitlines(), start=1):
            if unfinished_pattern.search(line):
                critical.append(
                    f"{relative}:{line_number}: unfinished placeholder marker found"
                )

    for page in pages.values():
        text = read_text(page.path)
        if re.search(r'class=["\'][^"\']*\bmodel-card\b', text):
            disclosure_text = strip_html(text).casefold()
            if not (
                "not client case studies" in disclosure_text
                or "not presented as client case studies" in disclosure_text
                or "representative solution model" in disclosure_text
            ):
                critical.append(
                    f"{page.path.relative_to(root).as_posix()}: representative "
                    f"work is missing a clear case-study disclosure"
                )

    for legal_relative in ("privacy-policy/index.html", "terms/index.html"):
        legal_path = root / legal_relative
        if not legal_path.is_file():
            critical.append(f"{legal_relative}: required legal page is missing")
            continue
        match = re.search(
            r"(?i)Last\s+updated:\s*([A-Z][a-z]+\s+\d{1,2},\s+\d{4})",
            strip_html(read_text(legal_path)),
        )
        if not match:
            critical.append(
                f"{legal_relative}: missing parseable Last updated date"
            )
            continue
        try:
            legal_date = datetime.strptime(match.group(1), "%B %d, %Y").date()
        except ValueError:
            critical.append(
                f"{legal_relative}: invalid Last updated date {match.group(1)!r}"
            )
            continue
        if legal_date > date.today():
            critical.append(
                f"{legal_relative}: Last updated date is in the future "
                f"({match.group(1)})"
            )

    pricing_markers_validated = 0
    pricing_path = (root / "pricing" / "index.html").resolve()
    pricing_page = pages.get(pricing_path)
    if pricing_page is None:
        critical.append("pricing/index.html: required pricing page is missing")
    else:
        pricing_text = normalize_text(
            " ".join(pricing_page.visible_text_parts)
        )
        if not re.search(
            r"(?i)\bprices?\b.{0,80}\b(?:USD|US dollars)\b",
            pricing_text,
        ):
            critical.append(
                "pricing/index.html: pricing must clearly state that prices "
                "are in USD or US dollars"
            )

        expected_price_patterns = {
            **{
                marker: re.compile(
                    rf"{re.escape(marker)}\s+USD\b(?!\s*/\s*month)",
                    re.I,
                )
                for marker in EXPECTED_ONE_TIME_PRICES
            },
            **{
                marker: re.compile(
                    rf"{re.escape(marker)}\s*/\s*month\b",
                    re.I,
                )
                for marker in EXPECTED_MONTHLY_PRICES
            },
        }
        for marker, expected_pattern in sorted(
            expected_price_patterns.items()
        ):
            marker_count = len(
                re.findall(re.escape(marker), pricing_text)
            )
            if marker_count != 1:
                critical.append(
                    f"pricing/index.html: expected exactly one visible "
                    f"{marker} price marker, found {marker_count}"
                )
            elif not expected_pattern.search(pricing_text):
                cadence = (
                    "one-time price followed by USD"
                    if marker in EXPECTED_ONE_TIME_PRICES
                    else "monthly price followed by /month"
                )
                critical.append(
                    f"pricing/index.html: {marker} must remain a {cadence}"
                )
            else:
                pricing_markers_validated += 1

        found_visible_prices = set(
            re.findall(r"\$\d+(?:,\d{3})*(?:\.\d{1,2})?", pricing_text)
        )
        expected_visible_prices = (
            EXPECTED_ONE_TIME_PRICES | EXPECTED_MONTHLY_PRICES
        )
        for marker in sorted(
            found_visible_prices - expected_visible_prices
        ):
            critical.append(
                f"pricing/index.html: unexpected visible price marker "
                f"{marker}"
            )

    numerical_claim_pattern = re.compile(
        r"(?i)(?<![\w$])"
        r"(?:\d{1,3}(?:,\d{3})+|\d+(?:\.\d+)?)"
        r"\s*(?:\+\s*)?"
        r"(?:%|percent\b|years?\b|clients?\b|customers?\b|projects?\b|"
        r"business(?:es)?\b|leads?\b|revenue\b|roi\b|[x×]\b)"
    )
    numerical_claim_matches = 0
    for page in indexable_pages:
        visible_text = normalize_text(" ".join(page.visible_text_parts))
        matches = sorted(
            {normalize_text(match.group(0)) for match in numerical_claim_pattern.finditer(visible_text)},
            key=str.casefold,
        )
        if not matches:
            continue
        numerical_claim_matches += len(matches)
        warnings.append(
            f"{page.path.relative_to(root).as_posix()}: potential unsupported "
            f"numerical claim pattern(s): {', '.join(matches)}"
        )

    config_path = root / "_config.yml"
    if not config_path.is_file():
        warnings.append(
            "_config.yml: GitHub Pages exclusion configuration is missing"
        )
    else:
        deploy_excludes, config_errors = parse_github_pages_excludes(config_path)
        critical.extend(config_errors)

    artifact_paths: set[str] = set()
    for path in root.rglob("*"):
        try:
            relative_path = path.relative_to(root)
        except ValueError:
            continue
        if ".git" in relative_path.parts:
            continue
        if path.is_dir() and path.name in BUILD_ARTIFACT_DIRECTORIES:
            artifact_paths.add(relative_path.as_posix() + "/")
            continue
        if not path.is_file():
            continue
        if (
            path.name in BUILD_ARTIFACT_NAMES
            or path.suffix.lower() in BUILD_ARTIFACT_SUFFIXES
        ):
            artifact_paths.add(relative_path.as_posix())
        if len(relative_path.parts) == 1 and any(
            fnmatch(path.name.upper(), pattern.upper())
            for pattern in ROOT_INTERNAL_DOCUMENT_PATTERNS
        ):
            artifact_paths.add(relative_path.as_posix())
    for relative in collapse_artifact_paths(artifact_paths):
        if deploy_path_is_excluded(relative, deploy_excludes):
            excluded_artifact_count += 1
        else:
            warnings.append(
                f"{relative}: development or internal artifact is not "
                f"excluded from the GitHub Pages build"
            )

    text_files = sorted(iter_files(root, public_source_extensions))
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
    calendly_count = production_html.count(CALENDLY_URL)
    email_count = production_html.count(EMAIL_URL)
    linkedin_count = production_html.count(LINKEDIN_URL)
    if portal_count == 0:
        critical.append(f"required Client Portal URL is missing: {PORTAL_URL}")
    if formspree_count == 0:
        critical.append(f"required Formspree endpoint is missing: {FORMSPREE_URL}")
    if calendly_count == 0:
        critical.append(f"required Calendly URL is missing: {CALENDLY_URL}")
    if email_count == 0:
        critical.append(f"required email link is missing: {EMAIL_URL}")
    if linkedin_count == 0:
        critical.append(f"required LinkedIn URL is missing: {LINKEDIN_URL}")

    integration_urls = {
        value
        for page in pages.values()
        for value in (
            [anchor.href for anchor in page.anchors]
            + [form.action for form in page.forms if form.action]
        )
    }
    for value in sorted(integration_urls):
        parsed_value = urlsplit(value)
        scheme = parsed_value.scheme.lower()
        host = (parsed_value.hostname or "").lower()
        if scheme == "mailto" and value != EMAIL_URL:
            critical.append(
                f"unexpected mailto endpoint found: {value}"
            )
        elif host == "portal.rielart.com" and value.rstrip("/") != PORTAL_URL:
            critical.append(
                f"unexpected Client Portal endpoint variant found: {value}"
            )
        elif host == "formspree.io" and value.rstrip("/") != FORMSPREE_URL:
            critical.append(
                f"unexpected Formspree endpoint variant found: {value}"
            )
        elif host in {"calendly.com", "www.calendly.com"} and value != CALENDLY_URL:
            critical.append(
                f"unexpected Calendly endpoint variant found: {value}"
            )
        elif host in {"linkedin.com", "www.linkedin.com"} and value not in {
            LINKEDIN_URL,
            LINKEDIN_URL.rstrip("/"),
        }:
            critical.append(
                f"unexpected LinkedIn endpoint variant found: {value}"
            )
        elif host == "buy.stripe.com" and value not in EXPECTED_STRIPE_URLS:
            critical.append(
                f"unexpected Stripe Payment Link variant found: {value}"
            )

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
            f"Sitemap lastmod values checked: {len(sitemap_lastmods)}",
            f"Local and remote asset references checked: {asset_reference_count}",
            f"Images checked for alt text and dimensions: {image_count}",
            f"JSON-LD blocks checked: {json_ld_block_count}",
            f"Forms checked: {form_count}",
            f"Orphan indexable pages found: {len(orphan_pages)}",
            f"Approved visible pricing markers found: "
            f"{pricing_markers_validated}/6",
            f"Redirect rules checked: {len(redirects)}",
            f"GitHub Pages exclusions checked: {len(deploy_excludes)}",
            f"Internal artifact paths safely excluded: "
            f"{excluded_artifact_count}",
            f"Client Portal URL occurrences: {portal_count}",
            f"Formspree endpoint occurrences: {formspree_count}",
            f"Calendly URL occurrences: {calendly_count}",
            f"Approved email-link occurrences: {email_count}",
            f"Approved LinkedIn URL occurrences: {linkedin_count}",
            f"Approved Stripe Payment Links found: "
            f"{len(found_stripe_urls & EXPECTED_STRIPE_URLS)}/6",
            f"Potential unsupported numerical claims flagged: "
            f"{numerical_claim_matches}",
            f"Warnings: {len(warnings)}",
        ]
    )

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
