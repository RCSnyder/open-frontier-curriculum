# Contributing

Open Frontier is maintained as a **living, adversarially tested reference architecture**. Contributions should improve truth, coverage, teachability, accessibility, or validation - not merely make the graph larger.

## Curriculum changes

For a new branch, module or node, state the deletion failure, prerequisite closure,
exit capability, mastery test and source roles. Include life-pillar routes,
formation modes, AI policy and relevant global/temporal evidence.
Explain why the material cannot be taught adequately within an existing unit.

Use an RFC under `rfcs/curriculum/` for structural additions/deletions. Stable IDs are never silently reused.

## Quality gates

Use the frozen environment: `uv sync --frozen`. Run commands with `uv run --frozen`.

```bash
uv run --frozen python scripts/validate_repo.py
uv run --frozen python -m unittest discover -s tests
uv run --frozen ruff check scripts tests
uv run --frozen python scripts/lint_prose.py --strict
uv run --frozen python scripts/audit_ui.py
uv run --frozen python scripts/audit_contrast.py
uv run --frozen zensical build --clean
uv run --frozen python scripts/audit_ui.py --site site
```

After canonical changes, regenerate audit views, then catalog/manifests:

```bash
uv run --frozen python scripts/sync_release_version.py
uv run --frozen python scripts/audit_obelisk.py
uv run --frozen python scripts/generate_obelisk_catalog.py
uv run --frozen python scripts/audit_obelisk.py --check
uv run --frozen python scripts/generate_obelisk_catalog.py --check
```

The reconciliation script's `--apply` option is an import migration, not a normal
generation command. Preserve substantive legacy teaching pages and stable URLs.
Canonical JSON owns structure; attached prose owns exposition. Do not edit generated
views directly or modify preserved snapshot folders to make current gates pass.

## Evidence and review

Keep source identity, scholarly evaluation, teaching readiness and measured learning
separate. A URL resolving does not establish a claim, and a source count does not
establish global coverage. Record edition, translation, source role and rights.
No permission to copy external works follows from a bibliographic entry.

New teaching must contain a specific task, failure case, assessment and human/AI
boundary. Independent performance and augmented performance receive separate records.
Review claims above assessment-ready need target-bound, file-backed evidence and
hashes. Maintainers must still assess reviewer competence, independence and method.

Use respectful, reproducible issue reports with exact IDs and commands. Do not
publish learner identities, sensitive field records, private examiner material or
credentials. High-risk practice needs qualified supervision and consent.

Pull requests should explain the change, tests, source checks, remaining uncertainty,
and any proposed RFC. Architecture changes require explicit maintainer approval.
