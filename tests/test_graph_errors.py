import contextlib
import importlib.util
import io
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


class GraphErrorTest(unittest.TestCase):
    def run_validator(self, transform=None, missing_schema=False):
        original_read = Path.read_text

        def read_text(path, *args, **kwargs):
            text = original_read(path, *args, **kwargs)
            if transform and path.name == "nodes.json":
                return transform(text)
            return text

        spec = importlib.util.spec_from_file_location(
            "scripts.validator_fixture", ROOT / "scripts" / "validate_obelisk.py"
        )
        module = importlib.util.module_from_spec(spec)
        output = io.StringIO()
        with (
            patch.object(Path, "read_text", read_text),
            contextlib.redirect_stdout(output),
            patch.dict("sys.modules", {"jsonschema": None} if missing_schema else {}),
        ):
            try:
                spec.loader.exec_module(module)
            except SystemExit as exc:
                return exc.code, output.getvalue()
        return 0, output.getvalue()

    def test_unknown_module_is_reported_without_traceback(self):
        import json

        def unknown_module(text):
            document = json.loads(text)
            document["nodes"][0]["module_id"] = "MISSING-MODULE"
            return json.dumps(document)

        status, output = self.run_validator(unknown_module)
        self.assertEqual(status, 1)
        self.assertIn("unresolved module MISSING-MODULE", output)

    def test_schema_dependency_is_required(self):
        status, output = self.run_validator(missing_schema=True)
        self.assertEqual(status, 1)
        self.assertIn("jsonschema", output)


if __name__ == "__main__":
    unittest.main()