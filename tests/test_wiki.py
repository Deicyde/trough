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


def concepts() -> dict:
    record = {"kind": "theorem", "line": 1, "doc": "Doc.", "signature": "theorem x : True", "statement": [], "proof": []}
    return {name: dict(record, module=f"Mathlib.{name}") for name in "ABC"}


def fake_sources(cited: dict | None = None) -> mathlib.Sources:
    lists = {
        "overview": [mathlib.Item("overview", key, ("Area", "Sub"), title, line, decls=(name,))
                     for line, (key, title, name) in enumerate([("a", "alpha", "A"), ("b", "beta", "B"),
                                                                ("c", "gamma", "C")], 1)],
        "undergrad": [],
        "100": [],
        "1000": [],
    }
    deps = {"mathlib_rev": "r", "concepts": concepts(), "modules": {}, "cited": cited or {}}
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


def test_an_article_that_breaks_the_format_is_refused(tmp_path):
    with pytest.raises(ValueError, match="article_id and concept"):
        write(tmp_path, bare="No front matter.\n")
    (tmp_path / "bare.md").unlink()
    with pytest.raises(ValueError, match="not a"):
        write(tmp_path, alpha=ARTICLE.replace("- [Gamma](trough:C)", "Gamma, mostly."))
    (tmp_path / "alpha.md").unlink()
    with pytest.raises(ValueError, match="both about A"):
        write(tmp_path, alpha=ARTICLE, again=ARTICLE.replace("0001", "0003"))


def test_an_authored_article_takes_the_place_of_the_generated_text(tmp_path):
    authored = write(tmp_path, alpha=ARTICLE, area=AREA)
    root, stats, targets = mathlib.chapter(fake_sources({"A.«two words»": {"module": "Mathlib.Two"}}), authored)
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
    assert "mathlib4_docs/Mathlib/C.html#C" in area.prose
    render_tree(root, Path("blueprint"))  # the vault writer takes the authored pages


def test_a_name_the_dump_has_not_read_links_to_the_documentation_search(tmp_path):
    authored = write(tmp_path, alpha=ARTICLE)
    _, _, targets = mathlib.chapter(fake_sources(), authored)
    assert "[a lemma](https://leanprover-community.github.io/mathlib4_docs/find?pattern=A.%C2%ABtwo%20words%C2%BB#doc)" \
        in targets["A"].body


def test_an_article_about_no_concept_or_naming_none_stops_the_chapter(tmp_path):
    with pytest.raises(ValueError, match="no concept"):
        mathlib.chapter(fake_sources(), write(tmp_path, stray=ARTICLE.replace("concept: A", "concept: Z")))
    (tmp_path / "stray.md").unlink()
    with pytest.raises(ValueError, match="no article for Q"):
        mathlib.chapter(fake_sources(), write(tmp_path, alpha=ARTICLE.replace("(trough:C)", "(trough:Q)")))
    (tmp_path / "alpha.md").unlink()
    with pytest.raises(ValueError, match="no section"):
        mathlib.chapter(fake_sources(), write(tmp_path, area=AREA.replace("area:Area/Sub", "area:Area/None")))


def test_prerequisites_that_close_a_cycle_stop_the_chapter(tmp_path):
    beta = ARTICLE.replace("concept: A", "concept: B").replace("0001", "0004").replace("(trough:B)", "(trough:A)")
    beta = beta.replace("- [Gamma](trough:C)", "- [Alpha](trough:A)")
    with pytest.raises(ValueError, match="cycle"):
        mathlib.chapter(fake_sources(), write(tmp_path, alpha=ARTICLE, beta=beta))


def test_the_wikis_articles_are_valid():
    """Every committed article reads, and names concepts and prerequisites that exist."""
    data = Path(__file__).resolve().parent.parent / "data"
    authored = wiki.load(data.parent / "wiki" / "mathlib")
    _, stats, _ = mathlib.chapter(mathlib.load_sources(data), authored)
    assert stats["authored"] == sum(1 for key in authored if not key.startswith("area:"))
