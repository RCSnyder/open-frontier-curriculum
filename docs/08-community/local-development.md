# Local development with uv + Zensical

The documentation environment is intentionally tiny: **Python + uv + one pinned Zensical dependency**.

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
uv run --frozen zensical build --clean
uv run --frozen python scripts/audit_ui.py --site site
```

The output is written to `site/` and is ignored by Git.

## Why uv

`uv run` automatically keeps the project environment synchronized with `pyproject.toml`/`uv.lock`, which makes the docs toolchain reproducible without asking contributors to manually activate a virtualenv.

## Why Zensical

Zensical is only the **renderer**. Curriculum content stays Markdown-first. GitHub/GitLab remain readable, and a future renderer migration does not require rewriting the curriculum.

## Repository/site URL after you create the remote

Once the final GitHub repository name is known, add the real `site_url`, `repo_url`, and `edit_uri` to `zensical.toml`. That enables canonical URLs, instant navigation, and "edit/view source" actions without baking fake placeholder URLs into the starter patch.

## 5. Browser review

Check the home page, specialization index, one specialization, one frontier index, and one long module at 390, 768, 1440, and 1728 CSS pixels wide. Check both color schemes. The detailed checklist is in [UI review](ui-review.md).
