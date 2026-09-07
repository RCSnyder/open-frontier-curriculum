import unittest
from html.parser import HTMLParser
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parents[1]


class FoundationGridParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.depth = 0
        self.children = []

    def handle_starttag(self, tag, attrs):
        if tag == "div" and "atlas-foundations" in dict(attrs).get("class", "").split():
            self.depth = 1
        elif self.depth:
            if self.depth == 1:
                self.children.append(tag)
            if tag not in {"img", "br", "hr", "input"}:
                self.depth += 1

    def handle_endtag(self, tag):
        if self.depth:
            self.depth -= 1


class HomepageTests(unittest.TestCase):
    def test_foundation_cards_are_direct_grid_children(self):
        source = (ROOT / "docs/index.md").read_text(encoding="utf-8")
        rendered = markdown.markdown(source, extensions=["meta", "md_in_html"])
        parser = FoundationGridParser()
        parser.feed(rendered)
        self.assertEqual(parser.children, ["a"] * 4)


if __name__ == "__main__":
    unittest.main()