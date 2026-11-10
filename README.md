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
roadmaps' status files name and the results its docstrings name, five
research projects from their leanblueprints (Imperial's FLT, PFR, Equational
Theories, Strong PNT and PNT+), the Formal Frontier libraries from their
headline results, Formal Conjectures from its problem files, Lean Pool from
its project cards, Anthropic's FLT from the landmark theorems of its proof,
and Axiom's CFSG from its proof's case division and its milestones.

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
"Serre duality" when another title writes "Serre's", "Hille--Yosida for
contraction semigroups"), has "theorem" within its first six words, or is at
most three words pinned to a textbook theorem ("Global existence (Milne VII,
Theorem 9.5)"). A result noun other than theorem, lemma or conjecture counts
only where it ends its phrase and is not a predicate, so "the Serre duality
pairing" and "The Künneth map is an isomorphism" do not. A definition counts
when its title names a theorem it carries as data. The four theorems Tau Ceti's website
shows are always in. The rest of a roadmap, its plan, its `Suggested.lean`
signatures and its frontier, says what Tau Ceti may add and is left out, and so
is the status files' prose, which a model writes and Tau Ceti does not check.

The forms of one result in one area, a module's first two levels under
`TauCeti`, such as "Menger's theorem for fans" and "Menger's theorem for fans,
predicate form", share an article. A declaration a status names leads its own,
and each form no status names joins the one whose title shares the most words
with its own; otherwise the lead is a form the website shows, then one not
titled by names alone ("Perron–Frobenius"), the form titled by the result's
name alone, or the one with the shortest title that is not a Lean name. The
others are listed under *Other forms*. Parts follow the library's top-level areas, those with fewer than ten
articles together as *Other Areas*. A roadmap whose status names a declaration
has a section in the part with most of its articles, holding what the status
names and the named results in a module where only its status names
declarations, or else in a folder of modules below the areas where only it
names two or more; the other named results have a section for each area, and an
area with fewer than three joins its part's *Other results*. An article's text
is its lead's docstring and signature, titled by the docstring's bold opening,
or by the sentence its bold words begin when the rest of that sentence is short
and holds no link.

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

## The Formal Frontier chapter

[Formal Frontier](https://github.com/FormalFrontier) publishes Lean libraries
written by AI agents, 44 of them in the catalog. Each has a
[formalization.yaml](https://github.com/mathlib-initiative/formalization.yaml)
(v0.4) and a README whose "Headline results" section says what it proves. The
chapter has a part per subject, the catalog's `subject` field, and a page per
library: its description, review and automation statements quoted from its
formalization.yaml, the Formal Frontier libraries it builds on and those built
on it, its headline results, and a page listing the main results its
formalization.yaml names. An article is a highlight of the formalization.yaml
whose declarations the scan below finds, or a headline result whose declaration
link names a declaration the scan finds in the linked file. Any other headline
result stays as quoted text on the library's page, and the main results, close
to the whole API in several libraries, are not articles. A library whose
quoted headline results pass 40 KB has them on a page of their own, and a
main-results list of more than 100 rows is split into pages. No Lean runs for
this chapter yet, so its articles have no edges.

1. `tools/refresh_ff.py CHECKOUTS` reads a checkout of each library and writes
   `data/ff/<name>.json`: the commit, the formalization.yaml's facts,
   highlights and main results (`tools/trough/formalization.py`), the Formal
   Frontier libraries its `lake-manifest.json` names, and the README's
   headline results, split as Formal Frontier's
   [dashboard](https://formalfrontier.github.io) splits them but each with its
   whole text as written; an entry that only links into the README or `docs/`
   belongs to a table of contents and is left out.
2. For every declaration those name, `tools/trough/leansource.py` reads the
   named file's source without Lean, with comments, docstrings and strings
   blanked and scopes followed through `namespace`, `section` and `end`. A
   name counts as declared only when a declaration command in that file names
   it in full under the namespaces it sits in, a `private` declaration and
   anything after `#exit` count as not declared, and a file whose scopes don't
   close as they open declares nothing: a name the reading can't place is
   left out rather than guessed. A declaration whose text in the file holds
   `sorry` (or `sorryAx`, `admit`, a `stop` tactic) is recorded as stated
   without proof, and its article says so. Each
   article's Lean name links its line in the library's source at the pin.
3. The **Formal Frontier data** workflow (`.github/workflows/ff-data.yml`)
   fetches each library at the commit its data file pins, as a blobless
   sparse checkout of the files the refresh reads, runs the refresh,
   regenerates the pages and runs the tests; on a pull request it fails when
   the committed data differ from what the pins give. The weekly run, or a
   dispatch with `newest`, moves each pin to its library's newest commit. A
   refresh writes nothing, and the workflow fails, when a library is not
   Apache-2.0 or its record finds under half the declarations the last one
   found.

## The Formal Conjectures chapter

[Formal Conjectures](https://github.com/google-deepmind/formal-conjectures),
from Google DeepMind, states open and solved problems in Lean, a file per
problem in a folder per source: Erdős problems, OEIS, Wikipedia, papers and
others. Every statement carries one `category` attribute (research open,
research solved, textbook, API or test), most carry `AMS` subject codes, and
some `formal_proof` links to proofs elsewhere. The chapter has a part per source
folder, the Erdős problems in sections by hundreds, an article per problem file
that states a research or textbook statement, and in it a card per such
statement: whether it is open, solved with or without a proof elsewhere, or
proved here, its docstring, its Lean statement and its line in the source. Test
and API statements are counted in their problem's article, not shown, and a
file that states neither kind has no article. Two indexes link the articles: a
page per top-level AMS subject, and a page per FC100 list, Formal Conjectures'
benchmark sets. No Lean runs for this chapter, so its articles have no edges.

1. `tools/refresh_formal_conjectures.py CHECKOUT` reads a checkout and writes
   `data/formal-conjectures/source.json`, the commit, and `problems.json`: each
   problem file's title and module docstring, its research and textbook
   statements, its counts of test and API statements, the FC100 lists, and the
   names Formal Conjectures gives the AMS codes.
2. `tools/trough/leansource.py` reads each file as it does for Formal Frontier,
   and gives each declaration what is written before it: its docstring and the
   attributes of its `@[...]` list, which may span lines. A statement is a named
   declaration whose list holds one category; its Lean statement runs to the
   `:=` (or `where`) that starts its proof, and it is proved here when the text
   from there on holds no `sorry`, which, like Formal Conjectures' own
   `hasSorryFreeProof`, says nothing of the statements that proof uses. A
   statement with no name, an `example`, or a `private` one is left out, as
   Formal Conjectures' site leaves them out.
3. The **Formal Conjectures data** workflow (`.github/workflows/fc-data.yml`)
   fetches the repository at the commit `source.json` pins, as a blobless
   sparse checkout of the files the refresh reads, runs the refresh,
   regenerates the pages and runs the tests; on a pull request it fails when
   the committed data differ from what the pin gives. The weekly run, or a
   dispatch with `newest`, moves the pin to the newest main commit whose build
   passed. A refresh writes nothing, and the workflow fails, when the repository
   is not Apache-2.0, when its checkout gives no AMS subject names or lacks a
   file the commit lists, when a declaration with a category does not read (its
   attributes don't, it has two categories or no `:=`, or its file's scopes
   don't close), naming each, or when it keeps under half the statements the
   last record kept.

## The Lean Pool chapter

[Lean Pool](https://github.com/LeanPool/lean-pool) keeps Lean projects outside
Mathlib's scope, each in a directory of its own under `LeanPool/` with a card,
`LeanPool/projects/<slug>.yaml`: its title, summary, authors, sources, license,
provenance, MSC2020 codes and main results, each a declaration with an informal
statement. The chapter has a section per top-level MSC2020 class, the class of
the first code a card lists, titled by its MSC2020 name, and an article per
card, titled by the card's title. An article quotes the card's summary, names
the project's authors, links its sources (DOI, then arXiv, then URL, then a
paper, manuscript, proof or problem page the card links), with the card's
citation, mathematical source, background and notes on them, and its own
repository at the commit the card gives, says who wrote its Lean proofs as the
card's provenance does in Lean Pool's words, gives its license, quoting the
copyright line or note Lean Pool's notice file keeps for a project published
under MIT, and lists its main results: each informal statement quoted, with its
declaration linked to Lean Pool's
[documentation](https://leanpool.github.io/lean-pool/) and to its line at the
pin when the scan below finds it. A main result the scan does not find keeps
its statement and says so. The articles show no Lean signatures and have no
edges, which need Lean, and no Lean runs for this chapter.

1. `tools/refresh_lean_pool.py CHECKOUT` reads a checkout of Lean Pool and
   writes `data/lean-pool/source.json`, the commit with its Lean toolchain and
   Mathlib, and `data/lean-pool/projects.json`, the cards with the notes its
   `NOTICE.extra.yml` keeps for MIT projects. For each main result it looks for
   the declaration in the project's `.lean` files with `tools/trough/leansource.py`,
   as the Formal Frontier chapter does, and records its module, line and kind
   and whether its text holds `sorry`; a name declared in two of the project's
   files is left out, since the project imports all of them together and Lean
   would refuse it. Lean Pool's CI checks that each card's main declarations
   exist, so a main declaration the scan misses is a gap in the scan.
2. The **Lean Pool data** workflow (`.github/workflows/lean-pool-data.yml`)
   fetches Lean Pool at the commit `data/lean-pool/source.json` pins, as a
   blobless sparse checkout of the cards and the `.lean` files, runs the
   refresh, regenerates the pages and runs the tests; on a pull request it
   fails when the committed data differ from what the pin gives. The weekly
   run, or a dispatch with `newest`, moves the pin to Lean Pool's newest main
   commit whose Lean CI passed. A refresh writes nothing, and the workflow
   fails, when Lean Pool is not Apache-2.0, a card lacks what the chapter reads,
   has a license other than Apache-2.0 or MIT or names an entry module the
   checkout lacks, or the scan places under half the main results the last
   record placed.

## The Anthropic FLT chapter

[anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem),
by Anthropic, states that it is a Lean proof of Fermat's Last Theorem along the
route of Frey, Serre, Ribet, Wiles and Taylor-Wiles, derived in part from
Imperial's FLT project, flt-regular and Mathlib. Its `PROOF-PATH.md` describes
the route in six steps and a section on the exact strength of the named steps,
and the data of its web pages list its 29,511 theorems, mark 49 of them as
landmarks and give the citation graph. The chapter has a part per step, quoting
it, with an article for each landmark the web pages place there: its Lean
statement, its aliases and a link to its line at the pinned commit, and under
"Proof depends on" the landmarks its proof reaches. The other theorems are
counted, not mapped, and the web pages' English titles and summaries are left
out, as the repository says they are generated and their references not
individually verified. No Lean runs: the chapter records what the repository
states.

1. `tools/refresh_anthropic_flt.py CHECKOUT` writes `data/anthropic-flt/source.json`
   (the commit, the formalization.yaml's facts and PROOF-PATH.md's steps) and
   `landmarks.json`. A landmark's stage and aliases come from `html/data/meta.js`;
   its statement is the text of its `Theorems/Thm_X_y.lean` from the end of the
   imports and `attribute` lines to the top-level `:=`; and the landmarks its
   proof reaches are the nearest ones in `html/data/edges.js`, the import lines
   of the proof modules, passing only through theorems that are not landmarks. A
   theorem a step opens with, when the web pages place it in that step, takes
   the step's name as its title; the web pages put `fermat_last_theorem` in a
   stage before the first step, so it opens part 1. The section on the exact
   strength of the named steps is quoted by its "Proved:" clauses, cut with …
   where the text goes on, and by its entries that say neither what is proved
   nor what is not, whole: the map records what the repository proves, not what
   it leaves out.
2. Where a landmark's name, or another declaration its statement file makes, is
   also a Lean name in the Imperial FLT chapter, its article links that article.
   The names are compared as written.
3. The **Anthropic FLT data** workflow (`.github/workflows/anthropic-flt-data.yml`)
   fetches the repository at the pinned commit, as a blobless sparse checkout of
   the files the refresh reads, runs the refresh, regenerates the pages and runs
   the tests; on a pull request it fails when the committed data differ from
   what the pin gives. The weekly run, or a dispatch with `newest`, moves the
   pin to the repository's newest commit. The articles link the repository's
   documentation site only when the run finds that the site serves the
   landmarks' pages; when the site does not answer at all, the last record's
   link stays. A refresh writes nothing, and the workflow fails, when the
   repository is not Apache-2.0, a file the refresh reads is missing from the
   checkout, a landmark's statement file states another theorem or may be cut
   short, or the landmarks drop under half the last count.

## The CFSG chapter

[AxiomMath/CFSG](https://github.com/AxiomMath/CFSG), by Axiom Math, is a Lean
proof of the classification of finite simple groups, built on Mathlib and Tau
Ceti, whose statement of the classification it uses. Its code has no docstrings
outside `CFSG/ThirdParty/`, so the chapter follows the proof as the Lean writes
it and titles its articles by Lean names. `CFSG/Statement.lean` states the
classification; its proof applies `CFSG.Assembly.classification` to the catalog
of simple groups and to a theorem for each case of a case division that
`CFSG/Assembly/Reduction.lean` defines, a proposition per case. The first part
has an article for the top theorem, one for the reduction, with the case
propositions' definitions, and one per case: what it asserts, the theorem that
proves it and the milestones its file reaches. The second part has an article
per milestone module, the results the authors single out directly under
`CFSG/Milestones/`: each declaration's Lean statement, its line in the source
and whether its proof holds `sorry`. The front page quotes the README and the
facts and main results of its formalization.yaml, and counts the files and
theorems of the largest folders. The top theorem depends on the reduction and
the cases, as its proof names them; every other edge means that one case or
milestone file imports another's, directly or not, through no other case or
milestone file, and imports of the file that declares the catalog are left out.
Where a statement writes out the name of a declaration with an article in the
Tau Ceti chapter, the article links it.

1. `tools/refresh_cfsg.py CHECKOUT` reads a checkout and writes
   `data/cfsg/source.json`, the commit, its date, toolchain, Mathlib and Tau
   Ceti, and `proof.json`: the top theorem and the catalog, the reduction's
   declarations, each case with its proposition and theorem, each milestone
   module's declarations, the case and milestone files each such file
   imports, directly or not, through no other, the main results, the facts of
   formalization.yaml, the README's opening and the files and theorems of each
   folder. It reads every Lean file but the certificates, which it counts.
2. `tools/trough/leansource.py` reads each file as it does for Formal Frontier.
   The top theorem's proof is read as a function and its arguments: the
   reduction, the catalog, a theorem per hypothesis of the reduction, in its
   order, and the group. The repository cannot be built in CI: its README says
   a build takes most of a day, with changes to Lake.
3. The **CFSG data** workflow (`.github/workflows/cfsg-data.yml`) fetches the
   repository at the commit `source.json` pins, as a blobless sparse checkout
   of every Lean file but the certificates, runs the refresh, regenerates the
   pages and runs the tests; on a pull request it fails when the committed data
   differ from what the pin gives. The weekly run, or a dispatch with `newest`,
   moves the pin to the newest main commit. A refresh writes nothing, and the
   workflow fails, when the repository is not Apache-2.0, lacks a file the
   commit lists, or when the top theorem, the reduction, a case or a main
   result is not found where it should be, a milestone module's scopes don't
   close, or the milestones drop under half the last count.

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
[Tau Ceti](https://github.com/TauCetiProject/TauCeti), both Apache-2.0. The
text quoted in `data/ff/` comes from the formalization.yaml and README of each
[Formal Frontier](https://github.com/FormalFrontier) library, Apache-2.0. The
docstrings and Lean statements in `data/formal-conjectures/` come from
[Formal Conjectures](https://github.com/google-deepmind/formal-conjectures)
(Google DeepMind), Apache-2.0; Formal Conjectures asks that its Erdős
problems' docstrings follow [erdosproblems.com](https://www.erdosproblems.com).
The text in `data/lean-pool/` comes from the project cards and
`NOTICE.extra.yml` of [Lean Pool](https://github.com/LeanPool/lean-pool),
Apache-2.0; each article names its project's authors.
The text quoted in `data/anthropic-flt/` comes from the PROOF-PATH.md,
formalization.yaml and `Theorems/` files of
[anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem),
Apache-2.0.
The README text and Lean source in `data/cfsg/` come from
[Axiom Math's CFSG](https://github.com/AxiomMath/CFSG), Apache-2.0.
