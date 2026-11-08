#!/usr/bin/env python3
"""Write trough's AutoformBot vault from its data and catalog.

    python tools/generate.py            write the pages
    python tools/generate.py --check    fail if a page differs from what would be written
    python tools/generate.py --concepts lean/concepts.txt --modules lean/modules.txt --cited lean/cited.txt
                                        write the Lean dump's inputs and stop
    python tools/generate.py --follow-pin
                                        rewrite wiki/ articles for a new Mathlib pin and log
                                        the changes in wiki/pin-changes.json (the data
                                        workflow does this on main, before generating)

Everything under blueprint/roadmap/ and blueprint/links/ is generated, and so are
blueprint/coverage/README.md, blueprint/sources/README.md and
hooks/lean-links.json; a stale file under blueprint/roadmap/ or blueprint/links/
is deleted.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from collections import Counter

from trough import blueprints, catalog, links, mathlib, tauceti, wiki
from trough.vault import Leaf, assign_paths, render_tree, walk

ROOT = Path(__file__).resolve().parent.parent
VAULT = ROOT / "blueprint"
ROADMAP = VAULT / "roadmap"
LINKS = VAULT / "links"
DATA = ROOT / "data"
WIKI = ROOT / "wiki" / "mathlib"
PARKING = ROOT / "wiki" / "unplaced"
PIN_CHANGES = ROOT / "wiki" / "pin-changes.json"


def generate() -> dict[Path, str]:
    libraries = catalog.load(ROOT / "catalog" / "libraries.toml")
    sources = mathlib.load_sources(DATA)
    chapter, stats, targets = mathlib.chapter(sources, wiki.load(WIKI))
    assign_paths(chapter, ROADMAP / "mathlib")
    blueprints.resolve(blueprints.Built(chapter, targets, {}, {}, Counter()), VAULT)
    files = render_tree(chapter, VAULT, annotated=True)
    files.update(links.files(chapter, LINKS / "mathlib", sources.rev))
    chapters = {"mathlib": "mathlib/README.md"}
    # A blueprint node in Mathlib is the Mathlib-chapter article its first declaration heads.
    heads = {}
    for node in walk(chapter):
        if isinstance(node, Leaf):
            first = dict(node.fields).get("mathlib_declaration", "").split(", ")[0]
            if first:
                heads.setdefault(first, node)
    blueprint_rows, lean_links = [], {}
    projects = blueprints.load_projects(DATA, libraries)
    for project in projects:
        built = blueprints.chapter(project, blueprints.load_blueprint(project), heads)
        assign_paths(built.root, ROADMAP / project.id)
        blueprints.resolve(built, VAULT)
        files.update(render_tree(built.root, VAULT))
        chapters[project.id] = f"{project.id}/README.md"
        lean_links[project.id] = dict(sorted(built.lean_links.items()))
        count = built.stats["nodes"]
        blueprint_rows.append((project.name, "DECOMPOSED",
                               f"[{count} blueprint nodes in Lean](../roadmap/{project.id}/README.md), one article per node."))
        unknown = ", ".join(f"\\{name}" for name, _ in built.unknown.most_common(8))
        print(
            f"{project.id}: {count} nodes, {built.stats.get('statements_formalized', 0)} formalized statements and "
            f"{built.stats.get('proofs_formalized', 0)} proofs, {built.stats.get('statement_edges', 0)} statement and "
            f"{built.stats.get('proof_edges', 0)} proof edges, {built.stats.get('problems', 0)} problems"
            + (f"; unknown TeX: {unknown}" if unknown else ""),
            file=sys.stderr,
        )
    tau = tauceti.load_sources(DATA)
    if tau and tau.deps:
        tau_root, tau_stats, tau_links = tauceti.chapter(tau)
        assign_paths(tau_root, ROADMAP / "tauceti")
        files.update(render_tree(tau_root, VAULT))
        chapters["tauceti"] = "tauceti/README.md"
        lean_links["tauceti"] = dict(sorted(tau_links.items()))
        blueprint_rows.append(("Tau Ceti", "DECOMPOSED",
                               f"[{tau_stats['articles']:,} articles on {tau_stats['declarations']:,} declarations]"
                               "(../roadmap/tauceti/README.md) its roadmaps' statuses name or its docstrings name as "
                               "results, the forms of one result in one article."))
        print(
            f"tauceti: {tau_stats['articles']} articles on {tau_stats['declarations']} declarations "
            f"({tau_stats.get('theorems', 0)} theorems, {tau_stats.get('definitions', 0)} definitions, "
            f"{tau_stats.get('sorry', 0)} reaching sorry; {tau_stats['named']} named by statuses, {tau_stats['chosen']} "
            f"more by docstrings; {tau_stats.get('forms', 0)} articles with several forms) in {tau_stats['parts']} parts, "
            f"{tau_stats['roadmaps']} roadmap and {tau_stats.get('areas', 0)} area sections; {tau_stats['missing']} names "
            f"missing at the pin; {tau_stats.get('statement_edges', 0)} statement and "
            f"{tau_stats.get('proof_edges', 0)} proof edges",
            file=sys.stderr,
        )
    files[ROOT / "hooks" / "lean-links.json"] = json.dumps(lean_links, indent=1, ensure_ascii=False) + "\n"
    root = ROADMAP / "README.md"
    previous = root.read_text(encoding="utf-8") if root.is_file() else None
    files[root] = catalog.roadmap_root(libraries, chapters, previous)
    rows = []
    for entry in chapter.entries:
        node = entry.node
        total, present = stats["in_lists"][_list_of(node.slug)]
        rows.append(
            (
                f"Mathlib / {node.title}",
                "DECOMPOSED",
                f"[{present:,} of {total:,} list items](../roadmap/mathlib/{node.slug}/README.md) in Mathlib, "
                "one article per concept.",
            )
        )
    files[VAULT / "coverage" / "README.md"] = catalog.coverage(libraries, rows + blueprint_rows)
    files[VAULT / "sources" / "README.md"] = catalog.sources_readme(
        libraries, sources.rev, sources.thousand_plus,
        [(project.id, project.name, project.repo, project.license, project.text) for project in projects],
        (tau.rev, tau.roadmap_rev) if tau and tau.deps else None,
    )
    print(
        f"mathlib: {stats['articles']} articles ({stats['formalized']} in Mathlib, {stats['stated']} stated only, "
        f"{stats['authored']} authored; {stats['left_out']} concepts Mathlib lacks left out), {stats['statement']} statement and {stats['proof']} proof edges, "
        f"{stats['informal']} informal",
        file=sys.stderr,
    )
    return files


def _list_of(slug: str) -> str:
    return next(name for name, value in mathlib.LIST_SLUGS.items() if value == slug)


def owned() -> set[Path]:
    return set(ROADMAP.rglob("*.md")) | {path for path in LINKS.rglob("*") if path.is_file()}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--check", action="store_true", help="fail if any generated page is stale")
    parser.add_argument("--concepts", type=Path, help="write the listed declaration names here and stop")
    parser.add_argument("--modules", type=Path, help="write the listed module names here and stop")
    parser.add_argument("--cited", type=Path,
                        help="write the names the wiki's articles cite or are keyed on, and those blueprints "
                             "credit to Mathlib, here and stop")
    parser.add_argument("--follow-pin", action="store_true",
                        help="rewrite the wiki's articles for the data's Mathlib pin and stop")
    args = parser.parse_args()
    if args.follow_pin:
        changes = mathlib.follow_pin(mathlib.load_sources(DATA), WIKI, PARKING)
        if changes:
            logged = json.loads(PIN_CHANGES.read_text(encoding="utf-8")) if PIN_CHANGES.is_file() else []
            PIN_CHANGES.write_text(json.dumps(logged + changes, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"{len(changes)} changes to the wiki's articles for this pin", file=sys.stderr)
        return 0
    if args.cited:
        articles = wiki.load(WIKI)
        # Keys too, so the dump says what replaces a concept's declaration when Mathlib renames it.
        keys = {key for article in articles.values()
                for key in [article.concept, *article.depends, *article.proof_depends, *wiki.linked(article)]}
        # And the names a blueprint page credits to Mathlib, so each of those has a record too.
        libraries = catalog.load(ROOT / "catalog" / "libraries.toml")
        credited = {name for project in blueprints.load_projects(DATA, libraries)
                    for node in blueprints.load_blueprint(project).graph if node.mathlibok for name in node.lean}
        names = sorted(set(wiki.cited(articles)) | credited | {key for key in keys if not re.match(r"[^.:]*:", key)})
        args.cited.write_text("".join(f"{name}\n" for name in names), encoding="utf-8")
    if args.concepts or args.modules:
        # Listing needs only the lists: the dump may be of the previous pin.
        articles = mathlib.merge(mathlib.load_sources(DATA, deps=False).lists)
        statements = sorted({item.statement for article in articles for item in article.items if item.statement})
        if args.concepts:
            names = sorted(set(mathlib.concept_names(articles)) | set(statements))
            args.concepts.write_text("".join(f"{name}\n" for name in names), encoding="utf-8")
        if args.modules:
            args.modules.write_text("".join(f"{name}\n" for name in mathlib.module_names(articles)), encoding="utf-8")
    if args.concepts or args.modules or args.cited:
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
