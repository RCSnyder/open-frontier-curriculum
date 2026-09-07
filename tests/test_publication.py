import json
import shutil
import tempfile
import tomllib
import unittest
from pathlib import Path

from scripts.generate_obelisk_catalog import generate
from scripts.learning_atlas import render_atlas
from scripts.sync_release_version import synchronize

ROOT = Path(__file__).resolve().parents[1]


class PublicationTests(unittest.TestCase):
    def test_release_stamp_regenerates_all_public_versions(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in ("docs", "data", "scripts", "schemas", "tests", "rfcs", ".github"):
                shutil.copytree(ROOT / name, root / name, ignore=shutil.ignore_patterns("__pycache__"))
            for path in ROOT.iterdir():
                if path.is_file():
                    shutil.copy2(path, root / path.name)
            (root / "release.toml").write_text('version = "0.6.0"\n', encoding="utf-8")
            synchronize(root, "0.6.0")
            for name in ("data/program.json", "data/obelisk/catalog.json", "data/obelisk/release-status.json"):
                self.assertEqual(json.loads((root / name).read_text(encoding="utf-8"))["version"], "0.6.0")
            self.assertIn("Public preview: 0.6.0.", (root / "docs/project/evidence.md").read_text(encoding="utf-8"))
            for path, text in generate(root).items():
                self.assertEqual((root / path).read_text(encoding="utf-8"), text)
            with self.assertRaisesRegex(ValueError, "disagrees"):
                synchronize(root, "0.7.0")

    def test_public_identity_is_consistent(self):
        name = "Open Frontier Curriculum"
        config = tomllib.loads((ROOT / "zensical.toml").read_text(encoding="utf-8"))
        self.assertEqual(config["project"]["site_name"], name)
        for path in ("README.md", "docs/index.md", "CONSTITUTION.md"):
            self.assertIn(f"# {name}", (ROOT / path).read_text(encoding="utf-8"))
        outputs = generate()
        self.assertEqual(json.loads(outputs["data/obelisk/catalog.json"])["name"], name)
        self.assertIn(name, (ROOT / "CITATION.cff").read_text(encoding="utf-8"))

    def test_technology_section_explains_scope_without_forecasting(self):
        page = render_atlas()["docs/05-frontier/README.md"]
        self.assertIn("# Science Fiction to Science", page)
        self.assertIn("not a forecast", page)


if __name__ == "__main__":
    unittest.main()