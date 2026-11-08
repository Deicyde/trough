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

- [Bundle.ContMDiffRiemannianMetric.HasPositiveScalarCurvature](bundle-contmdiffriemannianmetric-haspositivescal.md)

## Proof depends on

- [The Koszul formula](../manifold/part-02/the-koszul-formula.md)
- [The scalar curvature of a product metric `g₁ × g₂` is the sum of the scalar curvatures of the factors](the-scalar-curvature-of-a-product-metric-g1-g2-i.md)

## Lean

Formalized in Tau Ceti as [`Bundle.ContMDiffRiemannianMetric.equivalence_concordant`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Concordance.html#Bundle.ContMDiffRiemannianMetric.equivalence_concordant).

## Sources

- [Tau Ceti documentation: `Bundle.ContMDiffRiemannianMetric.equivalence_concordant`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Concordance.html#Bundle.ContMDiffRiemannianMetric.equivalence_concordant)
- [Source of `Bundle.ContMDiffRiemannianMetric.equivalence_concordant` in TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Concordance.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Concordance.lean#L430)
- [Tau Ceti roadmap status: Positive scalar curvature, surgery and bordism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PositiveScalarCurvature/STATUS.md)
