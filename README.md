# Open Frontier Curriculum

**Capability, context, judgment and representation, brought together through practice.**

**Public preview, not a validated curriculum.** See [publication status and evidence](docs/project/evidence.md)
for teaching availability, source-review coverage and the limits of the imported evaluation records.

Open Frontier asks a harder question than “what should someone know for a career?”:

> **What must a human being know, practice, become, value, and remain responsible for even if machine intelligence becomes vastly more capable than any individual human?**

The learner experience has four foundations: Open Frontier, Human Worlds,
Philosophy and Expressive Command. Praxis integrates them. Development shapes
entry routes, learning practices support all four, and life contexts connect
study to responsibility. The six legacy branch classifications remain compatible
source data, rather than six competing learner-level foundations.

Read the [constitution](CONSTITUTION.md) and [design](DESIGN.md).

## Educational aim

A serious completer should connect a broad inheritance of human knowledge with practiced competence across the critical pillars of life.
Independent and AI-augmented judgment, cultivated taste, and practical and relational agency belong together.
Continued formation requires responsible authorship and stewardship in a high-capability civilization.

These are intended outcomes, not demonstrated effects or a promise to current learners.

The acceptance question is not “did they finish the pages?” It is:

> Would I trust this person to understand what matters, revise worthy ends, learn what is needed, and distinguish evidence from persuasion?
> Can they use human and machine intelligence responsibly, act competently, preserve others' agency and dignity, and accept responsibility for what they help create?

## Preserved source inventory

| Layer | Count | Purpose |
| --- | ---: | --- |
| Knowledge trunks | 6 | Technical Systems; Philosophy & Judgment; Human Worlds; Expression & Interpretation; Mind, Learning & Agency; Design & Representation |
| Modules | 84 | Load-bearing teachable units |
| Nodes / outcomes | 364 | Stable addressable intellectual capabilities |
| Life pillars | 12 | Critical domains of lived competence |
| Life competencies | 72 | Functional capability nodes across life |
| Formation modes | 12 | Read, reconstruct, practice, make, dialogue, serve, red-team, curate, decide, teach, defend, retest |
| Source records | 303 | Identified works/resources and reading areas awaiting selection; not 303 verified or unique publications |
| Source links | 911 | Recorded recommendations, including inherited routes and unselected reading areas |
| All Souls prompt mappings | 417 | Imported Philosophy / general judgment mappings; independent hold-out provenance unverified |

## Start

- [Explore the four foundations](docs/index.md)
- [Find your starting point](docs/paths/index.md)
- [Integrated practice](docs/praxis/index.md)
- [Library](docs/library/index.md)
- [Life in practice](docs/life/index.md)
- [Project purpose and limits](docs/project/index.md)

## Validate

```bash
uv sync --frozen
uv run --frozen python scripts/validate_repo.py
uv run --frozen python -m unittest discover -s tests
```

Optional documentation preview:

```bash
uv run --frozen zensical serve
```

## Status

**Unfinished public preview.** Local engineering checks do not establish scholarly completeness or curriculum efficacy.
Most study homes remain outlines, source review is incomplete, and independent learner outcomes have not been established.
The current version and source-derived counts appear in [publication status and evidence](docs/project/evidence.md).

## License

Original curriculum text: CC BY 4.0. Tooling/scripts: MIT. External sources retain their original licenses. See `LICENSE.md`.
