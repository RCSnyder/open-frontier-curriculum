#!/usr/bin/env python3
"""One-time, additive reconciliation of the staged 0.6 import with preserved prose."""

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "obelisk"
BASE = "8b98ed1"
TS_DELETION = [
    "Without quantifiers, counterexamples and proof, specifications cannot distinguish testing from necessity.",
    "Without local linearization and accumulation, continuous physical models and their approximations cannot be reconstructed.",
    "Without rank, projection and conditioning, inverse problems and multivariate models hide non-identifiability.",
    "Without state evolution, equilibria and stability, feedback and time-dependent physical systems become opaque.",
    "Without conditional probability and distributions, uncertain evidence cannot support calibrated decisions.",
    "Without estimands, confounding and uncertainty, observational association is mistaken for intervention effects.",
    "Without numerical error and reproducible computation, a plausible simulation cannot be independently checked.",
    "Without constraints, duality and optimality conditions, designs confuse feasible improvement with a defensible optimum.",
    "Without sampling, spectra and information limits, measurements and communication hide irreversible information loss.",
    "Without observability, estimation and stability, closed-loop systems can fail despite individually accurate components.",
    "Without calibration, error budgets and experimental design, model agreement can be an instrument artifact.",
    "Without conservation and electromagnetic fields, machines and circuits lose their physical constraint model.",
    "Without entropy, free energy and statistical ensembles, energy conversion and material behavior are misbounded.",
    "Without quantum states and material electronic structure, device-scale explanations become unsupported analogies.",
    "Without bonding, kinetics and processing-structure-property relations, materials choices cannot be defended.",
    "Without circuits, timing and embedded constraints, sensing and actuation cannot be made reliable in hardware.",
    "Without stress, flow, geometry and stability, mechanical designs conceal failure under real loads.",
    "Without cellular mechanisms and regulation, biological interventions lack a causal substrate.",
    "Without inheritance, selection and system interaction, biological predictions ignore adaptation and population variation.",
    "Without neural and physiological mechanisms, human-interface and health claims lose their biological bounds.",
    "Without yield, variation, throughput and quality control, a laboratory success is mistaken for scalable production.",
    "Without hazard analysis, reliability and security, component performance can conceal unacceptable system risk.",
]


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def reconcile():
    modules = load("modules.json")
    pages = sorted((ROOT / "docs" / "02-core" / "wave-1").glob("[0-9]*.md"))
    pages += sorted((ROOT / "docs" / "02-core" / "wave-2").glob("[0-9]*.md"))
    technical = [module for module in modules["modules"] if module["branch_id"] == "TS"]
    if len(pages) != 22 or len(technical) != 22:
        raise ValueError("Expected exactly 22 preserved technical teaching sequences")
    evidence_path = DATA / "content-evidence.json"
    evidence = load("content-evidence.json") if evidence_path.exists() else {
        "schema_version": 1,
        "review_scope": "Documentary teaching/assessment inspection, not learner or expert validation",
        "targets": {},
    }
    for module, page, deletion in zip(technical, pages, TS_DELETION, strict=True):
        text = page.read_text(encoding="utf-8")
        if not all(heading in text for heading in ("## Weeks", "## Exit gate", "## Transfer problems")):
            raise ValueError(f"Incomplete teaching sequence: {page}")
        module["core_concepts"] = module.get("core_concepts") or re.findall(
            r"^\*\*Know:\*\* (.+)$", text, re.MULTILINE
        )
        module["deletion_reason"] = module.get("deletion_reason") or deletion
        module["exposition_path"] = page.relative_to(ROOT).as_posix()
        evidence["targets"].setdefault(module["id"], {
            "teaching_path": module["exposition_path"],
            "teaching_review": "Preserved weekly readings, reconstruction, execution and defense tasks inspected",
            "assessment_path": module["exposition_path"],
            "assessment_review": "Exit and transfer problems present; independent grading calibration pending",
        })
    dump(DATA / "modules.json", modules)
    dump(evidence_path, evidence)

    interfaces = load("interfaces.json")
    corrected = {
        "IF-017": (["ML02"], "ML02 Attention, working memory and cognitive load"),
        "IF-018": (["ML06", "ML12"], "ML06 Expertise; ML12 Social learning and mentorship"),
        "IF-019": (["ML14"], "ML14 Judgment under bounded cognition"),
        "IF-020": (["DR03", "DR06"], "DR03 Visual reasoning; DR06 Spatial representation"),
    }
    identities = {record["id"] for record in modules["modules"] + load("nodes.json")["nodes"]}
    identities |= {record["id"] for record in load("branches.json")["branches"]}
    identities |= {record["ID"] for record in load("life-pillars.json")["life_pillars"]}
    for interface in interfaces["interfaces"]:
        if interface["id"] in corrected:
            interface.setdefault("imported_from_label", interface["from"])
            interface["from_ids"], interface["from"] = corrected[interface["id"]]
        for end in ("from", "to"):
            if end + "_ids" not in interface:
                candidates = re.findall(r"[A-Z]{2}-[A-Z]\d{2}|[A-Z]{2}\d{2}|L\d{2}|\b[A-Z]{2}\b", interface[end])
                resolved = list(dict.fromkeys(candidate for candidate in candidates if candidate in identities))
                if not resolved:
                    raise ValueError(f"No explicit endpoint for {interface['id']} {end}")
                interface[end + "_ids"] = resolved
    dump(DATA / "interfaces.json", interfaces)
    print("Reconciled 22 technical prose attachments and 63 typed interfaces")


def compatibility_only(old, current):
    def unpack(payload):
        text = payload.decode("utf-8").replace("\r\n", "\n")
        metadata = {}
        if text.startswith("---\n"):
            header, text = text[4:].split("\n---\n", 1)
            metadata = yaml.safe_load(header) or {}
        text = text.lstrip("\n")
        if text.startswith("<!-- atlas-route -->\n"):
            text = text.split("<!-- /atlas-route -->\n\n", 1)[1]
            if metadata.pop("search", None) != {"exclude": True}:
                return None
        return metadata, text

    try:
        return b"<!-- atlas-route -->" in current and unpack(old) == unpack(current)
    except (UnicodeDecodeError, ValueError, yaml.YAMLError):
        return False


def inventory():
    changed = subprocess.check_output(
        ["git", "diff", "--name-only", "--diff-filter=M", BASE], cwd=ROOT, text=True
    ).splitlines()
    rows = []
    for name in changed:
        old = subprocess.check_output(["git", "show", f"{BASE}:{name}"], cwd=ROOT)
        current = (ROOT / name).read_bytes()
        rows.append({"path": name, "base_sha256": hashlib.sha256(old).hexdigest(),
                     "current_sha256": hashlib.sha256(current).hexdigest(),
                     "base_lines": len(old.splitlines()), "current_lines": len(current.splitlines())})
    protected = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", BASE, "docs/02-core", "docs/05-frontier/technologies",
         "docs/04-integration", "docs/06-proof-of-work", "docs/07-resources/textbooks", "data/tracks"],
        cwd=ROOT, text=True,
    ).splitlines()
    altered = []
    compatibility = []
    for name in protected:
        old = subprocess.check_output(["git", "show", f"{BASE}:{name}"], cwd=ROOT)
        if not (ROOT / name).is_file() or old.replace(b"\r\n", b"\n") != (ROOT / name).read_bytes().replace(b"\r\n", b"\n"):
            altered.append(name)
            if (ROOT / name).is_file() and compatibility_only(old, (ROOT / name).read_bytes()):
                compatibility.append(name)
    dump(ROOT / "reports" / "legacy-reconciliation.json", {
        "base": BASE, "modified_legacy_files": rows, "protected_legacy_files": len(protected),
        "altered_protected_files": altered,
        "compatibility_only_files": compatibility,
        "substantive_alterations": [name for name in altered if name not in compatibility],
        "interpretation": "Compatibility-only changes preserve parsed frontmatter fields and the complete teaching body; other changes require explicit review",
    })
    print(f"Inventoried {len(rows)} changed legacy files; {len(protected)} protected; {len(altered)} altered")
    print(f"Compatibility-only: {len(compatibility)}; substantive alterations: {len(altered) - len(compatibility)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    if args.apply:
        reconcile()
    inventory()