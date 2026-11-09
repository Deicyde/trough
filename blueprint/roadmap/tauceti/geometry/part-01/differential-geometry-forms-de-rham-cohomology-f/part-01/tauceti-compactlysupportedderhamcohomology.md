---
declaration: abbrev
origin: cited
lean: TauCeti.compactlySupportedDeRhamCohomology
statement: formalized
---

# TauCeti.compactlySupportedDeRhamCohomology

Compactly supported de Rham cohomology is the categorical homology of the compactly
supported de Rham complex.

```lean
TauCeti.compactlySupportedDeRhamCohomology.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H] (I : ModelWithCorners ℝ E H)
  (M : Type u_3) [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 2 M] (k : ℕ) :
  Type (max u_1 u_3)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.compactlySupportedDeRhamCohomology`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/CompactSupport.html#TauCeti.compactlySupportedDeRhamCohomology).

## Sources

- [Tau Ceti documentation: `TauCeti.compactlySupportedDeRhamCohomology`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/CompactSupport.html#TauCeti.compactlySupportedDeRhamCohomology)
- [Source of `TauCeti.compactlySupportedDeRhamCohomology` in TauCeti/Geometry/Manifold/DeRham/CompactSupport.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/DeRham/CompactSupport.lean#L198)
- [Tau Ceti roadmap status: Differential geometry — forms, de Rham cohomology, flows, and degree](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
