# Trough

Maps of Lean formalization libraries: what each one formalizes and how its
results depend on one another, not what the library may add. The maps are AutoformBot
vaults, rendered with [AutoformBot](https://github.com/facebookresearch/autoform-bot)
and published at https://deicyde.github.io/trough/. The book shows no Lean
progress: the generated `blueprint/roadmap/README.md` sets `tracks_lean: false`.

`catalog/libraries.toml` lists the 61 libraries trough targets: Mathlib, Tau
Ceti, ATLAS, the research projects with blueprints (Imperial's FLT, PNT+, PFR,
Equational Theories, Strong PNT), Formal Conjectures, Physlib, CSLib,
Foundation, the Analysis I companion, the large corpora (Anthropic's FLT, Lean
Pool, OpenAI Math, Axiom's CFSG) and the 44 Formal Frontier libraries. Each
gets the article unit that suits it, recorded as `map_unit` and `map_plan`.
Mathlib is mapped from its curated lists, Tau Ceti from the declarations its
roadmaps' status files name, and five research projects from their
leanblueprints: Imperial's FLT, PFR, Equational Theories, Strong PNT and PNT+.

## The Mathlib map

Mathlib's maintainers keep four curated lists: `docs/overview.yaml`,
`docs/undergrad.yaml`, `docs/100.yaml` and `docs/1000.yaml`. The map has one
article per concept on them that Mathlib has: its declarations, a module, or a
statement Mathlib states without a proof, whose article says so. Items
naming the same declarations, or the same first declaration, are one article,
placed in the first list that has it (overview, undergraduate, 100, 1000+); the
other lists link to it. An item naming none of these has no article, and its
list's page counts it: the map records what the library contains, not what it
may add.

1. `data/mathlib/yaml/` holds the four lists at the Mathlib commit pinned in
   `lean/lakefile.toml`, and `data/mathlib/source.json` records that commit.
2. The **Mathlib data** workflow (`.github/workflows/mathlib-data.yml`) fetches
   Mathlib's build cache and runs `lean/ConceptDeps.lean` over the whole
   library. For each listed declaration it writes the kind, docstring,
   signature, and the nearest listed declarations its statement and its proof
   use to `data/mathlib/concept-deps.json`. The walk goes through declarations
   on no list by their statements, an instance by its type alone. A proof also
   takes in the proofs of unlisted lemmas from its own file, and for a lemma
   from another file the listed theorems it is proved from there, but no proofs
   further away, which would reach most of the library. A weekly run moves the
   pin to Mathlib's newest master commit whose CI passed.
3. `tools/generate.py` writes the vault, `blueprint/`, from those files,
   `data/thousand-plus.json` (subject classes and Wikipedia pages from the
   [1000+ theorems project](https://1000-plus.github.io/)) and the catalog.
   Edges that would close a cycle become "Informally uses", and a dependency
   already reached through another is left out. Each article's facts (its
   declarations, kind and identity) go in a
   [literature-links](https://github.com/mathlib-initiative/literature-links)
   annotation in `blueprint/links/mathlib/`, not in the page's front matter.
4. The **Pages** workflow checks that the committed pages are what the
   generator writes, runs `autoform check` and `autoform audit`, renders the
   site with the Autoform commit in `.github/autoform-ref`, and deploys it. A
   daily run tries Autoform's newest main commit and pins it once the site
   builds.

## The blueprint chapters

A library with a leanblueprint becomes a chapter with one article per node
that the project has in Lean, following the blueprint's chapters and sections.
A node has an article when the blueprint names its Lean declarations and marks
them formalized, the statement at least, or in Mathlib; any other node only
plans a declaration and has none, and text that refers to it is left unlinked. Each part, chapter and
section is a page that reads in the blueprint's order: its prose, remarks and
examples, smaller units as headings, and each node's card where the node
stands. A labelled display, figure or table shows a number, counted on its
page, and references print it; tables, listings and figure captions are kept.

1. `data/blueprints/<id>/source.json` pins the library's commit, names its
   web entry file and records its node count. `src/` holds the TeX and BibTeX
   files that entry reads, with the repository's `LICENSE`. Strong PNT gives
   no license, so it has `structure.json` instead: titles, labels, Lean
   names, marks and places, but no text.
2. `tools/trough/leanblueprint.py` reads a blueprint the way leanblueprint
   does: the nodes are the theorem-like environments of the kinds in its
   `thms=` option, a node's id is its last `\label`, and a proof belongs to
   the node its `\proves` names or else to the nearest one before it.
   `tools/trough/tex.py` writes the text as Markdown, with each library's
   macros expanded in its own formulas; `tools/trough/bibtex.py` turns its
   citations into author-year labels linked to each work.
3. A node's status follows its marks: `\leanok` makes its statement, or its
   proof, formalized, and `\mathlibok` puts it in Mathlib. A Mathlib node whose first Lean name heads a Mathlib-chapter
   article is that article. `\uses` in a statement go under "Depends on",
   and in a proof under "Proof depends on".
4. AutoformBot looks Lean names up only in this repository, which holds none
   of these libraries' Lean, so `hooks/lean_links.py` links each one to the
   library's documentation instead.
5. The **Blueprint data** workflow refreshes the sources weekly from each
   library's newest commit; `tools/refresh_blueprints.py ID CHECKOUT` does the
   same from a local checkout. PNT+'s blueprint is LeanArchitect output that
   `lake build :blueprint` writes, so the **Blueprint build** workflow builds
   it in CI first and the copy of that output sits in `src/leanarchitect/`. A refresh writes nothing, and the workflow
   fails, when the blueprint names a file its repository lacks, reads to no
   nodes or to under half the last count, or when a library whose text is
   shown loses its license or changes it.

## The Tau Ceti chapter

Tau Ceti's human-written roadmaps live in TauCetiRoadmap, and most carry a
generated `STATUS.md` whose "Named results" and "Notable definitions and
infrastructure" link declarations in Tau Ceti's documentation. A model writes
those files and names at most five results in each, so the chapter maps two
kinds of declaration that Tau Ceti has at the pinned commit: those the statuses
link, and those whose own docstrings name a result. A theorem's docstring names
one when its bold title's head clause, the title before its first qualifier, is
a result named after a person ("Burnside's pᵃqᵇ theorem", "Schur-Weyl duality",
"Serre duality" when another title writes "Serre's"), a phrase of at most six
words ending in "theorem", or at most three words pinned to a textbook theorem
("Global existence (Milne VII, Theorem 9.5)"); a definition counts when its
title names a theorem it carries as data. The four theorems Tau Ceti's website
shows are always in. The rest of a roadmap, its plan, its `Suggested.lean`
signatures and its frontier, says what Tau Ceti may add and is left out, and so
is the status files' prose, which a model writes and Tau Ceti does not check.

The forms of one result in one top-level area, such as "Menger's theorem" and
"Menger's theorem, predicate form", share an article: a declaration a status
names leads its own, otherwise a form the website shows, the form titled by the
result's name alone, or the one with the shortest title. The others are listed
under *Other forms*. Parts follow the library's top-level areas, those with
fewer than ten articles together as *Other Areas*. A roadmap whose status
names a declaration has a section in the part with most of its articles,
holding what the status names and the named results in a module, or else a
folder of modules, where only its status names a declaration; the other named
results have a section for each area of modules, the module's first two levels,
and an area with fewer than three joins its part's *Other results*. An article's
text is its lead's docstring and signature, titled by the docstring's bold
opening, or by the sentence its bold words begin.

1. `tools/refresh_tauceti.py CHECKOUT` writes `data/tauceti/roadmaps.json`
   from a TauCetiRoadmap checkout: each roadmap's title and the names its
   status links in those two sections, nothing else.
2. The **Tau Ceti data** workflow fetches Tau Ceti at the commit
   `data/tauceti/source.json` pins, with its build cache. It runs
   `lean/tauceti/TauCetiSurvey.lean` over every Tau Ceti module, which writes
   each declaration's kind, module and the start of its docstring, and
   `tools/select_tauceti.py` chooses from those (`tools/trough/tauceti_select.py`
   has the rules) into `data/tauceti/selection.json`, with the proposition a
   chosen theorem is stated from when it lives in that proposition's namespace.
3. Then `lean/tauceti/TauCetiDeps.lean` reads the names the statuses give and
   the chosen ones. For each name that resolves it writes the module, kind, line,
   docstring, signature, whether the proof reaches `sorry`, and the nearest mapped
   declarations the statement reaches through unmapped statements and the proof
   through any chain of unmapped Tau Ceti declarations; a name that does not
   resolve is listed as missing and has no article, as is one that now resolves
   outside Tau Ceti. A theorem whose proof reaches `sorry`, itself or through
   another mapped declaration, is recorded as stated, not proved, and its article
   says so; one whose binders take the proposition it is stated from says what it
   assumes.
4. A change to either pin file runs the workflow too, so the committed dump
   always matches the pins. The weekly run, or a dispatch with `newest`, moves both pins: Tau Ceti to
   its newest main commit whose CI passed, so its cache exists, and the
   roadmaps to their newest commit.

## Working on it

    uv run python tools/generate.py           # rewrite blueprint/ from data/ and catalog/
    uv run python tools/generate.py --check   # fail if blueprint/ is stale
    uv run pytest
    uvx --from "git+https://github.com/facebookresearch/autoform-bot.git@$(cat .github/autoform-ref)" autoform check blueprint

A concept can have an authored article in `wiki/mathlib/`: original text in
Markdown and TeX that takes the place of its docstring. An article is two files.
`<name>.md` is the text alone, with no front matter. `<name>.jsonl` holds its
links to Mathlib as [literature-links](https://github.com/mathlib-initiative/literature-links)
annotations, which the folder's `_defaults.json` points at Mathlib:

- The first annotation is about the whole article. Its `id` is the article's
  durable identity, and its object is the concept: the article's first
  declaration, statement or module. An overview section's prose
  (`area:<headings>`) has an empty object and the key in
  `extensions["org.trough"]["concept"]`.
- Every other annotation is a citation. Its subject quotes the cited words in the
  `.md` file (a `generic` end whose location is `{"quote": {"exact": ...}}`, with
  a `prefix` only when the words occur more than once), and its object is the
  declaration they cite. The generator links the words to its documentation.

`tools/split_wiki.py FILE...` writes the two files from an article drafted in one
file, with front matter (`article_id`, `concept`) and `[words](lean:Name)`
citations; run it again after editing an article's text, so its quotes stay the
shortest that work (a test checks this). In the text, `[words](trough:key)` links
another concept's article. Its `## Depends on` and `## Proof depends on` lists take
the place of the edges from Mathlib's declaration graph. The Mathlib data workflow
reads every cited name in Mathlib's environment. The generator stops on a citation
it has no record of or that Mathlib deprecates; on a quote that matches nowhere,
more than once, across paragraphs or over a link; on a `trough:` key with no
article; and on a `lean:` link in the Markdown or a `trough:` link in any other
shape (with a title, a capital scheme, or spaces). The Tests workflow checks the
annotations with `literature-links scan`. A run on main, which may move the Mathlib
pin, repairs instead (`tools/generate.py --follow-pin`): a deprecated citation is
renamed to its replacement, and so is a concept key that no longer has a page; a
citation Mathlib no longer has, or one with no replacement, is dropped and its
words stay plain text; an article whose concept has no page moves, with its
annotations, to `wiki/unplaced/`; and `wiki/pin-changes.json` lists each change so
the articles can be checked again. A name the run's data did not read, from an
article merged meanwhile, is left for the next run.

Everything under `blueprint/roadmap/` and `blueprint/links/` is generated; edit the generator, the
data, the catalog or `wiki/` instead. `tools/refresh_thousand_plus.py` refreshes the
1000+ data from a checkout of `1000-plus/1000-plus.github.io`.

## Licenses

Trough is Apache-2.0 (`LICENSE`). The articles in `wiki/`, by trough's
contributors, are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/),
and so is their text wherever it appears: the generated pages under
`blueprint/roadmap/` and the site, which marks it. Each `data/blueprints/<id>/src/` is
that library's blueprint, under its own license, copied beside it; the
chapters quote it. `data/mathlib/yaml/` comes from
[Mathlib](https://github.com/leanprover-community/mathlib4) (Apache-2.0), and so
do the docstrings and signatures in `data/mathlib/concept-deps.json`, which a
concept with no authored article shows; and
`data/thousand-plus.json` from
[1000-plus](https://github.com/1000-plus/1000-plus.github.io), which is in the
public domain. `data/tauceti/roadmaps.json` comes from
[TauCetiRoadmap](https://github.com/TauCetiProject/TauCetiRoadmap) and the
docstrings and signatures in `data/tauceti/deps.json` from
[Tau Ceti](https://github.com/TauCetiProject/TauCeti), both Apache-2.0.
