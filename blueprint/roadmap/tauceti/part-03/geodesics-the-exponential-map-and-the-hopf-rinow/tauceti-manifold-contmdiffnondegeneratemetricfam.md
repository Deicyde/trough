---
declaration: structure
origin: cited
lean: TauCeti.Manifold.ContMDiffNondegenerateMetricFamily
statement: formalized
---

# TauCeti.Manifold.ContMDiffNondegenerateMetricFamily

A smooth family, parametrized by `P`, of symmetric nondegenerate real bilinear forms on the
tangent bundle of `M`.

The family is a native smooth section over `P × M` of the pullback of the tangent
bilinear-form bundle of `M` along the projection `P × M → M`; its value at `(p, x)` is a bilinear
form on `T_x M`. As for a single metric, no positivity or signature is imposed.

```lean
TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.{u_1, u_2, u_3, u_4, u_5, u_6} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  (I : ModelWithCorners ℝ E H) (M : Type u_3) [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] {EP : Type u_4} [NormedAddCommGroup EP] [NormedSpace ℝ EP] {HP : Type u_5}
  [TopologicalSpace HP] (IP : ModelWithCorners ℝ EP HP) (P : Type u_6) [TopologicalSpace P]
  [ChartedSpace HP P] : Type (max (max u_1 u_3) u_6)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.ContMDiffNondegenerateMetricFamily`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/NondegenerateMetric/Family.html#TauCeti.Manifold.ContMDiffNondegenerateMetricFamily).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.ContMDiffNondegenerateMetricFamily`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/NondegenerateMetric/Family.html#TauCeti.Manifold.ContMDiffNondegenerateMetricFamily)
- [Source of `TauCeti.Manifold.ContMDiffNondegenerateMetricFamily` in TauCeti/Geometry/Manifold/VectorBundle/NondegenerateMetric/Family.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/VectorBundle/NondegenerateMetric/Family.lean#L67)
- [Tau Ceti roadmap status: Geodesics, the exponential map, and the Hopf–Rinow theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/HopfRinow/STATUS.md)
