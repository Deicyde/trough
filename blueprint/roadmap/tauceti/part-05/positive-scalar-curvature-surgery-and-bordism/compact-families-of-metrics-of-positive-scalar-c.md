---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.exists_pos_forall_le_scalarCurvature
statement: formalized
proof: formalized
---

# Compact families of metrics of positive scalar curvature have a uniform scalar gap

On a
compact manifold, a family of metrics of positive scalar curvature indexed by a compact space, whose
chart metrics have Gram matrices, first and second derivatives in the basis `b` depending
continuously on the parameter and the chart point, has scalar curvature bounded below by a common
positive constant.

```lean
TauCeti.Manifold.exists_pos_forall_le_scalarCurvature.{u_1, u_2, u_3, u_4, u_5} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [T2Space M] [ChartedSpace H M] [IsManifold I (↑⊤) M] {P : Type u_4}
  [TopologicalSpace P] (g : P → Bundle.ContMDiffRiemannianMetric I (↑⊤) E fun x => TangentSpace I x)
  {ι : Type u_5} [Fintype ι] [DecidableEq ι] (b : Module.Basis ι ℝ E) [CompactSpace P]
  [CompactSpace M]
  (h₀ :
    ∀ (p : P) (x : M),
      ContinuousAt
        (fun r =>
          (LinearMap.toMatrix₂ b b) ((g r.1).toNondegenerateMetric.chartMetric x r.2).toBilinForm)
        (p, ↑(extChartAt I x) x))
  (h₁ :
    ∀ (p : P) (x : M),
      ContinuousAt
        (fun r k i j =>
          (fderiv ℝ (fun z => (((g r.1).toNondegenerateMetric.chartMetric x z) (b i)) (b j)) r.2)
            (b k))
        (p, ↑(extChartAt I x) x))
  (h₂ :
    ∀ (p : P) (x : M),
      ContinuousAt
        (fun r m k i j =>
          (fderiv ℝ
              (fun z =>
                (fderiv ℝ (fun z' => (((g r.1).toNondegenerateMetric.chartMetric x z') (b i)) (b j))
                    z)
                  (b k))
              r.2)
            (b m))
        (p, ↑(extChartAt I x) x))
  (hpos : ∀ (p : P), (g p).HasPositiveScalarCurvature) :
  ∃ ε, 0 < ε ∧ ∀ (p : P) (x : M), ε ≤ (g p).scalarCurvature x
```

## Depends on

- [Bundle.ContMDiffRiemannianMetric.HasPositiveScalarCurvature](bundle-contmdiffriemannianmetric-haspositivescal.md)

## Proof depends on

- [Scalar curvature is continuous in the second-order jet of the metric](scalar-curvature-is-continuous-in-the-second-ord.md)
- [TauCeti.Manifold.scalarCurvatureOfJet](tauceti-manifold-scalarcurvatureofjet.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.exists_pos_forall_le_scalarCurvature`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Family.html#TauCeti.Manifold.exists_pos_forall_le_scalarCurvature).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.exists_pos_forall_le_scalarCurvature`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Family.html#TauCeti.Manifold.exists_pos_forall_le_scalarCurvature)
- [Source of `TauCeti.Manifold.exists_pos_forall_le_scalarCurvature` in TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Family.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Family.lean#L90)
- [Tau Ceti roadmap status: Positive scalar curvature, surgery and bordism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PositiveScalarCurvature/STATUS.md)
