---
declaration: corollary
origin: cited
lean: Rep.periodicCohomology, periodicTateCohomology
statement: formalized
proof: formalized
---

# periodic cohomology

Let $G$ be a finite cyclic group. For all $n > 0$ and all representations $M$ we have an isomorphism $H^{n}(G,M) \cong H^{n+2}(G,M)$. Similarly for all integers $n$ we have isomorphisms $H^{n}_{\mathrm{Tate}}(G,M) \cong H^{n+2}_{\mathrm{Tate}}(G,M)$.

## Depends on

- [Tate up down isos](../dimension-shifting/cor-tate-up-down-isos.md)
- [up iso down](def-up-iso-down.md)

## Proof

By the dimension-shifting isomorphisms we have $H^{n}(G,M) \cong H^{n+1}(G,\mathrm{down}(M)) \cong H^{n+1}(G,\mathrm{up}(M)) \cong H^{n+2}(G,M)$, and similarly for Tate cohomology.

## Lean

Formalized as [`Rep.periodicCohomology`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.periodicCohomology), [`periodicTateCohomology`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/periodicTateCohomology).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 1591](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L1591)
