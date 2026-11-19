from pathlib import Path

import refresh_library
from trough import comppoly
from trough.vault import Container, Leaf, walk

ROOT = Path(__file__).resolve().parent.parent

README = """# CompPoly

A formally verified library for computable polynomial operations over finite fields and
general rings, supporting univariate, multivariate, multilinear, and bivariate
polynomials. It aims to serve as the mathematical foundation for zero-knowledge
circuit verification.

## Origins and license

This repository was created by merging content.
"""


def test_the_readme_description_is_its_first_sentence():
    assert comppoly.readme_description(README) == [
        "A formally verified library for computable polynomial operations over finite fields and general rings, "
        "supporting univariate, multivariate, multilinear, and bivariate polynomials."]
    assert refresh_library.LIBRARIES["comppoly"] is comppoly.COMPPOLY


def test_the_committed_data_build_the_chapter():
    loaded = comppoly.load(ROOT / "data")
    assert loaded is not None and loaded["schema"] == comppoly.SCHEMA and loaded["repo"] == comppoly.REPO
    assert len(loaded["rev"]) == 40 and loaded["license"] == "Apache-2.0" and loaded["modules"] and loaded["mathlib"]
    result, links = comppoly.chapter(loaded)
    leaves = [node for node in walk(result.root) if isinstance(node, Leaf)]
    assert len(leaves) == result.stats["articles"] == len(result.files)
    assert result.stats["articles"] + result.stats.get("listed", 0) + result.stats.get("unbuilt", 0) == len(loaded["modules"])
    assert set(links) >= {name for leaf in leaves for name in dict(leaf.fields).get("lean", "").split(", ") if name}
    assert all(len(node.children) <= 20 for node in walk(result.root) if isinstance(node, Container))
    titles = [leaf.title for leaf in leaves]
    assert len(titles) == len(set(titles))
    assert loaded["deps"] and "built" in loaded["deps"]
    # The front page names the Mathlib commit the library builds on.
    assert f"and Mathlib {loaded['mathlib'][:8]}" in result.root.prose
