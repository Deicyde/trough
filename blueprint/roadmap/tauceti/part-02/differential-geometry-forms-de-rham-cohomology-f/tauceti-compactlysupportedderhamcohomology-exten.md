---
declaration: def
origin: cited
lean: TauCeti.compactlySupportedDeRhamCohomology.extendByZero
statement: formalized
---

# TauCeti.compactlySupportedDeRhamCohomology.extendByZero

The map on compactly supported de Rham cohomology induced by extension by zero along an
inclusion `U ≤ W` of open subsets of a Hausdorff manifold.

```lean
TauCeti.compactlySupportedDeRhamCohomology.extendByZero.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [T2Space M]
  [IsManifold I 2 M] {U W : TopologicalSpace.Opens M} (h : U ≤ W) (k : ℕ) :
  TauCeti.compactlySupportedDeRhamCohomology I (↥U) k →ₗ[ℝ]
    TauCeti.compactlySupportedDeRhamCohomology I (↥W) k
```

## Depends on

- [TauCeti.compactlySupportedDeRhamCohomology](tauceti-compactlysupportedderhamcohomology.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.compactlySupportedDeRhamCohomology.extendByZero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/ExtendByZero.html#TauCeti.compactlySupportedDeRhamCohomology.extendByZero).

## Sources

- [Tau Ceti documentation: `TauCeti.compactlySupportedDeRhamCohomology.extendByZero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/ExtendByZero.html#TauCeti.compactlySupportedDeRhamCohomology.extendByZero)
- [Source of `TauCeti.compactlySupportedDeRhamCohomology.extendByZero` in TauCeti/Geometry/Manifold/DeRham/ExtendByZero.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/DeRham/ExtendByZero.lean#L306)
- [Tau Ceti roadmap status: Differential geometry — forms, de Rham cohomology, flows, and degree](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
