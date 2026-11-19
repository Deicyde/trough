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
blueprint/coverage/README.md, blueprint/sources/README.md, the declaration
ledgers under blueprint/sources/ (JSON files) and hooks/lean-links.json; a stale
file under blueprint/roadmap/ or blueprint/links/, or a stale ledger, is deleted.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from collections import Counter

from trough import aesop, anthropic_flt, atlas, batteries, blueprints, catalog, cfsg, comppoly, cslib, ff, formal_conjectures, lean_pool, links, mathlib, openai_math, physlib, satellites, stacks, tauceti, wiki
from trough.vault import Container, Leaf, assign_paths, render_container, render_tree, walk

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
    # The page of each live chapter, by catalog id, where a satellite project that requires its library goes.
    hosts: dict[str, Container] = {}
    projects = blueprints.load_projects(DATA, libraries)
    imperial = None
    for project in projects:
        built = blueprints.chapter(project, blueprints.load_blueprint(project), heads)
        assign_paths(built.root, ROADMAP / project.id)
        hosts[project.id] = built.root
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
        hosts["tauceti"] = tau_root
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
        hosts.update(ff_built.targets)
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
        hosts["formal-conjectures"] = fc_built.root
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
        hosts["lean-pool"] = pool_root
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
        hosts["anthropic-flt"] = aflt_built.root
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
        hosts["cfsg"] = cfsg_built.root
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
        hosts["stacks"] = stacks_built.root
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
        hosts["atlas-lean"] = atlas_built.root
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
        hosts["openai-math"] = oai_built.root
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
    cslib_data = cslib.load(DATA)
    if cslib_data:
        cslib_built, cslib_links = cslib.chapter(cslib_data)
        assign_paths(cslib_built.root, ROADMAP / "cslib")
        hosts["cslib"] = cslib_built.root
        blueprints.resolve(cslib_built, VAULT)
        files.update(render_tree(cslib_built.root, VAULT))
        files.update({VAULT / path: text for path, text in cslib_built.files.items()})
        chapters["cslib"] = "cslib/README.md"
        lean_links["cslib"] = cslib_links
        cs = Counter(cslib_built.stats)
        blueprint_rows.append(("CSLib", "INVENTORIED",
                               f"[{cs['articles']:,} modules](../roadmap/cslib/README.md), one article each, with a "
                               "block per public declaration."))
        print(
            f"cslib: {cs['articles']} module articles in {cs['folders']} folders and {cs['parts']} parts; "
            f"{cs['declarations']} public declarations, {cs['documented']} documented, {cs['sorry']} holding sorry; "
            f"{cs['statement_edges']} statement and {cs['proof_edges']} proof edges",
            file=sys.stderr,
        )
    # The libraries trough.library reads with their modules that declare nothing public listed.
    readers = []
    for reader in (batteries, aesop, comppoly):
        lib = reader.LIBRARY
        reader_data = reader.load(DATA)
        if not reader_data:
            continue
        reader_built, reader_links = reader.chapter(reader_data)
        assign_paths(reader_built.root, ROADMAP / lib.id)
        blueprints.resolve(reader_built, VAULT)
        files.update(render_tree(reader_built.root, VAULT))
        files.update({VAULT / path: text for path, text in reader_built.files.items()})
        chapters[lib.id] = f"{lib.id}/README.md"
        lean_links[lib.id] = reader_links
        if lib.id == satellites.CORE_HOME:
            hosts[lib.id] = reader_built.root
        readers.append((lib.id, lib.name, lib.repo, reader_data["rev"], bool(reader_data.get("mathlib"))))
        rs = Counter(reader_built.stats)
        blueprint_rows.append((lib.name, "INVENTORIED",
                               f"[{rs['articles']:,} modules](../roadmap/{lib.id}/README.md), one article each, with a "
                               f"block per public declaration; {rs['listed']:,} modules that declare nothing public by "
                               "name are listed on their folders' pages"
                               + (f", and {rs['unbuilt']:,} that did not build on the front page" if rs["unbuilt"] else "")
                               + "."))
        print(
            f"{lib.id}: {rs['articles']} module articles in {rs['folders']} folders and {rs['parts']} parts, "
            f"{rs['listed']} modules listed"
            + (f", {rs['unbuilt']} unbuilt" if rs["unbuilt"] else "")
            + f"; {rs['declarations']} public declarations, {rs['documented']} documented, "
            f"{rs['sorry']} holding sorry; {rs['statement_edges']} statement and {rs['proof_edges']} proof edges",
            file=sys.stderr,
        )
    physlib_data = physlib.load(DATA)
    if physlib_data:
        physlib_built, physlib_links = physlib.chapter(physlib_data, tau_root)
        assign_paths(physlib_built.root, ROADMAP / "physlib")
        blueprints.resolve(physlib_built, VAULT)
        files.update(render_tree(physlib_built.root, VAULT))
        chapters["physlib"] = "physlib/README.md"
        hosts["physlib"] = physlib_built.root
        lean_links["physlib"] = physlib_links
        ph = Counter(physlib_built.stats)
        blueprint_rows.append((physlib.TITLE, "DECOMPOSED",
                               f"[{ph['articles']:,} modules](../roadmap/physlib/README.md) with a declaration, one "
                               "article each, with a block per declaration."))
        print(
            f"physlib: {ph['articles']} module articles on {ph['pages']} folder pages in {ph['parts']} parts; "
            f"{ph['declarations']} declarations ({ph['instances']} instances with no name, {ph['documented']} "
            f"documented, {ph['significant']} significant, {ph['sorry']} with sorry), {ph['private']} private not shown, "
            f"{ph['unresolved']} not in Lean; {ph['unshown']} modules without an article; {ph['statement_edges']} "
            f"statement and {ph['proof_edges']} proof edges",
            file=sys.stderr,
        )
    sat_records, sat_packages, sat_overrides = satellites.load(DATA)
    sat_stats = None
    if sat_records:
        overview = chapter.entries[0].node
        areas = {f"mathlib:{area.slug}": area for area in overview.children if isinstance(area, Container)}
        names: dict[str, Leaf] = {}
        for root in {id(host): host for host in hosts.values()}.values():
            for node in walk(root):
                if isinstance(node, Leaf):
                    for name in dict(node.fields).get("lean", "").split(", "):
                        if name:
                            names.setdefault(name, node)
        pages, sat_stats, sat_targets = satellites.chapter(
            sat_records, sat_packages, sat_overrides, libraries, areas | {satellites.OVERVIEW: overview} | hosts,
            heads, names)
        for host, projects_page, _ in pages:
            if any(child.slug == "projects" for child in host.children):
                raise ValueError(f"{host.path}: a child named projects is in the way of its satellite projects")
            assign_paths(projects_page, host.path.parent / "projects")
        for host, projects_page, names_here in pages:
            blueprints.resolve(blueprints.Built(projects_page, sat_targets, {}, {}, Counter()), VAULT)
            files.update(render_tree(projects_page, VAULT))
            if names_here:
                lean_links[projects_page.path.parent.relative_to(ROADMAP).as_posix()] = dict(sorted(names_here.items()))
            satellites.attach(host, projects_page)
        if any(host.path.is_relative_to(ROADMAP / "mathlib") for host, _, _ in pages):
            chapter.prose += ("\n\nLean projects outside the libraries mapped here that build on Mathlib have cards in a "
                              "projects box beside the sections of the overview area they draw on most.")
            pages.append((chapter, None, None))
        for host in {id(host): host for host, _, _ in pages}.values():
            # The host's page, again, now that it lists its projects page; Mathlib's pages keep their facts in
            # annotations.
            previous = host.path.read_text(encoding="utf-8") if host.path.is_file() else None
            files[host.path] = render_container(host, VAULT, previous, not host.path.is_relative_to(ROADMAP / "mathlib"))
        boxes = ", ".join(f"[{page.title}](../roadmap/{page.path.relative_to(ROADMAP).as_posix()})"
                          for _, page, _ in pages if page is not None and page.children)
        blueprint_rows.append((
            "Satellite projects", "DECOMPOSED",
            f"{sat_stats['cards']} project cards by their main results and {sat_stats['module_nodes']} by their root "
            f"modules, each in a projects box on the page of the library it builds on ({boxes}); "
            f"{sat_stats['listed']} more listed there without a named main result or a root module of their own"
            + (f"; {sat_stats['held_back']} held back, as they build on neither Mathlib nor a library mapped here"
               if sat_stats["held_back"] else "") + "."))
        print(
            f"satellites: {sat_stats['cards']} cards of {sat_stats['admitted']} admitted projects "
            f"({sat_stats['projects']} read) in {sat_stats['homes']} homes; {sat_stats['without_headline']} without "
            f"a headline: {sat_stats['module_nodes']} root-module cards ({sat_stats['module_proved']} with proof), "
            f"{sat_stats['listed']} listed; {sat_stats['held_back']} held back; headlines by blueprint {sat_stats['rule_blueprint']}, "
            f"README {sat_stats['rule_readme']}, Main module {sat_stats['rule_main']}; {sat_stats['statement_edges']} "
            f"statement, {sat_stats['proof_edges']} proof and {sat_stats['satellite_edges']} project edges; "
            f"{sat_stats['mathlib_edges']} cards with Mathlib edges",
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
        cslib=cslib_data["rev"] if cslib_data else None,
        readers=readers,
        physlib=physlib_data["source"]["rev"] if physlib_data else None,
        satellites=sat_stats["projects"] if sat_stats else None,
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
    # The generated files under sources/ are the module catalogs' declaration ledgers, JSON files.
    return (set(ROADMAP.rglob("*.md")) | {path for path in LINKS.rglob("*") if path.is_file()}
            | set((VAULT / "sources").rglob("*.json")))


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
