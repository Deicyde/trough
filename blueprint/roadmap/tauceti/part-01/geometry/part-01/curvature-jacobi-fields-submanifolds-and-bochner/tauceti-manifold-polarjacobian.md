---
declaration: def
origin: cited
lean: TauCeti.Manifold.polarJacobian
statement: formalized
---

# TauCeti.Manifold.polarJacobian

The polar Jacobian `‖d(exp_p)_(r v)(r w)‖` of the exponential map at `p`, for a radial
direction `v` and an angular vector `w`. In geodesic polar coordinates with angular arclength it is
the coefficient `j` of `F*g = dr² + j² dθ²`.

```lean
TauCeti.Manifold.polarJacobian.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] (p : M) (v w : TangentSpace I p)
  (r : ℝ) : ℝ
```

## Depends on

- [TauCeti.Manifold.riemannianExp](../geodesics-the-exponential-map-and-the-hopf-rinow/tauceti-manifold-riemannianexp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.polarJacobian`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Gauss/Polar/Jacobian.html#TauCeti.Manifold.polarJacobian).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.polarJacobian`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Gauss/Polar/Jacobian.html#TauCeti.Manifold.polarJacobian)
- [Source of `TauCeti.Manifold.polarJacobian` in TauCeti/Geometry/Manifold/Riemannian/Geodesic/Gauss/Polar/Jacobian.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Gauss/Polar/Jacobian.lean#L57)
- [Tau Ceti roadmap status: Curvature, Jacobi fields, submanifolds, and Bochner geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RiemannianGeometry/STATUS.md)
