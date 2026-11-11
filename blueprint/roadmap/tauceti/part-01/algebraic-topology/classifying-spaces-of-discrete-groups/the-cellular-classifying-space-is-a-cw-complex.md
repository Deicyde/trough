---
declaration: instance
origin: cited
lean: TauCeti.instCWComplexCellularClassifyingSpace
statement: formalized
---

# The cellular classifying space is a CW complex

Its cells are those of the presentation
complex, one `0`-cell, one `1`-cell for each generator and one `2`-cell for each relator, together
with the cells of dimension at least `3` attached to kill the higher homotopy groups
(`TauCeti.killHomotopyGroupsCWComplexCellEquiv`).

```lean
TauCeti.instCWComplexCellularClassifyingSpace.{u} {S : Type u} (R : Set (FreeGroup S)) :
  Topology.CWComplex Set.univ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Seifert--van Kampen theorem for a family with a common pairwise intersection](../fundamental-group/the-seifert-van-kampen-theorem-for-a-family-with.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.instCWComplexCellularClassifyingSpace`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/Cellular.html#TauCeti.instCWComplexCellularClassifyingSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.instCWComplexCellularClassifyingSpace`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/Cellular.html#TauCeti.instCWComplexCellularClassifyingSpace)
- [Source of `TauCeti.instCWComplexCellularClassifyingSpace` in TauCeti/AlgebraicTopology/ClassifyingSpace/Cellular.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/ClassifyingSpace/Cellular.lean#L205)
- [Tau Ceti roadmap status: Classifying spaces of discrete groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ClassifyingSpaces/STATUS.md)
