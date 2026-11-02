# Mathlib

Mathlib's maintainers keep four curated lists of what the library contains: an overview of its main concepts, an undergraduate curriculum, Freek Wiedijk's 100 theorems, and the theorems of the 1000+ theorems project. This chapter has one article per concept on those lists, read at Mathlib commit [1b1ccf4b](https://github.com/leanprover-community/mathlib4/tree/1b1ccf4b088b32fa3f23f2de1127433254a81e1e) (2026-11-02): 2,054 articles, 886 of them in Mathlib and 1,168 not yet.

Items that name the same declarations in several lists, or name none and share a title, are one article, placed in the first list that has it; the other lists link to it. An article in Mathlib names its declarations, with their documentation and source. One that Mathlib lacks is marked not ready: its statement and prerequisites are still to be written.

An article's *Depends on* list names the nearest concepts on these lists that its statement uses, and *Proof depends on* those its proof uses, read from Mathlib's declaration graph by `lean/ConceptDeps.lean` in GitHub Actions; a dependency already reached through another is left out. This leaves 2,942 statement and 4,178 proof edges, from 14,172 and 17,784 nearest-concept edges.

- [Mathlib overview](overview/README.md)
- [Undergraduate mathematics](undergraduate/README.md)
- [Freek Wiedijk's 100 theorems](hundred-theorems/README.md)
- [1000+ theorems](thousand-plus/README.md)
