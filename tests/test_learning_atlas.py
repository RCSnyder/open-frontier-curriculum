import json
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.build_docs import build_config, validate_page_routes
from scripts.learning_atlas import ROOT, build_atlas, render_atlas
from scripts.reconcile_obelisk_import import compatibility_only


class LearningAtlasTests(unittest.TestCase):
    def test_duplicate_published_home_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            docs = Path(directory)
            (docs / "README.md").write_text("# Earlier home", encoding="utf-8")
            (docs / "index.md").write_text("# Current home", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Duplicate published route"):
                validate_page_routes(docs)

    def test_preservation_check_detects_teaching_changes(self):
        original = b"# Proof\n\nExplain the claim.\n"
        current = (b"---\nsearch:\n  exclude: true\n---\n\n<!-- atlas-route -->\n"
                   b"> Current route\n<!-- /atlas-route -->\n\n" + original)
        self.assertTrue(compatibility_only(original, current))
        self.assertFalse(compatibility_only(original, current.replace(b"Explain", b"Skip")))

    def test_isolated_build_keeps_source_and_portable_paths(self):
        config = build_config(ROOT)
        self.assertEqual(config["docs_dir"], "docs")
        self.assertEqual(config["site_dir"], "site")

    def test_legacy_route_keeps_original_and_links_to_study_home(self):
        outputs = render_atlas()
        path = "docs/02-knowledge-trunks/ts/ts-f01-mathematical-reasoning-proof.md"
        self.assertIn("search:\n  exclude: true", outputs[path])
        self.assertIn("../../learn/mathematical-reasoning.md", outputs[path])
        self.assertIn("# TS-F01", outputs[path])

    def test_outcome_readings_remain_attached_to_subject(self):
        atlas = build_atlas()
        nodes = json.loads((ROOT / "data/obelisk/nodes.json").read_text(encoding="utf-8"))["nodes"]
        parents = {node["id"]: node["module_id"] for node in nodes if node.get("module_id")}
        links = json.loads((ROOT / "data/obelisk/source-links.json").read_text(encoding="utf-8"))["links"]
        for link in links:
            if link["target_id"] in parents:
                owner = atlas["subjects"][parents[link["target_id"]]]
                self.assertIn(link["source_id"], owner["resources"])

    def test_each_subject_has_same_dependency_view(self):
        atlas = build_atlas()
        outputs = render_atlas()
        for subject in atlas["subjects"].values():
            self.assertIn('class="atlas-dependencies"', outputs[subject["path"]])

    def test_partial_life_routes_are_not_presented_as_complete(self):
        outputs = render_atlas()
        self.assertIn("Partial coverage", outputs["docs/life/l09.md"])
        self.assertIn("Partial coverage", outputs["docs/life/l12.md"])

    def test_conflicting_foundation_membership_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "data", root / "data")
            path = root / "data/learning-design.json"
            design = json.loads(path.read_text(encoding="utf-8"))
            design["foundations"]["judgment"]["branches"].append("TS")
            path.write_text(json.dumps(design), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Duplicate foundation membership"):
                build_atlas(root)

    def test_relation_kinds_do_not_confuse_recommendations_with_prerequisites(self):
        atlas = build_atlas()
        identities = set(atlas["subjects"]) | set(atlas["resources"])
        identities.update(outcome["id"] for subject in atlas["subjects"].values()
                          for outcome in subject["outcomes"])
        for relation in atlas["relations"]:
            self.assertIn(relation["from"], identities)
            self.assertIn(relation["to"], identities)
            if relation["kind"] == "requires":
                self.assertIn(relation["from"], atlas["subjects"])
                self.assertIn(relation["to"], atlas["subjects"])
            elif relation["kind"] == "reading-recommendation":
                self.assertIn(relation["from"], atlas["resources"])

    def test_generation_is_deterministic(self):
        self.assertEqual(render_atlas(), render_atlas())

    def test_publication_status_exposes_evidence_limits(self):
        page = render_atlas()["docs/project/evidence.md"]
        status = json.loads((ROOT / "data/obelisk/release-status.json").read_text(encoding="utf-8"))
        self.assertIn(status["version"], page)
        self.assertIn("Public preview", page)
        resources = build_atlas()["resources"].values()
        reading_areas = sum(row.get("record_kind") == "reading-area" for row in resources)
        self.assertIn(f"| Identified work/resource records | {len(build_atlas()['resources']) - reading_areas} |", page)
        self.assertIn(f"| Reading areas awaiting selection | {reading_areas} |", page)
        self.assertIn("independent freeze provenance is unverified", page)
        self.assertIn("No learner-outcome or curriculum-efficacy claim", page)

    def test_reading_areas_are_not_presented_as_identified_works(self):
        outputs = render_atlas()
        index = outputs["docs/library/index.md"]
        works, areas = index.split("## Reading areas needing selection")
        for identity in ("src-ca070", "src-ex-027", "src-ph-e008", "src-ph-i016"):
            self.assertNotIn(f"]({identity}.md)", works)
            self.assertIn(f"]({identity}.md)", areas)
            page = outputs[f"docs/library/{identity}.md"]
            self.assertIn("Reading area, not a selected publication", page)
            self.assertNotIn("Open the work or publisher record", page)
            self.assertNotIn("**Author or institution:** Gap/Search", page)
        self.assertIn("[Hamlet](src-ex-022.md)", works)
        atlas = build_atlas()
        for resource in atlas["resources"].values():
            if resource.get("role") == "Gap/Search":
                self.assertEqual(resource["record_kind"], "reading-area")

    def test_teaching_source_references_preserve_prose_and_citations(self):
        outputs = render_atlas()
        literature = outputs["docs/learn/reading-literature.md"]
        learning = outputs["docs/learn/ml01.md"]
        self.assertIn("([Hamlet](../library/src-ex-014.md), "
                  "[Hamlet](../library/src-ex-022.md))", literature)
        self.assertNotIn("() points to", literature)
        self.assertIn("[How People Learn II", learning)
        self.assertIn("../library/src-ml-hpl2.md),", learning)
        self.assertNotIn("This is source \n", learning)

    def test_teaching_body_survives_compatibility_metadata(self):
        path = "docs/02-core/wave-1/01-mathematical-reasoning-proof.md"
        original = (ROOT / path).read_text(encoding="utf-8")
        original = original[original.index("# Mathematical reasoning + proof"):]
        generated = render_atlas()[path]
        self.assertTrue(generated.endswith(original))
        self.assertIn("search:\n  exclude: true", generated)

    def test_subjects_have_exactly_one_home(self):
        atlas = build_atlas()
        modules = json.loads((ROOT / "data/obelisk/modules.json").read_text(encoding="utf-8"))["modules"]
        nodes = json.loads((ROOT / "data/obelisk/nodes.json").read_text(encoding="utf-8"))["nodes"]
        self.assertEqual(len(atlas["subjects"]), len(modules) + sum(not node.get("module_id") for node in nodes))
        paths = [subject["path"] for subject in atlas["subjects"].values()]
        self.assertEqual(len(paths), len(set(paths)))
        self.assertEqual(set(atlas["foundations"]),
                         {"capability", "context", "judgment", "representation"})

    def test_prerequisites_and_resources_resolve(self):
        atlas = build_atlas()
        for subject in atlas["subjects"].values():
            for prerequisite in subject["prerequisites"]:
                self.assertIn(prerequisite, atlas["subjects"])
            for resource in subject["resources"]:
                self.assertIn(resource, atlas["resources"])

    def test_complete_journeys_have_readings_practice_and_onward_routes(self):
        outputs = render_atlas()
        for slug in ("mathematical-reasoning", "collective-action", "reading-literature"):
            page = outputs[f"docs/learn/{slug}.md"]
            for heading in ("## Before you begin", "## Study and practice", "## Continue"):
                self.assertIn(heading, page)
            self.assertNotIn("## Week", page)
            self.assertNotIn("## Deletion test", page)
            self.assertNotIn("A0, A1", page)


if __name__ == "__main__":
    unittest.main()