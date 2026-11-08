import json
from pathlib import Path

from trough import tauceti, tauceti_select
from trough.vault import Leaf, assign_paths, render_tree, walk

DATA = Path(__file__).resolve().parent.parent / "data"

STATUS = """# Status: Example

## Where this roadmap stands

**At a glance.** Prose about [`notNamed`](https://taucetiproject.org/docs/TauCeti/A.html#notNamed).

### Named results

- **A theorem** — states it ([`main`](https://taucetiproject.github.io/TauCeti/docs/TauCeti/A.html#Ex.main)), with
  [`helper`](https://taucetiproject.org/docs/TauCeti/B.html#Ex.helper%C2%B9).
- **No link** — a result the status names without a declaration.

### Notable definitions and infrastructure

- **A definition** ([`thing`](https://taucetiproject.org/docs/TauCeti/A.html#Ex.thing)), and `main` again
  ([`main`](https://taucetiproject.org/docs/TauCeti/A.html#Ex.main)).
- **Mathlib's** ([`Nat`](https://leanprover-community.github.io/mathlib4_docs/Init/Prelude.html#Nat)).

### Roadmap coverage

Layer 1 uses [`coverage`](https://taucetiproject.org/docs/TauCeti/A.html#Ex.coverage).

## The frontier

- **Next** — [`planned`](https://taucetiproject.org/docs/TauCeti/A.html#Ex.planned).
"""


def test_a_status_names_the_declarations_of_its_named_results_and_definitions_only():
    assert tauceti.status_names(STATUS) == ["Ex.main", "Ex.helper¹", "Ex.thing"]


def test_a_roadmap_title_drops_the_roadmap_prefix():
    assert tauceti.roadmap_title("# Roadmap: local fields and ramification\n\ntext", "X") == "Local fields and ramification"
    assert tauceti.roadmap_title("# Real algebraic geometry\n", "X") == "Real algebraic geometry"
    assert tauceti.roadmap_title("no heading", "Fallback") == "Fallback"
    assert tauceti.roadmap_title("# Roadmap: p-adic measures\n", "X") == "p-adic measures"


def test_read_roadmaps_keeps_roadmaps_whose_status_names_a_declaration(tmp_path):
    for path, status in [("TauCetiRoadmap/Example", STATUS), ("Completed/Empty", "## The frontier\n"),
                         ("TauCetiRoadmap/NoStatus", None)]:
        directory = tmp_path / path
        directory.mkdir(parents=True)
        (directory / "README.md").write_text("# Roadmap: an example\n", encoding="utf-8")
        if status is not None:
            (directory / "STATUS.md").write_text(status, encoding="utf-8")
    assert tauceti.read_roadmaps(tmp_path) == [
        {"id": "Example", "path": "TauCetiRoadmap/Example", "title": "An example", "names": ["Ex.main", "Ex.helper¹", "Ex.thing"]}
    ]


def test_a_docstrings_bold_opening_titles_it_with_its_sentence():
    assert tauceti.title_and_text("X.y", "**The density theorem.** For a field `K`, ...") == (
        "The density theorem", "For a field `K`, ...")
    assert tauceti.title_and_text("X.y", "**Weighted form**: if `G` is abelian") == ("Weighted form", "if `G` is abelian")
    assert tauceti.title_and_text("X.y", "**A long title that wraps\nonto a second line.** Text") == (
        "A long title that wraps onto a second line", "Text")
    assert tauceti.title_and_text("X.y", "**Weak-* compactness of `K_β`.** Text") == ("Weak-* compactness of `K_β`", "Text")
    # Bold words the sentence goes on from: the whole sentence is the title.
    lindemann = "**The Lindemann–Weierstrass theorem**, in Baker's form. The exponentials ..."
    assert tauceti.title_and_text("X.y", lindemann) == ("The Lindemann–Weierstrass theorem, in Baker's form", "The exponentials ...")
    assert tauceti.title_and_text("X.y", "**Young's inequality** for an `L¹` kernel: `‖h ⋆ f‖ ≤ ‖h‖₁ ‖f‖`.") == (
        "Young's inequality for an `L¹` kernel", "`‖h ⋆ f‖ ≤ ‖h‖₁ ‖f‖`.")
    assert tauceti.title_and_text("X.y", "**Global existence** (Milne VII, Theorem 9.5). For a number field") == (
        "Global existence (Milne VII, Theorem 9.5)", "For a number field")
    # A sentence that runs on too long, or past a blank line, leaves the docstring untitled.
    assert tauceti.title_and_text("X.y", "**Long** " + "word " * 60 + ".")[0] == "X.y"
    assert tauceti.title_and_text("X.y", "**Bold**\n\nnot a title.") == ("X.y", "**Bold**\n\nnot a title.")
    assert tauceti.title_and_text("X.y", "The `K`-points, with **bold** later.") == ("X.y", "The `K`-points, with **bold** later.")
    assert tauceti.title_and_text("X.y", None) == ("X.y", "")


def record(module="TauCeti.A", kind="theorem", doc=None, sorry=False, statement=(), proof=()):
    return {"module": module, "kind": kind, "line": 7, "signature": "theorem t : True", "doc": doc, "sorry": sorry,
            "statement": list(statement), "proof": list(proof)}


def sources(roadmaps, declarations):
    return tauceti.Sources("a" * 40, "2026-11-07T00:00:00Z", "b" * 40, roadmaps, {"declarations": declarations})


def build(roadmaps, declarations):
    root, stats, links = tauceti.chapter(sources(roadmaps, declarations))
    assign_paths(root, Path("blueprint/roadmap/tauceti"))
    return root, stats, links


def leaves(root):
    return {dict(node.fields)["lean"].split(", ")[0]: node for node in walk(root) if isinstance(node, Leaf)}


def sections(root):
    """The containers that list articles, by title; pagination parts are left out."""
    return {node.title: node for node in walk(root)
            if not isinstance(node, Leaf) and any(isinstance(entry.node, Leaf) for entry in node.entries)}


def test_only_declarations_tau_ceti_has_get_articles():
    roadmaps = [
        {"id": "B", "path": "TauCetiRoadmap/B", "title": "Beta", "names": ["Ex.main", "Ex.gone"]},
        {"id": "C", "path": "TauCetiRoadmap/C", "title": "Gamma", "names": ["Ex.gone"]},
    ]
    root, stats, links = build(roadmaps, {"Ex.main": record(doc="**Main.** It holds.")})
    assert list(leaves(root)) == ["Ex.main"]
    assert list(sections(root)) == ["Beta"]
    assert stats["missing"] == 1 and stats["roadmaps_left_out"] == 1
    assert links == {"Ex.main": "https://taucetiproject.org/docs/TauCeti/A.html#Ex.main"}
    assert "The one name the statuses give" in root.prose


def test_a_declaration_two_roadmaps_name_lives_in_the_first_by_title():
    roadmaps = [
        {"id": "Z", "path": "TauCetiRoadmap/Z", "title": "Zeta", "names": ["Ex.shared"]},
        {"id": "A", "path": "Completed/A", "title": "The alpha", "names": ["Ex.shared", "Ex.own"]},
    ]
    root, _, _ = build(roadmaps, {"Ex.shared": record(), "Ex.own": record()})
    alpha, zeta = sections(root)["The alpha"], sections(root)["Zeta"]
    assert alpha.title == "The alpha" and [entry.owned for entry in alpha.entries] == [True, True]
    assert [entry.owned for entry in zeta.entries] == [False]
    shared = leaves(root)["Ex.shared"]
    assert [label for label, _ in shared.sources][-2:] == ["Tau Ceti roadmap status: Zeta", "Tau Ceti roadmap status: The alpha"]


def test_edges_link_mapped_declarations_and_a_sorry_proof_reads_as_stated():
    roadmaps = [{"id": "A", "path": "TauCetiRoadmap/A", "title": "Alpha", "names": ["Ex.thm", "Ex.def", "Ex.lemma"]}]
    declarations = {
        "Ex.thm": record(statement=["Ex.def", "Ex.unmapped"], proof=["Ex.lemma", "Ex.def", "Ex.thm"]),
        "Ex.def": record(kind="def", doc="**A thing.**"),
        "Ex.lemma": record(sorry=True),
    }
    root, stats, _ = build(roadmaps, declarations)
    by_name = leaves(root)
    thm = by_name["Ex.thm"]
    assert [node.title for node in thm.depends] == ["A thing"]
    assert [node.title for node in thm.proof_depends] == ["Ex.lemma"]
    # Its proof goes through a mapped lemma whose proof reaches sorry, so it is stated, not proved.
    assert "proof" not in dict(thm.fields)
    assert "its proof reaches `sorry`" in dict(thm.notes)["Lean"]
    lemma = dict(by_name["Ex.lemma"].fields)
    assert lemma["statement"] == "formalized" and "proof" not in lemma
    assert "its proof reaches `sorry`" in dict(by_name["Ex.lemma"].notes)["Lean"]
    assert "proof" not in dict(by_name["Ex.def"].fields)
    assert "Formalized in Tau Ceti" in dict(by_name["Ex.def"].notes)["Lean"]
    assert stats["sorry"] == 2 and stats["statement_edges"] == 1 and stats["proof_edges"] == 1


def test_a_definition_reaching_sorry_says_so():
    roadmaps = [{"id": "A", "path": "TauCetiRoadmap/A", "title": "Alpha", "names": ["Ex.def"]}]
    root, stats, _ = build(roadmaps, {"Ex.def": record(kind="def", sorry=True)})
    assert "its definition reaches `sorry`" in dict(leaves(root)["Ex.def"].notes)["Lean"]
    assert stats["sorry"] == 1


def test_a_name_that_resolves_outside_tau_ceti_has_no_article():
    roadmaps = [{"id": "A", "path": "TauCetiRoadmap/A", "title": "Alpha", "names": ["Ex.thm", "Polynomial.moved"]}]
    root, stats, links = build(roadmaps, {"Ex.thm": record(), "Polynomial.moved": record(module="Mathlib.RingTheory.X")})
    assert list(links) == ["Ex.thm"] and stats["missing"] == 1


def test_a_shared_bold_title_is_followed_by_each_name():
    roadmaps = [{"id": "A", "path": "TauCetiRoadmap/A", "title": "Alpha", "names": ["Ex.b", "Ex.a"]}]
    doc = "**The Riemann–Roch theorem.** For a curve ..."
    root, _, _ = build(roadmaps, {"Ex.a": record(doc=doc), "Ex.b": record(doc=doc)})
    assert [entry.node.title for entry in sections(root)["Alpha"].entries] == [
        "The Riemann–Roch theorem (`Ex.b`)", "The Riemann–Roch theorem (`Ex.a`)"]


def test_an_article_shows_the_docstring_signature_and_where_it_comes_from():
    roadmaps = [{"id": "A", "path": "TauCetiRoadmap/A", "title": "Alpha", "names": ["Ex.thm"]}]
    doc = "**The theorem.** For `K`, see [Serre](serre1979) and [neukirch1999].\n\n# Details\nMore."
    root, _, _ = build(roadmaps, {"Ex.thm": record(module="TauCeti.Num.Thm", doc=doc)})
    page = render_tree(root, Path("blueprint"))[Path("blueprint/roadmap/tauceti/other-areas/alpha/the-theorem.md")]
    assert "# The theorem\n\nFor `K`, see [Serre](https://taucetiproject.org/docs/references.html#ref_serre1979)" in page
    assert "[neukirch1999](https://taucetiproject.org/docs/references.html#ref_neukirch1999)" in page
    assert "**Details**\nMore." in page
    assert "```lean\ntheorem t : True\n```" in page
    assert "https://github.com/TauCetiProject/TauCeti/blob/" + "a" * 40 + "/TauCeti/Num/Thm.lean#L7" in page
    assert "lean: Ex.thm\nstatement: formalized\nproof: formalized\n" in page


def test_the_committed_data_build_a_chapter():
    data = tauceti.load_sources(DATA)
    assert data is not None
    roadmaps = json.loads((DATA / "tauceti" / "roadmaps.json").read_text(encoding="utf-8"))
    assert roadmaps["schema"] == tauceti.ROADMAPS_SCHEMA and roadmaps["roadmaps"]
    if data.deps is None:
        return
    # The dump was made from these pins: the Tau Ceti commit, and exactly the names the roadmaps give
    # and the docstrings' results chosen at that commit.
    assert data.deps["tauceti_rev"] == data.rev
    names = {name for roadmap in roadmaps["roadmaps"] for name in roadmap["names"]}
    if data.selection is not None:
        assert data.selection["schema"] == tauceti_select.SELECTION_SCHEMA
        assert data.selection["tauceti_rev"] == data.rev
        names |= set(data.selection["chosen"])
    assert names == set(data.deps["declarations"]) | set(data.deps["missing"])
    root, stats, links = tauceti.chapter(data)
    assert stats["declarations"] == len(links) >= stats["articles"] > 0
    assert set(links) <= set(data.deps["declarations"])
    assert not set(links) & set(data.deps["missing"])


def test_forms_of_one_result_share_an_article_led_by_its_plain_name():
    roadmaps = [{"id": "A", "path": "TauCetiRoadmap/A", "title": "Alpha", "names": ["Ex.status"]}]
    declarations = {
        "Ex.status": record(module="TauCeti.Graph.Menger", doc="**Menger's theorem for adjacent vertices.** Text"),
        "Ex.plain": record(module="TauCeti.Graph.Other", doc="**Menger's theorem.** Text", statement=["Ex.dep"]),
        "Ex.form": record(module="TauCeti.Graph.Other", doc="**Menger's theorem, predicate form.** Text",
                          statement=["Ex.plain", "Ex.dep"], proof=["Ex.dep2"]),
        "Ex.else": record(module="TauCeti.Topo.Other", doc="**Menger's theorem for curves.** Text"),
        "Ex.dep": record(module="TauCeti.Graph.Other", doc="**Hall's marriage theorem.** Text"),
        "Ex.dep2": record(module="TauCeti.Graph.Other", doc="**König's theorem.** Text"),
    }
    chosen = {name: "named theorem" for name in declarations if name != "Ex.status"}
    data = sources(roadmaps, declarations)
    data.selection = {"chosen": chosen, "assuming": {}}
    root, stats, links = tauceti.chapter(data)
    assign_paths(root, Path("blueprint/roadmap/tauceti"))
    by_name = leaves(root)
    # The status's declaration leads its own article, and the forms no status names join it.
    assert dict(by_name["Ex.status"].fields)["lean"] == "Ex.status, Ex.plain, Ex.form"
    assert "Other forms" in dict(by_name["Ex.status"].notes)
    assert "**Menger's theorem.** Formalized in Tau Ceti as [`Ex.plain`]" in dict(by_name["Ex.status"].notes)["Other forms"]
    # The same name in another top-level area is another result.
    assert dict(by_name["Ex.else"].fields)["lean"] == "Ex.else"
    # Edges join articles: the forms' uses count, and one form's use of another does not.
    assert [node.title for node in by_name["Ex.status"].depends] == ["Hall's marriage theorem"]
    assert [node.title for node in by_name["Ex.status"].proof_depends] == ["König's theorem"]
    assert set(links) == set(declarations) and stats["declarations"] == 6 and stats["articles"] == 4
    assert stats["named"] == 1 and stats["chosen"] == 5 and stats["forms"] == 1


def test_a_group_no_status_names_is_led_by_its_plain_title():
    declarations = {
        "Ex.long": record(module="TauCeti.Graph.M", doc="**Menger's theorem**, for adjacent vertices: text"),
        "Ex.plain": record(module="TauCeti.Graph.M", doc="**Menger's theorem**: text"),
    }
    data = sources([], declarations)
    data.selection = {"chosen": {name: "named theorem" for name in declarations}, "assuming": {}}
    root, _, _ = tauceti.chapter(data)
    assert [dict(leaf.fields)["lean"] for leaf in walk(root) if isinstance(leaf, Leaf)] == ["Ex.plain, Ex.long"]


def test_added_results_go_to_the_roadmap_whose_status_alone_reaches_their_module():
    roadmaps = [
        {"id": "A", "path": "TauCetiRoadmap/A", "title": "Alpha", "names": ["Ex.a", "Ex.shared"]},
        {"id": "B", "path": "TauCetiRoadmap/B", "title": "Beta", "names": ["Ex.b", "Ex.shared2"]},
    ]
    declarations = {
        "Ex.a": record(module="TauCeti.Num.Alpha.Main"),
        "Ex.b": record(module="TauCeti.Num.Beta.Main"),
        "Ex.shared": record(module="TauCeti.Num.Both"),
        "Ex.shared2": record(module="TauCeti.Num.Both"),
        # The same module as a status's declaration, its folder, a module two statuses reach, none.
        "Ex.same": record(module="TauCeti.Num.Alpha.Main", doc="**Abel's theorem.** Text"),
        "Ex.folder": record(module="TauCeti.Num.Beta.Other", doc="**Bezout's theorem.** Text"),
        "Ex.both": record(module="TauCeti.Num.Both", doc="**Cauchy's theorem.** Text"),
        "Ex.area1": record(module="TauCeti.Num.Free.X", doc="**Dirac's theorem.** Text"),
        "Ex.area2": record(module="TauCeti.Num.Free.Y", doc="**Euler's theorem.** Text"),
        "Ex.area3": record(module="TauCeti.Num.Free.Z", doc="**Fermat's theorem.** Text"),
    }
    chosen = {name: "named theorem" for name in ("Ex.same", "Ex.folder", "Ex.both", "Ex.area1", "Ex.area2", "Ex.area3")}
    data = sources(roadmaps, declarations)
    data.selection = {"chosen": chosen, "assuming": {}}
    root, stats, _ = tauceti.chapter(data)
    found = {title: [entry.node.title for entry in section.entries] for title, section in sections(root).items()}
    assert found["Alpha"] == ["Ex.a", "Ex.shared", "Abel's theorem"]
    assert found["Beta"] == ["Ex.b", "Ex.shared2", "Bezout's theorem"]
    # An area with three results gets its own section; the one two statuses reach is left to its area's.
    assert found["Free"] == ["Dirac's theorem", "Euler's theorem", "Fermat's theorem"]
    assert found["Other results"] == ["Cauchy's theorem"]
    assert stats["roadmaps"] == 2 and stats["areas"] == 2


def test_a_large_area_is_a_part_and_small_ones_share_other_areas():
    people = ["Abel", "Baire", "Cantor", "Dedekind", "Euler", "Fatou", "Gauss", "Hardy", "Ising", "Jensen", "Klein", "Lagrange"]
    declarations = {f"Ex.big{i}": record(module=f"TauCeti.Big.Sub{i % 2}", doc=f"**{person}'s theorem.** Text")
                    for i, person in enumerate(people)}
    declarations["Ex.small"] = record(module="TauCeti.Small.Sub", doc="**Bezout's theorem.** Text")
    data = sources([], declarations)
    data.selection = {"chosen": {name: "named theorem" for name in declarations}, "assuming": {}}
    root, stats, _ = tauceti.chapter(data)
    assert [entry.node.title for entry in root.entries] == ["Big", "Other Areas"]
    big, other = (entry.node for entry in root.entries)
    assert [entry.node.title for entry in big.entries] == ["Sub0", "Sub1"]
    assert [entry.node.title for entry in other.entries] == ["Small"]
    assert stats["parts"] == 2


def test_a_result_stated_from_a_defined_proposition_says_what_it_assumes():
    declarations = {
        "Ex.Szpiro.frey": record(module="TauCeti.Num.Szpiro", doc="**Szpiro's conjecture for Frey curves.** Text"),
        "Ex.Szpiro.other": record(module="TauCeti.Num.Szpiro", doc="**Szpiro's bound.** Text"),
    }
    declarations["Ex.Szpiro.frey"]["signature"] = "theorem Ex.Szpiro.frey (h : Szpiro) : FreyBound"
    declarations["Ex.Szpiro.other"]["signature"] = "theorem Ex.Szpiro.other : Szpiro ↔ True"
    assuming = {name: {"statement": "Ex.Szpiro", "module": "TauCeti.Num.Szpiro"} for name in declarations}
    data = sources([], declarations)
    data.selection = {"chosen": {name: "named theorem" for name in declarations}, "assuming": assuming}
    root, _, _ = tauceti.chapter(data)
    by_name = leaves(root)
    assert "assuming [`Ex.Szpiro`](https://taucetiproject.org/docs/TauCeti/Num/Szpiro.html#Ex.Szpiro)" in dict(
        by_name["Ex.Szpiro.frey"].notes)["Lean"]
    # A conclusion that mentions the proposition assumes nothing.
    assert "assuming" not in dict(by_name["Ex.Szpiro.other"].notes)["Lean"]


def test_area_titles_read_as_words():
    assert [tauceti.area_title(word) for word in ("NumberTheory", "PDE", "SU2", "Lie")] == [
        "Number Theory", "PDE", "SU2", "Lie"]
