import json
import os
import subprocess
from pathlib import Path

import pytest

import refresh_ff
from trough import blueprints, catalog, ff
from trough.vault import Container, Leaf, assign_paths, render_tree, walk

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
- **Led** ([`Lib.led`](Lib/C.lean)). The lead link goes.
- [The file](Lib/C.lean)
- [Contents](docs/Guide.md#contents)
- [More contents](#headline-results)

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
  - id: "https://github.com/FormalFrontier/base/tree/0123abcd"
    relationship: "builds-on"
automation:
  methods:
    - method: "agent"
      framework: "Lean"
      prompting_notes: "Hypotheses stated."
      notes: "No cost claim."
review:
  status: "agent-reviewed"
  notes: "Reviewed by agents."
  reviewers: ["An agent"]
status:
  main_results:
    - declaration: "Lib.thm"
      file: "Lib/A.lean"
      note: "The main | result."
      sorry_count: 0
    - declaration: "Lib.helper"
      file: "Lib/A.lean"
    - declaration: "Other.thm"
      file: "../other/Other.lean"
"""

LEAN = {
    "Lib/A.lean": "namespace Lib\n\ntheorem thm : True := trivial\n\ntheorem stated : True := by\n  sorry\n\nend Lib\n",
    "Lib/B.lean": "namespace Lib.B\ntheorem grouped : True := trivial\nend Lib.B\n",
    "Lib/C.lean": "theorem Lib.alone : True := trivial\ntheorem Lib.led : True := trivial\n",
}

APACHE = "\n                                 Apache License\n                           Version 2.0, January 2004\n"
OTHER_THM = "theorem Other.thm : True := trivial\n"


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
    # A sibling checkout must not answer for a file outside this one.
    (tmp_path / "other").mkdir(exist_ok=True)
    (tmp_path / "other" / "Other.lean").write_text(OTHER_THM, encoding="utf-8")
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
    # The two entries that only link into the README or docs/ are a table of contents, not results.
    assert kinds == ["item"] * 10 + ["heading", "prose", "item", "item"]
    bold, lead, guide, several, plain = items[:5]
    # Each item's text is as the README writes it, with its links made absolute.
    assert bold["title"] == "Bold title" and bold["title_from"] == "bold"
    assert bold["text"] == f"**Bold title.** It holds for every `x`\n([module]({BLOB}/Lib/A.lean))."
    assert bold["link"] == {"text": "module", "url": f"{BLOB}/Lib/A.lean", "code": False} and bold["declaration"] is None
    assert lead["title"] == "`Lib.thm`" and lead["title_from"] == "declaration"
    assert lead["text"] == f"[`Lib.thm`]({BLOB}/Lib/A.lean): if `p` then `q`."
    assert lead["declaration"] == {"name": "Lib.thm", "file": "Lib/A.lean"}
    assert guide["title"] == "Guide" and guide["text"] == f"[Guide]({BLOB}/docs/Guide.md) explains the setup."
    assert several["declaration"] is None
    assert plain["title"] == "A plain result with no link" and plain["title_from"] == "sentence"
    assert items[9]["title"] == "The file" and items[9]["text"] == f"[The file]({BLOB}/Lib/C.lean)"
    assert items[11] == {"kind": "prose", "text": f"Group intro with [a file]({BLOB}/Lib/B.lean)."}
    grouped, alone = items[12:]
    # A link in a title keeps only its label; a line anchor is not part of the file.
    assert grouped["title"] == "Grouped" and grouped["declaration"] == {"name": "Lib.B.grouped", "file": "Lib/B.lean"}
    # A heading with no list under it is one result: the prose is its text.
    assert alone["title"] == "A result on its own" and alone["title_from"] == "heading"
    assert alone["declaration"]["name"] == "Lib.alone"
    assert alone["text"].endswith("```lean\n## not a heading\n```")


def test_quoted_openings_keep_the_sources_marks():
    assert ff.opening("Bounds for rings; with more after.") == "Bounds for rings; …"
    assert ff.opening("One sentence only.") == "One sentence only."
    assert ff.opening("Word " * 40) == ("Word " * 28).strip() + " …"
    # Titles drop the closing mark instead.
    assert ff.first_sentence("Bounds for rings; with more after.") == "Bounds for rings"


def test_an_article_quotes_its_item_as_written():
    led = {"title_from": "declaration", "declaration": {"name": "PolyRing"},
           "text": "[`PolyRing R n`](https://example.org/A.lean) has `n` central indeterminates."}
    assert ff.article_text(led) == led["text"]
    bold = {"title_from": "bold", "declaration": {"name": "X.y"},
            "text": "**Title** ([`X.y`](https://example.org/A.lean)). It holds, see [`X.y`](https://example.org/A.lean)."}
    assert ff.article_text(bold) == "It holds, see [`X.y`](https://example.org/A.lean)."


def test_a_library_record_finds_each_named_declaration_in_its_file(tmp_path):
    record = lib_record(tmp_path)
    assert record["schema"] == ff.SCHEMA and record["id"] == "ff-lib" and record["rev"] == REV
    assert record["toolchain"] == "v4.34.0-rc2" and record["mathlib"] == "c" * 40
    assert record["depends"] == [{"name": "base", "rev": BASE_REV}]
    assert record["related"] == [{"name": "base", "relationship": "builds-on"}]
    assert "scope" not in record and record["review"]["reviewers"] == ["An agent"]
    assert record["automation"]["methods"] == [
        {"method": "agent", "framework": "Lean", "prompting_notes": "Hypotheses stated.", "notes": "No cost claim."}]
    [highlight] = record["highlights"]
    assert highlight["declarations"] == [
        {"name": "Lib.thm", "file": "Lib/A.lean", "found": {"line": 3, "kind": "theorem", "stated": False}},
        {"name": "Lib.gone", "file": "Lib/A.lean", "found": None},
    ]
    named = {item["declaration"]["name"]: item["declaration"]["found"] for item in record["headlines"] if item.get("declaration")}
    assert named == {"Lib.thm": {"line": 3, "kind": "theorem", "stated": False},
                     "Lib.stated": {"line": 5, "kind": "theorem", "stated": True}, "Lib.A": None,
                     "Lib.B.grouped": {"line": 2, "kind": "theorem", "stated": False},
                     "Lib.led": {"line": 2, "kind": "theorem", "stated": False},
                     "Lib.alone": {"line": 1, "kind": "theorem", "stated": False}}
    assert [(result["name"], result["found"] is not None) for result in record["main_results"]] == [
        ("Lib.thm", True), ("Lib.helper", False), ("Other.thm", False)]
    assert record["main_results"][2]["file"] == "../other/Other.lean"
    assert record["main_results"][0]["note"] == "The main | result." and record["main_results"][0]["sorry_count"] == 0
    assert ff.found_names(record) == {"Lib.thm", "Lib.stated", "Lib.led", "Lib.B.grouped", "Lib.alone"}


def test_a_library_that_is_not_apache_licensed_is_refused(tmp_path):
    root = checkout(tmp_path, "mit", YAML, README, LEAN, MANIFEST, license_text="MIT License\n\nCopyright ...")
    with pytest.raises(ValueError, match="not Apache-2.0"):
        ff.read_library(root, "mit", REV, "", set(LEAN))
    root = checkout(tmp_path, "other", YAML.replace('license: "Apache-2.0"', 'license: "MIT"'), README, LEAN, MANIFEST)
    with pytest.raises(ValueError, match="'MIT'"):
        ff.read_library(root, "other", REV, "", set(LEAN))
    # Naming the license is not enough: the text must open as the Apache License 2.0 does.
    root = checkout(tmp_path, "loose", YAML, README, LEAN, MANIFEST, license_text="Not the Apache License Version 2.0\n")
    with pytest.raises(ValueError, match="not Apache-2.0"):
        ff.read_library(root, "loose", REV, "", set(LEAN))


def build(tmp_path, base=None):
    entries = [{"id": "ff-lib", "name": "Lib", "repo": "FormalFrontier/lib", "group": "formal-frontier", "subject": "Topology"},
               {"id": "ff-base", "name": "Base", "repo": "FormalFrontier/base", "group": "formal-frontier",
                "subject": "Commutative algebra"}]
    built, sections = ff.chapter(list(zip(entries, [lib_record(tmp_path), base or base_record(tmp_path)])))
    vault = Path("blueprint")
    assign_paths(built.root, vault / "roadmap" / "formal-frontier")
    blueprints.resolve(built, vault)
    return built, sections, render_tree(built.root, vault)


def test_articles_are_the_highlights_and_the_headline_results_with_a_declaration_found(tmp_path):
    built, sections, _ = build(tmp_path)
    leaves = {node.title: node for node in walk(built.root) if isinstance(node, Leaf)}
    assert set(leaves) == {"The highlight", "Stated", "Led", "Grouped", "A result on its own"}
    stats = built.stats
    assert stats["articles"] == 5 and stats["highlight_articles"] == 1 and stats["headline_articles"] == 4
    # `Lib.thm` heads the highlight's article, so the two README items naming it link that article.
    assert stats["headline_duplicates"] == 2 and stats["headline_not_found"] == 1 and stats["headline_unnamed"] == 6
    # `Lib.A` names its file's module.
    assert stats["headline_module_links"] == 1
    assert stats["libraries_without_articles"] == 1 and stats["libraries"] == 2
    lib, links, counts = next(item for item in sections if item[0].slug == "lib")
    shared = [entry for entry in lib.entries if entry.node is leaves["The highlight"]]
    assert [(entry.owned, entry.label) for entry in shared] == [(True, None), (False, "`Lib.thm`"), (False, "Again")]
    assert [entry.node.title for entry in built.root.entries] == ["Commutative algebra", "Topology"]
    assert links["Lib.thm"] == f"{BLOB}/Lib/A.lean#L3"
    assert set(links) == {"Lib.thm", "Lib.stated", "Lib.led", "Lib.B.grouped", "Lib.alone"}
    assert counts["highlight_articles"] == 1 and counts["headline_articles"] == 4


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
    # The leading link to its own declaration goes: the Lean section shows it.
    led = files[Path("blueprint/roadmap/formal-frontier/topology/lib/led.md")]
    assert "# Led\n\nThe lead link goes.\n" in led


def test_a_library_page_has_its_facts_links_text_and_main_results(tmp_path):
    _, _, files = build(tmp_path)
    page = files[Path("blueprint/roadmap/formal-frontier/topology/lib/README.md")]
    assert "> A library for tests.\n\n*Quoted from the project description" in page
    assert "- Review status: “agent-reviewed”.\n- Review notes: “Reviewed by agents.”\n- Reviewers: “An agent”." in page
    assert ("- Automation: agent; framework “Lean”; prompting notes “Hypotheses stated.”; notes “No cost claim.”"
            in page)
    assert "- [A book](https://example.org/book), A. Author (book; background)." in page
    assert f"- [Base](../../commutative-algebra/base/README.md) (a Lake dependency, pinned at bbbbbbbb)" in page
    assert "## Headline results\n\n*Quoted from the headline results in [README.md]" in page
    assert "### A group\n\nGroup intro with" in page
    assert "**Bold title.** It holds for every `x`" in page
    assert f"[`Lib.thm`]({BLOB}/Lib/A.lean): if `p` then `q`." not in page  # it links the highlight's article
    assert f"\n[The file]({BLOB}/Lib/C.lean)\n" in page and "Contents" not in page
    assert "A plain result with no link. And a second sentence." in page and "**A plain result" not in page
    assert "## Scope" not in page
    # The main results have a page of their own; the library's page counts them and names the scan's misses.
    assert "Its formalization.yaml lists 3 main results, and the scan finds 1 of them" in page
    assert f"`Lib.helper` ([Lib/A.lean]({BLOB}/Lib/A.lean))" in page
    assert "- [Main results](main-results/README.md)" in page
    assert "| `Lib.thm` |" not in page
    table = files[Path("blueprint/roadmap/formal-frontier/topology/lib/main-results/README.md")]
    assert f"| `Lib.thm` | theorem | [Lib/A.lean, line 3]({BLOB}/Lib/A.lean#L3) | The main \\| result. Sorry count 0. |" in table
    assert "The scan does not find 2 of them; [the library's page](../README.md) names them." in table and "*Quoted from the main results in [formalization.yaml]" in table
    base = files[Path("blueprint/roadmap/formal-frontier/commutative-algebra/base/README.md")]
    assert ("No articles: its formalization.yaml lists no highlights, and none of its 1 headline result links a "
            "declaration that the scan finds in the linked file at this commit, so they are quoted below.") in base
    assert "## Used by\n\n- [Lib](../../topology/lib/README.md)" in base
    assert "**Nothing named.** Text." in base
    root = files[Path("blueprint/roadmap/formal-frontier/README.md")]
    assert "- [Lib](topology/lib/README.md) (5 articles): A library for tests." in root


def test_a_long_table_of_main_results_is_split_into_pages(tmp_path):
    rows, ff.TABLE_ROWS = ff.TABLE_ROWS, 1
    try:
        record = lib_record(tmp_path)
        record["main_results"][1]["found"] = record["main_results"][0]["found"]
        page = ff.main_results_page(record)
    finally:
        ff.TABLE_ROWS = rows
    assert [entry.node.title for entry in page.entries] == ["Main results 1 to 1", "Main results 2 to 2"]
    assert "| `Lib.helper` |" in page.entries[1].node.prose and "| Declaration |" not in page.prose


def test_long_quoted_headline_results_get_a_page_of_their_own(tmp_path):
    limit, ff.QUOTE_LIMIT = ff.QUOTE_LIMIT, 100
    try:
        _, _, files = build(tmp_path)
    finally:
        ff.QUOTE_LIMIT = limit
    page = files[Path("blueprint/roadmap/formal-frontier/topology/lib/README.md")]
    assert ("## Headline results\n\nThe 12 headline results of its README are on a page of their own: 4 articles, "
            "6 quoted as text, and 2 that link an article above.\n\n- [Headline results](headline-results/README.md)") in page
    headlines = files[Path("blueprint/roadmap/formal-frontier/topology/lib/headline-results/README.md")]
    assert headlines.startswith("# Headline results\n\n*Quoted from the headline results in [README.md]")
    assert Path("blueprint/roadmap/formal-frontier/topology/lib/headline-results/led.md") in files


def test_a_part_page_holding_quoted_readme_text_credits_it(tmp_path):
    readme = "# lib\n\n## Headline results\n\n" + "".join(
        f"- **Text {n}.** Quoted.\n- **Result {n}.** See [`Lib.r{n}`](Lib/R.lean).\n" for n in range(25))
    lean = {"Lib/R.lean": "".join(f"theorem Lib.r{n} : True := trivial\n" for n in range(25))}
    root = checkout(tmp_path, "lib", YAML.split("highlights:")[0] + YAML[YAML.index("sources:"):], readme, lean, {"packages": []})
    record = ff.read_library(root, "lib", REV, "", set(lean))
    section, _, _ = ff.library_section(record, {"lib"}, {"lib": "Lib"}, [])
    parts = [entry.node for entry in section.entries if isinstance(entry.node, Container) and entry.node.navigation]
    assert len(parts) == 2
    # The first part opens with the heading and its credit; the second credits the text it holds.
    assert parts[0].prose == "" and parts[0].entries[0].before.startswith("## Headline results\n\n*Quoted from")
    assert parts[1].prose.startswith("*Quoted from the headline results in [README.md]")


def git(path: Path, *args: str) -> None:
    env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.org", "GIT_COMMITTER_NAME": "t",
           "GIT_COMMITTER_EMAIL": "t@example.org", "GIT_AUTHOR_DATE": "2026-11-05T12:00:00+02:00",
           "GIT_COMMITTER_DATE": "2026-11-05T12:00:00+02:00"}
    subprocess.run(["git", "-C", str(path), *args], check=True, capture_output=True, env=env)


def repository(root: Path) -> Path:
    git(root, "init", "--quiet")
    git(root, "add", "-A")
    git(root, "commit", "--quiet", "-m", "release")
    return root


LIBRARIES = [{"id": "ff-lib", "repo": "FormalFrontier/lib"}, {"id": "ff-base", "repo": "FormalFrontier/base"}]


def test_the_refresh_writes_every_record_or_none(tmp_path):
    checkouts, out = tmp_path / "checkouts", tmp_path / "out"
    repository(checkout(checkouts, "lib", YAML, README, LEAN, MANIFEST))
    base = repository(checkout(checkouts, "base", YAML.replace('"lib"', '"base"'), README, LEAN, {"packages": []}))
    assert refresh_ff.refresh(checkouts, LIBRARIES, out) == []
    record = json.loads((out / "lib.json").read_text(encoding="utf-8"))
    # The commit date is written in UTC.
    assert record["date"] == "2026-11-05T10:00:00Z" and len(record["rev"]) == 40
    assert ff.found_names(record) == {"Lib.thm", "Lib.stated", "Lib.led", "Lib.B.grouped", "Lib.alone"}
    # A library whose yaml no longer parses stops the whole refresh, and the other's record stays as it was.
    (base / "formalization.yaml").write_text("version: [\n", encoding="utf-8")
    git(base, "commit", "--quiet", "-am", "broken")
    kept = json.dumps(record | {"kept": True})
    (out / "lib.json").write_text(kept, encoding="utf-8")
    problems = refresh_ff.refresh(checkouts, LIBRARIES, out)
    assert len(problems) == 1 and problems[0].startswith("base: ")
    assert (out / "lib.json").read_text(encoding="utf-8") == kept


def test_the_refresh_refuses_a_record_that_finds_under_half_the_last(tmp_path):
    checkouts, out = tmp_path / "checkouts", tmp_path / "out"
    repository(checkout(checkouts, "lib", YAML, README, LEAN, MANIFEST))
    out.mkdir()
    last = {"highlights": [], "main_results": [],
            "headlines": [{"kind": "item", "declaration": {"name": f"Lib.n{n}", "found": {"line": 1}}} for n in range(11)]}
    (out / "lib.json").write_text(json.dumps(last), encoding="utf-8")
    assert refresh_ff.refresh(checkouts, LIBRARIES[:1], out) == [
        "lib: finds 5 declarations, under half the 11 its last record found"]
    assert json.loads((out / "lib.json").read_text(encoding="utf-8")) == last


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
    linked = {name for _, links, _ in sections for name in links}
    assert linked == {name for leaf in leaves for name in dict(leaf.fields)["lean"].split(", ")}
