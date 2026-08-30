#!/usr/bin/env python3
"""Check the explicit Open Frontier Curriculum palette against WCAG contrast.

The site deliberately overrides Zensical's slate foreground ladder. This test
keeps the high-traffic semantic colors above WCAG AA and keeps the primary
reading colors at AAA where practical.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CSS = ROOT / "docs" / "stylesheets" / "extra.css"
text = CSS.read_text(encoding="utf-8")


def rgb(value: str) -> tuple[float, float, float]:
    value = value.lstrip("#")
    if len(value) != 6:
        raise ValueError(value)
    return tuple(int(value[i:i+2], 16) / 255 for i in (0, 2, 4))  # type: ignore[return-value]


def channel(value: float) -> float:
    return value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4


def luminance(value: str) -> float:
    r, g, b = rgb(value)
    return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b)


def contrast(fg: str, bg: str) -> float:
    a, b = luminance(fg), luminance(bg)
    return (max(a, b) + 0.05) / (min(a, b) + 0.05)


def slate_var(name: str) -> str:
    match = re.search(
        r'\[data-md-color-scheme="slate"\]\s*\{(?P<body>.*?)\n\}', text, re.S
    )
    if not match:
        raise RuntimeError("slate palette block missing")
    item = re.search(rf"{re.escape(name)}\s*:\s*(#[0-9a-fA-F]{{6}})", match.group("body"))
    if not item:
        raise RuntimeError(f"slate variable missing or not a hex color: {name}")
    return item.group(1).lower()


errors: list[str] = []
checks = [
    ("body text / page", "--ofc-text", "--md-default-bg-color", 7.0),
    ("heading / page", "--ofc-heading", "--md-default-bg-color", 7.0),
    ("muted copy / page", "--ofc-muted", "--md-default-bg-color", 7.0),
    ("link / page", "--ofc-link", "--md-default-bg-color", 7.0),
    ("body text / card", "--ofc-text", "--ofc-surface", 7.0),
    ("heading / card", "--ofc-heading", "--ofc-surface", 7.0),
    ("muted copy / card", "--ofc-muted", "--ofc-surface", 7.0),
    ("link / card", "--ofc-link", "--ofc-surface", 7.0),
    ("header text / primary surface", "--ofc-heading", "--md-primary-fg-color", 7.0),
]

print("Dark-mode contrast")
for label, fg_name, bg_name, minimum in checks:
    fg, bg = slate_var(fg_name), slate_var(bg_name)
    ratio = contrast(fg, bg)
    print(f" - {label}: {ratio:.2f}:1 ({fg} on {bg})")
    if ratio < minimum:
        errors.append(f"{label}: {ratio:.2f}:1 is below {minimum:.1f}:1")

header_ratio = contrast("#eef4f8", slate_var("--md-primary-fg-color"))
print(f" - header chrome: {header_ratio:.2f}:1 (#eef4f8 on {slate_var('--md-primary-fg-color')})")
if header_ratio < 7.0:
    errors.append(f"header chrome: {header_ratio:.2f}:1 is below 7.0:1")

search_ratio = contrast("#bdc8d3", "#18232e")
print(f" - search placeholder: {search_ratio:.2f}:1 (#bdc8d3 on #18232e)")
if search_ratio < 7.0:
    errors.append(f"search placeholder: {search_ratio:.2f}:1 is below 7.0:1")

badge_pairs = [
    ("A badge", "#78dbb3", "#12382d"),
    ("B badge", "#8bcaff", "#15354d"),
    ("C badge", "#f4d06f", "#3a3018"),
    ("D badge", "#ffaaaa", "#452525"),
    ("E badge", "#d7b0f4", "#372344"),
]
for label, fg, bg in badge_pairs:
    ratio = contrast(fg, bg)
    print(f" - {label}: {ratio:.2f}:1")
    if ratio < 4.5:
        errors.append(f"{label}: {ratio:.2f}:1 is below 4.5:1")

if errors:
    print("CONTRAST AUDIT FAILED")
    for error in errors:
        print(" -", error)
    sys.exit(1)

print("CONTRAST AUDIT PASSED")
