# Trough

Maps of Lean formalization libraries: what each one formalizes, how its results
depend on one another, and what is still missing. The maps are AutoformBot
vaults, rendered with [AutoformBot](https://github.com/facebookresearch/autoform-bot)
and published at https://deicyde.github.io/trough/.

`catalog/libraries.toml` lists the 61 libraries trough targets: Mathlib, Tau
Ceti, ATLAS, the research projects with blueprints (Imperial's FLT, PNT+, PFR,
Equational Theories, Strong PNT), Formal Conjectures, Physlib, CSLib,
Foundation, the Analysis I companion, the large corpora (Anthropic's FLT, Lean
Pool, OpenAI Math, Axiom's CFSG) and the 44 Formal Frontier libraries. Each
gets the article unit that suits it, recorded as `map_unit` and `map_plan`.
Mathlib is mapped from its curated lists, and five research projects from
their leanblueprints: Imperial's FLT, PFR, Equational Theories, Strong PNT and
PNT+.

## The Mathlib map

Mathlib's maintainers keep four curated lists: `docs/overview.yaml`,
`docs/undergrad.yaml`, `docs/100.yaml` and `docs/1000.yaml`. The map has one
article per concept on them. Items naming the same declarations, or the same
first declaration, are one article, placed in the first list that has it
(overview, undergraduate, 100, 1000+); the other lists link to it. An item
naming no declaration is an article marked not ready, shared with any item of
the same title in another list.

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
   already reached through another is left out.
4. The **Pages** workflow checks that the committed pages are what the
   generator writes, runs `autoform check` and `autoform audit`, renders the
   site with the Autoform commit in `.github/autoform-ref`, and deploys it. A
   daily run tries Autoform's newest main commit and pins it once the site
   builds.

## The blueprint chapters

A library with a leanblueprint becomes a chapter with one article per node,
following the blueprint's chapters and sections. Each part, chapter and
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
   proof, formalized, `\mathlibok` puts it in Mathlib, and `\notready` marks
   it not ready. A Mathlib node whose first Lean name heads a Mathlib-chapter
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

## Working on it

    uv run python tools/generate.py           # rewrite blueprint/ from data/ and catalog/
    uv run python tools/generate.py --check   # fail if blueprint/ is stale
    uv run pytest
    uvx --from "git+https://github.com/facebookresearch/autoform-bot.git@$(cat .github/autoform-ref)" autoform check blueprint

A concept can have an authored article in `wiki/mathlib/`: original text in
Markdown and TeX that takes the place of its docstring. Its front matter names
the concept (`concept:`, the article's first declaration, or
`<list>:<item key>` for one Mathlib lacks; `area:<headings>` gives a section of
the overview its prose) and a durable `article_id`. In the text,
`[words](lean:Full.Name)` cites a Mathlib declaration and becomes a link to its
documentation, and `[words](trough:key)` links another concept's article. Its
`## Depends on` and `## Proof depends on` lists take the place of the edges
from Mathlib's declaration graph. The Mathlib data workflow reads every cited
name in Mathlib's environment and fails on one that does not resolve or that
Mathlib deprecates.

Everything under `blueprint/roadmap/` is generated; edit the generator, the
data, the catalog or `wiki/` instead. `tools/refresh_thousand_plus.py` refreshes the
1000+ data from a checkout of `1000-plus/1000-plus.github.io`.

## Licenses

Trough is Apache-2.0 (`LICENSE`). Each `data/blueprints/<id>/src/` is
that library's blueprint, under its own license, copied beside it; the
chapters quote it. `data/mathlib/yaml/` comes from
[Mathlib](https://github.com/leanprover-community/mathlib4) (Apache-2.0), and so
do the docstrings and signatures in `data/mathlib/concept-deps.json`, which a
concept with no authored article shows; and
`data/thousand-plus.json` from
[1000-plus](https://github.com/1000-plus/1000-plus.github.io), which is in the
public domain.
