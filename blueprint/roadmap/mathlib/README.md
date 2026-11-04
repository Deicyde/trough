# Mathlib

Mathlib's maintainers keep four curated lists of what the library contains: an overview of its main concepts, an undergraduate curriculum, Freek Wiedijk's 100 theorems, and the theorems of the 1000+ theorems project. This chapter has one article per concept on those lists, read at Mathlib commit [1b1ccf4b](https://github.com/leanprover-community/mathlib4/tree/1b1ccf4b088b32fa3f23f2de1127433254a81e1e) (2026-11-02): 2,044 articles, 886 of them in Mathlib and 1,158 not yet.

Items that name the same declarations in several lists, or name none and share a title, are one article, placed in the first list that has it; the other lists link to it. An article in Mathlib names its declarations, with their documentation and source. One that Mathlib lacks is marked not ready, since its prerequisites are not mapped; its page says when Mathlib states it without a proof or another project has formalized it.

An article's *Depends on* list names the nearest concepts on these lists that its statement uses, and *Proof depends on* those its proof uses, counting its helper lemmas in the same Mathlib file and, for a lemma from another file, the listed theorems it is proved from there. Both are read from Mathlib's declaration graph by `lean/ConceptDeps.lean` in GitHub Actions; a dependency already reached through another is left out. This leaves 2,611 statement and 1,508 proof edges, from 11,230 and 4,180 nearest-concept edges.

1 article is written for this wiki: original text, whose citations link to Mathlib's documentation, and prerequisites chosen for the reader.

- [Mathlib overview](overview/README.md)
- [Undergraduate mathematics](undergraduate/README.md)
- [Freek Wiedijk's 100 theorems](hundred-theorems/README.md)
- [1000+ theorems](thousand-plus/README.md)
