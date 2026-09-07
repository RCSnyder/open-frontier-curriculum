#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

if __package__:
    from .preservation import preserved_identity_errors
else:
    from preservation import preserved_identity_errors

try:
    from jsonschema import Draft202012Validator
except ImportError:
    Draft202012Validator = None

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "obelisk"
errors: list[str] = []
warnings: list[str] = []

def load(name: str):
    path = DATA / name
    if not path.exists():
        errors.append(f"missing {path.relative_to(ROOT)}")
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
        return {}

def validate_schema_records(records, schema_name, label):
    if Draft202012Validator is None:
        message = "jsonschema is required; install the validation dependencies"
        if message not in errors:
            errors.append(message)
        return
    schema_path = ROOT / "schemas" / "obelisk" / schema_name
    if not schema_path.exists():
        errors.append(f"missing schema {schema_path.relative_to(ROOT)}")
        return
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        validator = Draft202012Validator(schema)
        for i, rec in enumerate(records):
            for err in validator.iter_errors(rec):
                errors.append(f"{label}[{i}] schema: {err.message}")
                break
    except (OSError, json.JSONDecodeError, ValueError, TypeError) as exc:
        errors.append(f"schema validation failure for {label}: {exc}")

def validate_schema_object(obj, schema_name, label):
    validate_schema_records([obj], schema_name, label)

def unique(records, key, label):
    seen = {}
    for i, rec in enumerate(records):
        value = rec.get(key)
        if not value:
            errors.append(f"{label}[{i}] missing {key}")
            continue
        if value in seen:
            errors.append(f"duplicate {label} {key}: {value}")
        seen[value] = rec
    return seen

branches = load("branches.json").get("branches", [])
modules = load("modules.json").get("modules", [])
nodes = load("nodes.json").get("nodes", [])
sources = load("sources.json").get("sources", [])
source_links = load("source-links.json").get("links", [])
pillars = load("life-pillars.json").get("life_pillars", [])
life = load("life-competencies.json").get("life_competencies", [])
formation = load("formation-modes.json").get("formation_modes", [])
ai_modes = load("ai-modes.json").get("ai_modes", [])
interfaces = load("interfaces.json").get("interfaces", [])
backtests = load("backtests.json")
foundational = load("foundational-doctrine.json")
world_transition = load("world-transition-model.json")
scarcity_shift = load("scarcity-shift.json")
human_authorship = load("human-authorship.json")
project_lexicon = load("project-lexicon.json")

branch_by_id = unique(branches, "id", "branch")
module_by_id = unique(modules, "id", "module")
node_by_id = unique(nodes, "id", "node")
source_by_id = unique(sources, "id", "source")
pillar_by_id = unique(pillars, "ID", "life pillar")
life_by_id = unique(life, "Node", "life competency")
unique(interfaces, "id", "interface")

# JSON Schema validation for canonical record families and V0.5 constitutional objects
validate_schema_records(branches, "branch.schema.json", "branch")
validate_schema_records(modules, "module.schema.json", "module")
validate_schema_records(nodes, "node.schema.json", "node")
validate_schema_records(sources, "source.schema.json", "source")
validate_schema_records(life, "life-competency.schema.json", "life competency")
validate_schema_object(foundational, "foundational-doctrine.schema.json", "foundational doctrine")
validate_schema_object(world_transition, "world-transition-model.schema.json", "world transition")
validate_schema_object(scarcity_shift, "scarcity-shift.schema.json", "scarcity shift")
validate_schema_object(human_authorship, "human-authorship.schema.json", "human authorship")
validate_schema_object(project_lexicon, "project-lexicon.schema.json", "project lexicon")
validate_schema_object(backtests, "backtest.schema.json", "backtests")

expected_branches = {"TS","PH","HW","EX","ML","DR"}
if set(branch_by_id) != expected_branches:
    errors.append(f"branch set must be {sorted(expected_branches)}, got {sorted(branch_by_id)}")

if len(pillars) != 12:
    errors.append(f"expected 12 life pillars, found {len(pillars)}")
if len(life) != 72:
    errors.append(f"expected 72 life competencies, found {len(life)}")
if len(formation) != 12:
    errors.append(f"expected 12 formation modes, found {len(formation)}")
if len(ai_modes) != 6:
    errors.append(f"expected 6 AI modes, found {len(ai_modes)}")

# Foundational doctrine invariants
if len(foundational.get("axioms", [])) != 18:
    errors.append(f"expected 18 foundational axioms, found {len(foundational.get('axioms', []))}")
if len(foundational.get("eight_verbs", [])) != 8:
    errors.append(f"expected 8 formation verbs, found {len(foundational.get('eight_verbs', []))}")
if len(world_transition.get("theses", [])) != 14:
    errors.append(f"expected 14 world-transition theses, found {len(world_transition.get('theses', []))}")
if len(scarcity_shift.get("scarcities", [])) != 14:
    errors.append(f"expected 14 scarcity-shift entries, found {len(scarcity_shift.get('scarcities', []))}")
if len(human_authorship.get("domains", [])) != 12:
    errors.append(f"expected 12 human-authorship domains, found {len(human_authorship.get('domains', []))}")
if len(project_lexicon.get("terms", [])) < 20:
    errors.append(f"expected at least 20 project lexicon terms, found {len(project_lexicon.get('terms', []))}")

for thesis in world_transition.get("theses", []):
    for sid in thesis.get("evidence_refs", []):
        if sid not in source_by_id:
            errors.append(f"{thesis.get('id')}: unresolved transition evidence source {sid}")

formation_codes = {x.get("Code") for x in formation}
ai_codes = {x.get("Mode") for x in ai_modes}
for m in modules:
    bid = m.get("branch_id")
    if bid not in branch_by_id:
        errors.append(f"{m.get('id')}: unknown branch {bid}")
    for pid in m.get("prerequisite_ids", []):
        if pid not in module_by_id:
            errors.append(f"{m.get('id')}: unresolved prerequisite {pid}")
    for code in m.get("formation_modes", []):
        if code not in formation_codes:
            errors.append(f"{m.get('id')}: unknown formation mode {code}")
    for code in m.get("ai_modes", []):
        if code not in ai_codes:
            errors.append(f"{m.get('id')}: unknown AI mode {code}")
    if not m.get("title") or not m.get("exit_capability") or not m.get("gate"):
        errors.append(f"{m.get('id')}: missing title, exit capability, or gate")

for n in nodes:
    bid = n.get("branch_id")
    if bid not in branch_by_id:
        errors.append(f"{n.get('id')}: unknown branch {bid}")
    mid = n.get("module_id")
    if mid and mid not in module_by_id:
        errors.append(f"{n.get('id')}: unresolved module {mid}")
    if mid in module_by_id and module_by_id[mid].get("branch_id") != bid:
        errors.append(f"{n.get('id')}: module {mid} belongs to a different branch")
    for code in n.get("formation_modes", []):
        if code not in formation_codes:
            errors.append(f"{n.get('id')}: unknown formation mode {code}")
    for code in n.get("ai_modes", []):
        if code not in ai_codes:
            errors.append(f"{n.get('id')}: unknown AI mode {code}")
    if not n.get("title") or not n.get("deletion_reason") or not n.get("mastery_test"):
        errors.append(f"{n.get('id')}: missing title, deletion reason, or mastery test")

for item in life:
    if item.get("Pillar") not in pillar_by_id:
        errors.append(f"{item.get('Node')}: unresolved pillar {item.get('Pillar')}")

target_ids = set(module_by_id) | set(node_by_id) | set(branch_by_id) | set(pillar_by_id) | set(life_by_id)
for link in source_links:
    if link.get("source_id") not in source_by_id:
        errors.append(f"source link: unknown source {link.get('source_id')}")
    if link.get("target_id") not in target_ids:
        errors.append(f"source link: unknown target {link.get('target_id')}")

# Module prerequisite cycle check
graph = {mid: set(m.get("prerequisite_ids", [])) for mid,m in module_by_id.items()}
state = {}
stack = []
def visit(node):
    mark = state.get(node, 0)
    if mark == 1:
        cycle = " -> ".join(stack + [node])
        errors.append(f"module prerequisite cycle: {cycle}")
        return
    if mark == 2:
        return
    state[node] = 1
    stack.append(node)
    for dep in graph.get(node, ()):
        visit(dep)
    stack.pop()
    state[node] = 2
for mid in graph:
    visit(mid)

# Corpus invariants
all_souls = backtests.get("sets", {}).get("all_souls_holdout", [])
baseline = load("preservation-baseline.json")
if not all(key in baseline for key in ("all_souls_rows", "modules", "nodes")):
    errors.append("Missing preservation baseline fields")
else:
    if len(all_souls) != baseline["all_souls_rows"]:
        errors.append(f"expected {baseline['all_souls_rows']} preserved All Souls rows, found {len(all_souls)}")
    errors.extend(preserved_identity_errors({"modules": modules, "nodes": nodes}, baseline))

if errors:
    print("OBELISK VALIDATION FAILED")
    for e in errors:
        print(" -", e)
    if warnings:
        print("WARNINGS")
        for w in warnings:
            print(" -", w)
    sys.exit(1)

print("OBELISK VALIDATION PASSED")
print(f" - {len(branches)} branches")
print(f" - {len(modules)} modules")
print(f" - {len(nodes)} nodes / outcomes")
print(f" - {len(sources)} sources")
print(f" - {len(source_links)} source links")
print(f" - {len(pillars)} life pillars / {len(life)} life competencies")
print(f" - {len(all_souls)} All Souls hold-out rows")
print(f" - {len(foundational.get('axioms', []))} foundational axioms / {len(world_transition.get('theses', []))} transition theses")
