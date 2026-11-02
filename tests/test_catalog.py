from pathlib import Path

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
