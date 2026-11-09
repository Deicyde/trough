---
declaration: theorem
origin: cited
lean: Bundle.ContMDiffRiemannianMetric.exists_pos_hasPositiveScalarCurvature_prodTangentSpace_rescale
statement: formalized
proof: formalized
---

# Shrinking a compact factor of positive scalar curvature

Let `g₂` be a metric of positive
scalar curvature on a compact manifold `N`, and let `g` be a metric whose scalar curvature is
bounded below. Then there is `ε > 0` such that `g × c g₂` has positive scalar curvature for every
`0 < c < ε`.

```lean
Bundle.ContMDiffRiemannianMetric.exists_pos_hasPositiveScalarCurvature_prodTangentSpace_rescale.{u_1,
    u_2, u_3, u_4, u_5, u_6}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [T2Space M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M]
  (g : Bundle.ContMDiffRiemannianMetric I (↑⊤) E fun x => TangentSpace I x) {F : Type u_4}
  [NormedAddCommGroup F] [NormedSpace ℝ F] [FiniteDimensional ℝ F] {H' : Type u_5}
  [TopologicalSpace H'] {J : ModelWithCorners ℝ F H'} {N : Type u_6} [TopologicalSpace N]
  [T2Space N] [ChartedSpace H' N] [IsManifold J (↑⊤) N]
  {g₂ : Bundle.ContMDiffRiemannianMetric J (↑⊤) F fun y => TangentSpace J y} [CompactSpace N]
  (h : BddBelow (Set.range g.scalarCurvature)) (h₂ : g₂.HasPositiveScalarCurvature) :
  ∃ ε,
    0 < ε ∧
      ∀ (c : ℝ) (hc : 0 < c),
        c < ε → (g.prodTangentSpace (g₂.rescale (fun x => c) ⋯ ⋯)).HasPositiveScalarCurvature
```

## Depends on

- [Bundle.ContMDiffRiemannianMetric.HasPositiveScalarCurvature](bundle-contmdiffriemannianmetric-haspositivescal.md)

## Proof depends on

- [The Koszul formula](../manifold/part-02/the-koszul-formula.md)
- [The scalar curvature of a product metric](the-scalar-curvature-of-a-product-metric.md)

## Lean

Formalized in Tau Ceti as [`Bundle.ContMDiffRiemannianMetric.exists_pos_hasPositiveScalarCurvature_prodTangentSpace_rescale`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Basic.html#Bundle.ContMDiffRiemannianMetric.exists_pos_hasPositiveScalarCurvature_prodTangentSpace_rescale).

## Sources

- [Tau Ceti documentation: `Bundle.ContMDiffRiemannianMetric.exists_pos_hasPositiveScalarCurvature_prodTangentSpace_rescale`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Basic.html#Bundle.ContMDiffRiemannianMetric.exists_pos_hasPositiveScalarCurvature_prodTangentSpace_rescale)
- [Source of `Bundle.ContMDiffRiemannianMetric.exists_pos_hasPositiveScalarCurvature_prodTangentSpace_rescale` in TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Basic.lean#L329)
- [Tau Ceti roadmap status: Positive scalar curvature, surgery and bordism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PositiveScalarCurvature/STATUS.md)
