#!/usr/bin/env python3
"""Generate release catalog and deterministic, LF-normalized source manifests."""

import argparse
import hashlib
import json
import tomllib

if __package__:
    from .audit_obelisk import ROOT, load_documents, write_or_check
    from .frontier_data import csv_rows, load_frontier, load_tracks
else:
    from audit_obelisk import ROOT, load_documents, write_or_check
    from frontier_data import csv_rows, load_frontier, load_tracks


def serialize(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def generate(root=ROOT):
    documents = load_documents(root)
    release = tomllib.loads((root / "release.toml").read_text(encoding="utf-8"))["version"]
    name = tomllib.loads((root / "zensical.toml").read_text(encoding="utf-8"))["project"]["site_name"]
    branches = documents["branches"]["branches"]
    catalog = {
        "version": release, "name": name, "release_state": "reference-candidate",
        "architecture": {
            "knowledge_trunks": len(branches),
            "life_pillars": len(documents["life-pillars"]["life_pillars"]),
            "formation_modes": len(documents["formation-modes"]["formation_modes"]),
            "mastery_dimensions": len(documents["mastery"]["dimensions"]),
        },
        "counts": {name: len(documents[name][name]) for name in ("modules", "nodes", "sources")},
        "branches": {
            branch["id"]: {
                family: sum(record.get("branch_id") == branch["id"] for record in documents[family][family])
                for family in ("modules", "nodes", "sources")
            } for branch in branches
        },
    }
    catalog["counts"].update({
        "source_links": len(documents["source-links"]["links"]),
        "life_competencies": len(documents["life-competencies"]["life_competencies"]),
        "all_souls_prompts": len(documents["backtests"]["sets"]["all_souls_holdout"]),
    })
    outputs = {"data/obelisk/catalog.json": serialize(catalog)}
    frontier = load_frontier(root)
    tracks = load_tracks(root)
    program = {
        "version": release,
        "name": name,
        "legacy_technical_program_weeks": sum(len(csv_rows(root / "data" / name)) for name in
                                             ("wave-1-weeks.csv", "wave-2-weeks.csv", "wave-4-weeks.csv"))
                                          + max(track["weeks"] for track in tracks.values()),
        "frontier_targets": len(frontier["technologies"]),
        "frontier_tracks": [{"code": code, "name": track["name"],
                             "count": sum(row["track"] == code for row in frontier["technologies"])}
                            for code, track in tracks.items()],
        "obelisk": catalog,
    }
    outputs["data/frontier-100.json"] = serialize(frontier)
    outputs["data/program.json"] = serialize(program)
    excluded = {"site", ".git", ".venv", "__pycache__", ".pytest_cache", ".ruff_cache", "archive",
                "open-frontier-curriculum-obelisk-v0.6.0", "open-frontier-judgment-discovery-files"}
    manifest_paths = {"BUILD_MANIFEST.json", "data/obelisk/build-manifest.json",
                      "RELEASE_READINESS.md", "AGENT_STATE.md"}
    files = {}
    roots = [root / name for name in ("docs", "data", "schemas", "scripts", "tests", "rfcs", ".github")]
    paths = list(root.glob("*"))
    for directory in roots:
        paths.extend(directory.rglob("*"))
    for path in sorted(set(paths), key=lambda item: item.relative_to(root).as_posix()):
        relative = path.relative_to(root)
        name = relative.as_posix()
        if not path.is_file() or excluded.intersection(relative.parts) or name in manifest_paths:
            continue
        binary = path.suffix in {".jpg", ".png", ".webp", ".gif"}
        if not binary and path.name not in {".python-version", ".gitignore", ".gitattributes", ".editorconfig", "CODEOWNERS"} and path.suffix not in {".md", ".json", ".toml", ".py", ".csv", ".yml", ".yaml", ".cff", ".css", ".js", ".lock"}:
            continue
        payload = outputs[name].encode("utf-8") if name in outputs else path.read_bytes()
        files[name] = hashlib.sha256(payload if binary else payload.replace(b"\r\n", b"\n")).hexdigest()
    outputs["data/obelisk/build-manifest.json"] = serialize({
        "algorithm": "sha256", "normalization": "CRLF-to-LF", "files": {
            name: digest for name, digest in files.items() if name.startswith("data/obelisk/")
        },
    })
    outputs["BUILD_MANIFEST.json"] = serialize({
        "algorithm": "sha256", "normalization": "CRLF-to-LF for text; raw bytes for images", "version": release,
        "scope": "Owned source, configuration and generated docs; excludes import artifacts, reports (including RELEASE_READINESS.md), AGENT_STATE.md, caches and site output",
        "files": files,
    })
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale = write_or_check(ROOT, generate(), args.check)
    if args.check and stale:
        print("Catalog/manifest drift: " + ", ".join(stale))
        return 1
    print("Catalog and manifests " + ("verified" if args.check else "generated"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
