---
declaration: theorem
origin: cited
lean: Bundle.ContMDiffRiemannianMetric.equivalence_concordant
statement: formalized
proof: formalized
---

# Bundle.ContMDiffRiemannianMetric.equivalence_concordant

Concordance is an equivalence relation on the metrics of positive scalar curvature on `M`.

```lean
Bundle.ContMDiffRiemannianMetric.equivalence_concordant.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [FiniteDimensional ℝ E] [T2Space M] :
  Equivalence fun g₀ g₁ => (↑g₀).Concordant ↑g₁
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Koszul formula](../../part-02/manifold/part-02/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`Bundle.ContMDiffRiemannianMetric.equivalence_concordant`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Concordance.html#Bundle.ContMDiffRiemannianMetric.equivalence_concordant).

## Sources

- [Tau Ceti documentation: `Bundle.ContMDiffRiemannianMetric.equivalence_concordant`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Concordance.html#Bundle.ContMDiffRiemannianMetric.equivalence_concordant)
- [Source of `Bundle.ContMDiffRiemannianMetric.equivalence_concordant` in TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Concordance.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Concordance.lean#L429)
- [Tau Ceti roadmap status: Positive scalar curvature, surgery and bordism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PositiveScalarCurvature/STATUS.md)
