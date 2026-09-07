#!/usr/bin/env python3
"""Copy the repository release version into public metadata files."""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def synchronize(root=ROOT, expected_version=None):
    version = tomllib.loads((root / "release.toml").read_text(encoding="utf-8"))["version"]
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?", version):
        raise ValueError(f"Invalid release version: {version}")
    if expected_version and expected_version != version:
        raise ValueError("NEW_VERSION disagrees with release.toml; version stamping must run first")
    citation = root / "CITATION.cff"
    text, count = re.subn(r"(?m)^version:\s*.*$", f"version: {version}",
                         citation.read_text(encoding="utf-8"), count=1)
    if count != 1:
        raise ValueError("Could not update CITATION.cff version")
    citation.write_text(text, encoding="utf-8", newline="\n")
    status_path = root / "data/obelisk/release-status.json"
    status = json.loads(status_path.read_text(encoding="utf-8"))
    status["version"] = version
    status_path.write_text(json.dumps(status, indent=2, ensure_ascii=False) + "\n",
                           encoding="utf-8", newline="\n")
    for script in ("audit_obelisk.py", "generate_obelisk_catalog.py"):
        subprocess.run([sys.executable, str(root / "scripts" / script)], cwd=root, check=True)
    print(f"Synchronized release metadata and generated evidence to {version}")


if __name__ == "__main__":
    synchronize(expected_version=os.environ.get("NEW_VERSION"))
