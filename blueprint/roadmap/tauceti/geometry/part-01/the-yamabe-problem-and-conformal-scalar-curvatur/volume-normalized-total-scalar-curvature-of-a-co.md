---
declaration: theorem
origin: cited
lean: TauCeti.Yamabe.integral_scalarCurvature_rescale_div_riemannianTotalVolume_rpow
statement: formalized
proof: formalized
---

# Volume-normalized total scalar curvature of a conformal metric

On a compact manifold of
dimension `n ≠ 2`, let `u` be a positive function such that `ĝ = u ^ (4 / (n - 2)) g` is a smooth
metric, and let `pₙ = 2 n / (n - 2)`. Then
`(∫ Scal_ĝ dV_ĝ) / Vol(ĝ) ^ (2 / pₙ) = (∫ u L_g u dV_g) / (∫ u ^ pₙ dV_g) ^ (2 / pₙ)`,
where `L_g` is the conformal Laplacian of `g`.

```lean
TauCeti.Yamabe.integral_scalarCurvature_rescale_div_riemannianTotalVolume_rpow.{u_1, u_2, u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M] [LindelofSpace M] [CompactSpace M]
  (g : Bundle.ContMDiffRiemannianMetric I (↑⊤) E fun x => TangentSpace I x)
  (hn : Module.finrank ℝ E ≠ 2) {u : M → ℝ} (hu_pos : ∀ (x : M), 0 < u x)
  {hf : ContMDiff I (modelWithCornersSelf ℝ ℝ) ↑⊤ fun x => u x ^ (4 / (↑(Module.finrank ℝ E) - 2))}
  {hf_pos : ∀ (x : M), 0 < u x ^ (4 / (↑(Module.finrank ℝ E) - 2))} :
  (∫ (x :
        TauCeti.WithMetric
          (g.rescale (fun x => u x ^ (4 / (↑(Module.finrank ℝ E) - 2))) hf hf_pos)),
        (g.rescale (fun x => u x ^ (4 / (↑(Module.finrank ℝ E) - 2))) hf hf_pos).scalarCurvature
          x.ofWithMetric ∂TauCeti.riemannianVolume I
          (TauCeti.WithMetric
            (g.rescale (fun x => u x ^ (4 / (↑(Module.finrank ℝ E) - 2))) hf hf_pos))) /
      TauCeti.riemannianTotalVolume I
          (TauCeti.WithMetric
            (g.rescale (fun x => u x ^ (4 / (↑(Module.finrank ℝ E) - 2))) hf hf_pos)) ^
        (2 / TauCeti.Yamabe.criticalExponent (Module.finrank ℝ E)) =
    (∫ (x : TauCeti.WithMetric g),
        u x.ofWithMetric *
          TauCeti.Yamabe.conformalLaplacian I u
            x.ofWithMetric ∂TauCeti.riemannianVolume I (TauCeti.WithMetric g)) /
      (∫ (x : TauCeti.WithMetric g),
          u x.ofWithMetric ^
            TauCeti.Yamabe.criticalExponent
              (Module.finrank ℝ E) ∂TauCeti.riemannianVolume I (TauCeti.WithMetric g)) ^
        (2 / TauCeti.Yamabe.criticalExponent (Module.finrank ℝ E))
```

## Depends on

- [TauCeti.Yamabe.conformalLaplacian](tauceti-yamabe-conformallaplacian.md)

## Proof depends on

- [Homeomorph.pullbackChartedSpace](../complex-manifolds-transport-quotients-bundles-an/homeomorph-pullbackchartedspace.md)
- [Homeomorph.pullbackDiffeomorph](../complex-manifolds-transport-quotients-bundles-an/homeomorph-pullbackdiffeomorph.md)
- [The Koszul formula](../manifold/part-02/the-koszul-formula.md)
- [Scalar curvature of a conformal metric](scalar-curvature-of-a-conformal-metric.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Yamabe.integral_scalarCurvature_rescale_div_riemannianTotalVolume_rpow`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Yamabe/TotalScalarCurvature.html#TauCeti.Yamabe.integral_scalarCurvature_rescale_div_riemannianTotalVolume_rpow).

## Sources

- [Tau Ceti documentation: `TauCeti.Yamabe.integral_scalarCurvature_rescale_div_riemannianTotalVolume_rpow`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Yamabe/TotalScalarCurvature.html#TauCeti.Yamabe.integral_scalarCurvature_rescale_div_riemannianTotalVolume_rpow)
- [Source of `TauCeti.Yamabe.integral_scalarCurvature_rescale_div_riemannianTotalVolume_rpow` in TauCeti/Analysis/PDE/Yamabe/TotalScalarCurvature.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Yamabe/TotalScalarCurvature.lean#L163)
- [Tau Ceti roadmap status: The Yamabe problem and conformal scalar curvature](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Yamabe/STATUS.md)
