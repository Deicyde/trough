---
declaration: def
origin: cited
lean: IsQuotientCoveringMap.cwComplexQuotient
statement: formalized
---

# The orbit space of a free cellular action is a CW complex

Let `p : E → B` be the quotient
covering map of an action of `G` on the Hausdorff CW complex `E` that carries every open `n`-cell
onto an open `n`-cell, and carries an open cell onto itself only by `1`. Then `B` is a CW complex
whose `n`-cells are the `G`-orbits of `n`-cells of `E`
(`IsQuotientCoveringMap.cellQuotientEquiv`). The characteristic map of an orbit is `p ∘ φ`, for
`φ` the characteristic map of the chosen representative of the orbit
(`IsQuotientCoveringMap.map_cellQuotientEquiv_symm`).

```lean
IsQuotientCoveringMap.cwComplexQuotient.{u, u_1} {E : Type u} [TopologicalSpace E] {G : Type u_1}
  {B : Type u} [TopologicalSpace B] [Topology.CWComplex Set.univ] [Group G] [MulAction G E]
  [T2Space E] {p : E → B} (hp : IsQuotientCoveringMap p G)
  (hcell :
    ∀ (g : G) (n : ℕ) (i : Topology.RelCWComplex.cell Set.univ n),
      ∃ j, g • Topology.RelCWComplex.openCell n i = Topology.RelCWComplex.openCell n j)
  (hfree :
    ∀ (g : G) (n : ℕ) (i : Topology.RelCWComplex.cell Set.univ n),
      g • Topology.RelCWComplex.openCell n i = Topology.RelCWComplex.openCell n i → g = 1) :
  Topology.CWComplex Set.univ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsQuotientCoveringMap.cwComplexQuotient`](https://taucetiproject.org/docs/TauCeti/Topology/CWComplex/Classical/OrbitSpace.html#IsQuotientCoveringMap.cwComplexQuotient).

## Sources

- [Tau Ceti documentation: `IsQuotientCoveringMap.cwComplexQuotient`](https://taucetiproject.org/docs/TauCeti/Topology/CWComplex/Classical/OrbitSpace.html#IsQuotientCoveringMap.cwComplexQuotient)
- [Source of `IsQuotientCoveringMap.cwComplexQuotient` in TauCeti/Topology/CWComplex/Classical/OrbitSpace.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/CWComplex/Classical/OrbitSpace.lean#L282)
- [Tau Ceti roadmap status: Classifying spaces of discrete groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ClassifyingSpaces/STATUS.md)
