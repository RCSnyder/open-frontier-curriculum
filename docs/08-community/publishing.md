# Publishing

GitHub Pages hosts the public site. Zensical builds the static files.

## One-time GitHub setup

1. Open **Settings -> Pages**.
2. Set **Source** to **GitHub Actions**.
3. Open **Settings -> Actions -> General**.
4. Under **Workflow permissions**, allow **Read and write permissions** so the release job can create tags and GitHub Releases.
5. Open **Settings -> General -> Pull Requests**.
6. Enable **Squash merging** and use the **pull request title** as the squash commit message.

The public site will be:

<https://rcsnyder.github.io/open-frontier-curriculum/>

## Normal workflow

1. Open a pull request with a Conventional Commit title, such as `feat: add optics path` or `fix: correct a source`.
2. Let the checks pass.
3. Merge with **Squash and merge**.
4. GitHub Actions creates the next version tag and GitHub Release.
5. The same workflow builds Zensical and deploys GitHub Pages.

No manual release or publish command is required.

## Local preview

```bash
uv sync --frozen
uv run --frozen zensical serve
```

Open `http://localhost:8000`.
