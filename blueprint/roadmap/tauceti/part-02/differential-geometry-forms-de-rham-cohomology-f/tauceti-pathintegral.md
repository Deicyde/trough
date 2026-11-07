---
declaration: def
origin: cited
lean: TauCeti.pathIntegral
statement: formalized
---

# TauCeti.pathIntegral

The integral of a `1`-form `φ` along a curve `γ : ℝ → M` over the oriented interval `a..b`:
the interval integral of `φ` evaluated on the velocity of `γ`.

```lean
TauCeti.pathIntegral.{u_1, u_2, u_3, u_4} {E : Type u_1} {H : Type u_2} {M : Type u_3}
  {F : Type u_4} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [NormedAddCommGroup F]
  [NormedSpace ℝ F] (φ : TauCeti.RoughForm I M F 1) (γ : ℝ → M) (a b : ℝ) : F
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.pathIntegral`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Path.html#TauCeti.pathIntegral).

## Sources

- [Tau Ceti documentation: `TauCeti.pathIntegral`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Path.html#TauCeti.pathIntegral)
- [Source of `TauCeti.pathIntegral` in TauCeti/Geometry/Manifold/DifferentialForm/Integration/Path.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Path.lean#L74)
- [Tau Ceti roadmap status: Differential geometry — forms, de Rham cohomology, flows, and degree](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
