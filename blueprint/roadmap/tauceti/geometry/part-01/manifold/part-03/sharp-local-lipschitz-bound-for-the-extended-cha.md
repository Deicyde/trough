---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.eventually_enorm_apply_extChartAt_sub_le
statement: formalized
proof: formalized
---

# Sharp local Lipschitz bound for the extended chart

For `r > 1`, near `x` every continuous
linear map `ℓ` from `T_x M` to a real normed space, read in the extended chart at `x`, is
`(r ‖ℓ‖)`-Lipschitz at `x` for the Riemannian distance.

```lean
TauCeti.Manifold.eventually_enorm_apply_extChartAt_sub_le.{u_1, u_2, u_3, u_4} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {F : Type u_2} [NormedAddCommGroup F] [NormedSpace ℝ F]
  {H : Type u_3} [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_4}
  [PseudoEMetricSpace M] [ChartedSpace H M] [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsManifold I 1 M] [IsRiemannianManifold I M]
  [IsContinuousRiemannianBundle E fun x => TangentSpace I x] (x : M) {r : ℝ} (hr : 1 < r) :
  ∀ᶠ (y : M) in nhds x,
    ∀ (ℓ : TangentSpace I x →L[ℝ] F),
      ‖ℓ (↑(extChartAt I x) y - ↑(extChartAt I x) x)‖ₑ ≤ ENNReal.ofReal r * ‖ℓ‖ₑ * edist x y
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.eventually_enorm_apply_extChartAt_sub_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/MetricBridge.html#TauCeti.Manifold.eventually_enorm_apply_extChartAt_sub_le).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.eventually_enorm_apply_extChartAt_sub_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/MetricBridge.html#TauCeti.Manifold.eventually_enorm_apply_extChartAt_sub_le)
- [Source of `TauCeti.Manifold.eventually_enorm_apply_extChartAt_sub_le` in TauCeti/Geometry/Manifold/Riemannian/MetricBridge.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Riemannian/MetricBridge.lean#L185)
