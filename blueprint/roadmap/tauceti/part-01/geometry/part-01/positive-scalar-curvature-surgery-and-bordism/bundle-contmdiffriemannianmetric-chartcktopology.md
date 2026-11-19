---
declaration: def
origin: cited
lean: Bundle.ContMDiffRiemannianMetric.chartCkTopology
statement: formalized
---

# Bundle.ContMDiffRiemannianMetric.chartCkTopology

The topology of uniform convergence on compact chart sets of coordinate derivatives of order
at most `k` on the native smooth Riemannian metric carrier. Orders `k = 2` and `k = ⊤` give the
chart C² and C∞ topologies `chartC2Topology` and `chartCInftyTopology`.

```lean
Bundle.ContMDiffRiemannianMetric.chartCkTopology.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] (k : ℕ∞) :
  TopologicalSpace (Bundle.ContMDiffRiemannianMetric I (↑⊤) E fun x => TangentSpace I x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Bundle.ContMDiffRiemannianMetric.chartCkTopology`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/Riemannian/Topology.html#Bundle.ContMDiffRiemannianMetric.chartCkTopology).

## Sources

- [Tau Ceti documentation: `Bundle.ContMDiffRiemannianMetric.chartCkTopology`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/Riemannian/Topology.html#Bundle.ContMDiffRiemannianMetric.chartCkTopology)
- [Source of `Bundle.ContMDiffRiemannianMetric.chartCkTopology` in TauCeti/Geometry/Manifold/VectorBundle/Riemannian/Topology.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/VectorBundle/Riemannian/Topology.lean#L108)
- [Tau Ceti roadmap status: Positive scalar curvature, surgery and bordism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PositiveScalarCurvature/STATUS.md)
