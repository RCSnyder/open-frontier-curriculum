#!/usr/bin/env python3
"""Copy the repository release version into public metadata files."""
from __future__ import annotations
import json
import os
import re
import tomllib
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
with (ROOT / "release.toml").open("rb") as fh:
    configured_version = tomllib.load(fh)["version"]
version = os.environ.get("NEW_VERSION", configured_version)
if not re.fullmatch(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?", version):
    raise SystemExit(f"Invalid release version: {version}")
citation = ROOT / "CITATION.cff"
text = citation.read_text(encoding="utf-8")
text, count = re.subn(r"(?m)^version:\s*.*$", f"version: {version}", text, count=1)
if count != 1:
    raise SystemExit("Could not update CITATION.cff version")
citation.write_text(text, encoding="utf-8")
program_path = ROOT / "data" / "program.json"
program = json.loads(program_path.read_text(encoding="utf-8"))
program["version"] = version
program_path.write_text(json.dumps(program, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Synchronized release metadata to {version}")
