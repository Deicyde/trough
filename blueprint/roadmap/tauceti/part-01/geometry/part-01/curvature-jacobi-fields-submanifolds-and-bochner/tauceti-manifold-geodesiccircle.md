---
declaration: def
origin: cited
lean: TauCeti.Manifold.geodesicCircle
statement: formalized
---

# TauCeti.Manifold.geodesicCircle

The geodesic circle of radius `r` about `p` in the tangent plane framed by the linear isometry
`b : ℂ →ₗᵢ[ℝ] T_p M`, parametrized by the angle: the curve `θ ↦ exp_p (r • b (circleMap 0 1 θ))`.
As a function of `(r, θ)` it is the geodesic polar coordinate map. At a vector outside the domain
of the exponential map it takes the junk value of `riemannianExp`.

```lean
TauCeti.Manifold.geodesicCircle.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] {p : M}
  (b : ℂ →ₗᵢ[ℝ] TangentSpace I p) (r θ : ℝ) : M
```

## Depends on

- [TauCeti.Manifold.riemannianExp](../geodesics-the-exponential-map-and-the-hopf-rinow/tauceti-manifold-riemannianexp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.geodesicCircle`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Gauss/Polar/Circle.html#TauCeti.Manifold.geodesicCircle).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.geodesicCircle`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Gauss/Polar/Circle.html#TauCeti.Manifold.geodesicCircle)
- [Source of `TauCeti.Manifold.geodesicCircle` in TauCeti/Geometry/Manifold/Riemannian/Geodesic/Gauss/Polar/Circle.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Gauss/Polar/Circle.lean#L68)
- [Tau Ceti roadmap status: Curvature, Jacobi fields, submanifolds, and Bochner geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RiemannianGeometry/STATUS.md)
