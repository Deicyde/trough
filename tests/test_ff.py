import json
from pathlib import Path

import pytest

from trough import blueprints, catalog, ff
from trough.vault import Leaf, assign_paths, render_tree, walk

ROOT = Path(__file__).resolve().parent.parent
REV = "a" * 40
BASE_REV = "b" * 40
BLOB = f"https://github.com/FormalFrontier/lib/blob/{REV}"

README = """# lib

Intro, with [a guide](docs/Guide.md).

## Headline results

- **Bold title.** It holds for every `x`
  ([module](Lib/A.lean)).
- [`Lib.thm`](Lib/A.lean): if `p` then `q`.
- [Guide](docs/Guide.md) explains the setup.
- [`Lib.a` and `Lib.b`](Lib/A.lean) are equal.
- A plain result with no link. And a second sentence.
- **Again.** The [`Lib.thm`](Lib/A.lean) theorem, once more.
- **Stated.** See [`Lib.stated`](Lib/A.lean).
- **A module.** See [`Lib.A`](Lib/A.lean).

### A group

Group intro with [a file](Lib/B.lean).

- **[Grouped](Lib/B.lean).** Uses [`Lib.B.grouped`](Lib/B.lean#L3).

### A result on its own

The prose [`Lib.alone`](Lib/C.lean) proves it.

```lean
## not a heading
```

## Other

- **Not a headline.**
"""

YAML = """version: "v0.4"
project:
  name: "lib"
  description: "A library for tests."
  authors: ["Formal Frontier Agents"]
  license: "Apache-2.0"
highlights:
  - title: "The highlight"
    statement: "For every `x`, the theorem holds."
    declarations:
      - declaration: "Lib.thm"
        file: "Lib/A.lean"
      - declaration: "Lib.gone"
        file: "Lib/A.lean"
sources:
  - title: "A book"
    authors: ["A. Author"]
    id: "https://example.org/book"
    type: "book"
    relationship: "background"
related_formalizations:
  - id: "https://github.com/FormalFrontier/base"
    relationship: "builds-on"
automation:
  methods:
    - method: "agent"
      framework: "Lean"
review:
  status: "agent-reviewed"
  notes: "Reviewed by agents."
status:
  scope: "Tests only."
  main_results:
    - declaration: "Lib.thm"
      file: "Lib/A.lean"
      note: "The main | result."
      sorry_count: 0
    - declaration: "Lib.helper"
      file: "Lib/A.lean"
"""

LEAN = {
    "Lib/A.lean": "namespace Lib\n\ntheorem thm : True := trivial\n\ntheorem stated : True := by\n  sorry\n\nend Lib\n",
    "Lib/B.lean": "namespace Lib.B\ntheorem grouped : True := trivial\nend Lib.B\n",
    "Lib/C.lean": "theorem Lib.alone : True := trivial\n",
}

APACHE = "\n                                 Apache License\n                           Version 2.0, January 2004\n"


def checkout(tmp_path: Path, name: str, yaml: str, readme: str, lean: dict[str, str], manifest: dict,
             license_text: str = APACHE) -> Path:
    root = tmp_path / name
    files = {"formalization.yaml": yaml, "README.md": readme, "LICENSE": license_text,
             "lean-toolchain": "leanprover/lean4:v4.34.0-rc2\n", "lake-manifest.json": json.dumps(manifest), **lean}
    for path, text in files.items():
        (root / path).parent.mkdir(parents=True, exist_ok=True)
        (root / path).write_text(text, encoding="utf-8")
    return root


MANIFEST = {"packages": [
    {"name": "base", "url": "https://github.com/FormalFrontier/base", "rev": BASE_REV, "inherited": False},
    {"name": "mathlib", "url": "https://github.com/leanprover-community/mathlib4", "rev": "c" * 40, "inherited": False},
    {"name": "far", "url": "https://github.com/FormalFrontier/far.git", "rev": "d" * 40, "inherited": True},
]}


def lib_record(tmp_path):
    root = checkout(tmp_path, "lib", YAML, README, LEAN, MANIFEST)
    paths = set(LEAN) | {"README.md", "docs/Guide.md", "formalization.yaml"}
    return ff.read_library(root, "lib", REV, "2026-11-05T00:00:00Z", paths)


def base_record(tmp_path):
    yaml = YAML.split("highlights:")[0] + "sources:\n  - title: \"Folklore\"\n" + (
        "automation:\n  methods:\n    - method: \"agent\"\nreview:\n  status: \"unchecked\"\n")
    root = checkout(tmp_path, "base", yaml.replace('"lib"', '"base"'), "# base\n\n## Headline results\n\n- **Nothing named.** Text.\n",
                    {}, {"packages": []})
    return ff.read_library(root, "base", BASE_REV, "2026-11-01T00:00:00Z", {"README.md"})


def test_the_headline_section_ends_at_the_next_section_and_skips_code():
    lines = ff.section(README)
    assert lines[0] == "" and "- **Not a headline.**" not in lines
    assert "## not a heading" in lines


def test_headline_items_take_their_titles_text_and_declaration_links():
    items = ff.headlines(README, ff.Links("lib", REV, set(LEAN) | {"docs/Guide.md"}))
    kinds = [item["kind"] for item in items]
    assert kinds == ["item"] * 8 + ["heading", "prose", "item", "item"]
    bold, lead, guide, several, plain = items[:5]
    assert bold["title"] == "Bold title"
    assert bold["text"] == f"It holds for every `x`\n([module]({BLOB}/Lib/A.lean))."
    assert bold["link"] == {"text": "module", "url": f"{BLOB}/Lib/A.lean", "code": False} and bold["declaration"] is None
    assert lead["title"] == "`Lib.thm`" and lead["text"] == "If `p` then `q`."
    assert lead["declaration"] == {"name": "Lib.thm", "file": "Lib/A.lean"}
    assert guide["title"] == "Guide" and guide["text"] == "explains the setup."
    assert several["declaration"] is None
    assert plain["title"] == "A plain result with no link" and plain["title_in_text"]
    assert items[9] == {"kind": "prose", "text": f"Group intro with [a file]({BLOB}/Lib/B.lean)."}
    grouped, alone = items[10:]
    # A link in a title keeps only its label; a line anchor is not part of the file.
    assert grouped["title"] == "Grouped" and grouped["declaration"] == {"name": "Lib.B.grouped", "file": "Lib/B.lean"}
    # A heading with no list under it is one result: the prose is its text.
    assert alone["title"] == "A result on its own" and alone["declaration"]["name"] == "Lib.alone"
    assert alone["text"].endswith("```lean\n## not a heading\n```")


def test_a_library_record_finds_each_named_declaration_in_its_file(tmp_path):
    record = lib_record(tmp_path)
    assert record["schema"] == ff.SCHEMA and record["id"] == "ff-lib" and record["rev"] == REV
    assert record["toolchain"] == "v4.34.0-rc2" and record["mathlib"] == "c" * 40
    assert record["depends"] == [{"name": "base", "rev": BASE_REV}]
    assert record["related"] == [{"name": "base", "relationship": "builds-on"}]
    [highlight] = record["highlights"]
    assert highlight["declarations"] == [
        {"name": "Lib.thm", "file": "Lib/A.lean", "found": {"line": 3, "kind": "theorem", "stated": False}},
        {"name": "Lib.gone", "file": "Lib/A.lean", "found": None},
    ]
    named = {item["declaration"]["name"]: item["declaration"]["found"] for item in record["headlines"] if item.get("declaration")}
    assert named == {"Lib.thm": {"line": 3, "kind": "theorem", "stated": False},
                     "Lib.stated": {"line": 5, "kind": "theorem", "stated": True}, "Lib.A": None,
                     "Lib.B.grouped": {"line": 2, "kind": "theorem", "stated": False},
                     "Lib.alone": {"line": 1, "kind": "theorem", "stated": False}}
    assert [(result["name"], result["found"] is not None) for result in record["main_results"]] == [
        ("Lib.thm", True), ("Lib.helper", False)]
    assert record["main_results"][0]["note"] == "The main | result." and record["main_results"][0]["sorry_count"] == 0
    assert ff.found_names(record) == {"Lib.thm", "Lib.stated", "Lib.B.grouped", "Lib.alone"}


def test_a_library_that_is_not_apache_licensed_is_refused(tmp_path):
    root = checkout(tmp_path, "mit", YAML, README, LEAN, MANIFEST, license_text="MIT License\n\nCopyright ...")
    with pytest.raises(ValueError, match="not Apache-2.0"):
        ff.read_library(root, "mit", REV, "", set(LEAN))
    root = checkout(tmp_path, "other", YAML.replace('license: "Apache-2.0"', 'license: "MIT"'), README, LEAN, MANIFEST)
    with pytest.raises(ValueError, match="'MIT'"):
        ff.read_library(root, "other", REV, "", set(LEAN))


def build(tmp_path):
    entries = [{"id": "ff-lib", "name": "Lib", "repo": "FormalFrontier/lib", "group": "formal-frontier", "subject": "Topology"},
               {"id": "ff-base", "name": "Base", "repo": "FormalFrontier/base", "group": "formal-frontier",
                "subject": "Commutative algebra"}]
    built, sections = ff.chapter(list(zip(entries, [lib_record(tmp_path), base_record(tmp_path)])))
    vault = Path("blueprint")
    assign_paths(built.root, vault / "roadmap" / "formal-frontier")
    blueprints.resolve(built, vault)
    return built, sections, render_tree(built.root, vault)


def test_articles_are_the_highlights_and_the_headline_results_with_a_declaration_found(tmp_path):
    built, sections, _ = build(tmp_path)
    leaves = {node.title: node for node in walk(built.root) if isinstance(node, Leaf)}
    assert set(leaves) == {"The highlight", "Stated", "Grouped", "A result on its own"}
    stats = built.stats
    assert stats["articles"] == 4 and stats["highlight_articles"] == 1 and stats["headline_articles"] == 3
    # `Lib.thm` heads the highlight's article, so the two README items naming it link that article.
    assert stats["headline_duplicates"] == 2 and stats["headline_not_found"] == 1 and stats["headline_unnamed"] == 5
    assert stats["libraries_without_articles"] == 1 and stats["libraries"] == 2
    lib = next(section for section, _ in sections if section.slug == "lib")
    shared = [entry for entry in lib.entries if entry.node is leaves["The highlight"]]
    assert [(entry.owned, entry.label) for entry in shared] == [(True, None), (False, "`Lib.thm`"), (False, "Again")]
    assert [entry.node.title for entry in built.root.entries] == ["Commutative algebra", "Topology"]
    links = dict(sections)[lib]
    assert links["Lib.thm"] == f"{BLOB}/Lib/A.lean#L3" and set(links) == {"Lib.thm", "Lib.stated", "Lib.B.grouped", "Lib.alone"}


def test_an_article_quotes_its_statement_and_links_its_declaration(tmp_path):
    _, _, files = build(tmp_path)
    page = files[Path("blueprint/roadmap/formal-frontier/topology/lib/the-highlight.md")]
    assert page.startswith("---\ndeclaration: theorem\norigin: cited\nlean: Lib.thm\nstatement: formalized\nproof: formalized\n---")
    assert "For every `x`, the theorem holds.\n\n*Quoted from the highlights in [formalization.yaml]" in page
    assert f"at commit [aaaaaaaa](https://github.com/FormalFrontier/lib/tree/{REV}), Apache-2.0.*" in page
    assert f"- `Lib.thm` (theorem), declared in [Lib/A.lean, line 3]({BLOB}/Lib/A.lean#L3)." in page
    assert f"- `Lib.gone`, which it also names, is not found declared in [Lib/A.lean]({BLOB}/Lib/A.lean)." in page
    assert ff.NO_DEPENDS in page
    stated = files[Path("blueprint/roadmap/formal-frontier/topology/lib/stated.md")]
    assert "statement: formalized\n---" in stated and "proof:" not in stated
    assert "its text there contains `sorry`, so it is stated without proof" in stated
    assert "*Quoted from the headline results in [README.md]" in stated


def test_a_library_page_has_its_facts_links_text_and_main_results(tmp_path):
    _, _, files = build(tmp_path)
    page = files[Path("blueprint/roadmap/formal-frontier/topology/lib/README.md")]
    assert "> A library for tests.\n\n*Quoted from the project description" in page
    assert "- Review status: “agent-reviewed”\n- Review notes: “Reviewed by agents.”" in page
    assert "- Automation: agent; framework “Lean”" in page
    assert "- [A book](https://example.org/book), A. Author (book; background)." in page
    assert f"- [Base](../../commutative-algebra/base/README.md) (a Lake dependency, pinned at bbbbbbbb)" in page
    assert "### A group\n\nGroup intro with" in page
    assert "**Bold title.** It holds for every `x`" in page
    assert "A plain result with no link. And a second sentence." in page and "**A plain result" not in page
    assert f"| `Lib.thm` | theorem | [Lib/A.lean, line 3]({BLOB}/Lib/A.lean#L3) | The main \\| result. Sorry count 0. |" in page
    assert f"`Lib.helper` ([Lib/A.lean]({BLOB}/Lib/A.lean))" in page
    base = files[Path("blueprint/roadmap/formal-frontier/commutative-algebra/base/README.md")]
    assert "No articles: its formalization.yaml lists no highlights, and none of the 1 headline results" in base
    assert "## Used by\n\n- [Lib](../../topology/lib/README.md)" in base
    assert "**Nothing named.** Text." in base
    root = files[Path("blueprint/roadmap/formal-frontier/README.md")]
    assert "- [Lib](topology/lib/README.md) (4 articles): A library for tests." in root


def test_the_committed_records_build_the_chapter():
    libraries = catalog.load(ROOT / "catalog" / "libraries.toml")
    members = [library for library in libraries if library["group"] == "formal-frontier"]
    pairs = ff.load_libraries(ROOT / "data", libraries)
    assert len(pairs) == len(members) and {library["subject"] for library in members} <= set(catalog.SUBJECTS)
    for library, record in pairs:
        assert record["schema"] == ff.SCHEMA and record["id"] == library["id"] and record["repo"] == library["repo"]
        assert len(record["rev"]) == 40 and record["license"] == "Apache-2.0"
    built, sections = ff.chapter(pairs)
    leaves = [node for node in walk(built.root) if isinstance(node, Leaf)]
    assert len(leaves) == built.stats["articles"] > 0
    linked = {name for _, links in sections for name in links}
    assert linked == {name for leaf in leaves for name in dict(leaf.fields)["lean"].split(", ")}
