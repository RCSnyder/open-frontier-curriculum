# Contributing

Pull requests and merge requests are welcome.

## Small changes

Submit typos, broken links, source updates, and clear wording fixes directly.

## Curriculum changes

Use an RFC for additions, deletions, prerequisite changes, frontier-route changes, or major changes to the curriculum structure.

A substantive proposal must state:

- capability gained;
- prerequisite and downstream effects;
- deletion test;
- opportunity cost;
- evidence;
- proof of mastery;
- strongest argument against the change;
- safety or governance effects.

`This is important` is not enough.

## Sources

Prefer primary, official, author-hosted, publisher-hosted, university, standards-body, or open-license sources. Do not submit pirate copies.

Label normative arguments, memoirs, practitioner methods, and empirical research by source type.

## Writing

Read [STYLE.md](STYLE.md). Use plain technical English. Keep established technical terms exact. Remove filler, promotional language, fake suspense, and repeated conclusions.

## Safety

The repository can explain risky technologies at the level needed for prerequisites, safety, governance, and research boundaries. Do not add instructions that materially enable weapons, malicious software, or unsafe biological manipulation.

## Checks

```bash
uv sync --frozen
uv run --frozen python scripts/lint_prose.py
uv run --frozen python scripts/validate_repo.py
uv run --frozen zensical build --clean
```

## Tool updates

Normal setup uses the committed lockfile:

```bash
uv sync --frozen
```

Update the toolchain in a focused pull request. Regenerate `uv.lock`, inspect the diff, and return CI to frozen commands.

## Commit messages

Use Conventional Commits. Prefer `feat(curriculum): ...` for substantive additions and `fix(...): ...` for corrections. `docs:` is for documentation-only maintenance that should not create a release by itself. Pull request titles are checked because the repository expects squash merges.

See `docs/08-community/releases.md`.
