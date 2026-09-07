#!/usr/bin/env python3
"""Deterministic curriculum evidence audits; structural coverage is not mastery."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import tomllib
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlsplit

if __package__:
    from .frontier_data import load_frontier, load_tracks
    from .learning_atlas import render_atlas
else:
    from frontier_data import load_frontier, load_tracks
    from learning_atlas import render_atlas

ROOT = Path(__file__).resolve().parents[1]


MATURITY_STATES = (
    "SCAFFOLD", "STRUCTURED", "SOURCE-SPINED", "TAUGHT", "ASSESSMENT-READY",
    "INTERNALLY STRESS-TESTED", "EXTERNALLY STRESS-TESTED", "REFERENCE-GRADE",
)


def source_routes(target, links):
    direct = [link for link in links if link["target_id"] == target["id"]]
    inherited = [link for link in links if link["target_id"] == target.get("module_id")]
    return direct, inherited


def verified_review(review, target_id, root):
    if not isinstance(review, dict) or review.get("target_id") != target_id:
        return False
    if review.get("decision") != "pass" or not review.get("reviewed_by"):
        return False
    path = (root / review.get("path", "")).resolve()
    return (
        path.is_relative_to(root.resolve()) and path.is_file()
        and hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()
        == review.get("sha256")
    )


def content_maturity(target, links, sources, evidence=None, root=ROOT):
    evidence = evidence or {}
    direct, inherited = source_routes(target, links)
    resolved = [link for link in direct + inherited if link["source_id"] in sources]
    is_module = "exit_capability" in target
    structure = {
        "identity": bool(target.get("title") and target.get("branch_id")),
        "scope": bool(target.get("core_concepts") or target.get("family")),
        "deletion_rationale": bool(target.get("deletion_reason")),
        "prerequisite_position": "prerequisite_ids" in target,
        "exit": bool(target.get("exit_capability") or target.get("mastery_test")),
    }
    gates = [
        all(structure.values()),
        bool(resolved),
        bool(evidence.get("teaching_path") and evidence.get("teaching_review")),
        bool(evidence.get("assessment_path") and evidence.get("assessment_review")),
        verified_review(evidence.get("internal_review"), target["id"], root),
        verified_review(evidence.get("external_review"), target["id"], root)
        and verified_review(evidence.get("frozen_architecture"), target["id"], root),
        verified_review(evidence.get("reference_review"), target["id"], root)
        and verified_review(evidence.get("source_review"), target["id"], root),
    ]
    level = 0
    for gate in gates:
        if not gate:
            break
        level += 1
    return {
        "id": target["id"], "branch_id": target["branch_id"],
        "kind": "module" if is_module else "node", "title": target["title"],
        "level": level, "state": MATURITY_STATES[level],
        "structure": structure, "gates": gates,
        "direct_sources": sorted({link["source_id"] for link in direct}),
        "inherited_sources": sorted({link["source_id"] for link in inherited}),
        "evidence": evidence,
    }


def branch_summary(records):
    summary = defaultdict(lambda: defaultdict(int))
    for record in records:
        summary[record["branch_id"]][record["state"]] += 1
    return {branch: dict(counts) for branch, counts in sorted(summary.items())}


def load_documents(root):
    return {
        path.stem: json.loads(path.read_text(encoding="utf-8"))
        for path in sorted((root / "data" / "obelisk").glob("*.json"))
        if path.name not in {"build-manifest.json", "catalog.json"}
    }


def source_audit(source, quality):
    review = quality.get(source["id"], {})
    return {
        "id": source["id"], "branch_id": source.get("branch_id"),
        "title": source["title"], "url": source.get("url"),
        "tier": review.get("tier", "UNREVIEWED"),
        "tier_rationale": review.get("rationale", "No individual quality review recorded"),
        "verification": review.get("verification", "verification-needed"),
        "checked": review.get("checked"),
        "evidence_url": review.get("evidence_url"),
        "limitations": review.get("limitations", "No individual limitations review recorded"),
        "volatility": review.get("volatility", "unassessed"),
        "revalidation_required": review.get("volatility") != "stable",
        "license_status": review.get("license_status", "external-rights-not-assessed"),
        "missing_fields": [field for field in ("url", "author_or_authority")
                           if not source.get(field)],
    }


def audit(root=ROOT):
    documents = load_documents(root)
    modules = documents["modules"]["modules"]
    nodes = documents["nodes"]["nodes"]
    sources = {source["id"]: source for source in documents["sources"]["sources"]}
    links = documents["source-links"]["links"]
    attachments = documents.get("content-evidence", {}).get("targets", {})
    quality = documents.get("source-quality", {}).get("sources", {})
    targets = modules + nodes
    maturity = [content_maturity(target, links, sources, attachments.get(target["id"]), root)
                for target in targets]
    source_records = [source_audit(source, quality) for source in sources.values()]
    source_coverage = []
    for target in maturity:
        roles = sorted({link["role"] for link in links if link["target_id"] == target["id"]})
        source_coverage.append({
            "id": target["id"], "branch_id": target["branch_id"],
            "direct": len(target["direct_sources"]),
            "inherited": len(target["inherited_sources"]), "roles": roles,
            "role_review": "required" if len(roles) < 2 else "unreviewed",
            "missing_role_candidates": [role for role in ("primary", "rival", "case", "global")
                                        if not any(role in value for value in roles)],
        })
    life = []
    pillar_rules = documents.get("life-scope", {}).get("pillars", {})
    life_routes = documents.get("life-routes", {}).get("routes", {})
    for competency in documents["life-competencies"]["life_competencies"]:
        scope = pillar_rules.get(competency["Pillar"], {})
        life.append({
            "id": competency["Node"], "pillar_id": competency["Pillar"],
            "title": competency["Competency"],
            "knowledge": bool(competency.get("Knowledge to study")),
            "judgment": bool(competency.get("Judgment to form")),
            "practice": bool(competency.get("Practice")),
            "evidence": bool(competency.get("Evidence")),
            "knowledge_ids": life_routes.get(competency["Node"], []),
            "scope": scope, "route_level": "specific" if life_routes.get(competency["Node"])
            else "unresolved",
            "route_gap": documents.get("life-routes", {}).get("partial_routes", {}).get(competency["Node"]),
        })
    inventory = {}
    for name, document in documents.items():
        inventory[name] = {key: len(value) for key, value in document.items()
                           if isinstance(value, list)}
    inventory["files"] = {
        "docs": len(list((root / "docs").rglob("*.md"))),
        "schemas": len(list((root / "schemas").rglob("*.json"))),
        "tests": len(list((root / "tests").glob("test_*.py"))),
        "scripts": len(list((root / "scripts").glob("*.py"))),
        "workflows": len(list((root / ".github" / "workflows").glob("*.yml"))),
        "rfcs": len(list((root / "rfcs").rglob("*.md"))),
    }
    used_sources = {link["source_id"] for link in links}
    constitutional_sources = {
        identity for thesis in documents["world-transition-model"]["theses"]
        for identity in thesis.get("evidence_refs", [])
    }
    inventory["backtest_sets"] = {
        key: len(value) for key, value in documents["backtests"]["sets"].items()
    }
    return {
        "schema_version": 1,
        "release_version": tomllib.loads((root / "release.toml").read_text())["version"],
        "method": "Sequential evidence gates; source roles and review are not inferred from counts",
        "inventory": inventory, "content_maturity": maturity,
        "branch_maturity": branch_summary(maturity), "source_maturity": source_records,
        "source_coverage": source_coverage, "life_coverage": life,
        "orphan_sources": sorted(set(sources) - used_sources - constitutional_sources),
        "constitutional_only_sources": sorted(constitutional_sources - used_sources),
        "source_usage_scope": "Explicit source-links and constitutional evidence_refs only; anchor titles are not inferred ID links",
        "external_validation": {
            "provenance_status": "Imported registry assertions; independent freeze and administration not verified in this audit",
            "registry": documents["holdout-registry"],
        },
        "saturation": documents["technical-gap-candidates"],
        "findings": graph_findings(documents, root),
    }


def graph_findings(documents, root):
    findings = []
    from jsonschema import Draft202012Validator

    schema = json.loads((root / "schemas/obelisk/editorial-metadata.schema.json").read_text(encoding="utf-8"))
    for family in ("interfaces", "life-routes", "life-scope", "source-quality", "pathways", "content-evidence"):
        validator = Draft202012Validator({**schema, "$ref": f"#/$defs/{family}"},
                         format_checker=Draft202012Validator.FORMAT_CHECKER)
        failures = list(validator.iter_errors(documents.get(family)))
        for failure in failures:
            findings.append({"severity": "error", "code": "metadata-schema", "family": family,
                             "path": list(failure.absolute_path), "message": failure.message})
    if findings:
        return findings
    registry = {}
    record_families = {}
    identity_keys = ("id", "ID", "Node", "Code", "Mode")
    families = ("branches", "modules", "nodes", "sources", "life-pillars",
                "life-competencies", "formation-modes", "ai-modes", "interfaces",
                "great-questions", "capstones", "practica", "civilizational-anchors")
    for family in families:
        for values in documents[family].values():
            if not isinstance(values, list):
                continue
            for record in values:
                identity = next((record[key] for key in identity_keys if key in record), None)
                if not identity:
                    findings.append({"severity": "error", "code": "missing-id", "family": family})
                elif identity in registry:
                    findings.append({"severity": "error", "code": "duplicate-id", "id": identity})
                else:
                    registry[identity] = record
                    record_families[identity] = family

    def check_reference(owner, target, relation, allowed=None):
        if target not in registry:
            findings.append({"severity": "error", "code": "unresolved-reference",
                             "id": owner, "target": target, "relation": relation})
        elif allowed and record_families[target] not in allowed:
            findings.append({"severity": "error", "code": "wrong-reference-family",
                             "id": owner, "target": target, "relation": relation,
                             "actual_family": record_families[target], "allowed": sorted(allowed)})

    for interface in documents["interfaces"]["interfaces"]:
        for end in ("from", "to"):
            explicit = interface.get(end + "_ids")
            if explicit is None:
                findings.append({"severity": "warning", "code": "untyped-interface",
                                 "id": interface["id"], "field": end,
                                 "value": interface[end]})
            else:
                for identity in explicit:
                    check_reference(interface["id"], identity, end,
                                    {"branches", "modules", "nodes", "life-pillars", "life-competencies"})
    for node in documents["nodes"]["nodes"]:
        for prerequisite in node.get("prerequisite_ids", []):
            check_reference(node["id"], prerequisite, "prerequisite", {"modules", "nodes"})
    for owner, identities in documents.get("life-routes", {}).get("routes", {}).items():
        check_reference(owner, owner, "life-route-owner", {"life-competencies"})
        for identity in identities:
            check_reference(owner, identity, "knowledge", {"modules", "nodes"})
    life_ids = {record["Node"] for record in documents["life-competencies"]["life_competencies"]}
    route_ids = set(documents.get("life-routes", {}).get("routes", {}))
    for identity in sorted(life_ids - route_ids):
        findings.append({"severity": "error", "code": "missing-life-route", "id": identity})
    for stage in documents.get("pathways", {}).get("stages", []):
        for identity in stage["routes"]:
            check_reference(stage["id"], identity, "stage-route", {"modules", "nodes", "life-competencies"})
    graph = {record["id"]: record.get("prerequisite_ids", [])
             for family in ("modules", "nodes") for record in documents[family][family]}
    for cycle in prerequisite_cycles(graph):
        findings.append({"severity": "error", "code": "prerequisite-cycle", "path": cycle})
    source_ids = {record["id"] for record in documents["sources"]["sources"]}
    for identity, review in documents.get("source-quality", {}).get("sources", {}).items():
        check_reference(identity, identity, "source-quality", {"sources"})
        if review.get("evidence_url"):
            try:
                address = urlsplit(review["evidence_url"])
                valid_address = (address.scheme in {"http", "https"} and bool(address.hostname)
                                 and address.username is None and address.password is None
                                 and (address.port is None or 0 < address.port < 65536))
            except ValueError:
                valid_address = False
            if not valid_address:
                findings.append({"severity": "error", "code": "invalid-source-review-url", "id": identity})
        if identity not in source_ids or review.get("tier") not in ("A", "B", "C", "D", "E"):
            findings.append({"severity": "error", "code": "invalid-source-quality", "id": identity})
    for link in documents["source-links"]["links"]:
        if not link.get("role"):
            findings.append({"severity": "error", "code": "missing-source-role", "id": link.get("target_id")})
    for number, row in enumerate(documents["backtests"]["sets"]["all_souls_holdout"], 1):
        for identity in [row["Primary node"]] + row.get("Supporting nodes", []):
            check_reference(f"all-souls-{number}", identity, "backtest", {"nodes"})
    for target_id, evidence in documents.get("content-evidence", {}).get("targets", {}).items():
        check_reference(target_id, target_id, "content-evidence", {"modules", "nodes"})
        for field, value in evidence.items():
            if field.endswith("_path") and (
                not (root / value).resolve().is_relative_to((root / "docs").resolve())
                or not (root / value).is_file()
            ):
                findings.append({"severity": "error", "code": "missing-evidence",
                                 "id": target_id, "path": value})
            if field in ("internal_review", "external_review", "frozen_architecture",
                         "reference_review", "source_review") and not verified_review(value, target_id, root):
                findings.append({"severity": "error", "code": "invalid-review-evidence",
                                 "id": target_id, "field": field})
    return findings


def prerequisite_cycles(graph):
    active = []
    visited = set()
    cycles = []

    def visit(identity):
        if identity in active:
            cycles.append(active[active.index(identity):] + [identity])
            return
        if identity in visited:
            return
        active.append(identity)
        for prerequisite in sorted(graph.get(identity, [])):
            visit(prerequisite)
        active.pop()
        visited.add(identity)

    for identity in sorted(graph):
        visit(identity)
    return cycles


def markdown_table(headers, rows):
    def cell(value):
        return str(value).replace("|", "\\|").replace("\n", " ")
    return "\n".join(
        ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
        + ["| " + " | ".join(cell(value) for value in row) + " |" for row in rows]
    )


def render_reports(report):
    maturity = report["content_maturity"]
    content = ["# Content maturity", "", "Generated by `scripts/audit_obelisk.py`; do not edit.", "",
               "These are conservative documentary states, not measured learner outcomes.",
               "Missing prerequisite declarations block structured status; inherited reading routes",
               "do not become direct scholarship. Existing teaching prose is preserved even when",
               "its canonical contract is incomplete. No automatic gate proves reference quality.", "",
               "## State machine", ""]
    content.extend(f"{level}. {state}" for level, state in enumerate(MATURITY_STATES))
    content += ["", "## Branch summary", "", markdown_table(
        ["Branch"] + list(MATURITY_STATES),
        [[branch] + [counts.get(state, 0) for state in MATURITY_STATES]
         for branch, counts in report["branch_maturity"].items()]), "",
        "## Modules and nodes", "", markdown_table(
            ["ID", "Title", "Level", "State", "Missing structure"],
            [[row["id"], row["title"], row["level"], row["state"],
              ", ".join(key for key, value in row["structure"].items() if not value) or "none"]
             for row in maturity]), ""]
    sources = ["# Source maturity", "", "Generated by `scripts/audit_obelisk.py`; do not edit.", "",
               "A bibliographic route is not independent verification. UNREVIEWED is neither a",
               "quality tier nor an accusation of fabrication. Role candidates below require",
               "intellectual judgment, not mandatory bibliography padding.", "",
               "Coverage counts include links to reading areas awaiting selection and inherited recommendations.",
               "They count recorded routes, not verified publications, assigned readings or scholarly completeness.", "",
               "Tier A: primary/official; B: scholarly synthesis; C: introductory/professional;",
               "D: secondary explanation; E: contextual/experiential. Tiers require recorded reasons.", "",
               "## Branch coverage", ""]
    coverage = report["source_coverage"]
    sources.append(markdown_table(
        ["Branch", "Targets", "Direct", "Inherited only", "No route", "Single-role or less"],
        [[branch, len(rows), sum(row["direct"] > 0 for row in rows),
          sum(row["direct"] == 0 and row["inherited"] > 0 for row in rows),
          sum(row["direct"] + row["inherited"] == 0 for row in rows),
          sum(len(row["roles"]) < 2 for row in rows)]
         for branch in report["branch_maturity"]
         for rows in [[row for row in coverage if row["branch_id"] == branch]]]))
    sources += ["", "## Quality and provenance", "", markdown_table(
        ["Tier", "Records"], sorted(Counter(row["tier"] for row in report["source_maturity"]).items())),
        "", f"Orphan sources: {len(report['orphan_sources'])}. See the machine-readable report for IDs.",
        "", "## Source records", "", markdown_table(
            ["ID", "Title", "Tier", "Verification", "Volatility", "Missing metadata"],
            [[row["id"], row["title"], row["tier"], row["verification"], row["volatility"],
              ", ".join(row["missing_fields"]) or "none"] for row in report["source_maturity"]]), ""]
    return {"CONTENT_MATURITY.md": "\n".join(content), "SOURCE_MATURITY.md": "\n".join(sources)}


def render_discovery(report, root=ROOT):
    documents = load_documents(root)
    outputs = {}
    notice = "Generated structural view. Curated exposition and evidence remain separately identified."
    index = ["# Curriculum ID index", "", notice, "",
             ("[Life routes](life-coverage.md) | [Source index](source-index.md) | "
             "[Learner stages](pathways.md) | [Great questions](great-questions.md) | "
             "[Formation and assessment](formation.md)"), ""]
    modules = {record["id"]: record for record in documents["modules"]["modules"]}
    for row in report["content_maturity"]:
        index += [f"## {row['id']}", "", f"**{row['title']}**. {row['state']}.", ""]
        target = modules.get(row["id"])
        if target:
            index += [target["exit_capability"], "",
                      "Prerequisites: " + (", ".join(f"[{identity}](#{identity.lower()})"
                       for identity in target["prerequisite_ids"]) or "No module prerequisite declared."), ""]
        evidence = row["evidence"]
        if evidence.get("teaching_path"):
            relative = os.path.relpath(root / evidence["teaching_path"], root / "docs" / "09-obelisk").replace("\\", "/")
            index += [f"[Teaching and assessment]({relative})", ""]
        index += ["Sources: " + (", ".join(f"[{identity}](source-index.md#{identity.lower()})"
                   for identity in sorted(set(row["direct_sources"] + row["inherited_sources"]))) or "Sources: unresolved"), ""]
    outputs["docs/09-obelisk/curriculum-index.md"] = "\n".join(index)
    life = ["# Life competency routes", "", notice, "",
            "Disciplinary routes are prerequisites, not substitutes for domain practice or professional advice.", ""]
    competencies = {row["Node"]: row for row in documents["life-competencies"]["life_competencies"]}
    for row in report["life_coverage"]:
        source = competencies[row["id"]]
        life += [f"## {row['id']}: {row['title']} {{#{row['id'].lower()}}}", "",
                 "Knowledge routes: " + ", ".join(f"[{identity}](curriculum-index.md#{identity.lower()})" for identity in row["knowledge_ids"]), ""]
        for key in ("Knowledge to study", "Judgment to form", "Practice", "Evidence"):
            life += [f"**{key}:** {source[key]}", ""]
        for key, value in row["scope"].items():
            life += [f"**{key.replace('_', ' ').capitalize()}:** {value}", ""]
        if row.get("route_gap"):
            life += [f"**Partial route:** {row['route_gap']}", ""]
    outputs["docs/09-obelisk/life-coverage.md"] = "\n".join(life)
    sources = ["# Source index", "", notice, "",
               "Bibliographic records retain their original licenses. A working URL does not verify a claim.", ""]
    for row in report["source_maturity"]:
        sources += [f"## {row['id']}", "", row["title"], "",
                    (f"Quality: {row['tier']}. Verification: {row['verification']}. "
                     f"Volatility: {row['volatility']}."), ""]
        if row["url"]:
            sources += [f"[Source]({row['url']})", ""]
        if row["evidence_url"]:
            sources += [f"[Review evidence]({row['evidence_url']}) (checked {row['checked']}).", ""]
        sources += [f"**Rationale:** {row['tier_rationale']}", "",
                    f"**Limitations:** {row['limitations']}", "",
                    f"**Rights:** {row['license_status']}", ""]
    outputs["docs/09-obelisk/source-index.md"] = "\n".join(sources)
    stages = ["# Learner stages", "", documents["pathways"]["policy"], ""]
    for stage in documents["pathways"]["stages"]:
        stages += [f"## {stage['title']}", "", f"**Readiness:** {stage['readiness']}", "",
                   f"**Practice:** {stage['practice']}", "", f"**Assessment:** {stage['assessment']}", "",
                   "AI permissions: " + ", ".join(stage["ai_modes"]), "",
                   "Entry routes: " + ", ".join(
                       f"[{identity}]({'life-coverage.md' if identity.startswith('L') else 'curriculum-index.md'}#{identity.lower()})"
                       for identity in stage["routes"]), ""]
    outputs["docs/09-obelisk/pathways.md"] = "\n".join(stages)
    tracks = load_tracks(root)
    frontier = load_frontier(root)["technologies"]
    index = ["# Frontier specializations", "", "Choose at least one for serious depth after the relevant foundations.", "",
             '<div class="grid cards ofc-track-grid" markdown>', ""]
    for code, detail in tracks.items():
        track = {**detail, "code": code, "count": sum(row["track"] == code for row in frontier)}
        index += [f'- <span class="ofc-card-title">**[{track["name"]}]({detail["path"]})**</span>', "",
                  (f'    <span class="ofc-card-meta"><span>{track["code"]}</span><span>{detail["weeks"]} weeks</span>'
                   f'<span>{track["count"]} primary targets</span></span>'), ""]
        outputs[f"docs/03-specializations/{detail['summary']}"] = (
            "---\nsearch:\n  exclude: true\n---\n\n"
            f"# {track['name']}\n\n[Current specialization: sequence and resources]({detail['path']})\n"
        )
    index += ["</div>", "", "Research gates: reproduce, extend, integrate, defend.", "",
              "[Explore technologies, study connections and resources](../05-frontier/README.md)", ""]
    outputs["docs/03-specializations/README.md"] = "\n".join(index)
    for technology in frontier:
        prefix = f"{technology['id']:03d}-"
        summaries = list((root / "docs/03-specializations/technologies").glob(prefix + "*.md"))
        details = list((root / "docs/05-frontier/technologies").glob(prefix + "*.md"))
        if len(summaries) != 1 or len(details) != 1:
            raise ValueError(f"Frontier {technology['id']} must have one summary and one preserved detail")
        outputs[summaries[0].relative_to(root).as_posix()] = "\n".join([
            "---", "search:", "  exclude: true", "---", "",
            f"# {technology['id']:03d}: {technology['title']}", "",
            f"[Current technology page: study connections and first exercise](../../05-frontier/technologies/{details[0].name})", "",
        ])
    return outputs


def write_or_check(root, outputs, check=False):
    stale = []
    for relative, text in outputs.items():
        path = root / relative
        text = text.replace("\r\n", "\n")
        if relative.endswith(".md"):
            text = text.replace("\u2014", " - ").replace("\u2192", " -> ")
        payload = text.encode("utf-8")
        if not path.exists() or path.read_bytes() != payload:
            stale.append(relative)
            if not check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(payload)
    return stale


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail on generated drift without writing")
    args = parser.parse_args()
    report = audit()
    outputs = render_reports(report)
    outputs.update(render_discovery(report))
    for name in ("curriculum-index", "source-index", "life-coverage", "pathways"):
        path = f"docs/09-obelisk/{name}.md"
        outputs[path] = "---\nsearch:\n  exclude: true\n---\n\n" + outputs[path]
    outputs.update(render_atlas())
    outputs["reports/obelisk-audit.json"] = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    stale = write_or_check(ROOT, outputs, args.check)
    errors = [finding for finding in report["findings"] if finding["severity"] == "error"]
    print(f"Audited {len(report['content_maturity'])} module/node records; "
          f"{len(report['source_maturity'])} sources; {len(report['life_coverage'])} life competencies")
    print(f"Graph audit: {len(errors)} errors; {len(report['findings']) - len(errors)} warnings")
    for error in errors:
        print(json.dumps(error))
    if args.check and stale:
        print("Generated drift: " + ", ".join(stale))
    return int(bool(errors or (args.check and stale)))


if __name__ == "__main__":
    raise SystemExit(main())