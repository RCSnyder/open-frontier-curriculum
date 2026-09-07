import csv
import hashlib
import io
import json
import unittest

from scripts.generate_obelisk_catalog import ROOT, generate


class CatalogTest(unittest.TestCase):
    def test_frontier_json_and_track_counts_are_derived_from_csv(self):
        outputs = generate()
        rows = list(csv.DictReader(io.StringIO((ROOT / "data/frontier-100.csv").read_text(encoding="utf-8"))))
        frontier = json.loads(outputs["data/frontier-100.json"])["technologies"]
        self.assertEqual([row["title"] for row in frontier],
                 [" ".join(row["Frontier technology"].replace("\u2014", " - ").split()) for row in rows])
        program = json.loads(outputs["data/program.json"])
        self.assertEqual(program["frontier_targets"], len(rows))
        for track in program["frontier_tracks"]:
            self.assertEqual(track["count"], sum(row["Primary track"] == track["code"] for row in rows))

    def test_manifest_includes_raw_images_and_learner_script(self):
        files = json.loads(generate()["BUILD_MANIFEST.json"])["files"]
        image = "docs/assets/atlas/circuit.jpg"
        self.assertEqual(files[image], hashlib.sha256((ROOT / image).read_bytes()).hexdigest())
        self.assertIn("docs/javascripts/atlas.js", files)

    def test_manifest_uses_platform_independent_path_order(self):
        outputs = generate()
        paths = list(json.loads(outputs["BUILD_MANIFEST.json"])["files"])
        self.assertEqual(paths, sorted(paths))