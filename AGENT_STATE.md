# Agent State

## PR 2 pipeline repair: 2026-09-07

- Both failed CI runs (34094823642 and 34094798237) stopped at Ruff EXE001 for 12 non-executable shebang scripts.
- Corrected the Git modes to 100755. Windows Ruff skips this permission rule; a cross-platform Git-index regression now covers it.
- Canonical validation now uses the same pinned checkout and strict prose gate as the other workflows.
- Local verification: 58 tests and all 14 release gates pass. All workflow YAML parses and third-party actions are pinned.
- User authorized amending these fixes into the latest commit. No force-push or remote rerun is performed here.
- Hosted checks still refer to the previous commit until the amended branch is pushed. Linux CI has not yet rerun against these fixes.

## Discovery and ownership closeout: 2026-09-07

- Foundation and frontier overviews now offer expandable previews, direct resource links and URL-backed filters.
- Four technologies have explicit explained subject connections and reverse application links. Other technologies show labelled introductory track resources, not invented mappings.
- Frontier CSV is authoritative; JSON exports, track counts, program inventory and browse listings derive from shared readers.
- Learning-support policy moved into learning-design data. Historical identity preservation is separate from current catalog size.
- Resolved two validator fixture failures by loading the fixture within the scripts package.
- The prose warning was concatenated dropdown labels, not a long narrative sentence; generated options now occupy separate lines.
- Final validation: 53 tests and all 14 release gates pass; strict prose has zero warnings.
- Browser: 12 expanded-page checks across frontier and five foundation/support pages at 390 and 1440 pixels passed without horizontal overflow.
- DOM interaction checks verified the robotics resource link, reverse course connection, empty/reset states and filter restoration after returning from a course.
  Foreground click retesting was limited by shared browser tabs reporting hidden visibility; this is recorded in the browser report.
- No commit, push or index mutation by the agent. User staging remains untouched.

## Publication credibility fixes: 2026-09-07

- Addressed all four publication-review findings without promoting scholarly or empirical maturity.
- Source IDs in attached teaching now render as linked titles; punctuation and original teaching bodies remain intact.
- The library separates 281 identified work/resource records from 22 reading areas awaiting selection.
  These are records, not unique or independently verified publications. Existing IDs and recommendation links remain intact.
- A generated public evidence page reports the current candidate, 26 teaching attachments, 175 study outlines and source-review limits.
- Home, About, README and validation pages disclose unfinished preview status and unverified independent All Souls provenance.
- Old branch labels are explicitly imported editorial labels; the old snapshot handoff is marked historical.
- Verification: 44 tests and all 14 local release gates pass. Independent read-only review of these four fixes found no required changes.
- Browser checks: 16 route/viewport combinations at 390 and 1440 pixels, library group filtering and reset, citation links and current evidence text passed.
  Cards remain equal-height with loaded images at both widths. See the publication-review section of `reports/browser-verification.json`.
- Preservation: 176 protected files, 22 compatibility-only changes, zero substantive alterations. No Git/index mutation by the agent.
- This remains a public preview. Bibliographic verification, specialist review, learner outcomes and hosted deployment remain incomplete or unverified.
- The minor theme-owned 404 skip-link defect noted in engineering review is outside these four publication-content fixes.

## Current iteration: 2026-09-07

The user authorized a learner-facing redesign and clarified that preservation
means valuable intellectual content, not a permanent parallel legacy website.
The sections below this update describe the earlier hardening pass.

- Four foundations now lead the site: capability, context, judgment and representation.
- Praxis, developmental routes, learning support, life applications and library have distinct roles.
- 201 subject homes join canonical outcomes, prerequisites, sources and available teaching.
- The learner catalog has explicit subject, outcome, resource and relationship kinds.
- Three complete entry journeys cover proof, collective action and whole-work interpretation.
- 303 resource pages expose reading purpose, scope and study connections; indexes have local filters.
- Compatibility notices preserve teaching bodies and reduce duplicate search results.
  The deeper canonical ID migration and removal of all superseded files remain unfinished.
- The unnecessary legacy overview was removed. Competing root README/index output
  was a real homepage collision; builds now reject duplicate published routes.
- Verification builds use a separate temporary working directory, then publish to
  `.verification/site`, avoiding the user's running Zensical server cache.
- Preview: http://127.0.0.1:8002/ . Existing user preview processes were not stopped.
- Preservation audit: 176 protected files, 22 compatibility-only changes, zero substantive alterations.
- Final results are recorded in `RELEASE_READINESS.md` and `reports/release-verification.json`.
  Earlier independent engineering review does not cover this redesign.
- Closeout verified: 41 tests and all 14 local gates pass. All 28 responsive
  route checks pass across phone, tablet, desktop and wide desktop. Navigation,
  source links, local filters, empty states, mobile drawer and search were exercised.
  Details: `reports/browser-verification.json`. Manifest/report binding verified.
- Foundation card alignment verified at six widths from 320 to 1728 pixels:
  identical heights and aligned images, titles and descriptions within rows.
  Removed Markdown paragraph wrappers and added a rendered-markup regression test.
- No commit, push, branch change or index mutation was performed by this agent.
  The user has staged work independently during the session.

## Repository facts

- Branch: `complete-refactor`; do not push, rewrite history, or discard user work.
- Base reference: `8b98ed1` (`main`, `origin/main`, `v0.1.0` at inspection).
- Initial state: staged Obelisk import on the base commit; preserve the index.
- No unresolved merge entries reported by Git.
- Canonical structure: `data/obelisk/`; preserve curated legacy exposition and
  attach it to stable IDs rather than replacing it with structural summaries.
- Package: Python >=3.11, Obelisk candidate version 0.6.0-rc.1.
- Validation: `python scripts/validate_repo.py`.
- Tests: `python -m unittest discover -s tests`.
- Compilation: `python -m compileall -q scripts tests`.
- Frozen environment: `uv sync --frozen`; prefix commands with `uv run --frozen`.
- Documentation: `zensical build --clean`; restored theme/extensions build passes.
- Audit/generation: `python scripts/audit_obelisk.py`; `--check` is read-only drift detection.
- Legacy inventory: `python scripts/reconcile_obelisk_import.py`; `--apply` is a
  bounded additive migration, not a general regeneration command.
- Baseline: imported validator and two smoke tests passed; prose/UI gates failed.
  Schema absence was silently accepted; malformed module references crashed.
  Both defects now have passing regression tests.
- Proposed release: `0.6.0-rc.1`; virtual tooling version remains `0.0.0`.

## Architecture inventory

Verified canonical counts: six trunks, 84 modules, 364 nodes, twelve life pillars,
72 competencies, twelve formation modes, six AI modes, 303 sources, 911 source
links, 417 All Souls rows, 63 interfaces, 48 great questions, 72 civilizational
anchors, twelve capstones, nine practica, eleven mastery dimensions, twelve
assessment dimensions. The two dimension families are not interchangeable.
Protected legacy inventory: 176 files, zero content changes at reconciliation.
Current reports: `reports/obelisk-audit.json`, `reports/legacy-reconciliation.json`,
`CONTENT_MATURITY.md`, `SOURCE_MATURITY.md`.

## Work queue

| Phase | State | Proof / intended scope |
| --- | --- | --- |
| 0 Safety and constitutional inventory | COMPLETE | Git/base snapshot, instructions, commands, baseline checks |
| 1 Merge reconciliation | VERIFIED | 31 changed legacy files inventoried; 176 protected files unchanged; technical navigation and rendering restored |
| 2 Graph integrity | VERIFIED WITH LIMITS | 63 typed interfaces; schemas, references, cycles, route coverage and mutation tests; unmodeled semantics still need review |
| 3-4 Maturity and sources | PARTIAL / BLOCKED | All 448 targets and 303 sources audited; five quality records, three official bibliographic checks; remaining scholarship unresolved |
| 5-10 Knowledge trunks | PARTIAL / BLOCKED | 22 TS attachments plus four substantive labs; 58 modules source-spined, 364 nodes lack prerequisite contracts; full teaching completion remains open |
| 11-12 Life and inheritance | PARTIAL / BLOCKED | 72 specific routes and twelve safety contracts; four partial routes; anchor editions and domain review incomplete |
| 13-14 Integration and Frontier | VERIFIED WITH LIMITS | Seven tracks and all 100 identities/classes/primary tracks preserved; typed interfaces; feasibility not independently revalidated |
| 15-16 Pathways and evidence | PARTIAL / BLOCKED | Six stage entry routes and prospective protocol published; no observed learner or fresh unseen holdout evidence |
| 17 Engineering | VERIFIED | 25 tests; frozen full CI; deterministic catalog/audit/manifest; recorded release runner |
| 18 Adversarial review | VERIFIED WITH LIMITS | Independent engineering review passed after four defects and URL edge cases were repaired; not scholarly certification |
| 19 Final verification | VERIFIED | 14 local gates passed; desktop/mobile browser checks; see exact release report and bounded scope |

States include PARTIAL / BLOCKED and VERIFIED WITH LIMITS where the mandated
scope exceeds the available intellectual or external evidence. Intellectual
readiness must not be inferred from a passing software gate.

## Slice plan

1. Recover legacy material and build contracts; prove with base comparisons and
   existing validators. Likely files: overwritten docs, configuration, tooling.
2. Strengthen canonical integrity and deterministic evidence-aware audits; prove
   with focused positive and negative tests before full generation.
3. Repair source-grounded curriculum gaps without inventing evidence or promoting
   maturity; prove with per-ID reports and representative substantive review.
4. Integrate reports, navigation, CI and release controls; prove with the complete
   final-tree checks and reproducibility verification.

## Decisions

### Preserve the staged import

- Issue: imported files overwrite an existing repository without a merge commit.
- Evidence: HEAD equals main; staged additions/modifications; handoff warns that
  Frontier routing pages are not copies of richer legacy detail pages.
- Decision: use `8b98ed1` as the fixed reconciliation base, preserve both valuable
  layers, and make reviewable working-tree edits without changing the index.
- Files affected: legacy comparison inventory and any proven regressions.
- RFC required: no for restoration; yes for substantive curriculum architecture.

## Open risks

- The snapshot labels its build/check date 2026-09-07, later than this session's
  stated date (2026-09-06). Imported dates are not independently verified.
- Protected technical material is unchanged; overwritten orientation/governance
  content was reconciled, with changes recorded against the fixed base.
- Source links/counts do not demonstrate scholarship, valid licenses, or learning.
- External review, unseen holdouts, and longitudinal outcomes cannot be invented.
- Reference-grade human formation is an aspiration, not a software-test result.
- PH's 117-node graph has no explicit node prerequisite list in the imported JSON.
  Preserve it without inventing scholarly closure; report this as a documentary gap.
- All Souls rows contain paraphrased cues, not permission to redistribute exam papers.
- The extracted duplicate snapshot directories are user-provided provenance artifacts,
  not another canonical curriculum. Preserve them but exclude them from owned-doc lint.

### Correct interfaces and attach preserved teaching

- Issue: ML-M01/03/05 and DR-D01 interface labels did not resolve to current module IDs.
- Evidence: canonical titles show attention=ML02, expertise/mentorship=ML06/ML12,
  bounded judgment=ML14, visual/spatial reasoning=DR03/DR06.
- Decision: preserve imported labels as provenance and add explicit endpoint arrays.
  Attach each TS-F01..22 to its existing weekly teaching and exit-assessment page;
  recover conceptual descriptions from those pages, and add specific deletion reasons.
- Files: modules, interfaces, content-evidence, reconciliation script and reports.
- RFC required: no new curriculum unit; architecture interpretation documented here.

### Life competency routes

- Issue: all 72 competencies had prose knowledge/practice/evidence but no stable
  disciplinary routes or professional scope contracts.
- Decision: add one canonical route map and twelve shared scope contracts. Explicitly
  label computation, software systems, Earth/ecology and food/water routes partial.
- Evidence: all target IDs resolve in the graph audit; full expertise is not implied.
- Files: `life-routes.json`, `life-scope.json`, audit/report generator.
- RFC required: crosswalk policy to be included in the reconciliation RFC.

## Final verification and handoff

- Run `uv run --frozen python scripts/verify_release.py` to repeat all 14 local gates.
- Recorded outputs: `reports/release-verification.json`; generated human summary:
  `RELEASE_READINESS.md`. Report files and this operational state are excluded from
  the source manifest to avoid report/self-hash cycles.
- 25 regression tests pass. Ruff, compilation, graph/repository validation, strict
  prose, contrast, source and built UI checks, clean Zensical build and both drift
  checks pass. Hosted CI was not executed.
- The bounded review found platform-specific manifest ordering, unstable life
  fragments, wrong-family references and weak source-review metadata. All have
  reproducing regression tests and passed the third review. No Critical or Required
  engineering findings remain in that review's scope.
- Browser checks: 1440x1000 and 390x844, home, specialization index, stage index,
  life routes and design studio. All had nonempty content, no horizontal overflow,
  and valid requested fragments. Screenshots inspected in dark desktop/mobile and
  light desktop. Search found and opened the learning lab; theme toggle worked.
- Local preview remains at http://127.0.0.1:8001/ (built site, not remote publication).
- Source inventory: 71 records lack explicit source-link/constitutional references;
  15 are constitutional-only. Many unlinked records are anchor candidates. Names
  alone are not inferred as typed teaching links.
- Documentary maturity: 26 modules assessment-ready, 58 source-spined, 364 nodes
  scaffold; zero internally stress-tested, externally stress-tested or reference-grade.
- The broad goal of fully taught, independently reviewed coverage is not complete.
  See `NEXT_RESEARCH.md` for specific authored and human-evidence obligations.
- No commit, push, tag, branch creation, remote PR, reset, rebase, checkout overwrite
  or index mutation was performed. The user's staged import remains staged; new
  work remains reviewable in the working tree and untracked files.
- Final Git inspection also reports 323 working-tree deletions under the duplicate
  `open-frontier-curriculum-obelisk-v0.6.0/` snapshot and its ZIP. These were not
  performed or reverted by this agent. Review them separately before staging;
  canonical and protected legacy content passed validation. Earlier statements
  about snapshot preservation describe initial inspection, not this final state.