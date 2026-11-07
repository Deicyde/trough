---
declaration: theorem
origin: cited
lean: Bundle.ContMDiffRiemannianMetric.concordant_iff_exists_isCollaredConcordance
statement: formalized
proof: formalized
---

# Bundle.ContMDiffRiemannianMetric.concordant\_iff\_exists\_isCollaredConcordance

Two metrics are concordant exactly when there is a collared concordance from one to the
other.

```lean
Bundle.ContMDiffRiemannianMetric.concordant_iff_exists_isCollaredConcordance.{u_1, u_2, u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [FiniteDimensional ℝ E] [T2Space M]
  {g₀ g₁ : Bundle.ContMDiffRiemannianMetric I (↑⊤) E fun x => TangentSpace I x} :
  g₀.Concordant g₁ ↔ ∃ Gc, Gc.IsCollaredConcordance g₀ g₁
```

## Depends on

- [Bundle.ContMDiffRiemannianMetric.HasPositiveScalarCurvature](bundle-contmdiffriemannianmetric-haspositivescal.md)

## Proof depends on

- [Bundle.ContMDiffRiemannianMetric.scalarCurvature\_prodTangentSpace](bundle-contmdiffriemannianmetric-scalarcurvature.md)

## Lean

Formalized in Tau Ceti as [`Bundle.ContMDiffRiemannianMetric.concordant_iff_exists_isCollaredConcordance`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Concordance.html#Bundle.ContMDiffRiemannianMetric.concordant_iff_exists_isCollaredConcordance).

## Sources

- [Tau Ceti documentation: `Bundle.ContMDiffRiemannianMetric.concordant_iff_exists_isCollaredConcordance`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Concordance.html#Bundle.ContMDiffRiemannianMetric.concordant_iff_exists_isCollaredConcordance)
- [Source of `Bundle.ContMDiffRiemannianMetric.concordant_iff_exists_isCollaredConcordance` in TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Concordance.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Concordance.lean#L807)
- [Tau Ceti roadmap status: Positive scalar curvature, surgery and bordism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PositiveScalarCurvature/STATUS.md)
