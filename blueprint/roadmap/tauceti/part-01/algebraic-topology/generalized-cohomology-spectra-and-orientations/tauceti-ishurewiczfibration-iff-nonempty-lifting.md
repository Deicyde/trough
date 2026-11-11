---
declaration: theorem
origin: cited
lean: TauCeti.isHurewiczFibration_iff_nonempty_liftingFunction
statement: formalized
proof: formalized
---

# TauCeti.isHurewiczFibration_iff_nonempty_liftingFunction

A map is a Hurewicz fibration for test spaces in `Type (max u v)` if and only if it has a
lifting function.

```lean
TauCeti.isHurewiczFibration_iff_nonempty_liftingFunction.{u, v} {E : Type u} {B : Type v}
  [TopologicalSpace E] [TopologicalSpace B] {p : C(E, B)} :
  TauCeti.IsHurewiczFibration ⇑p ↔ Nonempty (TauCeti.LiftingFunction p)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isHurewiczFibration_iff_nonempty_liftingFunction`](https://taucetiproject.org/docs/TauCeti/Topology/Homotopy/MappingPath/LiftingFunction.html#TauCeti.isHurewiczFibration_iff_nonempty_liftingFunction).

## Sources

- [Tau Ceti documentation: `TauCeti.isHurewiczFibration_iff_nonempty_liftingFunction`](https://taucetiproject.org/docs/TauCeti/Topology/Homotopy/MappingPath/LiftingFunction.html#TauCeti.isHurewiczFibration_iff_nonempty_liftingFunction)
- [Source of `TauCeti.isHurewiczFibration_iff_nonempty_liftingFunction` in TauCeti/Topology/Homotopy/MappingPath/LiftingFunction.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Homotopy/MappingPath/LiftingFunction.lean#L170)
- [Tau Ceti roadmap status: Generalized cohomology, spectra and orientations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeneralizedCohomology/STATUS.md)
