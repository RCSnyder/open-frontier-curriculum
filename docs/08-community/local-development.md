# Local development with uv + Zensical

The documentation toolchain uses Python, uv and Zensical, with validation and lint dependencies pinned in the lockfile.

## 1. Install uv

Follow the official uv installation method for your platform, then from the repository root:

```bash
uv sync --frozen
```

`uv.lock` is already committed. Ordinary setup must not re-resolve dependencies; `uv sync --frozen` installs exactly the checked-in resolution.

## 2. Preview the site

```bash
uv run --frozen zensical serve
```

Open `http://localhost:8000`.

## 3. Validate the repository

```bash
uv run --frozen python scripts/lint_prose.py --strict
uv run --frozen python scripts/validate_repo.py
uv run --frozen python scripts/audit_ui.py
uv run --frozen python scripts/audit_contrast.py
```

## 4. Build the static site

```bash
uv run --frozen python scripts/build_docs.py
uv run --frozen python scripts/audit_ui.py --site .verification/site
```

The isolated build writes to `.verification/site/`, which is ignored by Git.
It checks for duplicate published routes and can run alongside the preview server without sharing its build cache.

## Why uv

`uv run` automatically keeps the project environment synchronized with `pyproject.toml`/`uv.lock`, which makes the docs toolchain reproducible without asking contributors to manually activate a virtualenv.

## Why Zensical

Zensical is only the **renderer**. Curriculum content stays Markdown-first. GitHub/GitLab remain readable, and a future renderer migration does not require rewriting the curriculum.

## Repository and site URLs

The GitHub Pages URL, repository URL and edit path are configured in `zensical.toml`.
Update those values when publishing a fork, and verify the deployed site's paths after publication.
Local builds do not prove that GitHub Pages deployment has succeeded.

## 5. Browser review

Check the home page, specialization index, one specialization, one frontier index, and one long module at 390, 768, 1440, and 1728 CSS pixels wide. Check both color schemes. The detailed checklist is in [UI review](ui-review.md).
