import csv
import shutil
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts.validate_repo import ROOT, frontier_errors


class FrontierErrorsTest(unittest.TestCase):
    def setUp(self):
        self.directory = TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        (self.root / "data").mkdir()
        for name in ("frontier-100.csv", "frontier-100.json", "program.json"):
            shutil.copyfile(ROOT / "data" / name, self.root / "data" / name)
        shutil.copytree(ROOT / "data/tracks", self.root / "data/tracks")
        shutil.copytree(ROOT / "docs/05-frontier/technologies", self.root / "docs/05-frontier/technologies")

    def mutate_csv(self, change):
        path = self.root / "data/frontier-100.csv"
        with path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            fields = reader.fieldnames
            rows = list(reader)
        change(rows)
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)

    def test_preserved_frontier_passes(self):
        self.assertEqual(frontier_errors(self.root), [])

    def test_duplicate_rank_fails(self):
        self.mutate_csv(lambda rows: rows[0].update(Rank="2"))
        self.assertIn("Frontier CSV ranks must be unique 1..100", frontier_errors(self.root))

    def test_malformed_rank_is_diagnostic(self):
        self.mutate_csv(lambda rows: rows[0].update(Rank="unknown"))
        self.assertIn("Frontier CSV ranks must be integers 1..100", frontier_errors(self.root))

    def test_empty_class_fails(self):
        self.mutate_csv(lambda rows: rows[0].update(Class=""))
        self.assertIn("Invalid Frontier class/track: 1", frontier_errors(self.root))

    def test_missing_page_fails(self):
        next((self.root / "docs/05-frontier/technologies").glob("*.md")).unlink()
        self.assertTrue(any("Expected 100" in error for error in frontier_errors(self.root)))

    def test_title_drift_fails(self):
        self.mutate_csv(lambda rows: rows[0].update({"Frontier technology": "Changed title"}))
        self.assertIn("Frontier title/bottleneck drift: 1", frontier_errors(self.root))