---
declaration: theorem
origin: cited
lean: JoinedIn.concordant
statement: formalized
proof: formalized
---

# Isotopic metrics are concordant

On a closed manifold, two metrics joined by a path of
metrics of positive scalar curvature, continuous in the chart C² topology, are concordant.

```lean
JoinedIn.concordant.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] {H : Type u_2} [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  [I.Boundaryless] {M : Type u_3} [TopologicalSpace M] [T2Space M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [CompactSpace M]
  {g₀ g₁ : Bundle.ContMDiffRiemannianMetric I (↑⊤) E fun x => TangentSpace I x}
  (h : JoinedIn {g | g.HasPositiveScalarCurvature} g₀ g₁) : g₀.Concordant g₁
```

## Depends on

- [Bundle.ContMDiffRiemannianMetric.chartCkTopology](bundle-contmdiffriemannianmetric-chartcktopology.md)

## Proof depends on

- [Bundle.Trivialization.mem_maximalAtlas_contMDiffFiberwiseLinear_iff](../complex-manifolds-transport-quotients-bundles-an/bundle-trivialization-mem-maximalatlas-contmdiff.md)
- [The Koszul formula](../../part-02/manifold/part-03/the-koszul-formula.md)
- [Positive scalar curvature is C²-open](positive-scalar-curvature-is-c2-open.md)
- [TauCeti.Manifold.scalarCurvatureOfJet](tauceti-manifold-scalarcurvatureofjet.md)

## Lean

Formalized in Tau Ceti as [`JoinedIn.concordant`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Isotopy.html#JoinedIn.concordant).

## Sources

- [Tau Ceti documentation: `JoinedIn.concordant`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Isotopy.html#JoinedIn.concordant)
- [Source of `JoinedIn.concordant` in TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Isotopy.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Isotopy.lean#L106)
- [Tau Ceti roadmap status: Positive scalar curvature, surgery and bordism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PositiveScalarCurvature/STATUS.md)
