---
declaration: theorem
origin: cited
lean: TauCeti.MappingPathSpace.isHurewiczFibration_endpoint
statement: formalized
proof: formalized
---

# TauCeti.MappingPathSpace.isHurewiczFibration\_endpoint

The endpoint map of a mapping-path replacement is a Hurewicz fibration, for test spaces in
every universe.

```lean
TauCeti.MappingPathSpace.isHurewiczFibration_endpoint.{w, u', v'} {B : Type u'} {K : Type v'}
  [TopologicalSpace B] [TopologicalSpace K] (f : C(B, K)) :
  TauCeti.IsHurewiczFibration ⇑(TauCeti.MappingPathSpace.endpoint f)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MappingPathSpace.isHurewiczFibration_endpoint`](https://taucetiproject.org/docs/TauCeti/Topology/Homotopy/MappingPath/LiftingFunction.html#TauCeti.MappingPathSpace.isHurewiczFibration_endpoint).

## Sources

- [Tau Ceti documentation: `TauCeti.MappingPathSpace.isHurewiczFibration_endpoint`](https://taucetiproject.org/docs/TauCeti/Topology/Homotopy/MappingPath/LiftingFunction.html#TauCeti.MappingPathSpace.isHurewiczFibration_endpoint)
- [Source of `TauCeti.MappingPathSpace.isHurewiczFibration_endpoint` in TauCeti/Topology/Homotopy/MappingPath/LiftingFunction.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Homotopy/MappingPath/LiftingFunction.lean#L265)
- [Tau Ceti roadmap status: Generalized cohomology, spectra and orientations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeneralizedCohomology/STATUS.md)
