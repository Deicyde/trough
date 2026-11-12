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

from trough import anthropic_flt, atlas, blueprints, catalog, cfsg, ff, formal_conjectures, lean_pool, links, mathlib, openai_math, stacks, tauceti, wiki
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
    imperial = None
    for project in projects:
        built = blueprints.chapter(project, blueprints.load_blueprint(project), heads)
        assign_paths(built.root, ROADMAP / project.id)
        if project.id == anthropic_flt.IMPERIAL:
            imperial = built.root
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
    tau_root = None
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
    pool = lean_pool.load(DATA)
    if pool:
        pool_root, pool_stats, pool_parts = lean_pool.chapter(*pool)
        assign_paths(pool_root, ROADMAP / "lean-pool")
        files.update(render_tree(pool_root, VAULT))
        chapters["lean-pool"] = "lean-pool/README.md"
        for part, names in pool_parts:
            # Keyed by the part's directory, as a name may be declared in more than one project.
            if names:
                lean_links[part.path.parent.relative_to(ROADMAP).as_posix()] = dict(sorted(names.items()))
        blueprint_rows.append(("Lean Pool", "DECOMPOSED",
                               f"[{pool_stats['articles']} project cards](../roadmap/lean-pool/README.md), one article "
                               "per card."))
        print(
            f"lean-pool: {pool_stats['articles']} articles in {pool_stats['parts']} parts; "
            f"{pool_stats['main_results_found']} of {pool_stats['main_results']} main results and "
            f"{pool_stats['main_declarations_found']} of {pool_stats['main_declarations']} main declarations found",
            file=sys.stderr,
        )
    aflt = anthropic_flt.load(DATA)
    if aflt:
        aflt_built, aflt_links = anthropic_flt.chapter(*aflt, imperial)
        assign_paths(aflt_built.root, ROADMAP / "anthropic-flt")
        blueprints.resolve(aflt_built, VAULT)
        files.update(render_tree(aflt_built.root, VAULT))
        chapters["anthropic-flt"] = "anthropic-flt/README.md"
        lean_links["anthropic-flt"] = dict(sorted(aflt_links.items()))
        aflt_stats = aflt_built.stats
        blueprint_rows.append(("Fermat's Last Theorem (Anthropic)", "DECOMPOSED",
                               f"[{aflt_stats['articles']} landmark theorems](../roadmap/anthropic-flt/README.md) in the "
                               f"steps of PROOF-PATH.md, one article each; the other "
                               f"{aflt_stats['theorems'] - aflt_stats['articles']:,} theorems are counted, not mapped."))
        print(
            f"anthropic-flt: {aflt_stats['articles']} landmark articles of {aflt_stats['theorems']} theorems in "
            f"{aflt_stats['parts']} parts; {aflt_stats['landmark_edges']} edges between landmarks of "
            f"{aflt_stats['edges']}; {aflt_stats['imperial_matches']} names shared with Imperial FLT",
            file=sys.stderr,
        )
    cfsg_data = cfsg.load(DATA)
    if cfsg_data:
        cfsg_built, cfsg_links = cfsg.chapter(cfsg_data, tau_root)
        assign_paths(cfsg_built.root, ROADMAP / "cfsg")
        blueprints.resolve(cfsg_built, VAULT)
        files.update(render_tree(cfsg_built.root, VAULT))
        chapters["cfsg"] = "cfsg/README.md"
        lean_links["cfsg"] = cfsg_links
        cfsg_stats = Counter(cfsg_built.stats)  # the chapter keeps no zero counts
        blueprint_rows.append((cfsg.TITLE, "DECOMPOSED",
                               f"[The top theorem, its reduction to {cfsg_stats['cases']} cases and the theorem for each "
                               f"case, and {cfsg_stats['milestones']:,} milestone modules](../roadmap/cfsg/README.md), one "
                               "article each, with their Lean statements."))
        print(
            f"cfsg: {cfsg_stats['articles']} articles ({cfsg_stats['cases']} cases, {cfsg_stats['milestones']} milestones, "
            f"{cfsg_stats['indexed']} of them indexed, {cfsg_stats['unreached']} reached by no case), "
            f"{cfsg_stats['milestone_declarations']} milestone declarations, {cfsg_stats['sorry']} holding sorry, "
            f"{cfsg_stats['edges']} import edges, {cfsg_stats['tauceti']} linking Tau Ceti",
            file=sys.stderr,
        )
    stacks_data = stacks.load(DATA)
    if stacks_data:
        stacks_built, stacks_links = stacks.chapter(stacks_data)
        assign_paths(stacks_built.root, ROADMAP / "stacks")
        blueprints.resolve(stacks_built, VAULT)
        files.update(render_tree(stacks_built.root, VAULT))
        chapters["stacks"] = "stacks/README.md"
        lean_links["stacks"] = stacks_links
        st = Counter(stacks_built.stats)
        blueprint_rows.append(("The Stacks Project in Lean (Axiom)", "DECOMPOSED",
                               f"[{st['articles']:,} sections of the Stacks Project](../roadmap/stacks/README.md) with a "
                               "tag that a declaration carries, one article each, with a block per tag."))
        print(
            f"stacks: {st['articles']} articles in {st['chapters']} chapters and {st['parts']} parts; {st['tags']} tags "
            f"carried by {st['StacksCore']} StacksCore and {st['StacksFrontier']} StacksFrontier declarations and "
            f"{st['registrations']} registrations; {st['unplaced']} tags not placed; {st['ega_indexed']} EGA and "
            f"{st['sga_indexed']} SGA items indexed",
            file=sys.stderr,
        )
    atlas_data = atlas.load(DATA)
    if atlas_data:
        atlas_built, atlas_links = atlas.chapter(atlas_data)
        assign_paths(atlas_built.root, ROADMAP / "atlas")
        blueprints.resolve(atlas_built, VAULT)
        files.update(render_tree(atlas_built.root, VAULT))
        chapters["atlas-lean"] = "atlas/README.md"
        lean_links["atlas"] = atlas_links
        at = Counter(atlas_built.stats)
        blueprint_rows.append((atlas.TITLE, "DECOMPOSED",
                               f"[{at['articles']:,} topics of ATLAS's vault](../roadmap/atlas/README.md), one article "
                               "each, with a block per result."))
        print(
            f"atlas: {at['articles']} topic articles on {at['containers']} pages in {at['subjects']} subjects and "
            f"{at['parts']} areas; {at['results']} results: {at['proved']} proved, {at['wanted']} wanted, {at['sorry']} "
            f"with sorry, {at['absent']} not declared, {at['none']} without a declaration",
            file=sys.stderr,
        )
    oai_data = openai_math.load(DATA)
    if oai_data:
        oai_built, oai_links = openai_math.chapter(oai_data)
        assign_paths(oai_built.root, ROADMAP / "openai-math")
        blueprints.resolve(oai_built, VAULT)
        files.update(render_tree(oai_built.root, VAULT))
        chapters["openai-math"] = "openai-math/README.md"
        lean_links["openai-math"] = oai_links
        om = Counter(oai_built.stats)
        blueprint_rows.append((openai_math.TITLE, "DECOMPOSED",
                               f"[{om['families']:,} result families](../roadmap/openai-math/README.md), one article "
                               "each, with a block per manuscript and per formalized result."))
        print(
            f"openai-math: {om['families']} families in {om['parts']} subjects, {om['manuscripts']} manuscripts; "
            f"{om['formalized']} families with Lean, {om['statements']} statements, {om['proved']} proved in a file read",
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
        formal_conjectures=fc_data["rev"] if fc_data else None,
        lean_pool=pool[0]["rev"] if pool else None,
        anthropic_flt=aflt[0] if aflt else None,
        cfsg=cfsg_data["rev"] if cfsg_data else None,
        stacks=stacks_data["source"]["rev"] if stacks_data else None,
        atlas=atlas_data["source"]["rev"] if atlas_data else None,
        openai_math=oai_data["source"]["rev"] if oai_data else None,
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
