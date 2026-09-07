import os
import shlex
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import tomlkit
from git import Repo

ROOT = Path(__file__).resolve().parents[1]


class ReleaseAutomationTests(unittest.TestCase):
    def test_generated_sources_are_staged_not_uploaded(self):
        config = tomlkit.parse((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
        release = config["tool"]["semantic_release"]
        self.assertEqual(release["assets"], [])
        staging = shlex.split(release["build_command"].split(" && ")[-1])
        self.assertEqual(staging[:3], ["git", "add", "--"])
        self.assertEqual(set(staging[3:]), {
            "CITATION.cff", "data", "docs", "BUILD_MANIFEST.json", "CONTENT_MATURITY.md",
            "SOURCE_MATURITY.md", "RELEASE_READINESS.md", "reports/obelisk-audit.json",
            "reports/release-verification.json",
        })

    def test_semantic_release_follows_conventional_commits(self):
        with tempfile.TemporaryDirectory() as directory, Repo.init(directory, initial_branch="main") as repo:
            root = Path(directory)
            config = tomlkit.parse((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
            staging = config["tool"]["semantic_release"]["build_command"].split(" && ")[-1]
            config["tool"]["semantic_release"]["build_command"] = staging
            (root / "pyproject.toml").write_text(tomlkit.dumps(config), encoding="utf-8")
            (root / "release.toml").write_text('version = "0.6.0-rc.1"\n', encoding="utf-8")
            with repo.config_writer() as writer:
                writer.set_value("user", "name", "Release test")
                writer.set_value("user", "email", "release-test@example.invalid")
            repo.create_remote("origin", "https://github.com/example/release-fixture.git")
            repo.index.add(["pyproject.toml", "release.toml"])
            repo.index.commit("feat: candidate fixture")
            repo.create_tag("v0.1.0")
            repo.index.commit("fix: adjust fixture", skip_hooks=True)
            generated = []
            for relative in shlex.split(staging)[3:]:
                path = root / relative
                if relative in ("data", "docs"):
                    path = path / "generated.txt"
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("generated release content\n", encoding="utf-8")
                generated.append(path.relative_to(root).as_posix())

            def command(*arguments):
                invocation = [sys.executable, "-m", "semantic_release", "version", *arguments]
                if os.name == "nt":
                    invocation = ["cmd", "/c", *invocation]
                result = subprocess.run(
                    invocation, cwd=root,
                    env={**os.environ, "GH_TOKEN": ""}, text=True, capture_output=True, check=False)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                return result.stdout.strip()

            self.assertEqual(command("--print"), "0.1.1")
            command("--no-push", "--no-vcs-release")
            self.assertIn("v0.1.1", [tag.name for tag in repo.tags])
            for relative in generated:
                self.assertEqual(
                    (repo.head.commit.tree / relative).data_stream.read(),
                    b"generated release content\n")
            self.assertFalse(repo.is_dirty(untracked_files=True))
            self.assertEqual(command("--print"), "0.1.1")
            repo.index.commit("fix: adjust fixture", skip_hooks=True)
            self.assertEqual(command("--print"), "0.1.2")
            repo.index.commit("feat: extend fixture", skip_hooks=True)
            self.assertEqual(command("--print"), "0.2.0")


if __name__ == "__main__":
    unittest.main()