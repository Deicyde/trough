---
declaration: theorem
origin: cited
lean: Bundle.ContMDiffRiemannianMetric.concordant_iff_exists_isCollaredConcordance
statement: formalized
proof: formalized
---

# Bundle.ContMDiffRiemannianMetric.concordant_iff_exists_isCollaredConcordance

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

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Koszul formula](../../part-02/manifold/part-03/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`Bundle.ContMDiffRiemannianMetric.concordant_iff_exists_isCollaredConcordance`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Concordance.html#Bundle.ContMDiffRiemannianMetric.concordant_iff_exists_isCollaredConcordance).

## Sources

- [Tau Ceti documentation: `Bundle.ContMDiffRiemannianMetric.concordant_iff_exists_isCollaredConcordance`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Concordance.html#Bundle.ContMDiffRiemannianMetric.concordant_iff_exists_isCollaredConcordance)
- [Source of `Bundle.ContMDiffRiemannianMetric.concordant_iff_exists_isCollaredConcordance` in TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Concordance.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Concordance.lean#L805)
- [Tau Ceti roadmap status: Positive scalar curvature, surgery and bordism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PositiveScalarCurvature/STATUS.md)
