---
declaration: def
origin: cited
lean: Bundle.ContMDiffRiemannianMetric.positiveDefiniteSymmetricSectionEquiv
statement: formalized
---

# Bundle.ContMDiffRiemannianMetric.positiveDefiniteSymmetricSectionEquiv

Native finite-rank `C^n` metrics are exactly the positive-definite `C^n` sections of the
bundle of symmetric bilinear forms.

```lean
Bundle.ContMDiffRiemannianMetric.positiveDefiniteSymmetricSectionEquiv.{u_1, u_2, u_3, u_4, u_5}
  {EB : Type u_1} [NormedAddCommGroup EB] [NormedSpace ℝ EB] {HB : Type u_2} [TopologicalSpace HB]
  {IB : ModelWithCorners ℝ EB HB} {n : WithTop ℕ∞} {B : Type u_3} [TopologicalSpace B]
  [ChartedSpace HB B] {F : Type u_4} [NormedAddCommGroup F] [NormedSpace ℝ F] {V : B → Type u_5}
  [TopologicalSpace (Bundle.TotalSpace F V)] [(x : B) → TopologicalSpace (V x)]
  [(x : B) → AddCommGroup (V x)] [(x : B) → _root_.Module ℝ (V x)] [FiberBundle F V]
  [VectorBundle ℝ F V] [FiniteDimensional ℝ F] :
  Bundle.ContMDiffRiemannianMetric IB n F V ≃
    ↑(TauCeti.Manifold.positiveDefiniteSymmetricSections IB n F V)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Bundle.ContMDiffRiemannianMetric.positiveDefiniteSymmetricSectionEquiv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Section.html#Bundle.ContMDiffRiemannianMetric.positiveDefiniteSymmetricSectionEquiv).

## Sources

- [Tau Ceti documentation: `Bundle.ContMDiffRiemannianMetric.positiveDefiniteSymmetricSectionEquiv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Section.html#Bundle.ContMDiffRiemannianMetric.positiveDefiniteSymmetricSectionEquiv)
- [Source of `Bundle.ContMDiffRiemannianMetric.positiveDefiniteSymmetricSectionEquiv` in TauCeti/Geometry/Manifold/Riemannian/Section.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Riemannian/Section.lean#L297)
- [Tau Ceti roadmap status: Positive scalar curvature, surgery and bordism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PositiveScalarCurvature/STATUS.md)
