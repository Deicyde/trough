---
declaration: def
origin: cited
lean: TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.variation
statement: formalized
---

# TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.variation

The first variation `δ_u g` of a smooth nondegenerate metric family at the parameter `p` in
the direction `u ∈ T_p P`. Its value at `y : M` is the differential at `p` of the smooth map
`p' ↦ g (p', y)` into the bilinear forms on `T_y M`, applied to `u`.

```lean
TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.variation.{u_1, u_2, u_3, u_4, u_5, u_6}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] {EP : Type u_4} [NormedAddCommGroup EP] [NormedSpace ℝ EP] {HP : Type u_5}
  [TopologicalSpace HP] {IP : ModelWithCorners ℝ EP HP} {P : Type u_6} [TopologicalSpace P]
  [ChartedSpace HP P] (g : TauCeti.Manifold.ContMDiffNondegenerateMetricFamily I M IP P) (p : P)
  (u : TangentSpace IP p) (y : M) : TangentSpace I y →L[ℝ] TangentSpace I y →L[ℝ] ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.variation`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/NondegenerateMetric/Variation.html#TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.variation).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.variation`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/NondegenerateMetric/Variation.html#TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.variation)
- [Source of `TauCeti.Manifold.ContMDiffNondegenerateMetricFamily.variation` in TauCeti/Geometry/Manifold/VectorBundle/NondegenerateMetric/Variation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/VectorBundle/NondegenerateMetric/Variation.lean#L102)
- [Tau Ceti roadmap status: Geodesics, the exponential map, and the Hopf–Rinow theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/HopfRinow/STATUS.md)
