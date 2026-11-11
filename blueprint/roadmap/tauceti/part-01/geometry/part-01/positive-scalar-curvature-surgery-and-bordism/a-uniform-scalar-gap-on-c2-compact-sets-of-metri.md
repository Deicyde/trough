---
declaration: theorem
origin: cited
lean: IsCompact.exists_pos_forall_le_scalarCurvature_chartC2
statement: formalized
proof: formalized
---

# A uniform scalar gap on C²-compact sets of metrics

On a compact manifold without boundary,
let `K` be a set of smooth Riemannian metrics of positive scalar curvature that is compact in the
chart C² topology, such as the image of a continuous path of such metrics. Then the scalar
curvatures of the metrics in `K` are bounded below by a common positive constant.

```lean
IsCompact.exists_pos_forall_le_scalarCurvature_chartC2.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [T2Space M] [ChartedSpace H M] [IsManifold I (↑⊤) M] [CompactSpace M]
  {K : Set (Bundle.ContMDiffRiemannianMetric I (↑⊤) E fun x => TangentSpace I x)} (hK : IsCompact K)
  (hpos : ∀ g ∈ K, g.HasPositiveScalarCurvature) :
  ∃ ε, 0 < ε ∧ ∀ g ∈ K, ∀ (x : M), ε ≤ g.scalarCurvature x
```

## Depends on

- [Bundle.ContMDiffRiemannianMetric.chartCkTopology](bundle-contmdiffriemannianmetric-chartcktopology.md)

## Proof depends on

- [Bundle.Trivialization.mem_maximalAtlas_contMDiffFiberwiseLinear_iff](../complex-manifolds-transport-quotients-bundles-an/bundle-trivialization-mem-maximalatlas-contmdiff.md)
- [The Koszul formula](../../part-02/manifold/part-02/the-koszul-formula.md)
- [TauCeti.Manifold.scalarCurvatureOfJet](tauceti-manifold-scalarcurvatureofjet.md)

## Lean

Formalized in Tau Ceti as [`IsCompact.exists_pos_forall_le_scalarCurvature_chartC2`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Topology.html#IsCompact.exists_pos_forall_le_scalarCurvature_chartC2).

## Sources

- [Tau Ceti documentation: `IsCompact.exists_pos_forall_le_scalarCurvature_chartC2`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Topology.html#IsCompact.exists_pos_forall_le_scalarCurvature_chartC2)
- [Source of `IsCompact.exists_pos_forall_le_scalarCurvature_chartC2` in TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Topology.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Topology.lean#L185)
- [Tau Ceti roadmap status: Positive scalar curvature, surgery and bordism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PositiveScalarCurvature/STATUS.md)
