---
declaration: theorem
origin: cited
lean: TauCeti.dgNerve.quasicategory
statement: formalized
proof: formalized
---

# The differential graded nerve is a quasicategory

every inner horn in it has a filler.

```lean
TauCeti.dgNerve.quasicategory.{v, u} (R : Type v) [CommRing R] (C : Type u)
  [TauCeti.DGCategory R C] : (TauCeti.dgNerve R C).Quasicategory
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.dgNerve.quasicategory`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/DGNerve/Quasicategory.html#TauCeti.dgNerve.quasicategory).

## Sources

- [Tau Ceti documentation: `TauCeti.dgNerve.quasicategory`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/DGNerve/Quasicategory.html#TauCeti.dgNerve.quasicategory)
- [Source of `TauCeti.dgNerve.quasicategory` in TauCeti/AlgebraicTopology/DGNerve/Quasicategory.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/DGNerve/Quasicategory.lean#L241)
- [Tau Ceti roadmap status: Enhanced derived categories of sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EnhancedDerivedSheaves/STATUS.md)
