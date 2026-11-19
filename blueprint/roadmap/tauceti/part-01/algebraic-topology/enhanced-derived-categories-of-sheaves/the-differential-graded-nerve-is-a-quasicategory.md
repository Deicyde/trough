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
- [Source of `TauCeti.dgNerve.quasicategory` in TauCeti/AlgebraicTopology/DGNerve/Quasicategory.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/DGNerve/Quasicategory.lean#L241)
- [Tau Ceti roadmap status: Enhanced derived categories of sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EnhancedDerivedSheaves/STATUS.md)
