import json
import os
import subprocess
from pathlib import Path

import pytest

import refresh_lean_pool
from trough import lean_pool
from trough.vault import Container, Leaf, assign_paths, render_tree, walk

ROOT = Path(__file__).resolve().parent.parent
REV = "a" * 40
BLOB = f"https://github.com/LeanPool/lean-pool/blob/{REV}"
DOCS = "https://leanpool.github.io/lean-pool"

# LeanPool/projects/1mfld.yaml at faac47ac, as written.
ONE_MANIFOLD = """slug: 1mfld
title: The classification of compact 1-manifolds
summary: 'A Lean 4 (mathlib) proof of the classification of 1-manifolds, specifically
  that every compact, connected, Hausdorff topological space charted on the half-line
  [0,∞) is homeomorphic to the circle S¹ or to the closed unit interval [0,1]. The
  proof follows David Gale''s outline: shrink to a finite atlas of interval charts,
  then induct on the atlas size, merging two overlapping charts at each step; a connected
  overlap glues two charts into one (two boundary charts glue onto [0, 1]), while
  a disconnected overlap has exactly two components and yields the circle.'
branch: topology
entry_module: LeanPool.OneManifold
authors:
- Jim Fowler
- Dennis Sweeney
source:
  url: https://github.com/sweeneyde/1mfld
  github_repo: sweeneyde/1mfld
  commit: 83e961ba28dd8182e7bae844756aba614eb1512e
license: Apache-2.0
status: verified
main_declarations:
- OneMfld.homeomorph_circle_or_unitInterval
main_results:
- declaration: OneMfld.homeomorph_circle_or_unitInterval
  informal: Every compact connected Hausdorff space charted on the nonnegative real
    half-line is homeomorphic to the circle or the closed unit interval.
tags:
- topology
msc:
- 57N99
- 54F65
- 68V20
provenance: mix
"""

ART = """slug: art
title: Rings of order p * q over F_q[t]
summary: Proves that `R` is *simple*.
branch: ring theory
entry_module: LeanPool.Art
authors:
- A. Author
contributors:
- B. Helper
source:
  title: A Book on Rings
  authors:
  - C. Writer
  arxiv: 2311.05760
  doi: 10.1016/S0095-8956(03)00073-X
  github_repo: someone/art
license: MIT
status: verified
main_declarations:
- Art.main
main_results:
- declaration: Art.main
  informal: Every ring of order p * q is a field.
  source_ref: Theorem 1.2.
- declaration: Art.helper
  informal: A helper.
- declaration: Art.twice
  informal: Twice declared.
- declaration: Art.absent
  informal: Not in the files.
tags:
- rings
msc:
- 16D60
provenance: AI
provenance_note: The README says so.
"""

LEAN = {
    "LeanPool/OneManifold.lean": "module\n\npublic import LeanPool.OneManifold.Main\n\n/-! # The card -/\n",
    "LeanPool/OneManifold/Main.lean": (
        "module\n\npublic import Mathlib.Topology.Basic\n\n@[expose] public section\n\nnamespace OneMfld\n\n"
        "/-- The classification. -/\ntheorem homeomorph_circle_or_unitInterval : True := trivial\n\nend OneMfld\n"),
    "LeanPool/Art.lean": "module\n\npublic import LeanPool.Art.A\n",
    "LeanPool/Art/A.lean": "namespace Art\n\ntheorem main : True := trivial\n\ntheorem twice : True := trivial\n\nend Art\n",
    "LeanPool/Art/B.lean": "theorem Art.twice : True := trivial\n",
    # Its scopes don't close as they open, so it declares nothing.
    "LeanPool/Art/Broken.lean": "namespace Art\n\ntheorem helper : True := trivial\n\nend Other\n",
    # Another project's directory is not read.
    "LeanPool/Other/C.lean": "theorem Art.absent : True := trivial\n",
}

NOTICE = """# Per-project prose.
Art:
  note: Copyright (c) 2026 A. Author
OneManifold:
  note: Not a copyright line, as the project is Apache-2.0.
"""

APACHE = "\n                                 Apache License\n                           Version 2.0, January 2004\n"
MANIFEST = {"packages": [{"name": "mathlib", "rev": "c" * 40}, {"name": "TauCeti", "rev": "d" * 40}]}


def checkout(root: Path, cards: dict[str, str] | None = None, license_text: str = APACHE) -> Path:
    files = {"LICENSE": license_text, "NOTICE.extra.yml": NOTICE, "lean-toolchain": "leanprover/lean4:v4.35.0\n",
             "lake-manifest.json": json.dumps(MANIFEST), **LEAN}
    files |= {f"LeanPool/projects/{slug}.yaml": text
              for slug, text in (cards or {"1mfld": ONE_MANIFOLD, "art": ART}).items()}
    for path, text in files.items():
        (root / path).parent.mkdir(parents=True, exist_ok=True)
        (root / path).write_text(text, encoding="utf-8")
    return root


def pool(tmp_path):
    return lean_pool.read_pool(checkout(tmp_path / "lean-pool"), REV, "2026-11-08T13:44:30Z")


def test_a_card_keeps_its_scalars_as_written_and_must_have_what_the_chapter_reads():
    card = lean_pool.read_card(ART, "art.yaml")
    assert card["source"]["arxiv"] == "2311.05760" and card["msc"] == ["16D60"]
    with pytest.raises(ValueError, match="lacks summary"):
        lean_pool.read_card(ART.replace("summary: Proves that `R` is *simple*.\n", ""), "art.yaml")
    with pytest.raises(ValueError, match="license 'GPL-3.0'"):
        lean_pool.read_card(ART.replace("license: MIT", "license: GPL-3.0"), "art.yaml")
    with pytest.raises(ValueError, match="unknown provenance"):
        lean_pool.read_card(ART.replace("provenance: AI", "provenance: robot"), "art.yaml")
    with pytest.raises(ValueError, match="first MSC2020 code"):
        lean_pool.read_card(ART.replace("- 16D60", "- 99X99"), "art.yaml")


def test_the_pool_record_places_each_main_result_in_its_project_files(tmp_path):
    source, record, counts = pool(tmp_path)
    assert source == {"repo": "LeanPool/lean-pool", "rev": REV, "date": "2026-11-08T13:44:30Z",
                      "toolchain": "v4.35.0", "mathlib": "c" * 40}
    assert record["schema"] == lean_pool.SCHEMA and record["rev"] == REV
    manifold, art = record["projects"]
    assert manifold["slug"] == "1mfld" and manifold["directory"] == "OneManifold"
    assert manifold["source"] == {"url": "https://github.com/sweeneyde/1mfld", "github_repo": "sweeneyde/1mfld",
                                  "commit": "83e961ba28dd8182e7bae844756aba614eb1512e"}
    # The notice file's note is a copyright line only for a project published under MIT.
    assert manifold["notice"] is None and art["notice"] == "Copyright (c) 2026 A. Author"
    assert manifold["main_results"] == [{
        "declaration": "OneMfld.homeomorph_circle_or_unitInterval",
        "informal": "Every compact connected Hausdorff space charted on the nonnegative real half-line is "
                    "homeomorphic to the circle or the closed unit interval.",
        "main": True, "module": "LeanPool.OneManifold.Main", "line": 10, "kind": "theorem", "sorry": False}]
    results = {result["declaration"]: result for result in art["main_results"]}
    assert results["Art.main"]["module"] == "LeanPool.Art.A" and results["Art.main"]["source_ref"] == "Theorem 1.2."
    # Declared in two files, in a file whose scopes don't close, or only in another project: not placed.
    for name in ("Art.twice", "Art.helper", "Art.absent"):
        assert results[name]["module"] is None and results[name]["line"] is None and not results[name]["main"]
    assert art["contributors"] == ["B. Helper"] and art["provenance_note"] == "The README says so."
    assert art["source"]["authors"] == ["C. Writer"] and art["source"]["arxiv"] == "2311.05760"
    assert counts["files_unclosed"] == 1 and counts["declared_twice"] == 1
    assert lean_pool.found_count(record) == 2


def test_a_repository_that_is_not_apache_licensed_is_refused(tmp_path):
    with pytest.raises(ValueError, match="not the Apache License"):
        lean_pool.read_pool(checkout(tmp_path, license_text="MIT License\n"), REV, "")
    with pytest.raises(ValueError, match="slug 'art' is not its file's name"):
        lean_pool.read_pool(checkout(tmp_path / "renamed", {"other": ART}), REV, "")


def test_card_text_keeps_its_code_and_escapes_the_rest():
    assert lean_pool.text("`a * b` is 2 * c_d [0,1) #1 <= 2") == "`a * b` is 2 \\* c_d [0,1) \\#1 <= 2"
    assert lean_pool.text("One\n  line.\n\nTwo.") == "One line.\n\nTwo."
    # Brackets stay, as a backslash before one opens a formula, but none makes a link.
    assert lean_pool.text("F_q[t] and [x](y)") == "F_q[t] and [x\\](y)"
    # The site publishes no HTML and no character references, and Markdown can't escape them.
    assert lean_pool.text("[SL_2(Z) : <Gamma_1(N), -I>] and AT&amp; or `<b>`") == \
        "[SL_2(Z) : `<`Gamma_1(N), -I>] and AT`&`amp; or `<b>`"


def build(tmp_path):
    source, record, _ = pool(tmp_path)
    root, stats, parts = lean_pool.chapter(source, record)
    vault = Path("blueprint")
    assign_paths(root, vault / "roadmap" / "lean-pool")
    return root, stats, parts, render_tree(root, vault)


def test_the_chapter_has_a_part_per_msc_class_in_order_and_an_article_per_card(tmp_path):
    root, stats, parts, _ = build(tmp_path)
    assert [part.title for part, _ in parts] == ["Associative rings and algebras", "Manifolds and cell complexes"]
    assert [part.slug for part, _ in parts] == ["16-associative-rings-and-algebras", "57-manifolds-and-cell-complexes"]
    leaves = [node for node in walk(root) if isinstance(node, Leaf)]
    assert [leaf.slug for leaf in leaves] == ["art", "1mfld"]
    assert stats["articles"] == 2 and stats["main_results"] == 5 and stats["main_results_found"] == 2
    assert stats["main_declarations"] == 2 and stats["main_declarations_found"] == 2
    # The Lean row names the main declarations found, and each part links them to the documentation.
    assert dict(leaves[1].fields)["lean"] == "OneMfld.homeomorph_circle_or_unitInterval"
    assert parts[1][1] == {"OneMfld.homeomorph_circle_or_unitInterval":
                           f"{DOCS}/LeanPool/OneManifold/Main.html#OneMfld.homeomorph_circle_or_unitInterval"}
    assert "No Lean is run for this chapter" in root.prose and "have no dependencies" in root.prose
    assert "2 projects at commit [aaaaaaaa]" in root.prose and "Of the cards, 1 say AI, 0 human and 1 mix." in root.prose


def test_an_article_quotes_its_card_and_links_its_declarations(tmp_path):
    _, _, _, files = build(tmp_path)
    page = files[Path("blueprint/roadmap/lean-pool/57-manifolds-and-cell-complexes/1mfld.md")]
    assert page.startswith("---\ndeclaration: theorem\norigin: cited\nlean: OneMfld.homeomorph_circle_or_unitInterval\n"
                           "statement: formalized\nproof: formalized\n---\n\n# The classification of compact 1-manifolds\n")
    assert "\n> A Lean 4 (mathlib) proof of the classification of 1-manifolds, specifically that every compact" in page
    assert (f"*Quoted from the card [LeanPool/projects/1mfld.yaml]({BLOB}/LeanPool/projects/1mfld.yaml) of "
            "[LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [aaaaaaaa]") in page
    assert lean_pool.NO_DEPENDS in page
    assert (f"- [`OneMfld.homeomorph_circle_or_unitInterval`]({DOCS}/LeanPool/OneManifold/Main.html"
            "#OneMfld.homeomorph_circle_or_unitInterval) (theorem; a main declaration), declared in "
            f"[LeanPool/OneManifold/Main.lean, line 10]({BLOB}/LeanPool/OneManifold/Main.lean#L10): “Every compact") in page
    assert "- Authors: Jim Fowler, Dennis Sweeney." in page
    assert ("- Project repository: [sweeneyde/1mfld](https://github.com/sweeneyde/1mfld), at commit [83e961ba]"
            "(https://github.com/sweeneyde/1mfld/tree/83e961ba28dd8182e7bae844756aba614eb1512e).") in page
    assert "- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially”" in page
    assert "- License: Apache-2.0.\n- MSC2020: 57N99, 54F65, 68V20." in page
    art = files[Path("blueprint/roadmap/lean-pool/16-associative-rings-and-algebras/art.md")]
    assert "# Rings of order p \\* q over F_q[t]\n\n> Proves that `R` is \\*simple\\*." in art
    assert ("- Source: *A Book on Rings* by C. Writer, [doi:10.1016/S0095-8956(03)00073-X]"
            "(https://doi.org/10.1016/S0095-8956%2803%2900073-X), [arXiv:2311.05760](https://arxiv.org/abs/2311.05760).") in art
    assert ("- `Art.absent`, which the scan does not find declared in the project's files at this commit: "
            "“Not in the files.”") in art
    assert "“Every ring of order p \\* q is a field.” Its source, as the card gives it: “Theorem 1.2.”" in art
    assert "- Contributors: B. Helper." in art and "The card's note: “The README says so.”" in art
    assert "redistributes it under Apache-2.0, keeping its copyright line: “Copyright (c) 2026 A. Author”." in art
    # A part's listing links its articles by title.
    part = files[Path("blueprint/roadmap/lean-pool/16-associative-rings-and-algebras/README.md")]
    assert "- [Rings of order p \\* q over F_q\\[t\\]](art.md)" in part


def git(path: Path, *args: str) -> None:
    env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.org", "GIT_COMMITTER_NAME": "t",
           "GIT_COMMITTER_EMAIL": "t@example.org", "GIT_AUTHOR_DATE": "2026-11-08T12:00:00+02:00",
           "GIT_COMMITTER_DATE": "2026-11-08T12:00:00+02:00"}
    subprocess.run(["git", "-C", str(path), *args], check=True, capture_output=True, env=env)


def repository(root: Path) -> Path:
    git(root, "init", "--quiet")
    git(root, "add", "-A")
    git(root, "commit", "--quiet", "-m", "pool")
    return root


def test_the_refresh_writes_both_records_or_neither(tmp_path):
    out = tmp_path / "out"
    repo = repository(checkout(tmp_path / "lean-pool"))
    assert refresh_lean_pool.refresh(repo, out) == []
    source = json.loads((out / "source.json").read_text(encoding="utf-8"))
    # The commit date is written in UTC.
    assert source["date"] == "2026-11-08T10:00:00Z" and len(source["rev"]) == 40
    assert json.loads((out / "projects.json").read_text(encoding="utf-8"))["rev"] == source["rev"]
    # A card that no longer reads stops the refresh, and the records stay as they were.
    (repo / "LeanPool" / "projects" / "art.yaml").write_text(ART.replace("license: MIT", "license: GPL-3.0"),
                                                               encoding="utf-8")
    git(repo, "commit", "--quiet", "-am", "relicensed")
    kept = (out / "projects.json").read_text(encoding="utf-8")
    problems = refresh_lean_pool.refresh(repo, out)
    assert len(problems) == 1 and "license 'GPL-3.0'" in problems[0]
    assert (out / "projects.json").read_text(encoding="utf-8") == kept


def test_the_refresh_refuses_a_record_that_places_under_half_the_last(tmp_path):
    out = tmp_path / "out"
    out.mkdir()
    last = {"projects": [{"main_results": [{"module": "M"}] * 5}]}
    (out / "projects.json").write_text(json.dumps(last), encoding="utf-8")
    repo = repository(checkout(tmp_path / "lean-pool"))
    assert refresh_lean_pool.refresh(repo, out) == ["places 2 main results, under half the 5 the last record placed"]
    assert not (out / "source.json").exists()


@pytest.mark.skipif(not (ROOT / "data" / "lean-pool" / "projects.json").is_file(), reason="no Lean Pool data")
def test_the_committed_data_build_the_chapter():
    source, record = lean_pool.load(ROOT / "data")
    assert record["schema"] == lean_pool.SCHEMA and record["rev"] == source["rev"] and len(source["rev"]) == 40
    root, stats, parts = lean_pool.chapter(source, record)
    leaves = [node for node in walk(root) if isinstance(node, Leaf)]
    assert len(leaves) == len(record["projects"]) == stats["articles"]
    assert len({leaf.slug for leaf in leaves}) == len(leaves)
    # Every name an article's Lean row shows links from its part to that article's declaration, so no two
    # articles in a part name one declaration differently.
    links = {part.slug[:2]: names for part, names in parts}
    for project in record["projects"]:
        leaf, names = lean_pool.article(source, project)
        assert set(names) == set(dict(leaf.fields).get("lean", "").split(", ")) - {""}
        assert all(links[lean_pool.msc_class(project)][name] == url for name, url in names.items())
    assert all(isinstance(part, Container) and len(part.slug) > 3 for part, _ in parts)
    # Lean Pool's CI checks that every main declaration exists, so the scan should place each one; the only
    # names it can't read are those Lean gives anonymous instances.
    missed = [result["declaration"] for project in record["projects"] for result in project["main_results"]
              if result["main"] and not result["module"]]
    assert all(name.split(".")[-1].startswith("inst") for name in missed), missed
