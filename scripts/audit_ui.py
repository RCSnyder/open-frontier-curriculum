#!/usr/bin/env python3
"""UI structure checks for the Markdown source and built Zensical site.

This catches markup patterns that are valid Markdown but render poorly in card
layouts, plus a small set of accessibility and responsive-design invariants.
It does not replace browser review.
"""

from __future__ import annotations

from argparse import ArgumentParser
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
import tomllib

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CSS = DOCS / "stylesheets" / "extra.css"
errors: list[str] = []
warnings: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def card_blocks(text: str):
    pattern = re.compile(
        r'<div\s+class="[^"]*\bgrid\b[^"]*\bcards\b[^"]*"\s+markdown>\s*(.*?)\s*</div>',
        re.S,
    )
    yield from pattern.finditer(text)


# Source checks -------------------------------------------------------------
for path in sorted(DOCS.rglob("*.md")):
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)
    for block in card_blocks(text):
        body = block.group(1)
        if re.search(r"(?m)^\s*-\s+#{1,6}\s+", body):
            fail(f"{rel}: heading used as a card-list item title")
        if re.search(r"(?m)^\s{2,}[^\n`]*\s\|\s[^\n]*$", body):
            warn(f"{rel}: pipe-delimited card copy; use semantic metadata spans")

for path in sorted((DOCS / "03-specializations").glob("*.md")):
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)
    if path.name == "README.md":
        if text.count('class="ofc-card-meta"') != 7:
            fail("Specialization index must expose metadata for all seven tracks")
        if text.count("24 weeks") != 7:
            fail("Specialization index must show 24 weeks on all seven tracks")
    else:
        if 'class="grid cards ofc-track-summary"' not in text:
            fail(f"{rel}: missing specialization summary grid")
        if "## Sequence" in text:
            fail(f"{rel}: empty Sequence wrapper heading is not allowed")
        if "## Phase:" in text:
            fail(f"{rel}: phase labels should be direct section headings")

css = CSS.read_text(encoding="utf-8") if CSS.exists() else ""
for required in [
    ":focus-visible",
    "prefers-reduced-motion",
    "max-width: 44rem",
    '[data-md-color-scheme="slate"] .ofc-a',
    '--ofc-heading: #f8fafc',
    '--ofc-muted: #bdc8d3',
    '--ofc-link: #6ee7d8',
    '--md-primary-fg-color: #123f3b',
    '.md-search__input::placeholder',
    ".ofc-track-grid.grid",
    ".ofc-card-meta",
]:
    if required not in css:
        fail(f"CSS missing UI invariant: {required}")

try:
    cfg = tomllib.loads((ROOT / "zensical.toml").read_text(encoding="utf-8"))
    if cfg.get("project", {}).get("theme", {}).get("font") is not False:
        fail("Zensical theme must use system fonts (font = false)")
except Exception as exc:
    fail(f"Could not parse zensical.toml during UI audit: {exc}")


# Built-site checks ---------------------------------------------------------
class PageAudit(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.viewport = False
        self.h1 = 0
        self.empty_heading_stack: list[tuple[str, list[str]]] = []
        self.empty_headings: list[str] = []
        self.grid_cards_depth = 0
        self.heading_in_cards = False
        self.extra_css = False

    def handle_starttag(self, tag, attrs):
        attrs_d = dict(attrs)
        if tag == "meta" and attrs_d.get("name") == "viewport":
            self.viewport = True
        if tag == "link" and "stylesheets/extra.css" in attrs_d.get("href", ""):
            self.extra_css = True
        classes = set(attrs_d.get("class", "").split())
        if tag == "div" and {"grid", "cards"}.issubset(classes):
            self.grid_cards_depth += 1
        if tag == "h1":
            self.h1 += 1
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.empty_heading_stack.append((tag, []))
            if self.grid_cards_depth:
                self.heading_in_cards = True

    def handle_data(self, data):
        if self.empty_heading_stack:
            self.empty_heading_stack[-1][1].append(data)

    def handle_endtag(self, tag):
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"} and self.empty_heading_stack:
            htag, chunks = self.empty_heading_stack.pop()
            if not "".join(chunks).strip():
                self.empty_headings.append(htag)
        if tag == "div" and self.grid_cards_depth:
            # HTMLParser has no DOM stack. This is conservative: card grids in
            # our source aren't nested inside other divs after build.
            self.grid_cards_depth -= 1


def audit_site(site: Path) -> None:
    html_files = sorted(site.rglob("*.html"))
    if not html_files:
        fail(f"Built site contains no HTML: {site}")
        return
    for path in html_files:
        parser = PageAudit()
        try:
            parser.feed(path.read_text(encoding="utf-8"))
        except UnicodeDecodeError:
            fail(f"Built page is not UTF-8: {path.relative_to(ROOT)}")
            continue
        rel = path.relative_to(ROOT)
        if not parser.viewport:
            fail(f"{rel}: missing viewport meta tag")
        if not parser.extra_css:
            fail(f"{rel}: custom UI stylesheet not linked")
        if parser.h1 != 1:
            warn(f"{rel}: expected one h1, found {parser.h1}")
        if parser.empty_headings:
            fail(f"{rel}: empty headings: {', '.join(parser.empty_headings)}")
        if parser.heading_in_cards:
            fail(f"{rel}: heading element found inside card grid")


parser = ArgumentParser()
parser.add_argument("--site", type=Path, help="Optional built Zensical site directory")
args = parser.parse_args()
if args.site:
    audit_site(args.site.resolve())

if errors:
    print("UI AUDIT FAILED")
    for item in errors:
        print(" -", item)
else:
    print("UI AUDIT PASSED")

print(f"UI WARNINGS: {len(warnings)}")
for item in warnings[:50]:
    print(" -", item)
if len(warnings) > 50:
    print(f" - ... {len(warnings)-50} more")

sys.exit(1 if errors else 0)
