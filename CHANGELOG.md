# Changelog

<!-- version list -->

## v0.1.0 (2026-08-30)

- Initial Release

## 0.6.2 - 2026-08-30

- Fix GitHub Actions uv setup by using the current setup-uv v10.0.1 action.
- Configure the canonical GitHub Pages and repository URLs.
- Simplify one-time publishing instructions.


## 0.6.1 - Readable dark mode and one-merge publishing

- Fixed the Start-here footer links so Zensical renders them as page links.
- Replaced dim inherited dark-theme text with explicit high-contrast tokens.
- Added contrast checks for headings, body text, cards, links, header chrome, search, and badges.
- Simplified the release contract: every accepted Conventional Commit type creates a release after merge.
- Kept `feat:` as a minor bump and breaking changes as major; other accepted types bump patch.
- Kept GitHub Pages publication in the same successful main-branch pipeline.
- Added a PR-title safeguard for single-commit squash merges.

## 0.6.0 - High-contrast dark mode and automated delivery

- Replaced inherited slate text opacity with explicit high-contrast dark-mode tokens.
- Raised contrast for headings, card titles, body text, metadata, links, navigation, search results, tables, code, and admonitions.
- Kept feasibility badge colors distinct while raising all dark badge pairs above 7:1 contrast.
- Added a zero-dependency WCAG contrast audit and wired it into validation and Pages builds.
- Added dark-mode contrast requirements to the UI review checklist.
- Added Conventional Commit release automation with semantic version tags and GitHub Releases.
- Added Conventional Commit PR-title validation for squash-merge workflows.
- Consolidated validation, release, and GitHub Pages publication into a gated CI pipeline.
- Added release metadata synchronization for `CITATION.cff` and `data/program.json`.
- Pinned third-party GitHub Actions to reviewed immutable commit SHAs.
- Raised dark header and search contrast; automated checks now cover those surfaces.

## 0.5.0 - UI and information-foraging audit

- Rebuilt all index card markup around Zensical's supported card-list pattern.
- Removed heading elements from cards and converted pipe-delimited subtitles to semantic metadata.
- Added consistent specialization summary cards and simplified phase heading hierarchy.
- Converted feasibility-class pages from long heading lists to responsive reference cards.
- Added theme-aware accessibility colors, focus states, reduced-motion support, and mobile typography floors.
- Added source and built-site UI audits to CI.
- Switched the docs theme to system fonts to remove a render-blocking external font dependency.

## 0.4.0 - Plain technical English

- Added a house style based on plain-language and technical-writing practice.
- Added an ASD-STE100-inspired terminology rule without claiming STE compliance.
- Added AP-style newsroom discipline as a reference, without copying proprietary entries.
- Added tropes.fyi anti-pattern checks for narrative prose.
- Rewrote the home, premise, start, AI-use, and contribution pages for higher information density.
- Added a prose linter to CI.

## 0.3.0: Information-foraging redesign

- Renamed the project to **Open Frontier Curriculum**.
- Reduced the public thesis to a five-point premise.
- Reworked the home page around four orienting questions and three entry routes.
- Added a 22-module foundation index and an Essential 26 resource shelf.
- Converted frontier and resource pages to denser mobile-friendly reference layouts.
- Removed most manifesto/deletion-test rhetoric from learner-facing pages.
- Preserved prerequisite ordering, mastery gates, research tracks, and contribution standards.

## 0.2.1: Frozen uv toolchain

- Added committed `uv.lock`.
- Replaced bootstrap `exclude-newer` date cutoff with lockfile reproducibility.
- Changed local development and CI to `uv sync --frozen` / `uv run --frozen`.
- Fixed the Zensical warning caused by a docs page linking outside `docs/`.
- Validation now rejects published-doc links that escape the Zensical docs root.

## 0.2.0: Zensical + uv site layer

- Added a pinned uv-managed Zensical documentation environment.
- Added a two-path Zensical homepage, dependency atlas, and track-based frontier explorer.
- Added custom responsive styling while preserving Markdown portability.
- Added Zensical build validation and GitHub Pages deployment with separated permissions.
- Strengthened validator checks for Zensical nav, toolchain pins, and Frontier CSV/front-matter drift.

## 0.1.0: Repository conversion

- Converted the 136-week Open Frontier Curriculum spreadsheet into a GitHub/GitBook-friendly Markdown repository.
- Added one page per core module and specialization.
- Added one page per 100 frontier technologies.
- Added 26 textbook-target pages with Amazon/open links.
- Added Wave 4 integration pages.
- Added portfolio, final oral defense, contribution RFC, validation script, and GitHub templates.
