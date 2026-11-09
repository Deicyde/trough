---
declaration: def
origin: cited
lean: Bundle.ContMDiffRiemannianMetric.HasPositiveScalarCurvature
statement: formalized
---

# Bundle.ContMDiffRiemannianMetric.HasPositiveScalarCurvature

A smooth Riemannian metric has positive scalar curvature if its scalar curvature is positive
at every point.

```lean
Bundle.ContMDiffRiemannianMetric.HasPositiveScalarCurvature.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [T2Space M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M]
  (g : Bundle.ContMDiffRiemannianMetric I (↑⊤) E fun x => TangentSpace I x) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Koszul formula](../manifold/part-02/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`Bundle.ContMDiffRiemannianMetric.HasPositiveScalarCurvature`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Basic.html#Bundle.ContMDiffRiemannianMetric.HasPositiveScalarCurvature).

## Sources

- [Tau Ceti documentation: `Bundle.ContMDiffRiemannianMetric.HasPositiveScalarCurvature`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Basic.html#Bundle.ContMDiffRiemannianMetric.HasPositiveScalarCurvature)
- [Source of `Bundle.ContMDiffRiemannianMetric.HasPositiveScalarCurvature` in TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Basic.lean#L101)
- [Tau Ceti roadmap status: Positive scalar curvature, surgery and bordism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PositiveScalarCurvature/STATUS.md)
