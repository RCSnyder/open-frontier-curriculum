#!/usr/bin/env python3
"""Run candidate engineering gates and record their actual outputs, not scholarly efficacy."""

import hashlib
import json
import platform
import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMMANDS = [
    ["uv", "sync", "--frozen"],
    ["uv", "run", "--frozen", "ruff", "check", "scripts", "tests"],
    ["uv", "run", "--frozen", "python", "-m", "compileall", "-q", "scripts", "tests"],
    ["uv", "run", "--frozen", "python", "-m", "unittest", "discover", "-s", "tests"],
    ["uv", "run", "--frozen", "python", "scripts/validate_repo.py"],
    ["uv", "run", "--frozen", "python", "scripts/audit_obelisk.py", "--check"],
    ["uv", "run", "--frozen", "python", "scripts/generate_obelisk_catalog.py", "--check"],
    ["uv", "run", "--frozen", "python", "scripts/lint_prose.py", "--strict"],
    ["uv", "run", "--frozen", "python", "scripts/audit_ui.py"],
    ["uv", "run", "--frozen", "python", "scripts/audit_contrast.py"],
    ["uv", "run", "--frozen", "python", "scripts/check_saturation.py"],
    ["uv", "run", "--frozen", "python", "scripts/check_obelisk_release_readiness.py", "--claim", "candidate"],
    ["uv", "run", "--frozen", "python", "scripts/build_docs.py"],
    ["uv", "run", "--frozen", "python", "scripts/audit_ui.py", "--site", ".verification/site"],
]


def main():
    records = []
    for command in COMMANDS:
        print("Running: " + " ".join(command), flush=True)
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True,
                                encoding="utf-8", errors="replace", check=False)
        records.append({"command": command, "exit_code": result.returncode,
                        "stdout": result.stdout, "stderr": result.stderr})
        print("PASS" if result.returncode == 0 else "FAIL", flush=True)
    passed = all(record["exit_code"] == 0 for record in records)
    version = tomllib.loads((ROOT / "release.toml").read_text(encoding="utf-8"))["version"]
    manifest = (ROOT / "BUILD_MANIFEST.json").read_bytes()
    report = {
        "schema_version": 1, "release_version": version,
        "engineering_status": "pass" if passed else "fail",
        "scholarly_status": "not-reference-grade", "empirical_claim_status": "not-established",
        "python": platform.python_version(), "platform": platform.system(),
        "manifest_sha256": hashlib.sha256(manifest).hexdigest(),
        "scope": "Local engineering checks; remote CI, full external links and human scholarly review are not covered",
        "gates": records,
    }
    directory = ROOT / "reports"
    directory.mkdir(exist_ok=True)
    (directory / "release-verification.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    lines = ["# Release readiness", "", f"Candidate: **{version}**.", "",
             f"Local engineering gates: **{'PASS' if passed else 'FAIL'}**.",
             "Scholarly reference-grade readiness: **BLOCKED**. Empirical efficacy: **NOT ESTABLISHED**.", "",
             "## Verification", "", "| Command | Result |", "| --- | --- |"]
    lines += [f"| `{' '.join(record['command'])}` | {'PASS' if record['exit_code'] == 0 else 'FAIL'} |"
              for record in records]
    lines += ["", f"Runtime: Python {report['python']} on {report['platform']}.", "",
              f"Manifest SHA-256: `{report['manifest_sha256']}`.", "",
              "Exact commands, exit codes and output: [verification report](reports/release-verification.json).",
              "The manifest is LF-normalized source integrity, not a signed release or proof of learning.", "",
              "## Claim boundaries", "",
              "All 448 module/node targets have conservative documentary maturity records.",
              "Teaching and assessment routes do not establish learner mastery or scholarly completeness.",
              "Most source records, node prerequisites, external holdouts, professional scope and",
              "longitudinal outcomes still require independent work. No whole-life superiority is claimed.", "",
              "Hosted CI and remote deployment were not executed. Browser inspection is recorded separately",
              "in the operational state. Full external-link availability is not a gate in this local run.", "",
              "## Review order", "",
              "1. [Architecture audit](ARCHITECTURE_AUDIT.md)",
              "2. [Content maturity](CONTENT_MATURITY.md)",
              "3. [Source maturity](SOURCE_MATURITY.md)",
              "4. [Reconciliation RFC](rfcs/curriculum/0001-obelisk-reconciliation.md)",
              "5. [Remaining research and authored work](NEXT_RESEARCH.md)",
              "6. [Operational state](AGENT_STATE.md)", "",
              "No commit, push, tag, remote PR or history rewrite is performed by this runner.", ""]
    (ROOT / "RELEASE_READINESS.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())