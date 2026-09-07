import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import markdown

from scripts.audit_obelisk import (
    ROOT,
    content_maturity,
    graph_findings,
    load_documents,
    prerequisite_cycles,
    source_routes,
    write_or_check,
)


class MaturityTest(unittest.TestCase):
    def setUp(self):
        self.target = {
            "id": "HW01", "branch_id": "HW", "title": "Social evidence",
            "core_concepts": ["measurement"], "deletion_reason": "Cannot test claims",
            "prerequisite_ids": [], "exit_capability": "Compare two evidence routes",
        }
        self.links = [{"target_id": "HW01", "source_id": "SRC-1", "role": "spine"}]
        self.sources = {"SRC-1": {"title": "Existing source"}}

    def test_source_link_is_not_teaching_evidence(self):
        result = content_maturity(self.target, self.links, self.sources)
        self.assertEqual(result["state"], "SOURCE-SPINED")

    def test_missing_prerequisite_position_is_explicit(self):
        del self.target["prerequisite_ids"]
        result = content_maturity(self.target, self.links, self.sources)
        self.assertEqual(result["state"], "SCAFFOLD")

    def test_later_evidence_cannot_skip_earlier_gates(self):
        result = content_maturity(
            self.target, self.links, self.sources, {"reference_review": "claim"}
        )
        self.assertEqual(result["level"], 2)

    def test_inherited_coverage_does_not_become_direct(self):
        node = {"id": "HW01-N1", "module_id": "HW01"}
        direct, inherited = source_routes(node, self.links)
        self.assertEqual(direct, [])
        self.assertEqual(inherited, self.links)

    def test_review_labels_cannot_promote_stress_test_maturity(self):
        evidence = {"teaching_path": "lesson.md", "teaching_review": "reviewed",
                    "assessment_path": "exam.md", "assessment_review": "reviewed",
                    "internal_review": "passed", "external_review": "passed",
                    "frozen_architecture": "frozen", "reference_review": "passed",
                    "source_review": "passed"}
        result = content_maturity(self.target, self.links, self.sources, evidence)
        self.assertEqual(result["state"], "ASSESSMENT-READY")

    def test_unresolved_source_does_not_promote_maturity(self):
        result = content_maturity(self.target, self.links, {})
        self.assertEqual(result["state"], "STRUCTURED")

    def test_cycle_and_diamond_are_distinguished(self):
        self.assertEqual(prerequisite_cycles({"a": ["b", "c"], "b": ["d"], "c": ["d"]}), [])
        self.assertEqual(prerequisite_cycles({"a": ["b"], "b": ["a"]}), [["a", "b", "a"]])

    def test_drift_check_never_writes(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertEqual(write_or_check(root, {"view.md": "content\n"}, True), ["view.md"])
            self.assertFalse((root / "view.md").exists())
            write_or_check(root, {"view.md": "content\n"})
            self.assertEqual(write_or_check(root, {"view.md": "content\n"}, True), [])

    def test_typed_interface_unknown_target_fails(self):
        documents = load_documents(ROOT)
        documents["interfaces"]["interfaces"][0]["to_ids"] = ["NOT-A-NODE"]
        findings = graph_findings(documents, ROOT)
        self.assertTrue(any(row.get("target") == "NOT-A-NODE" for row in findings))

    def test_missing_life_route_fails(self):
        documents = load_documents(ROOT)
        del documents["life-routes"]["routes"]["L01-C01"]
        findings = graph_findings(documents, ROOT)
        self.assertTrue(any(row["code"] == "metadata-schema" and row["family"] == "life-routes"
                    for row in findings))

    def test_backtest_unknown_node_fails(self):
        documents = load_documents(ROOT)
        documents["backtests"]["sets"]["all_souls_holdout"][0]["Primary node"] = "NOT-A-NODE"
        findings = graph_findings(documents, ROOT)
        self.assertTrue(any(row.get("relation") == "backtest" for row in findings))

    def test_life_routes_render_stable_id_fragments(self):
        from scripts.audit_obelisk import audit, render_discovery

        output = render_discovery(audit())["docs/09-obelisk/life-coverage.md"]
        renderer = markdown.Markdown(extensions=["attr_list", "toc"])
        renderer.convert(output)
        fragments = {heading["id"] for heading in renderer.toc_tokens[0]["children"]}
        documents = load_documents(ROOT)
        for stage in documents["pathways"]["stages"]:
            for identity in stage["routes"]:
                if identity.startswith("L"):
                    self.assertIn(identity.lower(), fragments)

    def test_source_is_not_a_knowledge_target(self):
        for relation in ("life", "stage", "prerequisite"):
            with self.subTest(relation=relation):
                documents = load_documents(ROOT)
                source_id = documents["sources"]["sources"][0]["id"]
                if relation == "life":
                    documents["life-routes"]["routes"]["L01-C01"] = [source_id]
                elif relation == "stage":
                    documents["pathways"]["stages"][0]["routes"] = [source_id]
                else:
                    documents["nodes"]["nodes"][0]["prerequisite_ids"] = [source_id]
                self.assertTrue(any(row["code"] == "wrong-reference-family"
                                    for row in graph_findings(documents, ROOT)))

    def test_source_review_requires_real_date_and_nonempty_evidence(self):
        for field, value in (("checked", "2026-99-99"), ("rationale", ""),
                             ("evidence_url", ""), ("license_status", ""),
                             ("limitations", "   "), ("evidence_url", "not-a-url"),
                             ("evidence_url", "https://?"), ("evidence_url", "https://#"),
                             ("evidence_url", "https://:443")):
            with self.subTest(field=field, value=value):
                documents = load_documents(ROOT)
                documents["source-quality"]["sources"]["SRC-ML-HPL2"][field] = value
                self.assertTrue(any(row["code"] in {"metadata-schema", "invalid-source-review-url"}
                                    for row in graph_findings(documents, ROOT)))


if __name__ == "__main__":
    unittest.main()