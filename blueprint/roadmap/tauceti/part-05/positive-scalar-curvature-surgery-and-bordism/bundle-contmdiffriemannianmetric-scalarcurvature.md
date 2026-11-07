---
declaration: theorem
origin: cited
lean: Bundle.ContMDiffRiemannianMetric.scalarCurvature_prodTangentSpace
statement: formalized
proof: formalized
---

# Bundle.ContMDiffRiemannianMetric.scalarCurvature\_prodTangentSpace

**The scalar curvature of a product metric** `g₁ × g₂` is the sum of the scalar curvatures of
the factors: `Scal(x, y) = Scal_{g₁}(x) + Scal_{g₂}(y)`.

```lean
Bundle.ContMDiffRiemannianMetric.scalarCurvature_prodTangentSpace.{u_1, u_2, u_3, u_4, u_5, u_6}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [T2Space M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] {F : Type u_4} [NormedAddCommGroup F] [NormedSpace ℝ F]
  [FiniteDimensional ℝ F] {G : Type u_5} [TopologicalSpace G] {J : ModelWithCorners ℝ F G}
  {N : Type u_6} [TopologicalSpace N] [T2Space N] [ChartedSpace G N] [IsManifold J (↑⊤) N]
  (g₁ : Bundle.ContMDiffRiemannianMetric I (↑⊤) E fun x => TangentSpace I x)
  (g₂ : Bundle.ContMDiffRiemannianMetric J (↑⊤) F fun y => TangentSpace J y) (p : M × N) :
  (g₁.prodTangentSpace g₂).scalarCurvature p = g₁.scalarCurvature p.1 + g₂.scalarCurvature p.2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Bundle.ContMDiffRiemannianMetric.scalarCurvature_prodTangentSpace`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Prod.html#Bundle.ContMDiffRiemannianMetric.scalarCurvature_prodTangentSpace).

## Sources

- [Tau Ceti documentation: `Bundle.ContMDiffRiemannianMetric.scalarCurvature_prodTangentSpace`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Prod.html#Bundle.ContMDiffRiemannianMetric.scalarCurvature_prodTangentSpace)
- [Source of `Bundle.ContMDiffRiemannianMetric.scalarCurvature_prodTangentSpace` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Prod.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Prod.lean#L203)
- [Tau Ceti roadmap status: Positive scalar curvature, surgery and bordism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PositiveScalarCurvature/STATUS.md)
