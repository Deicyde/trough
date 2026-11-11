---
declaration: def
origin: cited
lean: TauCeti.dgNerve.homotopyCategoryEquiv
statement: formalized
---

# The homotopy category of the differential graded nerve

**The homotopy category of the differential graded nerve** is the homotopy category `H⁰(C)` of
the differential graded category. The equivalence is an isomorphism of categories: its functor is
the canonical functor `TauCeti.dgNerve.toHomotopyCategory`, its inverse is
`TauCeti.dgNerve.fromHomotopyCategory`, and both composites are identities.

```lean
TauCeti.dgNerve.homotopyCategoryEquiv.{v, u} (R : Type v) [CommRing R] (C : Type u)
  [TauCeti.DGCategory R C] : TauCeti.DGHomotopyCategory R C ≌ (TauCeti.dgNerve R C).HomotopyCategory
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.dgNerve.homotopyCategoryEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/DGNerve/HomotopyCategory.html#TauCeti.dgNerve.homotopyCategoryEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.dgNerve.homotopyCategoryEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/DGNerve/HomotopyCategory.html#TauCeti.dgNerve.homotopyCategoryEquiv)
- [Source of `TauCeti.dgNerve.homotopyCategoryEquiv` in TauCeti/AlgebraicTopology/DGNerve/HomotopyCategory.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/DGNerve/HomotopyCategory.lean#L326)
- [Tau Ceti roadmap status: Enhanced derived categories of sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EnhancedDerivedSheaves/STATUS.md)
