---
declaration: def
origin: cited
lean: TauCeti.HasApproximationProperty
statement: formalized
---

# TauCeti.HasApproximationProperty

The identity can be approximated uniformly on every norm-compact set by bounded operators
with finite-dimensional range.

```lean
TauCeti.HasApproximationProperty.{u_1, u_2} (𝕜 : Type u_1) (E : Type u_2)
  [NontriviallyNormedField 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.HasApproximationProperty`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/ApproximationProperty/Basic.html#TauCeti.HasApproximationProperty).

## Sources

- [Tau Ceti documentation: `TauCeti.HasApproximationProperty`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/ApproximationProperty/Basic.html#TauCeti.HasApproximationProperty)
- [Source of `TauCeti.HasApproximationProperty` in TauCeti/Analysis/Normed/Module/ApproximationProperty/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Module/ApproximationProperty/Basic.lean#L45)
- [Tau Ceti roadmap status: Banach space theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BanachSpaceTheory/STATUS.md)
