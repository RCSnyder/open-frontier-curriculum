import csv
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.learning_atlas import ROOT, build_atlas, render_atlas, render_frontier


class DiscoveryTests(unittest.TestCase):
    def test_frontier_csv_edit_updates_detail_without_changing_its_route(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "data", root / "data")
            shutil.copytree(ROOT / "docs/05-frontier", root / "docs/05-frontier")
            path = root / "data/frontier-100.csv"
            with path.open(encoding="utf-8", newline="") as handle:
                rows = list(csv.DictReader(handle))
            rows[32]["Frontier technology"] = "Service robotics in care"
            rows[32]["Dominant bottleneck"] = "Measured reliability under contact uncertainty"
            with path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
                writer.writeheader()
                writer.writerows(rows)
            atlas = build_atlas(root)
            original_path = build_atlas()["technologies"][33]["path"]
            self.assertEqual(atlas["technologies"][33]["path"], original_path)
            outputs = render_frontier(atlas, root)
            page = outputs[original_path]
            self.assertIn("# 33 | Service robotics in care", page)
            self.assertIn("## Bottleneck\n\nMeasured reliability under contact uncertainty", page)
            self.assertIn(rows[32]["Proof-of-work seed"], page)
            for index in ("docs/05-frontier/by-track.md", "docs/05-frontier/class-b.md", "docs/03-specializations/frontier-100.md"):
                self.assertIn("Service robotics in care", outputs[index])

    def test_support_view_comes_from_learning_design(self):
        atlas = build_atlas()
        design = json.loads((ROOT / "data/learning-design.json").read_text(encoding="utf-8"))
        self.assertEqual(atlas["support_views"], design["support_views"])

    def test_catalog_growth_and_title_change_do_not_require_count_edits(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "data", root / "data")
            shutil.copytree(ROOT / "docs/05-frontier", root / "docs/05-frontier")
            path = root / "data/obelisk/modules.json"
            document = json.loads(path.read_text(encoding="utf-8"))
            original = next(row for row in document["modules"] if row["id"] == "TS-F10")
            original["title"] = "Feedback and state estimation"
            document["modules"].append({**original, "id": "TS-F99", "title": "Additional study"})
            path.write_text(json.dumps(document), encoding="utf-8")
            atlas = build_atlas(root)
            self.assertEqual(len(atlas["subjects"]), len(build_atlas()["subjects"]) + 1)
            self.assertEqual(atlas["subjects"]["TS-F10"]["title"], original["title"])
            self.assertEqual(atlas["subjects"]["TS-F10"]["technologies"], [33])

    def test_overviews_offer_expandable_study_and_direct_resources(self):
        atlas = build_atlas()
        pages = render_atlas()
        for foundation in [*atlas["foundations"], "learning"]:
            page = pages[f"docs/foundations/{foundation}.md"]
            self.assertIn('<details class="atlas-preview">', page)
            self.assertIn("Open resource", page)
            self.assertIn("Reading details", page)
        frontier = pages["docs/05-frontier/README.md"]
        self.assertIn('data-atlas-filter="track"', frontier)
        self.assertIn('data-atlas-filter="class"', frontier)
        self.assertIn('data-atlas-filter="study"', frontier)
        self.assertIn("Introductory track resource", frontier)
        self.assertIn("Model feedback and state estimation", frontier)
        self.assertIn("Open resource", frontier)
        self.assertIn("Open resource", pages["docs/library/index.md"])
        course = pages["docs/learn/ts-f10.md"]
        self.assertIn("Eldercare/service robots", course)
        detail = pages[atlas["technologies"][33]["path"]]
        self.assertIn("## Connected study", detail)
        self.assertIn("../../learn/ts-f10.md", detail)
        self.assertIn("## First proof of work", detail)

    def test_technology_study_relationships_are_explicit_and_bidirectional(self):
        atlas = build_atlas()
        technology = atlas["technologies"][33]
        connection = next(row for row in technology["study"] if row["subject_id"] == "TS-F10")
        self.assertEqual(connection["relationship"], "background")
        self.assertTrue(connection["rationale"])
        self.assertIn(33, atlas["subjects"]["TS-F10"]["technologies"])
        self.assertTrue(technology["path"].startswith("docs/05-frontier/technologies/"))

    def test_unknown_subject_in_technology_mapping_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "data", root / "data")
            shutil.copytree(ROOT / "docs/05-frontier", root / "docs/05-frontier")
            path = root / "data/obelisk/technology-study.json"
            document = json.loads(path.read_text(encoding="utf-8"))
            document["connections"][0]["subject_id"] = "TS-MISSING"
            path.write_text(json.dumps(document), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Unknown technology study subject"):
                build_atlas(root)


if __name__ == "__main__":
    unittest.main()