import json
from pathlib import Path

import pytest

from trough.links import annotation, files
from trough.vault import Container, Entry, Leaf, assign_paths, render_tree

VAULT = Path("vault")
FOLDER = VAULT / "links" / "mathlib"


def chapter() -> Container:
    cited = Leaf("Cited", "cited", [("article_id", "af_000000000000000000000001"), ("declaration", "theorem"),
                                    ("origin", "cited"), ("mathlib", "true"), ("mathlib_declaration", "A.b, A.«c d»"),
                                    ("mathlib_file", "Mathlib/A/B.lean")], "Body.")
    wanted = Leaf("Wanted", "wanted", [("declaration", "theorem"), ("origin", "cited"), ("not_ready", "true")], "Body.")
    part = Container("Part", "part", [Entry(wanted)], navigation="transparent")
    root = Container("Mathlib", "mathlib", [Entry(cited), Entry(part)])
    assign_paths(root, VAULT / "roadmap" / "mathlib")
    return root


def test_each_page_with_facts_gets_one_annotation_and_no_front_matter():
    root = chapter()
    written = files(root, FOLDER, "f" * 40)
    assert json.loads(written[FOLDER / "_defaults.json"]) == {
        "object": {"type": "lean", "uri": "https://github.com/leanprover-community/mathlib4", "version": "f" * 40}}
    rows = [json.loads(line) for line in written[FOLDER / "articles.jsonl"].splitlines()]
    assert rows == [
        {"id": "af_000000000000000000000001", "kind": "theorem",
         "subject": [{"type": "generic", "uri": "../../roadmap/mathlib/cited.md"}],
         # The front matter's mathlib_file was the first name's module.
         "object": [{"location": {"declaration": "A.b", "module": "Mathlib.A.B"}}, {"location": {"declaration": "A.«c d»"}}],
         "extensions": {"org.autoform": {"origin": "cited", "mathlib": True}}},
        {"subject": [{"type": "generic", "uri": "../../roadmap/mathlib/part/README.md"}], "object": [],
         "extensions": {"org.autoform": {"navigation": "transparent"}}},
        {"kind": "theorem", "subject": [{"type": "generic", "uri": "../../roadmap/mathlib/part/wanted.md"}], "object": [],
         "extensions": {"org.autoform": {"origin": "cited", "not_ready": True}}},
    ]
    pages = render_tree(root, VAULT, annotated=True)
    assert all(text.startswith("# ") for text in pages.values())


def test_a_module_with_no_declarations_keeps_its_module():
    row = annotation([("mathlib", "true"), ("mathlib_file", "Mathlib/A/B.lean")], VAULT / "roadmap" / "m.md", FOLDER)
    assert row["object"] == [{"location": {"module": "Mathlib.A.B"}}]


def test_a_field_with_no_annotation_key_stops_the_chapter():
    with pytest.raises(ValueError, match="no annotation field for lean"):
        annotation([("lean", "Mine.thing")], VAULT / "roadmap" / "m.md", FOLDER)
