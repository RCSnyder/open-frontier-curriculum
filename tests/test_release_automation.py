import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import tomlkit
from git import Repo

ROOT = Path(__file__).resolve().parents[1]


class ReleaseAutomationTests(unittest.TestCase):
    def test_semantic_release_follows_conventional_commits(self):
        with tempfile.TemporaryDirectory() as directory, Repo.init(directory, initial_branch="main") as repo:
            root = Path(directory)
            config = tomlkit.parse((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
            config["tool"]["semantic_release"]["assets"] = []
            config["tool"]["semantic_release"]["build_command"] = ""
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

            def command(*arguments):
                result = subprocess.run(
                    [sys.executable, "-m", "semantic_release", "version", *arguments], cwd=root,
                    env={**os.environ, "GH_TOKEN": ""}, text=True, capture_output=True, check=True)
                return result.stdout.strip()

            self.assertEqual(command("--print"), "0.1.1")
            command("--no-push", "--no-vcs-release", "--skip-build")
            self.assertIn("v0.1.1", [tag.name for tag in repo.tags])
            self.assertEqual(command("--print"), "0.1.1")
            repo.index.commit("fix: adjust fixture", skip_hooks=True)
            self.assertEqual(command("--print"), "0.1.2")
            repo.index.commit("feat: extend fixture", skip_hooks=True)
            self.assertEqual(command("--print"), "0.2.0")


if __name__ == "__main__":
    unittest.main()