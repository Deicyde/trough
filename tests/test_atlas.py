import json
import os
import subprocess
from pathlib import Path

import refresh_atlas
from trough import atlas, blueprints
from trough.vault import Container, Leaf, assign_paths, render_tree, walk

ATLAS_JSON = json.dumps({"schema": "autoform-atlas/v1",
                         "areas": {"Analysis & Probability": ["Analysis", "Probability"], "Algebra": ["GroupTheory"]}})


def links(*rows: dict) -> str:
    return "".join(json.dumps(row) + "\n" for row in rows)


def annotation(path: str, name: str | None = None) -> dict:
    row = {"subject": [{"type": "generic", "uri": f"../roadmap/{path}"}]}
    if name:
        row["object"] = [{"location": {"declaration": name}}]
    return row


SHIFT = "Analysis/operator-theory/shift"
FILES = {
    "blueprint/atlas.json": ATLAS_JSON,
    "blueprint/roadmap/README.md": "# ATLAS roadmap\n",
    "blueprint/roadmap/Analysis/README.md": (
        "# Analysis\n\nAnalysis studies limits. [Operator theory](operator-theory/README.md) is the largest field: "
        "see [the shift](operator-theory/shift/README.md), [a result](operator-theory/shift/part-01/is-fredholm.md), "
        "[the web](https://example.org) and [a page gone](missing/README.md).\n\n"
        "- [Operator theory](operator-theory/README.md)\n- [A lone result](lone.md)\n"),
    "blueprint/roadmap/Analysis/lone.md": "# A lone result\n\nEvery $x$ equals $x$.\n",
    "blueprint/roadmap/Analysis/operator-theory/README.md": (
        "# Operator theory\n\n- [Unilateral shift](shift/README.md)\n- [Spectral theory](spectral/README.md)\n"),
    f"blueprint/roadmap/{SHIFT}/README.md": (
        "# Unilateral shift\n\nThe shift on $\\ell^2$.\n\n"
        "## [The shift is Fredholm to A wanted result](part-01/README.md)\n\n"
        "- [The shift is Fredholm](part-01/is-fredholm.md)\n- [A wanted result](part-01/wanted.md)\n\n"
        "## [A result with sorry](part-02/README.md)\n\n- [A result with sorry](part-02/sorry.md)\n"),
    f"blueprint/roadmap/{SHIFT}/part-01/README.md": "# The shift is Fredholm to A wanted result\n",
    f"blueprint/roadmap/{SHIFT}/part-02/README.md": "# A result with sorry\n",
    f"blueprint/roadmap/{SHIFT}/part-01/is-fredholm.md": (
        "# The shift is Fredholm\n\nThe shift $S$ is Fredholm of index $-1$; compare "
        "[the spectral theorem](../../spectral/README.md).\n"),
    f"blueprint/roadmap/{SHIFT}/part-01/wanted.md": "# A wanted result\n\nSomething whose proof is deferred.\n",
    f"blueprint/roadmap/{SHIFT}/part-02/sorry.md": "# A result with sorry\n\nSomething not yet proved.\n",
    "blueprint/roadmap/Analysis/operator-theory/spectral/README.md": (
        "# Spectral theory\n\n- [A name the Lean lacks](absent.md)\n- [No declaration](none.md)\n"),
    "blueprint/roadmap/Analysis/operator-theory/spectral/absent.md": "# A name the Lean lacks\n\nA statement.\n",
    "blueprint/roadmap/Analysis/operator-theory/spectral/none.md": "# No declaration\n\nAnother statement.\n",
    "blueprint/roadmap/GroupTheory/README.md": "# Group theory\n\n- [Sylow theorems](sylow/README.md)\n",
    "blueprint/roadmap/GroupTheory/sylow/README.md": "# Sylow theorems\n\n- [The first Sylow theorem](first.md)\n",
    "blueprint/roadmap/GroupTheory/sylow/first.md": "# The first Sylow theorem\n\nA finite group has a Sylow $p$-subgroup.\n",
    "blueprint/links/_defaults.json": json.dumps({"object": {"type": "lean", "uri": "../.."}}),
    "blueprint/links/Analysis.jsonl": links(
        annotation("Analysis/README.md"),
        annotation("Analysis/lone.md", "MathlibExt.lone"),
        annotation(f"{SHIFT}/part-01/is-fredholm.md", "MathlibExt.Shift.isFredholm"),
        annotation(f"{SHIFT}/part-01/wanted.md", "MathlibExt.Shift.wanted"),
        annotation(f"{SHIFT}/part-02/sorry.md", "MathlibExt.Shift.withSorry"),
        annotation("Analysis/operator-theory/spectral/absent.md", "MathlibExt.absent"),
        annotation("Analysis/operator-theory/spectral/none.md")),
    "blueprint/links/GroupTheory.jsonl": links(annotation("GroupTheory/sylow/first.md", "Atlas.Sylow.first")),
    "MathlibExt/Analysis/Shift.lean": (
        "namespace MathlibExt\n\ntheorem lone : True := trivial\n\nnamespace Shift\n\n"
        "theorem isFredholm : True := trivial\n\ntheorem withSorry : True := by\n  sorry\n\nend Shift\n\nend MathlibExt\n"),
    "WantedExt/Shift.lean": (
        "import Batteries.Util.ProofWanted\n\nnamespace MathlibExt.Shift\n\ntheorem_wanted wanted : 1 = 1\n\n"
        "end MathlibExt.Shift\n"),
    "Atlas/Group/Sylow.lean": "namespace Atlas.Sylow\n\ntheorem first : True := trivial\n\nend Atlas.Sylow\n",
    # A name MathlibExt declares too: the root library's declaration wins.
    "Atlas/Group/Again.lean": "namespace MathlibExt\n\ntheorem lone : True := trivial\n\nend MathlibExt\n",
    # Not read: a test library.
    "MathlibExtTest/Shift.lean": "namespace MathlibExt\n\ntheorem absent : True := trivial\n\nend MathlibExt\n",
}
LICENSE = ("Codebase is not intended for use to train models\n\n\n                                 Apache License\n"
           "                           Version 2.0, January 2004\n")
MANIFEST = json.dumps({"packages": [{"name": "mathlib", "rev": "d" * 40, "inputRev": "v4.35.0"}]})


def write(root: Path, files: dict[str, str]) -> Path:
    for name, text in files.items():
        (root / name).parent.mkdir(parents=True, exist_ok=True)
        (root / name).write_text(text, encoding="utf-8")
    return root


def git(path: Path, *args: str) -> str:
    env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.org", "GIT_COMMITTER_NAME": "t",
           "GIT_COMMITTER_EMAIL": "t@example.org", "GIT_AUTHOR_DATE": "2026-11-11T07:16:11+01:00",
           "GIT_COMMITTER_DATE": "2026-11-11T07:16:11+01:00"}
    return subprocess.run(["git", "-C", str(path), *args], check=True, capture_output=True, text=True, env=env).stdout


def checkout(root: Path, files: dict[str, str] = FILES, license_text: str = LICENSE) -> Path:
    # Shaped like the sparse checkout the workflow makes.
    write(root, files | {"LICENSE": license_text, "lean-toolchain": "leanprover/lean4:v4.35.0\n",
                         "lake-manifest.json": MANIFEST})
    git(root, "init", "--quiet")
    git(root, "add", "-A")
    git(root, "commit", "--quiet", "-m", "vault")
    return root


def cards(url: str, method: str) -> bytes | None:
    # Every page holds every card.
    return b" ".join(f'<h4 id="{name}">'.encode() for name in ("lone", "is-fredholm", "wanted", "sorry", "absent",
                                                                 "none", "first"))


def no_site(url: str, method: str) -> bytes | None:
    return None


def data(tmp_path: Path, site: bool = False) -> dict:
    out = tmp_path / "data" / "atlas"
    assert refresh_atlas.refresh(checkout(tmp_path / "atlas"), out, site, cards) == []
    return atlas.load(tmp_path / "data")


def build(tmp_path: Path, site: bool = False):
    built, lean_links = atlas.chapter(data(tmp_path, site))
    vault = Path("blueprint")
    assign_paths(built.root, vault / "roadmap" / "atlas")
    blueprints.resolve(built, vault)
    return built, lean_links, render_tree(built.root, vault)


ROOT = Path("blueprint/roadmap/atlas")
TOPIC = ROOT / "analysis-probability/analysis/operator-theory/shift.md"


def test_a_license_is_apache_after_any_sentence_of_its_own():
    assert atlas.license_notice(LICENSE) == "Codebase is not intended for use to train models"
    assert atlas.license_notice("  Apache License\n  Version 2.0, January 2004\n") == ""
    assert atlas.license_notice("MIT License\n") is None


def test_the_vault_gives_its_containers_articles_and_where_the_lean_declares_them(tmp_path):
    structure, articles, counts, problems = atlas.read(checkout(tmp_path))
    assert problems == []
    # An area keeps only the subjects the vault has.
    assert structure["areas"] == [{"title": "Analysis & Probability", "subjects": ["Analysis"]},
                                  {"title": "Algebra", "subjects": ["GroupTheory"]}]
    analysis = structure["subjects"]["Analysis"]
    assert analysis["title"] == "Analysis" and analysis["prose"].startswith("Analysis studies limits.")
    assert [entry.get("article") or entry["node"]["path"] for entry in analysis["entries"]] == [
        "Analysis/operator-theory", "Analysis/lone.md"]
    shift = analysis["entries"][0]["node"]["entries"][0]["node"]
    # The transparent parts' items are the topic's own.
    assert shift["prose"] == "The shift on $\\ell^2$." and [entry["article"] for entry in shift["entries"]] == [
        f"{SHIFT}/part-01/is-fredholm.md", f"{SHIFT}/part-01/wanted.md", f"{SHIFT}/part-02/sorry.md"]
    found = {article["path"]: article for records in articles.values() for article in records}
    assert found["Analysis/lone.md"]["lean"] == {"file": "MathlibExt/Analysis/Shift.lean", "line": 3, "kind": "theorem",
                                                 "sorry": False}
    assert found[f"{SHIFT}/part-01/wanted.md"]["lean"]["kind"] == "theorem_wanted"
    assert found[f"{SHIFT}/part-02/sorry.md"]["lean"]["sorry"] is True
    assert found["Analysis/operator-theory/spectral/absent.md"]["lean"] is None
    assert found["Analysis/operator-theory/spectral/none.md"]["declaration"] == ""
    assert found["GroupTheory/sylow/first.md"]["statement"] == "A finite group has a Sylow $p$-subgroup."
    assert (counts["results"], counts["results_proved"], counts["results_wanted"], counts["results_sorry"],
            counts["results_absent"], counts["results_none"]) == (7, 3, 1, 1, 1, 1)
    assert counts["lean_files"] == 4 and counts["names_declared_twice_MathlibExt_Atlas"] == 1


def test_what_does_not_read_is_listed(tmp_path):
    broken = FILES | {"blueprint/roadmap/GroupTheory/sylow/README.md": "# Sylow theorems\n\n- [Gone](gone.md)\n",
                      "blueprint/roadmap/Analysis/lone.md": "A lone result without a title line.\n",
                      "blueprint/links/Bad.jsonl": "{not json\n"}
    _, _, _, problems = atlas.read(checkout(tmp_path, broken))
    assert problems == ["Analysis/lone.md has no title line", "GroupTheory/sylow/README.md links gone.md, which is missing",
                        "links/Bad.jsonl:1 does not read"]


def test_the_chapter_has_a_part_per_area_a_page_per_subject_and_branch_and_an_article_per_topic(tmp_path):
    built, lean_links, files = build(tmp_path)
    assert built.root.title == atlas.TITLE
    assert [entry.node.title for entry in built.root.entries] == ["Analysis & Probability", "Algebra"]
    subject = built.root.entries[0].node.entries[0].node
    assert isinstance(subject, Container) and subject.title == "Analysis"
    # A subject's own results are an article of its own, at the place of the first.
    assert [entry.node.title for entry in subject.entries] == ["Operator theory", "Analysis: its own results"]
    branch = subject.entries[0].node
    assert [type(entry.node) for entry in branch.entries] == [Leaf, Leaf]
    assert [entry.node.title for entry in branch.entries] == ["Unilateral shift", "Spectral theory"]
    leaves = [node for node in walk(built.root) if isinstance(node, Leaf)]
    assert len(leaves) == built.stats["articles"] == 4
    assert (built.stats["results"], built.stats["proved"], built.stats["wanted"]) == (7, 3, 1)
    assert set(files) >= {ROOT / "README.md", TOPIC, ROOT / "algebra/group-theory/sylow.md"}
    assert lean_links["MathlibExt.Shift.isFredholm"] == (
        f"https://github.com/Deicyde/atlas-lean/blob/{data(tmp_path / 'again')['source']['rev']}"
        "/MathlibExt/Analysis/Shift.lean#L7")
    assert "MathlibExt.absent" not in lean_links


def test_a_topic_has_a_block_per_result_in_the_vaults_order(tmp_path):
    _, _, files = build(tmp_path)
    page = files[TOPIC]
    assert page.startswith("---\ndeclaration: section\norigin: cited\n"
                           "lean: MathlibExt.Shift.isFredholm, MathlibExt.Shift.wanted, MathlibExt.Shift.withSorry\n"
                           "statement: formalized\n---\n\n# Unilateral shift\n\n")
    # Not every result is proved, so the proof is not marked formalized.
    assert "proof: formalized" not in page
    assert "# Unilateral shift\n\n3 results, 1 proved, 1 with `sorry` in its value and 1 stated but not proved, quoted" in page
    assert page.index("## The shift is Fredholm") < page.index("## A wanted result") < page.index("## A result with sorry")
    assert "Formalized by `MathlibExt.Shift.isFredholm`, a theorem declared in [MathlibExt/Analysis/Shift.lean, line 7]" in page
    assert "Stated but not proved: `MathlibExt.Shift.wanted` is written with `theorem_wanted` in [WantedExt/Shift.lean, line 5]" in page
    assert "line 9](" in page and "Its value contains `sorry`." in page
    # A link to another topic's container points to its article.
    assert "compare [the spectral theorem](spectral.md)." in page
    spectral = files[TOPIC.with_name("spectral.md")]
    assert "Formalized by `MathlibExt.absent`, which the repository's Lean, as read here, does not declare." in spectral
    assert "The vault records no Lean declaration for it." in spectral
    sylow = files[ROOT / "algebra/group-theory/sylow.md"]
    assert "proof: formalized" in sylow and "\n\n1 result, proved, quoted from" in sylow


def test_the_vaults_links_point_to_this_chapters_pages(tmp_path):
    _, _, files = build(tmp_path)
    page = files[ROOT / "analysis-probability/analysis/README.md"]
    assert "[Operator theory](operator-theory/README.md) is the largest field" in page
    assert "see [the shift](operator-theory/shift.md), [a result](operator-theory/shift.md)" in page
    assert "[the web](https://example.org)" in page
    assert "[a page gone](https://github.com/Deicyde/atlas-lean/blob/" in page and "/blueprint/roadmap/Analysis/missing/README.md)" in page


def test_the_blocks_link_the_sites_cards_only_when_it_holds_them(tmp_path):
    _, _, files = build(tmp_path)
    assert "deicyde.github.io" not in files[TOPIC]
    _, _, files = build(tmp_path / "site", site=True)
    assert (f"[Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/{SHIFT}/part-01/index.html"
            "#is-fredholm).") in files[TOPIC]
    assert f"[its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/{SHIFT}/index.html)" in files[TOPIC]


def test_the_pages_credit_the_vault_and_note_its_license_once(tmp_path):
    _, _, files = build(tmp_path)
    root = files[ROOT / "README.md"]
    assert "under its Apache-2.0 license (its LICENSE file adds that the code is not meant for training models)." in root
    assert "not meant for training" not in files[ROOT / "analysis-probability/README.md"]
    assert "under its Apache-2.0 license." in files[ROOT / "analysis-probability/README.md"]


def test_the_refresh_writes_the_source_the_structure_and_the_articles(tmp_path):
    out = tmp_path / "data" / "atlas"
    repo = checkout(tmp_path / "atlas")
    assert refresh_atlas.refresh(repo, out, True, cards) == []
    source = json.loads((out / "source.json").read_text(encoding="utf-8"))
    rev = git(repo, "rev-parse", "HEAD").strip()
    # The commit date is written in UTC.
    assert (source["repo"], source["branch"], source["rev"], source["date"], source["toolchain"]) == (
        atlas.REPO, atlas.BRANCH, rev, "2026-11-11T06:16:11Z", "v4.35.0")
    assert (source["mathlib"], source["license_notice"]) == ("d" * 40, "Codebase is not intended for use to train models")
    assert source["site"] == {"url": atlas.SITE, "cards": True} and source["counts"]["results"] == 7
    assert sorted(path.name for path in (out / "articles").iterdir()) == ["Analysis.json", "GroupTheory.json"]
    structure = json.loads((out / "structure.json").read_text(encoding="utf-8"))
    assert structure["schema"] == atlas.SCHEMA and structure["rev"] == rev
    assert refresh_atlas.refresh(repo, tmp_path / "other", True, no_site) == []
    assert json.loads((tmp_path / "other" / "source.json").read_text(encoding="utf-8"))["site"]["cards"] is False


def test_the_refresh_writes_nothing_from_a_checkout_it_cannot_read(tmp_path):
    out = tmp_path / "out"
    mit = checkout(tmp_path / "mit", license_text="MIT License\n")
    assert refresh_atlas.refresh(mit, out) == [f"{atlas.REPO} at {git(mit, 'rev-parse', 'HEAD')[:8]}: its LICENSE is not Apache-2.0"]
    broken = checkout(tmp_path / "broken", FILES | {"blueprint/roadmap/GroupTheory/sylow/first.md": "No title.\n"})
    assert refresh_atlas.refresh(broken, out) == ["GroupTheory/sylow/first.md has no title line"]
    assert not out.exists()
    (out / "articles").mkdir(parents=True)
    last = {"schema": atlas.SCHEMA, "rev": "e" * 40, "articles": [{"path": f"X/{n}.md"} for n in range(20)]}
    (out / "articles" / "X.json").write_text(json.dumps(last), encoding="utf-8")
    assert refresh_atlas.refresh(checkout(tmp_path / "good"), out) == ["7 results, under half the 20 of the last record"]


def test_a_result_heading_escapes_its_braces_outside_code_and_formulas():
    # A heading ending in `{...}` would be read as an attribute list.
    assert atlas.heading("The gene tree with cherry {0, 2}") == "The gene tree with cherry \\{0, 2}"
    assert atlas.heading("Sums over $\\{0, 1\\}^n$ and `{x}`") == "Sums over $\\{0, 1\\}^n$ and `{x}`"
