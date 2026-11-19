---
declaration: theorem
origin: cited
lean: Bundle.ContMDiffRiemannianMetric.isOpen_setOf_hasPositiveScalarCurvature_chartC2
statement: formalized
proof: formalized
---

# Positive scalar curvature is C²-open

On a compact manifold without boundary, the smooth
Riemannian metrics of positive scalar curvature form an open set in the chart C² topology.

```lean
Bundle.ContMDiffRiemannianMetric.isOpen_setOf_hasPositiveScalarCurvature_chartC2.{u_1, u_2, u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [T2Space M] [ChartedSpace H M] [IsManifold I (↑⊤) M] [CompactSpace M] :
  IsOpen {g | g.HasPositiveScalarCurvature}
```

## Depends on

- [Bundle.ContMDiffRiemannianMetric.chartCkTopology](bundle-contmdiffriemannianmetric-chartcktopology.md)

## Proof depends on

- [Bundle.Trivialization.mem_maximalAtlas_contMDiffFiberwiseLinear_iff](../complex-manifolds-transport-quotients-bundles-an/bundle-trivialization-mem-maximalatlas-contmdiff.md)
- [The Koszul formula](../../part-02/manifold/part-03/the-koszul-formula.md)
- [TauCeti.Manifold.scalarCurvatureOfJet](tauceti-manifold-scalarcurvatureofjet.md)

## Lean

Formalized in Tau Ceti as [`Bundle.ContMDiffRiemannianMetric.isOpen_setOf_hasPositiveScalarCurvature_chartC2`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Topology.html#Bundle.ContMDiffRiemannianMetric.isOpen_setOf_hasPositiveScalarCurvature_chartC2).

## Sources

- [Tau Ceti documentation: `Bundle.ContMDiffRiemannianMetric.isOpen_setOf_hasPositiveScalarCurvature_chartC2`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Topology.html#Bundle.ContMDiffRiemannianMetric.isOpen_setOf_hasPositiveScalarCurvature_chartC2)
- [Source of `Bundle.ContMDiffRiemannianMetric.isOpen_setOf_hasPositiveScalarCurvature_chartC2` in TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Topology.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Topology.lean#L142)
- [Tau Ceti roadmap status: Positive scalar curvature, surgery and bordism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PositiveScalarCurvature/STATUS.md)
