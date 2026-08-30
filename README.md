# Open Frontier Curriculum

A technical curriculum, technology map, and resource index for students working with modern AI tools.

## Hypothesis

AI can reduce the time and labor needed to attempt some technical work. The effect is uneven. Physics, measurement, domain knowledge, manufacturing, safety, institutions, and judgment still limit results.

This curriculum emphasizes foundations that help people use stronger tools well. The [Frontier 100](docs/05-frontier/README.md) tests that emphasis against technologies that still require substantial scientific and engineering work.

## Browse

- [Start here](docs/00-start-here/README.md)
- [22 foundation modules](docs/02-core/README.md)
- [7 specialization tracks](docs/03-specializations/README.md)
- [100 frontier technologies](docs/05-frontier/README.md)
- [Essential 26-book shelf](docs/07-resources/essential-26.md)
- [Portfolio and mastery standard](docs/06-proof-of-work/README.md)
- [Human systems](docs/04-integration/README.md)

## Local preview

```bash
uv sync --frozen
uv run --frozen zensical serve
```

Open `http://localhost:8000`.

## Releases and publishing

Use a Conventional Commit title on the pull request and merge with **Squash and merge**. A successful merge to `main` creates a version tag and GitHub Release, then publishes GitHub Pages automatically. See [releases](docs/08-community/releases.md) and [publishing](docs/08-community/publishing.md).

## Writing and contributions

Read [STYLE.md](STYLE.md) before changing public prose. Read [CONTRIBUTING.md](CONTRIBUTING.md) before changing the curriculum.

Run:

```bash
uv run --frozen python scripts/lint_prose.py
uv run --frozen python scripts/validate_repo.py
```

## License

Original curriculum text: CC BY 4.0. Tooling and scripts: MIT. External sources keep their original licenses.
