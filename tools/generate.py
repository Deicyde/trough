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

from trough import analysis, blueprints, catalog, ff, formal_conjectures, links, mathlib, tauceti, wiki
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
                               f"[{tau_stats['articles']:,} declarations its roadmaps name](../roadmap/tauceti/README.md), "
                               "one article per declaration."))
        print(
            f"tauceti: {tau_stats['articles']} articles ({tau_stats.get('theorems', 0)} theorems, "
            f"{tau_stats.get('definitions', 0)} definitions, {tau_stats.get('sorry', 0)} reaching sorry) in "
            f"{tau_stats['roadmaps']} roadmaps; {tau_stats['missing']} names missing at the pin; "
            f"{tau_stats.get('statement_edges', 0)} statement and {tau_stats.get('proof_edges', 0)} proof edges",
            file=sys.stderr,
        )
    ff_libraries = ff.load_libraries(DATA, libraries)
    if ff_libraries:
        ff_built, ff_sections = ff.chapter(ff_libraries)
        assign_paths(ff_built.root, ROADMAP / "formal-frontier")
        blueprints.resolve(ff_built, VAULT)
        files.update(render_tree(ff_built.root, VAULT))
        chapters["formal-frontier"] = "formal-frontier/README.md"
        for section, names, counts in ff_sections:
            # Keyed by the library's directory: the hook takes the longest key a page's path starts with.
            here = section.path.parent.relative_to(ROADMAP).as_posix()
            if names:
                lean_links[here] = dict(sorted(names.items()))
            kinds = [text for number, text in (
                (counts["highlight_articles"], ff.plural(counts["highlight_articles"], "highlight") + " of its formalization.yaml"),
                (counts["headline_articles"], ff.plural(counts["headline_articles"], "headline result"))) if number]
            if kinds:
                blueprint_rows.append((f"Formal Frontier / {section.title}", "DECOMPOSED",
                                       f"[{' and '.join(kinds)}](../roadmap/{here}/README.md) whose declarations the scan "
                                       "finds in the linked file, one article each."))
            else:
                blueprint_rows.append((f"Formal Frontier / {section.title}", "OUT",
                                       f"Mapped as [a page](../roadmap/{here}/README.md) without articles: none of its "
                                       "headline results links a declaration the scan finds in the linked file at the "
                                       "pinned commit."))
        ff_stats = ff_built.stats
        print(
            f"formal-frontier: {ff_stats['articles']} articles ({ff_stats['highlight_articles']} highlights, "
            f"{ff_stats['headline_articles']} headline results) in {ff_stats['libraries']} libraries, "
            f"{ff_stats['libraries_without_articles']} with none; of {ff_stats['headline_items']} headline results, "
            f"{ff_stats['headline_unnamed']} link no declaration, {ff_stats['headline_not_found']} one not found, "
            f"{ff_stats['headline_duplicates']} one with an article; {ff_stats['main_results_found']} of "
            f"{ff_stats['main_results']} main results found",
            file=sys.stderr,
        )
    fc_data = formal_conjectures.load(DATA)
    if fc_data:
        fc_built, fc_links = formal_conjectures.chapter(fc_data)
        assign_paths(fc_built.root, ROADMAP / "formal-conjectures")
        blueprints.resolve(fc_built, VAULT)
        files.update(render_tree(fc_built.root, VAULT))
        chapters["formal-conjectures"] = "formal-conjectures/README.md"
        lean_links["formal-conjectures"] = fc_links
        fc_stats = Counter(fc_built.stats)  # the chapter keeps no zero counts
        blueprint_rows.append(("Formal Conjectures", "DECOMPOSED",
                               f"[{fc_stats['articles']:,} problem files](../roadmap/formal-conjectures/README.md) that state "
                               "a research or textbook statement, one article each, with a card per statement."))
        print(
            f"formal-conjectures: {fc_stats['articles']} articles of {fc_stats['problems']} problem files, "
            f"{fc_stats['statements']} statements ({fc_stats['open']} open, {fc_stats['open proved']} open proved, "
            f"{fc_stats['solved with proof']} solved with a proof link, {fc_stats['solved']} solved without, "
            f"{fc_stats['solved proved']} solved proved, {fc_stats['textbook']} textbook stated, "
            f"{fc_stats['textbook proved']} textbook proved) and {fc_stats['definition']} definitions; "
            f"{fc_stats['test']} test and {fc_stats['api']} API statements counted; {fc_stats['subjects']} subjects; "
            f"{fc_stats['subset_missing']} of {fc_stats['subset_names']} FC100 names without an article",
            file=sys.stderr,
        )
    analysis_data = analysis.load(DATA)
    if analysis_data:
        analysis_built, analysis_links, forward = analysis.chapter(analysis_data)
        assign_paths(analysis_built.root, ROADMAP / "analysis")
        blueprints.resolve(analysis_built, VAULT)
        files.update(render_tree(analysis_built.root, VAULT))
        chapters["analysis"] = "analysis/README.md"
        lean_links["analysis"] = analysis_links
        analysis_stats = analysis_built.stats
        blueprint_rows.append(("Analysis I companion", "DECOMPOSED",
                               f"[{analysis_stats['articles']} section modules](../roadmap/analysis/README.md) of Analysis I "
                               "and An introduction to measure theory, one article each, with a block per labelled item."))
        print(
            f"analysis: {analysis_stats['articles']} articles ({analysis_stats['analysis-i sections']} Analysis I, "
            f"{analysis_stats['measure-theory sections']} measure theory); {analysis_stats['items']} labelled items, "
            f"{analysis_stats['declarations']} declarations ({analysis_stats['proved']} proved here, "
            f"{analysis_stats['stated']} stated, {analysis_stats['exercise']} exercises stated, "
            f"{analysis_stats['definition']} definitions, {analysis_stats['definition sorry']} definitions left as sorry, "
            f"{analysis_stats['axiom']} axioms); {analysis_stats['edges']} import edges, {len(forward)} forward"
            + "".join(f"\n  forward import: {source} imports {target}" for source, target in forward),
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
        {library["id"]: record["rev"] for library, record in ff_libraries},
        fc_data["rev"] if fc_data else None,
        analysis_data["rev"] if analysis_data else None,
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
