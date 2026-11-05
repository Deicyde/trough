from pathlib import Path

import pytest

from trough import blueprints, mathlib, wiki
from trough.vault import assign_paths, render_tree

ARTICLE = """\
---
article_id: af_000000000000000000000001
concept: A
---

**Alpha** is [the first thing](lean:A), unlike [beta](trough:B), as [a lemma](<lean:A.«two words»>) says.

## Depends on

- [Gamma](trough:C)

## Proof depends on

- [Beta](trough:B)
"""

AREA = """\
---
article_id: af_000000000000000000000002
concept: area:Area/Sub
---

The section's own text, about [alpha](trough:A) and [the third](lean:C).
"""


def concepts(statements: dict[str, list[str]] | None = None) -> dict:
    record = {"kind": "theorem", "line": 1, "doc": "Doc.", "signature": "theorem x : True", "statement": [], "proof": []}
    return {name: dict(record, module=f"Mathlib.{name}", statement=(statements or {}).get(name, [])) for name in "ABC"}


def cited_records() -> dict:
    """What the dump's cited section gives for every name ARTICLE and AREA cite."""
    record = {"kind": "theorem", "line": 1, "signature": "theorem x : True", "deprecated": None}
    modules = {"A": "Mathlib.A", "A.«two words»": "Mathlib.Two", "C": "Mathlib.C"}
    return {name: dict(record, module=module) for name, module in modules.items()}


def fake_sources(cited: dict | None = None, unresolved: tuple[str, ...] = (),
                 statements: dict[str, list[str]] | None = None) -> mathlib.Sources:
    lists = {
        "overview": [mathlib.Item("overview", key, ("Area", "Sub"), title, line, decls=(name,))
                     for line, (key, title, name) in enumerate([("a", "alpha", "A"), ("b", "beta", "B"),
                                                                ("c", "gamma", "C")], 1)],
        "undergrad": [],
        "100": [],
        "1000": [],
    }
    deps = {"mathlib_rev": "r", "concepts": concepts(statements), "modules": {},
            "cited": cited_records() if cited is None else cited, "unresolved": list(unresolved)}
    return mathlib.Sources("r", "", lists, deps, None)


def write(directory: Path, **files: str) -> dict[str, wiki.Authored]:
    for name, text in files.items():
        (directory / f"{name}.md").write_text(text, encoding="utf-8")
    return wiki.load(directory)


def test_an_article_gives_its_concept_citations_and_prerequisites(tmp_path):
    articles = write(tmp_path, alpha=ARTICLE)
    article = articles["A"]
    assert (article.article_id, article.depends, article.proof_depends) == ("af_000000000000000000000001", ["C"], ["B"])
    assert "## Depends on" not in article.body and article.body.endswith("as [a lemma](<lean:A.«two words»>) says.")
    assert wiki.cited(articles) == ["A", "A.«two words»"]
    assert wiki.cited(write(tmp_path, area=AREA)) == ["A", "A.«two words»", "C"]  # area pages' citations too


def test_an_article_that_breaks_the_format_is_refused(tmp_path):
    with pytest.raises(ValueError, match="article_id and concept"):
        write(tmp_path, bare="No front matter.\n")
    (tmp_path / "bare.md").unlink()
    with pytest.raises(ValueError, match="not a"):
        write(tmp_path, alpha=ARTICLE.replace("- [Gamma](trough:C)", "Gamma, mostly."))
    (tmp_path / "alpha.md").unlink()
    with pytest.raises(ValueError, match="not a"):  # a second prerequisite on the same line would be lost
        write(tmp_path, alpha=ARTICLE.replace("- [Gamma](trough:C)", "- [Gamma](trough:C) and [Beta](trough:B)"))
    (tmp_path / "alpha.md").unlink()
    with pytest.raises(ValueError, match="both about A"):
        write(tmp_path, alpha=ARTICLE, again=ARTICLE.replace("0001", "0003"))
    (tmp_path / "again.md").unlink()
    with pytest.raises(ValueError, match="share an article_id"):
        write(tmp_path, alpha=ARTICLE, again=ARTICLE.replace("concept: A", "concept: B"))


def test_an_authored_article_takes_the_place_of_the_generated_text(tmp_path):
    authored = write(tmp_path, alpha=ARTICLE, area=AREA)
    root, stats, targets = mathlib.chapter(fake_sources(), authored)
    assign_paths(root, Path("blueprint/roadmap/mathlib"))
    blueprints.resolve(blueprints.Built(root, targets, {}, {}, {}), Path("blueprint"))
    alpha, beta, gamma = (targets[key] for key in "ABC")
    assert stats["authored"] == 1
    assert dict(alpha.fields)["article_id"] == "af_000000000000000000000001"
    assert alpha.fields[0][0] == "article_id"  # AutoformBot reads the id as the first front-matter line
    assert "lean:" not in alpha.body and "trough:" not in alpha.body
    assert "[the first thing](https://leanprover-community.github.io/mathlib4_docs/Mathlib/A.html#A)" in alpha.body
    assert "[a lemma](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Two.html#A.%C2%ABtwo%20words%C2%BB)" in alpha.body
    assert "[beta](beta.md)" in alpha.body
    assert alpha.depends == [gamma] and alpha.proof_depends == [beta] and not alpha.informal
    area = targets["area:Area/Sub"]
    assert area.prose.startswith("The section's own text, about [alpha](alpha.md)")
    assert alpha.body.endswith(mathlib.WRITTEN) and area.prose.endswith(mathlib.WRITTEN)  # marked as CC BY-SA text
    assert area.article_id == "af_000000000000000000000002"
    assert "mathlib4_docs/Mathlib/C.html#C" in area.prose
    render_tree(root, Path("blueprint"))  # the vault writer takes the authored pages


def test_a_citation_that_cannot_be_linked_stops_the_chapter(tmp_path):
    authored = write(tmp_path, alpha=ARTICLE)
    unread = {name: record for name, record in cited_records().items() if name != "A.«two words»"}
    with pytest.raises(ValueError, match="cites A.«two words», which the Mathlib data have no record of yet"):
        mathlib.chapter(fake_sources(unread), authored)
    with pytest.raises(ValueError, match="cites A.«two words», which Mathlib does not have at this pin"):
        mathlib.chapter(fake_sources(unread, unresolved=("A.«two words»",)), authored)
    deprecated = cited_records()
    deprecated["A"]["deprecated"] = {"replacement": "A.new"}
    with pytest.raises(ValueError, match="cites A, which Mathlib deprecates; cite A.new"):
        mathlib.chapter(fake_sources(deprecated), authored)
    deprecated["A"]["deprecated"] = {"replacement": None}
    with pytest.raises(ValueError, match="cites A, which Mathlib deprecates$"):
        mathlib.chapter(fake_sources(deprecated), authored)


def test_an_article_about_no_concept_or_naming_none_stops_the_chapter(tmp_path):
    with pytest.raises(ValueError, match="no concept"):
        mathlib.chapter(fake_sources(), write(tmp_path, stray=ARTICLE.replace("concept: A", "concept: Z")))
    (tmp_path / "stray.md").unlink()
    with pytest.raises(ValueError, match="no article for Q"):
        mathlib.chapter(fake_sources(), write(tmp_path, alpha=ARTICLE.replace("(trough:C)", "(trough:Q)")))
    (tmp_path / "alpha.md").unlink()
    with pytest.raises(ValueError, match="alpha.md: no article for Q"):
        mathlib.chapter(fake_sources(), write(tmp_path, alpha=ARTICLE.replace("[beta](trough:B)", "[beta](trough:Q)")))
    (tmp_path / "alpha.md").unlink()
    with pytest.raises(ValueError, match="no section"):
        mathlib.chapter(fake_sources(), write(tmp_path, area=AREA.replace("area:Area/Sub", "area:Area/None")))


def test_an_area_whose_heading_holds_a_slash_gets_its_text(tmp_path):
    sources = fake_sources()
    for item in sources.lists["overview"]:
        item.path = ("Area", "Normed spaces/Banach spaces")
    authored = write(tmp_path, area=AREA.replace("area:Area/Sub", "area:Area/Normed spaces/Banach spaces"))
    _, _, targets = mathlib.chapter(sources, authored)
    assert targets["area:Area/Normed spaces/Banach spaces"].prose.startswith("The section's own text")


def test_an_authored_articles_own_prerequisites_reshape_the_graph_around_it(tmp_path):
    """Lean says B uses A and C, and A uses C, so B's page shows only A. With an article for A
    that lists no prerequisites, A no longer leads to C, and B's page shows C again."""
    bare = ARTICLE.split("\n## Depends on")[0] + "\n"
    sources = fake_sources(statements={"B": ["A", "C"], "A": ["C"]})
    _, _, targets = mathlib.chapter(sources, {})
    assert [leaf.title for leaf in targets["B"].depends] == ["Alpha"]
    _, stats, targets = mathlib.chapter(sources, write(tmp_path, alpha=bare))
    assert [leaf.title for leaf in targets["B"].depends] == ["Alpha", "Gamma"] and targets["A"].depends == []
    assert (stats["lean_statement"], stats["authored_statement"]) == (1, 0)


def test_an_authored_article_drops_its_concepts_informal_edges(tmp_path):
    sources = fake_sources(statements={"A": ["B"], "B": ["A"]})  # merged, Lean's edges close a cycle
    _, stats, targets = mathlib.chapter(sources, {})
    assert [leaf.title for leaf in targets["B"].informal] == ["Alpha"] and stats["informal"] == 1
    beta = ARTICLE.replace("concept: A", "concept: B").replace("(trough:B)", "(trough:C)").split("\n## Depends on")[0]
    _, stats, targets = mathlib.chapter(sources, write(tmp_path, beta=beta + "\n"))
    assert targets["B"].informal == [] and stats["informal"] == 0


def test_a_prerequisite_may_be_a_concept_with_no_declarations(tmp_path):
    sources = fake_sources()
    sources.lists["overview"] += [mathlib.Item("overview", "w", ("Area", "Sub"), "wanted thing", 4),
                                  mathlib.Item("overview", "m", ("Area", "Sub"), "a module", 5, module="Mathlib.Mod")]
    alpha = ARTICLE.replace("- [Gamma](trough:C)", "- [Wanted](trough:overview:w)\n- [Module](trough:Mathlib.Mod)")
    _, _, targets = mathlib.chapter(sources, write(tmp_path, alpha=alpha))
    assert [leaf.title for leaf in targets["A"].depends] == ["Wanted thing", "A module"]


def test_prerequisites_that_close_a_cycle_stop_the_chapter(tmp_path):
    beta = ARTICLE.replace("concept: A", "concept: B").replace("0001", "0004").replace("(trough:B)", "(trough:A)")
    beta = beta.replace("- [Gamma](trough:C)", "- [Alpha](trough:A)")
    with pytest.raises(ValueError, match="cycle"):
        mathlib.chapter(fake_sources(), write(tmp_path, alpha=ARTICLE, beta=beta))


def test_generating_twice_writes_the_same_bytes_with_one_article_id(tmp_path):
    authored = write(tmp_path, alpha=ARTICLE, area=AREA)
    vault = tmp_path / "blueprint"
    outputs = []
    for _ in range(2):
        root, _, targets = mathlib.chapter(fake_sources(), authored)
        assign_paths(root, vault / "roadmap" / "mathlib")
        blueprints.resolve(blueprints.Built(root, targets, {}, {}, {}), vault)
        files = render_tree(root, vault)
        for path, text in files.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        outputs.append(files)
    assert outputs[0] == outputs[1]
    page = outputs[1][targets["A"].path]
    assert page.count("article_id:") == 1 and page.startswith("---\narticle_id: af_000000000000000000000001\n")


def test_link_words_join_onto_one_line_and_reference_definitions_are_refused(tmp_path):
    wrapped = ARTICLE.replace("[beta](trough:B)", "[the\nsecond $[G :\n H]$ thing](trough:B)")
    articles = write(tmp_path, alpha=wrapped)
    assert "[the second $[G : H]$ thing](trough:B)" in articles["A"].body
    # A half-open interval leaves the brackets unbalanced; the link's words still join, and nothing before them.
    interval = ARTICLE.replace("[beta](trough:B)", "[the interval $(0,\n1]$](trough:B)")
    body = write(tmp_path, alpha="\n\n## Notes\n\nA list:\n\n- one\n- two\n\n".join(interval.split("\n\n", 1)))["A"].body
    assert body.startswith("## Notes\n\nA list:\n\n- one\n- two\n\n**Alpha**")
    assert "[the interval $(0, 1]$](trough:B)" in body
    (tmp_path / "alpha.md").unlink()
    for definition in ("[beta]: trough:B", "[beta]: Lean:A", "  [beta]: < lean:A>"):
        with pytest.raises(ValueError, match="reference-style"):
            write(tmp_path, alpha=ARTICLE + f"\n{definition}\n")
        (tmp_path / "alpha.md").unlink()


@pytest.mark.parametrize("link", ['[x](lean:A "a title")', "[x](LEAN:A)", "[x]( lean:A)", "[x](<lean:A> 'a title')",
                                  "[x](< lean:A>)", "[x](lean:A\n)", '[x](trough:B "a title")', "[x](Trough:B)",
                                  "[x](trough:)"])
def test_a_link_the_generator_would_not_read_is_refused(tmp_path, link):
    """AutoformBot reads titles and capital schemes that trough's patterns skip: such a link would
    reach the site unchecked, or not at all."""
    with pytest.raises(ValueError, match=r"alpha.md:6: .* is not \(lean:Name\), \(<lean:Name>\) or \(trough:key\)"):
        write(tmp_path, alpha=ARTICLE.replace("[the first thing](lean:A)", link))


def test_the_wikis_articles_are_valid():
    """Every committed article reads, and names concepts and prerequisites that exist."""
    data = Path(__file__).resolve().parent.parent / "data"
    authored = wiki.load(data.parent / "wiki" / "mathlib")
    _, stats, _ = mathlib.chapter(mathlib.load_sources(data), authored)
    assert stats["authored"] == sum(1 for key in authored if not key.startswith("area:"))
