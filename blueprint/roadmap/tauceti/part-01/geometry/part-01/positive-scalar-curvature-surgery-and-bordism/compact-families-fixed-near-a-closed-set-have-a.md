---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.exists_pos_forall_le_scalarCurvature_of_eventually_inner_eq
statement: formalized
proof: formalized
---

# Compact families fixed near a closed set have a uniform scalar gap

On a compact manifold,
let `g p` be a family of metrics, indexed by a compact space, all of which agree with a fixed
metric `g₀` on a common neighbourhood of a closed set `C`. If the scalar curvature of `g₀` is
positive on `C`, and outside `C` the scalar curvature of each `g p` is positive and the chart
metrics have Gram matrices, first and second derivatives in the basis `b` depending continuously
on the parameter and the chart point, then the scalar curvatures of the metrics `g p` are bounded
below by a common positive constant.

```lean
TauCeti.Manifold.exists_pos_forall_le_scalarCurvature_of_eventually_inner_eq.{u_1, u_2, u_3, u_4,
    u_5}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [T2Space M] [ChartedSpace H M] [IsManifold I (↑⊤) M] {P : Type u_4}
  [TopologicalSpace P] (g : P → Bundle.ContMDiffRiemannianMetric I (↑⊤) E fun x => TangentSpace I x)
  {ι : Type u_5} [Fintype ι] [DecidableEq ι] (b : Module.Basis ι ℝ E) [CompactSpace P]
  [CompactSpace M] {C : Set M} (hC : IsClosed C)
  (g₀ : Bundle.ContMDiffRiemannianMetric I (↑⊤) E fun x => TangentSpace I x)
  (hfix : ∀ᶠ (x : M) in nhdsSet C, ∀ (p : P), (g p).inner x = g₀.inner x)
  (h₀ :
    ∀ (p : P),
      ∀ x ∉ C,
        ContinuousAt
          (fun r =>
            (LinearMap.toMatrix₂ b b) ((g r.1).toNondegenerateMetric.chartMetric x r.2).toBilinForm)
          (p, ↑(extChartAt I x) x))
  (h₁ :
    ∀ (p : P),
      ∀ x ∉ C,
        ContinuousAt
          (fun r k i j =>
            (fderiv ℝ (fun z => (((g r.1).toNondegenerateMetric.chartMetric x z) (b i)) (b j)) r.2)
              (b k))
          (p, ↑(extChartAt I x) x))
  (h₂ :
    ∀ (p : P),
      ∀ x ∉ C,
        ContinuousAt
          (fun r m k i j =>
            (fderiv ℝ
                (fun z =>
                  (fderiv ℝ
                      (fun z' => (((g r.1).toNondegenerateMetric.chartMetric x z') (b i)) (b j)) z)
                    (b k))
                r.2)
              (b m))
          (p, ↑(extChartAt I x) x))
  (hpos₀ : ∀ x ∈ C, 0 < g₀.scalarCurvature x)
  (hpos : ∀ (p : P), ∀ x ∉ C, 0 < (g p).scalarCurvature x) :
  ∃ ε, 0 < ε ∧ ∀ (p : P) (x : M), ε ≤ (g p).scalarCurvature x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Bundle.Trivialization.mem_maximalAtlas_contMDiffFiberwiseLinear_iff](../complex-manifolds-transport-quotients-bundles-an/bundle-trivialization-mem-maximalatlas-contmdiff.md)
- [The Koszul formula](../../part-02/manifold/part-02/the-koszul-formula.md)
- [TauCeti.Manifold.scalarCurvatureOfJet](tauceti-manifold-scalarcurvatureofjet.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.exists_pos_forall_le_scalarCurvature_of_eventually_inner_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Family.html#TauCeti.Manifold.exists_pos_forall_le_scalarCurvature_of_eventually_inner_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.exists_pos_forall_le_scalarCurvature_of_eventually_inner_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Family.html#TauCeti.Manifold.exists_pos_forall_le_scalarCurvature_of_eventually_inner_eq)
- [Source of `TauCeti.Manifold.exists_pos_forall_le_scalarCurvature_of_eventually_inner_eq` in TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Family.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Family.lean#L159)
- [Tau Ceti roadmap status: Positive scalar curvature, surgery and bordism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PositiveScalarCurvature/STATUS.md)
