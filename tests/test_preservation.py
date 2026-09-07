import json
import unittest

from scripts.learning_atlas import ROOT
from scripts.preservation import preserved_identity_errors


class PreservationTests(unittest.TestCase):
    def test_additions_are_allowed_but_missing_imported_identities_fail(self):
        baseline = {"modules": ["TS-F01"], "nodes": ["PH-M01"]}
        records = {"modules": [{"id": "TS-F01"}, {"id": "TS-F99"}], "nodes": [{"id": "PH-M01"}]}
        self.assertEqual(preserved_identity_errors(records, baseline), [])
        records["modules"].pop(0)
        self.assertIn("Missing preserved modules identity: TS-F01", preserved_identity_errors(records, baseline))

    def test_repository_baseline_is_preserved(self):
        baseline = json.loads((ROOT / "data/obelisk/preservation-baseline.json").read_text(encoding="utf-8"))
        records = {family: json.loads((ROOT / f"data/obelisk/{family}.json").read_text(encoding="utf-8"))[family]
                   for family in ("modules", "nodes")}
        self.assertEqual(preserved_identity_errors(records, baseline), [])


if __name__ == "__main__":
    unittest.main()