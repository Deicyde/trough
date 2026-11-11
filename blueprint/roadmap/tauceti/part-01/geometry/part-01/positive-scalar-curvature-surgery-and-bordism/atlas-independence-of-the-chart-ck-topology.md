---
declaration: theorem
origin: cited
lean: Bundle.ContMDiffRiemannianMetric.chartCkTopology_eq_induced
statement: formalized
proof: formalized
---

# Atlas independence of the chart Cᵏ topology

The chart Cᵏ topology is the topology induced
by the coordinate derivatives of order at most `k` in the charts at the points of any set `S`
whose chart domains cover `M`.

```lean
Bundle.ContMDiffRiemannianMetric.chartCkTopology_eq_induced.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] [I.Boundaryless] (k : ℕ∞) {S : Set M}
  (hS : ∀ (y : M), ∃ x ∈ S, y ∈ (chartAt H x).source) :
  Bundle.ContMDiffRiemannianMetric.chartCkTopology k =
    TopologicalSpace.induced (fun g x m => g.chartMetricDerivative ↑x ↑m) inferInstance
```

## Depends on

- [Bundle.ContMDiffRiemannianMetric.chartCkTopology](bundle-contmdiffriemannianmetric-chartcktopology.md)

## Lean

Formalized in Tau Ceti as [`Bundle.ContMDiffRiemannianMetric.chartCkTopology_eq_induced`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Pullback/Topology.html#Bundle.ContMDiffRiemannianMetric.chartCkTopology_eq_induced).

## Sources

- [Tau Ceti documentation: `Bundle.ContMDiffRiemannianMetric.chartCkTopology_eq_induced`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Pullback/Topology.html#Bundle.ContMDiffRiemannianMetric.chartCkTopology_eq_induced)
- [Source of `Bundle.ContMDiffRiemannianMetric.chartCkTopology_eq_induced` in TauCeti/Geometry/Manifold/Riemannian/Pullback/Topology.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Riemannian/Pullback/Topology.lean#L375)
- [Tau Ceti roadmap status: Positive scalar curvature, surgery and bordism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PositiveScalarCurvature/STATUS.md)
