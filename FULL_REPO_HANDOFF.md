# Imported Snapshot Handoff (Historical)

This document records the pre-reconciliation snapshot, originally labeled v0.6.0.
Its counts, test results and merge plan are historical, not the current release state.
Use [operational state](AGENT_STATE.md), [release readiness](RELEASE_READINESS.md)
and [public evidence limits](docs/project/evidence.md) for the current candidate.

This snapshot is a self-contained Open Frontier Curriculum repository candidate built on 2026-09-07.

## Included

- constitutional doctrine for human authorship/stewardship in a high-capability AI civilization;
- 6 knowledge trunks, 84 modules, 364 nodes/outcomes;
- 12 life pillars and 72 life competencies;
- formation, mastery, AI-use, graduate-profile and capstone systems;
- 302 source records and 910 typed source links;
- 417 All Souls backtest rows;
- the 7 technical specialization tracks;
- Frontier 100 index with all 100 current public track/class/bottleneck entries and generated routing pages;
- JSON Schemas, canonical data, validators, tests, CI, governance, contribution rules, RFC structure, Zensical site configuration and deterministic build manifest.

## Validation run

`python scripts/validate_repo.py`  -  PASS

`python -m unittest discover -s tests`  -  PASS
`python -m compileall -q scripts tests`  -  PASS

## Source-of-truth rule

`data/obelisk/` is the canonical Obelisk graph. Markdown is the navigable human view. Stable IDs and provenance should survive editorial rewrites.

## Important provenance note

The execution environment could inspect the public GitHub repository but could not perform a network `git clone`. The v0.6.0 snapshot is therefore a newly assembled self-contained repository, not a byte-for-byte clone of `main`. The Frontier 100 track/class/bottleneck surface was reconstructed from the public live `by-track.md` index checked on 2026-09-07; the 100 generated technology pages are Obelisk routing pages, not verbatim copies of the prior technology-detail pages. When merging into the existing GitHub repository, preserve any richer legacy technology evidence pages unless deliberately superseded.

## Original merge recommendation (superseded)

1. Create a branch from current `main`.
2. Copy canonical Obelisk directories and new docs into the branch.
3. Merge root/config/CI files selectively so current release automation and richer legacy pages survive.
4. Run the repository validator and existing live-repo checks together.
5. Review the constitutional/RFC change as a major curriculum architecture change rather than an ordinary docs patch.
