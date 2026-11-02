#!/usr/bin/env python3
"""Write trough's AutoformBot vault from its data and catalog.

    python tools/generate.py            write the pages
    python tools/generate.py --check    fail if a page differs from what would be written
    python tools/generate.py --concepts lean/concepts.txt --modules lean/modules.txt
                                        write the Lean dump's inputs and stop

Everything under blueprint/roadmap/ is generated, and so are
blueprint/coverage/README.md and blueprint/sources/README.md; a stale page
under blueprint/roadmap/ is deleted.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from trough import catalog, mathlib
from trough.vault import assign_paths, render_tree

ROOT = Path(__file__).resolve().parent.parent
VAULT = ROOT / "blueprint"
ROADMAP = VAULT / "roadmap"
DATA = ROOT / "data"


def generate() -> dict[Path, str]:
    libraries = catalog.load(ROOT / "catalog" / "libraries.toml")
    sources = mathlib.load_sources(DATA)
    chapter, stats = mathlib.chapter(sources)
    assign_paths(chapter, ROADMAP / "mathlib")
    files = render_tree(chapter, VAULT)
    root = ROADMAP / "README.md"
    previous = root.read_text(encoding="utf-8") if root.is_file() else None
    files[root] = catalog.roadmap_root(libraries, {"mathlib": "mathlib/README.md"}, previous)
    rows = []
    for entry in chapter.entries:
        node = entry.node
        count = sum(1 for item in sources.lists[_list_of(node.slug)])
        rows.append(
            (
                f"Mathlib / {node.title}",
                "DECOMPOSED",
                f"[{count} list items](../roadmap/mathlib/{node.slug}/README.md), one article per concept.",
            )
        )
    files[VAULT / "coverage" / "README.md"] = catalog.coverage(libraries, rows)
    files[VAULT / "sources" / "README.md"] = catalog.sources_readme(libraries, sources.rev, sources.thousand_plus)
    print(
        f"mathlib: {stats['articles']} articles ({stats['formalized']} in Mathlib, {stats['wanted']} not yet), "
        f"{stats['statement']} statement and {stats['proof']} proof edges, {stats['informal']} informal",
        file=sys.stderr,
    )
    return files


def _list_of(slug: str) -> str:
    return next(name for name, value in mathlib.LIST_SLUGS.items() if value == slug)


def owned() -> set[Path]:
    return set(ROADMAP.rglob("*.md")) if ROADMAP.is_dir() else set()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--check", action="store_true", help="fail if any generated page is stale")
    parser.add_argument("--concepts", type=Path, help="write the listed declaration names here and stop")
    parser.add_argument("--modules", type=Path, help="write the listed module names here and stop")
    args = parser.parse_args()
    if args.concepts or args.modules:
        # Listing needs only the lists: the dump may be of the previous pin.
        articles = mathlib.merge(mathlib.load_sources(DATA, deps=False).lists)
        statements = sorted({item.statement for article in articles for item in article.items if item.statement})
        if args.concepts:
            names = sorted(set(mathlib.concept_names(articles)) | set(statements))
            args.concepts.write_text("".join(f"{name}\n" for name in names), encoding="utf-8")
        if args.modules:
            args.modules.write_text("".join(f"{name}\n" for name in mathlib.module_names(articles)), encoding="utf-8")
        return 0
    files = generate()
    stale = sorted(owned() - set(files))
    changed = sorted(path for path, text in files.items() if not path.is_file() or path.read_text(encoding="utf-8") != text)
    if args.check:
        for path in changed + stale:
            print(f"stale: {path.relative_to(ROOT)}", file=sys.stderr)
        if changed or stale:
            print("Regenerate the pages with: uv run python tools/generate.py", file=sys.stderr)
            return 1
        return 0
    for path in stale:
        path.unlink()
    for path in changed:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(files[path], encoding="utf-8")
    for directory in sorted({path.parent for path in stale}, key=lambda path: len(path.parts), reverse=True):
        if directory.is_dir() and not any(directory.iterdir()):
            directory.rmdir()
    print(f"{len(changed)} pages written, {len(stale)} removed", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
