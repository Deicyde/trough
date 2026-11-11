---
declaration: theorem
origin: cited
lean: Bundle.ContMDiffRiemannianMetric.exists_hyperbolicMetric_metric_eq_rescale_iff
statement: formalized
proof: formalized
---

# Hyperbolic metrics in a conformal class and the curvature equation

A closed surface
carries a hyperbolic metric conformal to `g`, that is of the form `f g` for a smooth positive
function `f`, exactly when the curvature equation `Δ⁺φ + K + e^(2φ) = 0` has a smooth solution
`φ`; here `Δ⁺ = -div grad` is the nonnegative Laplacian of `g` and `K = Scal^g / 2` its Gaussian
curvature. The hyperbolic metric is then `e^(2φ) g`.

```lean
Bundle.ContMDiffRiemannianMetric.exists_hyperbolicMetric_metric_eq_rescale_iff.{u_1, u_2, u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [T3Space M]
  [PreconnectedSpace M] [CompactSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M]
  (g : Bundle.ContMDiffRiemannianMetric I (↑⊤) E fun x => TangentSpace I x)
  (hE : Module.finrank ℝ E = 2) :
  (∃ G f,
      ∃ (hf : ContMDiff I (modelWithCornersSelf ℝ ℝ) (↑⊤) f) (hf_pos : ∀ (x : M), 0 < f x),
        G.metric = g.rescale f hf hf_pos) ↔
    ∃ φ,
      ContMDiff I (modelWithCornersSelf ℝ ℝ) (↑⊤) φ ∧
        ∀ (x : M),
          -TauCeti.Manifold.laplaceBeltrami I φ x + g.scalarCurvature x / 2 + Real.exp (2 * φ x) = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Koszul formula](../../../part-02/manifold/part-02/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`Bundle.ContMDiffRiemannianMetric.exists_hyperbolicMetric_metric_eq_rescale_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Hyperbolic/ClosedSurface.html#Bundle.ContMDiffRiemannianMetric.exists_hyperbolicMetric_metric_eq_rescale_iff).

## Sources

- [Tau Ceti documentation: `Bundle.ContMDiffRiemannianMetric.exists_hyperbolicMetric_metric_eq_rescale_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Hyperbolic/ClosedSurface.html#Bundle.ContMDiffRiemannianMetric.exists_hyperbolicMetric_metric_eq_rescale_iff)
- [Source of `Bundle.ContMDiffRiemannianMetric.exists_hyperbolicMetric_metric_eq_rescale_iff` in TauCeti/Geometry/Manifold/Riemannian/Hyperbolic/ClosedSurface.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Riemannian/Hyperbolic/ClosedSurface.lean#L71)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
