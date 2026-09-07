"""Build documentation without sharing cache or output with a running preview."""

import json
import shutil
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def build_config(root):
    config = tomllib.loads((root / "zensical.toml").read_text(encoding="utf-8"))["project"]
    config["docs_dir"] = "docs"
    config["site_dir"] = "site"
    return config


def validate_page_routes(docs):
    routes = {}
    for path in docs.rglob("*.md"):
        relative = path.relative_to(docs)
        route = relative.parent if relative.stem.lower() in {"readme", "index"} else relative.with_suffix("")
        key = route.as_posix().casefold()
        if key in routes:
            raise ValueError(f"Duplicate published route: {routes[key]} and {relative}")
        routes[key] = relative


def main():
    validate_page_routes(ROOT / "docs")
    output = ROOT / ".verification"
    output.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="build-", dir=output) as temporary:
        directory = Path(temporary)
        config = build_config(ROOT)
        shutil.copytree(ROOT / "docs", directory / "docs")
        configuration = directory / "project.json"
        configuration.write_text(json.dumps(config), encoding="utf-8")
        result = subprocess.run(
            [sys.executable, "-c", "from zensical.main import cli; cli()",
             "build", "--clean", "-f", "project.json"],
            cwd=directory, check=False,
        )
        if result.returncode == 0:
            destination = output / "site"
            if destination.exists():
                shutil.rmtree(destination)
            shutil.copytree(directory / "site", destination)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())