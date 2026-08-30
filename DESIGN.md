# Content and interface design

The public site is a reference atlas with an opinionated curriculum.

## Reader tasks

Common visits include:

- Find the next subject to study.
- Trace the prerequisites for a technology.
- Pick a primary book for a subject.
- Check the mastery standard for a module.
- Find where history, institutions, economics, or ethics change a technical decision.

Put that information near the top of the page.

## Information design

1. Use descriptive links. Write `Fusion: bottleneck and prerequisites`, not `Learn more`.
2. Keep entry points shallow: foundations, practice, frontier, human systems.
3. Use progressive disclosure. Index pages summarize. Module pages contain execution detail. Source pages contain references.
4. Keep stable schemas. Frontier pages use `class / bottleneck / prerequisites / first project`. Module pages use `prerequisites / exit / weeks / gate / problems / books`.
5. Design for phones first. Prefer short lists and responsive cards. Use a table only when row-by-row comparison matters.
6. Use standard subject and technology names in headings.
7. Put one factual claim in a sentence when practical. Link primary or official sources for current claims.
8. Label source type: primary research, textbook, empirical synthesis, formal theory, normative argument, memoir, or practitioner method.
9. Remove motivational filler. The subjects, technologies, projects, and sources should carry the interest.
10. Keep sequence and mastery criteria explicit. They are the main editorial judgment of the curriculum.

## Prose

Public prose follows [STYLE.md](STYLE.md). Reference schemas may use fragments. Oral-defense pages may use questions. Technical terminology keeps its accepted meaning even when the word would otherwise be discouraged in general prose.

## AI claims

State the AI hypothesis once on major entry pages. Put current AI claims in the relevant specialization and source pages. Do not use AI as a reason to add repeated future-of-work commentary.

## UI acceptance criteria

The renderer is part of the product. Review the built site, not only the Markdown diff.

- Card titles are inline content. Do not put `h2`, `h3`, or other headings inside card-list items.
- Keep one card schema per index. Title, one short description, then metadata when needed.
- Use one column below 58 rem for modules, specializations, and frontier cards.
- Keep body text at 16 px or larger on common phone browsers. Reference metadata may be smaller but should remain at least 11.5 px at default zoom.
- All keyboard-focusable controls need a visible focus state.
- Color is supplementary. Status badges include the class letter in text.
- Respect reduced-motion preferences.
- Tables may scroll horizontally. Cards and headings must not create horizontal page scroll.
- Test light and dark themes. Dark narrative text, headings, links, and card metadata must meet at least WCAG AA; primary reading colors target 7:1.
- Do not add remote font dependencies. Use the system font stack unless a future design review changes this rule.

Before merging a UI change, inspect these viewports in the browser:

| Viewport | Purpose |
|---|---|
| 390 x 844 | current phone baseline |
| 768 x 1024 | tablet / narrow desktop |
| 1440 x 900 | common desktop |
| 1728 x 1117 | wide desktop |

Check `/`, `/03-specializations/`, one specialization page, `/05-frontier/by-track/`, one feasibility class, and one long module page.

Run the structural checks before browser review:

```bash
uv run --frozen python scripts/audit_ui.py
uv run --frozen python scripts/audit_contrast.py
uv run --frozen zensical build --clean
uv run --frozen python scripts/audit_ui.py --site site
```
