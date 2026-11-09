from pathlib import Path

import pytest

from trough import catalog

CATALOG = Path(__file__).resolve().parent.parent / "catalog" / "libraries.toml"


def test_catalog_loads_and_names_every_group():
    libraries = catalog.load(CATALOG)
    groups = {library["group"] for library in libraries}
    assert groups == {group for group, _ in catalog.GROUPS}
    assert sum(library["map_status"] == "live" for library in libraries) >= 1


def test_coverage_has_a_row_per_library_not_live():
    libraries = catalog.load(CATALOG)
    page = catalog.coverage(libraries, [("Mathlib / overview", "DECOMPOSED", "[x](a.md)")])
    rows = [line for line in page.splitlines() if line.startswith("| ") and "---" not in line]
    assert len(rows) == 2 + sum(library["map_status"] != "live" for library in libraries)


def test_the_book_shows_no_lean_progress():
    root = catalog.roadmap_root(catalog.load(CATALOG), {}, None)
    assert root.startswith("---\ntracks_lean: false\n---\n\n# Trough\n")


def test_a_formal_frontier_library_names_a_known_subject(tmp_path):
    entry = ('[[library]]\nid = "ff-x"\nname = "X"\nrepo = "FormalFrontier/x"\ngroup = "formal-frontier"\n'
             'map_status = "live"\nmap_unit = "headline result"\nmap_plan = "p"\n')
    path = tmp_path / "libraries.toml"
    path.write_text(entry + 'subject = "Topology"\n', encoding="utf-8")
    assert catalog.load(path)[0]["subject"] == "Topology"
    path.write_text(entry + 'subject = "Astrology"\n', encoding="utf-8")
    with pytest.raises(ValueError, match="unknown subject Astrology"):
        catalog.load(path)
    path.write_text(entry, encoding="utf-8")
    with pytest.raises(ValueError, match="unknown subject None"):
        catalog.load(path)


def test_the_formal_frontier_libraries_share_one_chapter_line():
    libraries = catalog.load(CATALOG)
    live = sum(library["group"] == "formal-frontier" and library["map_status"] == "live" for library in libraries)
    root = catalog.roadmap_root(libraries, {"formal-frontier": "formal-frontier/README.md"}, None)
    lines = [line for line in root.splitlines() if "Formal Frontier" in line and line.startswith("- [")]
    assert lines == [line for line in lines if line.startswith(f"- [Formal Frontier](formal-frontier/README.md): {live} libraries")]
    assert len(lines) == 1


def test_the_sources_page_takes_the_analysis_companions_commit_from_its_data():
    page = catalog.sources_readme(catalog.load(CATALOG), "a" * 40, None, analysis="c" * 40)
    assert f"[teorth/analysis at cccccccc](https://github.com/teorth/analysis/tree/{'c' * 40})" in page
    assert "- [Analysis I companion](https://github.com/teorth/analysis) at cccccccccccc: Terence Tao's" in page
