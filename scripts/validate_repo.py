#!/usr/bin/env python3
"""Validate Obelisk and preserved Open Frontier repository contracts."""

import csv
import json
import re
import subprocess
import sys
import tomllib
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

if __package__:
    from .audit_obelisk import graph_findings, load_documents
else:
    from audit_obelisk import graph_findings, load_documents

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def frontier_errors(root=ROOT):
    errors = []
    with (root / "data/frontier-100.csv").open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    technologies = json.loads((root / "data/frontier-100.json").read_text(encoding="utf-8"))["technologies"]
    try:
        ranks = [int(row["Rank"]) for row in rows]
    except (ValueError, KeyError):
        return ["Frontier CSV ranks must be integers 1..100"]
    if sorted(ranks) != list(range(1, 101)):
        errors.append("Frontier CSV ranks must be unique 1..100")
    if sorted(row["id"] for row in technologies) != list(range(1, 101)):
        errors.append("Frontier JSON IDs must be unique 1..100")
    indexed = {row["id"]: row for row in technologies}
    allowed = {"AI-AS", "ROB", "ENE", "MAT", "BIO", "NEU", "SPA"}
    pages = sorted((root / "docs/05-frontier/technologies").glob("*.md"))
    if len(pages) != 100:
        errors.append(f"Expected 100 preserved Frontier pages, got {len(pages)}")
    page_records = {}
    for page in pages:
        text = page.read_text(encoding="utf-8")
        try:
            metadata = yaml.safe_load(text.split("---", 2)[1])
            identity = metadata["rank"]
            if type(identity) is not int or metadata["feasibility"] not in set("ABCDE") or metadata["primary_track"] not in allowed:
                raise ValueError("Invalid frontier metadata")
        except (IndexError, KeyError, TypeError, ValueError, yaml.YAMLError):
            errors.append(f"Malformed Frontier front matter: {page.name}")
            continue
        if identity in page_records:
            errors.append(f"Duplicate Frontier page rank: {identity}")
        page_records[identity] = (metadata["feasibility"], metadata["primary_track"])
    for row in rows:
        identity = int(row["Rank"])
        value = indexed.get(identity, {})
        if row["Class"] not in set("ABCDE") or row["Primary track"] not in allowed:
            errors.append(f"Invalid Frontier class/track: {identity}")
        if (value.get("class"), value.get("track")) != (row["Class"], row["Primary track"]):
            errors.append(f"Frontier JSON/CSV drift: {identity}")
        title = " ".join(row["Frontier technology"].replace("\u2014", " - ").split())
        if value.get("title") != title or value.get("bottleneck") != row["Dominant bottleneck"]:
            errors.append(f"Frontier title/bottleneck drift: {identity}")
        if page_records.get(identity) != (row["Class"], row["Primary track"]):
            errors.append(f"Frontier Markdown/CSV drift: {identity}")
    program = json.loads((root / "data/program.json").read_text(encoding="utf-8"))
    if {track["code"] for track in program["frontier_tracks"]} != allowed:
        errors.append("Seven specialization codes must be preserved")
    for track in program["frontier_tracks"]:
        if track["count"] != sum(row["Primary track"] == track["code"] for row in rows):
            errors.append(f"Specialization count drift: {track['code']}")
        if not (root / "data/tracks" / f"{track['code']}.csv").is_file():
            errors.append(f"Missing specialization sequence: {track['code']}")
    return errors

def markdown_errors(root=ROOT):
    errors = []
    docs = root / "docs"
    for page in sorted(docs.rglob("*.md")) + sorted(root.glob("*.md")):
        text = page.read_text(encoding="utf-8")
        text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
        for raw in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            href = raw.split("#", 1)[0].strip()
            if not href or urlsplit(href).scheme:
                continue
            target = (page.parent / unquote(href)).resolve()
            if not target.exists():
                errors.append(f"{page.relative_to(root)}: broken link {raw}")
            elif page.is_relative_to(docs) and not target.is_relative_to(docs):
                errors.append(f"{page.relative_to(root)}: published link escapes docs: {raw}")
    return errors

def main():
    errors = []
    result = subprocess.run([sys.executable, str(ROOT / "scripts/validate_obelisk.py")], cwd=ROOT, check=False)
    if result.returncode:
        errors.append("Obelisk structural validation failed")
    documents = load_documents(ROOT)
    for finding in graph_findings(documents, ROOT):
        if finding["severity"] == "error":
            errors.append(json.dumps(finding))
    errors.extend(frontier_errors())
    errors.extend(markdown_errors())
    for relative, count in (("textbook-library-130.csv", 130), ("wave-1-weeks.csv", 48),
                            ("wave-2-weeks.csv", 52), ("wave-4-weeks.csv", 12)):
        with (ROOT / "data" / relative).open(encoding="utf-8-sig", newline="") as handle:
            if len(list(csv.DictReader(handle))) != count:
                errors.append(f"Legacy row-count drift: {relative}")
    config = tomllib.loads((ROOT / "zensical.toml").read_text(encoding="utf-8"))
    pending = [config["project"]["nav"]]
    while pending:
        value = pending.pop()
        if isinstance(value, list):
            pending.extend(value)
        elif isinstance(value, dict):
            pending.extend(value.values())
        elif isinstance(value, str) and not (DOCS / value).is_file():
            errors.append(f"Missing navigation target: {value}")
    release = tomllib.loads((ROOT / "release.toml").read_text(encoding="utf-8"))["version"]
    program = json.loads((ROOT / "data/program.json").read_text(encoding="utf-8"))
    citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    if program["version"] != release or f"version: {release}" not in citation:
        errors.append("Release metadata drift; run scripts/sync_release_version.py")
    if not (ROOT / "uv.lock").is_file():
        errors.append("Frozen uv.lock is required")
    if errors:
        print("REPOSITORY VALIDATION FAILED")
        for error in errors:
            print(" -", error)
        return 1
    print("REPOSITORY VALIDATION PASSED: graph, links, navigation, Frontier 100, seven tracks, legacy counts, release")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
