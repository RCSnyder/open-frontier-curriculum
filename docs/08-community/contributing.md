# Contributing

Submit small factual, link, edition, exercise, and wording fixes directly.

Use an RFC for changes to prerequisites, sequence, frontier routes, curriculum scope, or major source selections.

## Curriculum proposal fields

1. Target capability.
2. Prerequisite and downstream effects.
3. Deletion test.
4. Opportunity cost.
5. Strongest primary or official evidence.
6. Observable proof of mastery.
7. Strongest argument against the change.
8. Safety or misuse effects.
9. Source type for humanities and social-science material.
10. Files and data that must change.

## Checks

```bash
uv run --frozen python scripts/lint_prose.py
uv run --frozen python scripts/validate_repo.py
```

Read [Writing style](style.md) before changing public prose.
