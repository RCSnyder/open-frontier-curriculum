#!/usr/bin/env python3
"""Lightweight house-style checks for Markdown prose.

The linter enforces a small set of high-confidence rules and reports soft
readability signals. It does not claim ASD-STE100 or AP Stylebook compliance.
"""

from __future__ import annotations

from pathlib import Path
import argparse
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

# Narrative files receive sentence-length checks. Reference schemas, generated
# technology pages, module problem banks, and bibliography pages only receive
# hard anti-pattern checks.
NARRATIVE_PREFIXES = (
    ROOT / "README.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "DESIGN.md",
    ROOT / "STYLE.md",
    DOCS / "index.md",
    DOCS / "README.md",
    DOCS / "00-start-here",
    DOCS / "01-program",
    DOCS / "03-specializations" / "README.md",
    DOCS / "04-integration" / "README.md",
    DOCS / "05-frontier" / "README.md",
    DOCS / "06-proof-of-work" / "README.md",
    DOCS / "07-resources" / "README.md",
    DOCS / "08-community",
)

# These are high-confidence editorial patterns from the project house style and
# tropes.fyi. Technical terms with real domain meanings are not banned.
HARD_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("em dash", re.compile("—")),
    # ("smart double quote", re.compile("[""]")),
    ("decorative unicode arrow", re.compile("→")),
    ("filler: it's worth noting", re.compile(r"\bit(?:'|’)s worth noting\b", re.I)),
    ("filler: it bears mentioning", re.compile(r"\bit bears mentioning\b", re.I)),
    ("filler transition", re.compile(r"\b(?:importantly|interestingly|notably),", re.I)),
    ("fake suspense", re.compile(r"\bhere(?:'|’)s (?:the thing|the catch|the kicker)\b", re.I)),
    ("teacher voice", re.compile(r"\blet(?:'|’)s (?:break this down|unpack|explore|dive)\b", re.I)),
    ("signposted conclusion", re.compile(r"\b(?:in conclusion|to sum up|in summary)\b", re.I)),
    ("patronizing analogy lead", re.compile(r"\bthink of it as\b", re.I)),
    ("futurist sales lead", re.compile(r"\bimagine a world where\b", re.I)),
    ("AI stock word: delve", re.compile(r"\bdelv(?:e|es|ed|ing)\b", re.I)),
    ("pompous copula: serves as", re.compile(r"\bserves as\b", re.I)),
    ("promotional word: seamless", re.compile(r"\bseamless(?:ly)?\b", re.I)),
    ("promotional word: unprecedented", re.compile(r"\bunprecedented\b", re.I)),
]

SOFT_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("negative parallelism", re.compile(r"\b(?:it is|it's|this is|the [^.!?]{1,30} is) not\b[^.!?]{0,80}\b(?:but|it is|it's)\b", re.I)),
    ("marketing verb: leverage", re.compile(r"\b(?:leverage|leverages|leveraged|leveraging)\b", re.I)),
    ("magic adverb", re.compile(r"\b(?:quietly|deeply|fundamentally|remarkably|arguably)\b", re.I)),
    ("ornate stock noun", re.compile(r"\b(?:tapestry|landscape|synergy)\b", re.I)),
]

ALLOWED_TITLE_CASE = {
    "Open Frontier Curriculum",
    "Associated Press Stylebook",
    "ASD-STE100 Simplified Technical English",
}


def markdown_files() -> list[Path]:
    """Return project-authored Markdown only."""
    excluded_parts = {
        ".git",
        ".venv",
        ".cache",
        ".pytest_cache",
        "__pycache__",
        "archive",
        "node_modules",
        "site",
    }
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not excluded_parts.intersection(path.relative_to(ROOT).parts)
    )


def is_narrative(path: Path) -> bool:
    for prefix in NARRATIVE_PREFIXES:
        if prefix.is_file() and path == prefix:
            return True
        if prefix.is_dir() and path.is_relative_to(prefix):
            return True
    return False


def strip_non_prose(text: str) -> str:
    # YAML front matter.
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    # Fenced code blocks.
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    # HTML blocks/tags.
    text = re.sub(r"<[^>]+>", " ", text)
    # Markdown tables: skip whole rows.
    lines = []
    for line in text.splitlines():
        if line.lstrip().startswith("|"):
            continue
        if re.match(r"^\s*[-*+]\s+", line):
            # Keep bullet prose, but remove marker and bold field label.
            line = re.sub(r"^\s*[-*+]\s+", "", line)
        line = re.sub(r"^#{1,6}\s+", "", line)
        # Links -> visible text.
        line = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", line)
        # Inline code is a term, not prose syntax.
        line = re.sub(r"`([^`]+)`", r"\1", line)
        # Bold/italics.
        line = line.replace("**", "").replace("__", "")
        lines.append(line)
    return "\n".join(lines)


def sentence_word_counts(text: str) -> list[int]:
    prose = strip_non_prose(text)
    # Markdown line breaks often separate compact reference statements. Treat
    # them as sentence boundaries for length checks.
    prose = re.sub(r"\n+", ". ", prose)
    chunks = re.split(r"(?<=[.!?])\s+", prose)
    counts: list[int] = []
    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk or not re.search(r"[.!?]$", chunk):
            continue
        words = re.findall(r"\b[A-Za-z0-9][A-Za-z0-9'/-]*\b", chunk)
        if words:
            counts.append(len(words))
    return counts


def title_case_heading_issues(path: Path, text: str) -> list[tuple[int, str]]:
    issues = []
    small = {"a", "an", "and", "as", "at", "by", "for", "from", "in", "of", "on", "or", "the", "to", "with"}
    for n, line in enumerate(text.splitlines(), 1):
        m = re.match(r"^#{2,6}\s+(.+?)\s*$", line)
        if not m:
            continue
        heading = re.sub(r"[`*_]", "", m.group(1)).strip()
        if heading in ALLOWED_TITLE_CASE or heading.endswith("?"):
            continue
        words = re.findall(r"[A-Za-z][A-Za-z'-]*", heading)
        content = [w for w in words if w.lower() not in small]
        if len(content) >= 3 and all(w[0].isupper() for w in content):
            issues.append((n, heading))
    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="Fail on soft warnings and long narrative sentences.")
    args = parser.parse_args()

    hard: list[str] = []
    soft: list[str] = []
    total_sentences = 0
    long_sentences = 0

    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)

        if path != ROOT / "STYLE.md":
            for label, pattern in HARD_PATTERNS:
                for m in pattern.finditer(text):
                    line = text.count("\n", 0, m.start()) + 1
                    hard.append(f"{rel}:{line}: {label}: {m.group(0)!r}")

        if is_narrative(path) and path != ROOT / "STYLE.md":
            for label, pattern in SOFT_PATTERNS:
                for m in pattern.finditer(strip_non_prose(text)):
                    soft.append(f"{rel}: {label}: {m.group(0)!r}")

            for line, heading in title_case_heading_issues(path, text):
                soft.append(f"{rel}:{line}: title-case heading: {heading!r}")

            counts = sentence_word_counts(text)
            total_sentences += len(counts)
            for count in counts:
                if count > 32:
                    long_sentences += 1
                    soft.append(f"{rel}: sentence over 32 words ({count})")

    if hard:
        print("PROSE LINT FAILED")
        for item in hard:
            print(" -", item)
    else:
        print("PROSE LINT PASSED")

    if soft:
        print(f"SOFT WARNINGS: {len(soft)}")
        for item in soft[:60]:
            print(" -", item)
        if len(soft) > 60:
            print(f" - ... {len(soft) - 60} more")
    else:
        print("SOFT WARNINGS: 0")

    if total_sentences:
        print(f"Narrative sentences checked: {total_sentences}; over 32 words: {long_sentences}")

    if hard or (args.strict and soft):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
