# Release readiness

Candidate: **0.6.0-rc.1**.

Local engineering gates: **PASS**.
Scholarly reference-grade readiness: **BLOCKED**. Empirical efficacy: **NOT ESTABLISHED**.

## Verification

| Command | Result |
| --- | --- |
| `uv sync --frozen` | PASS |
| `uv run --frozen ruff check scripts tests` | PASS |
| `uv run --frozen python -m compileall -q scripts tests` | PASS |
| `uv run --frozen python -m unittest discover -s tests` | PASS |
| `uv run --frozen python scripts/validate_repo.py` | PASS |
| `uv run --frozen python scripts/audit_obelisk.py --check` | PASS |
| `uv run --frozen python scripts/generate_obelisk_catalog.py --check` | PASS |
| `uv run --frozen python scripts/lint_prose.py --strict` | PASS |
| `uv run --frozen python scripts/audit_ui.py` | PASS |
| `uv run --frozen python scripts/audit_contrast.py` | PASS |
| `uv run --frozen python scripts/check_saturation.py` | PASS |
| `uv run --frozen python scripts/check_obelisk_release_readiness.py --claim candidate` | PASS |
| `uv run --frozen python scripts/build_docs.py` | PASS |
| `uv run --frozen python scripts/audit_ui.py --site .verification/site` | PASS |

Runtime: Python 3.12.3 on Windows.

Manifest SHA-256: `85d169cda75d2a40648d27f1fdb92057ca2663ca32623e17764052d530b839c0`.

Exact commands, exit codes and output: [verification report](reports/release-verification.json).
The manifest is LF-normalized source integrity, not a signed release or proof of learning.

## Claim boundaries

All 448 module/node targets have conservative documentary maturity records.
Teaching and assessment routes do not establish learner mastery or scholarly completeness.
Most source records, node prerequisites, external holdouts, professional scope and
longitudinal outcomes still require independent work. No whole-life superiority is claimed.

Hosted CI and remote deployment were not executed. Browser inspection is recorded separately
in the operational state. Full external-link availability is not a gate in this local run.

## Review order

1. [Architecture audit](ARCHITECTURE_AUDIT.md)
2. [Content maturity](CONTENT_MATURITY.md)
3. [Source maturity](SOURCE_MATURITY.md)
4. [Reconciliation RFC](rfcs/curriculum/0001-obelisk-reconciliation.md)
5. [Remaining research and authored work](NEXT_RESEARCH.md)
6. [Operational state](AGENT_STATE.md)

No commit, push, tag, remote PR or history rewrite is performed by this runner.
