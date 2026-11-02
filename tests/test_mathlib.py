import io
from pathlib import Path

import yaml

from trough import mathlib
from trough.vault import assign_paths, walk

DATA = Path(__file__).resolve().parent.parent / "data"


def compose(text: str) -> yaml.MappingNode:
    return yaml.compose(io.StringIO(text), Loader=yaml.SafeLoader)


TREE = """\
Algebra:
  Groups:
    group: 'Group'
    Sylow theorems: 'Sylow.exists_subgroup_card_pow_prime'
  Fields:
    finite fields: 'Mathlib/FieldTheory/Finite/Basic.html'
    row reduction: 'https://en.wikipedia.org/wiki/Row_echelon_form'
    Galois theory: ''
"""

RECORDS = """\
1:
  title  : Irrationality of $\\sqrt 2$
  decl   : irrational_sqrt_two
  authors: mathlib
2:
  title  : Sylow's theorem
  decls  :
    - Sylow.exists_subgroup_card_pow_prime
    - Sylow.isPretransitive_of_finite
3:
  title  : Fermat's Last Theorem
  statement: FermatLastTheorem
  links  :
    result: https://example.org/flt
  note   : "Done elsewhere, see https://example.org/notes"
"""


def test_tree_items_classify_leaves():
    items = mathlib.tree_items("overview", compose(TREE))
    by_title = {item.title: item for item in items}
    assert by_title["group"].decls == ("Group",)
    assert by_title["group"].path == ("Algebra", "Groups")
    assert by_title["group"].line == 3
    assert by_title["finite fields"].module == "Mathlib.FieldTheory.Finite.Basic"
    assert by_title["row reduction"].url.startswith("https://")
    assert by_title["Galois theory"].decls == () and not by_title["Galois theory"].module


def test_record_items_read_every_field():
    items = mathlib.record_items("100", compose(RECORDS))
    assert items[0].decls == ("irrational_sqrt_two",)
    assert items[1].decls == ("Sylow.exists_subgroup_card_pow_prime", "Sylow.isPretransitive_of_finite")
    assert items[2].statement == "FermatLastTheorem"
    assert items[2].links == {"result": "https://example.org/flt"}
    assert items[2].label == "3. Fermat's Last Theorem"


def test_merge_on_declaration_set_or_first_declaration():
    lists = {
        "overview": mathlib.tree_items("overview", compose(TREE)),
        "undergrad": [],
        "100": mathlib.record_items("100", compose(RECORDS)),
        "1000": [],
    }
    articles = mathlib.merge(lists)
    sylow = [article for article in articles if "Sylow.exists_subgroup_card_pow_prime" in article.decls]
    assert len(sylow) == 1
    assert sylow[0].home.list == "overview"
    assert sylow[0].decls == ("Sylow.exists_subgroup_card_pow_prime",)
    kinds = sorted(article.kind for article in articles)
    assert kinds.count("module") == 1
    assert kinds.count("wanted") == 3  # row reduction, Galois theory, Fermat's Last Theorem


def test_note_text_links_bare_urls_only():
    assert mathlib.note_text("see https://a.org/x") == "see <https://a.org/x>."
    assert mathlib.note_text("see the [repo](https://a.org/x).") == "see the [repo](https://a.org/x)."


def fake_sources(concepts: dict) -> mathlib.Sources:
    lists = {
        "overview": [
            mathlib.Item("overview", "a", ("Area", "Sub"), "alpha", 1, decls=("A",)),
            mathlib.Item("overview", "b", ("Area", "Sub"), "beta", 2, decls=("B",)),
            mathlib.Item("overview", "c", ("Area", "Sub"), "gamma", 3, decls=("C",)),
        ],
        "undergrad": [],
        "100": [],
        "1000": [],
    }
    deps = {"mathlib_rev": "r", "concepts": concepts, "modules": {}}
    return mathlib.Sources("r", "", lists, deps, None)


def record(statement=(), proof=(), kind="theorem"):
    return {"module": "Mathlib.X", "kind": kind, "line": 1, "doc": "Doc.", "signature": "theorem x : True",
            "statement": list(statement), "proof": list(proof)}


def edges(sources):
    root, stats, _ = mathlib.chapter(sources)
    assign_paths(root, Path("blueprint/roadmap/mathlib"))
    leaves = {node.title: node for node in walk(root) if not hasattr(node, "entries")}
    return leaves, stats


def test_edges_drop_what_another_dependency_implies():
    leaves, stats = edges(fake_sources({
        "A": record(statement=["B", "C"]),
        "B": record(statement=["C"]),
        "C": record(kind="def"),
    }))
    assert [leaf.title for leaf in leaves["Alpha"].depends] == ["Beta"]
    assert [leaf.title for leaf in leaves["Beta"].depends] == ["Gamma"]
    assert stats["statement_raw"] == 3 and stats["statement"] == 2


def test_edges_that_close_a_cycle_become_informal():
    leaves, stats = edges(fake_sources({
        "A": record(statement=["B"]),
        "B": record(proof=["A"]),
        "C": record(),
    }))
    assert stats["informal"] == 1
    graph = {title: {d.title for d in leaf.depends + leaf.proof_depends} for title, leaf in leaves.items()}
    assert not ("Beta" in graph["Alpha"] and "Alpha" in graph["Beta"])


def test_real_lists_give_one_home_per_article_and_unique_first_declarations():
    sources = mathlib.load_sources(DATA)
    root, stats, _ = mathlib.chapter(sources)
    assign_paths(root, Path("blueprint/roadmap/mathlib"))
    leaves = [node for node in walk(root) if not hasattr(node, "entries")]
    assert len(leaves) == stats["articles"]
    firsts = [dict(leaf.fields).get("mathlib_declaration", "").split(", ")[0] for leaf in leaves]
    firsts = [name for name in firsts if name]
    assert len(firsts) == len(set(firsts))
    assert all(dict(leaf.fields).get("not_ready") == "true" or dict(leaf.fields).get("mathlib") == "true" for leaf in leaves)


def test_items_naming_nothing_merge_by_title_across_lists_only():
    lists = {
        "overview": [],
        "undergrad": [
            mathlib.Item("undergrad", "u1", ("Analysis", "Series"), "error estimation", 1),
            mathlib.Item("undergrad", "u2", ("Numerics", "Integration"), "error estimation", 2),
        ],
        "100": [mathlib.Item("100", "5", (), "Prime Number Theorem", 3)],
        "1000": [mathlib.Item("1000", "Q386292", (), "Prime number theorem", 4)],
    }
    articles = mathlib.merge(lists)
    assert sorted(len(article.items) for article in articles) == [1, 1, 2]
    pnt = next(article for article in articles if len(article.items) == 2)
    assert pnt.home.list == "100"


def test_shared_titles_get_the_nearest_section_that_differs():
    lists = {
        "overview": [mathlib.Item("overview", "a", ("Analysis", "Differentiability"), "chain rule", 1, decls=("A",))],
        "undergrad": [mathlib.Item("undergrad", "b", ("Real analysis", "Differentiability"), "chain rule", 2, decls=("B",))],
        "100": [],
        "1000": [mathlib.Item("1000", "Q1", (), "Chain rule", 3, decls=("C",))],
    }
    sources = mathlib.Sources("r", "", lists, None, None)
    root, _, _ = mathlib.chapter(sources)
    titles = sorted(node.title for node in walk(root) if not hasattr(node, "entries"))
    assert titles == ["Chain rule (1000+ theorems)", "Chain rule (Analysis)", "Chain rule (Real analysis)"]


def test_citation_keys_link_to_the_bibliography():
    doc = mathlib.clean_doc("See [Zwillinger](zwillinger2003) and [axler2024], not [x](https://a.org) or `l[i]`.")
    assert f"[Zwillinger]({mathlib.DOCS}/references.html#ref_zwillinger2003)" in doc
    assert f"[axler2024]({mathlib.DOCS}/references.html#ref_axler2024)" in doc
    assert "[x](https://a.org)" in doc and "`l[i]`" in doc


def test_a_shared_declaration_links_to_the_article_it_heads():
    lists = {
        "overview": [mathlib.Item("overview", "a", ("S",), "alpha", 1, decls=("A",)),
                     mathlib.Item("overview", "c", ("S",), "gamma", 2, decls=("C",))],
        "undergrad": [],
        "100": [mathlib.Item("100", "1", (), "Bundle", 3, decls=("B", "A"))],
        "1000": [],
    }
    deps = {"mathlib_rev": "r", "modules": {},
            "concepts": {"A": record(kind="def"), "B": record(), "C": record(statement=["A"])}}
    root, _, _ = mathlib.chapter(mathlib.Sources("r", "", lists, deps, None))
    leaves = {node.title: node for node in walk(root) if not hasattr(node, "entries")}
    assert [leaf.title for leaf in leaves["Gamma"].depends] == ["Alpha"]


def test_titles_match_across_typography_and_keys_the_project_replaced():
    lists = {
        "overview": [], "undergrad": [],
        "100": [mathlib.Item("100", "6", (), "Gödel’s Incompleteness Theorem", 1)],
        "1000": [mathlib.Item("1000", "Q200787", (), "Gödel's incompleteness theorem", 2),
                 mathlib.Item("1000", "Q230848", (), "Lamé’s theorem", 3)],
    }
    assert len(mathlib.merge(lists)) == 2
    thousand = {"entries": {"Q10380294": {"msc": "68", "wikipedia": ["Lamé's theorem"], "others": {}}}}
    sources = mathlib.Sources("r", "", lists, None, thousand)
    assert mathlib.thousand_entry(sources, lists["1000"][1])[0] == "Q10380294"


def test_headings_keep_list_titles_and_wikipedia_sections():
    assert mathlib.Item("100", "67", (), "e is Transcendental", 1).label == "67. e is Transcendental"
    assert mathlib.Item("overview", "x", ("A",), "group", 1).heading == "Group"
    assert mathlib.wikipedia_url("Integer partition#Odd parts") == "https://en.wikipedia.org/wiki/Integer_partition#Odd_parts"
