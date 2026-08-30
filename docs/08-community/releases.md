# Releases

Use a Conventional Commit title for each pull request. Merge with **Squash and merge**.

The merge to `main` creates a version tag and GitHub Release automatically. The same run publishes the site to GitHub Pages.

## Version bumps

| PR title | Version bump |
|---|---|
| `feat: ...` | minor |
| `type!: ...` or `BREAKING CHANGE:` | major |
| `fix: ...`, `docs: ...`, `chore: ...`, `ci: ...`, `style: ...`, `refactor: ...`, `test: ...`, `build: ...`, `perf: ...` | patch |

Examples:

```text
feat(curriculum): add plasma diagnostics exercises
fix(frontier): correct the fusion materials backchain
docs(site): clarify the start page
feat(data)!: change the frontier CSV schema
```

## Repository settings

Set these once in GitHub:

1. **Settings -> General -> Pull Requests:** enable **Squash merging**.
2. Set the squash commit message to use the **pull request title**.
3. **Settings -> Pages -> Build and deployment:** choose **GitHub Actions**.

After that, the routine is: open PR, pass checks, merge, wait for `ci`, then use the new GitHub Release tag or Pages URL.
