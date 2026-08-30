# UI review

Review the built site for every change that affects layout, navigation, cards, or typography.

## Required viewports

| Viewport | Use |
|---|---|
| 390 x 844 | phone baseline |
| 768 x 1024 | tablet / narrow desktop |
| 1440 x 900 | desktop |
| 1728 x 1117 | wide desktop |

Check both light and dark themes.

## Required pages

- Home page
- Specialization index
- One specialization page
- Frontier index by track
- One feasibility class
- One long foundation module

## Acceptance checks

- Card titles align with their descriptions and metadata.
- Cards use one column on narrow screens.
- Body text remains readable without zoom.
- Dark-mode headings, card titles, body text, muted metadata, and links retain clear contrast against page and card surfaces.
- No card, table, heading, code block, or URL creates horizontal page scroll.
- Keyboard focus is visible.
- Status labels remain clear without color.
- Reduced-motion settings remove hover and transition motion.
- Tables scroll inside their own container on narrow screens.

Run the source and built-site checks before browser review:

```bash
uv run --frozen python scripts/audit_ui.py
uv run --frozen python scripts/audit_contrast.py
uv run --frozen zensical build --clean
uv run --frozen python scripts/audit_ui.py --site site
```
