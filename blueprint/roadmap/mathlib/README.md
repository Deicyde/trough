# Mathlib

Mathlib's maintainers keep four curated lists of what the library contains: an overview of its main concepts, an undergraduate curriculum, Freek Wiedijk's 100 theorems, and the theorems of the 1000+ theorems project. This chapter has one article per concept on those lists that Mathlib has, read at Mathlib commit [9bac2d06](https://github.com/leanprover-community/mathlib4/tree/9bac2d0692944a775113f7c130fd5e5b4608a854) (2026-11-09): 887 articles, 1 of them stated in Mathlib without a proof. Concepts on the lists that are not in Mathlib, 1,157 of them, have no article: the map records what the library contains, not what it may add.

Items that name the same declarations in several lists, or name none and share a title, are one article, placed in the first list that has it; the other lists link to it. An article in Mathlib names its declarations, with their documentation and source; the docstrings and signatures it shows are Mathlib's, under Apache-2.0. One that Mathlib states without a proof says so, and its prerequisites are not mapped.

An article's *Depends on* list names the nearest concepts on these lists that its statement uses, and *Proof depends on* those its proof uses, counting its helper lemmas in the same Mathlib file and, for a lemma from another file, the listed theorems it is proved from there. Both are read from Mathlib's declaration graph by `lean/ConceptDeps.lean` in GitHub Actions; a dependency already reached through another is left out. This leaves 2,130 statement and 1,371 proof edges, from 10,208 and 3,914 nearest-concept edges.

155 articles are written for Trough, under CC BY-SA 4.0: original text, whose citations link to Mathlib's documentation, and prerequisites chosen for the reader: 498 statement and 116 proof edges, in place of the 1,047 and 272 nearest-concept edges Mathlib's graph gives those concepts.

Lean projects outside the libraries mapped here that build on Mathlib have cards in a projects box beside the sections of the overview area they draw on most.

- [Mathlib overview](overview/README.md)
- [Undergraduate mathematics](undergraduate/README.md)
- [Freek Wiedijk's 100 theorems](hundred-theorems/README.md)
- [1000+ theorems](thousand-plus/README.md)
