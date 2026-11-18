---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.deriv_deriv_polarJacobian_add_sectionalCurvature_mul
statement: formalized
proof: formalized
---

# The scalar Jacobi equation for the polar Jacobian

Let `v` be a unit tangent vector at
`p` and `w` a tangent vector orthogonal to it, in dimension two. If `r • v` lies in the domain of
`exp_p` and the polar Jacobian `j = polarJacobian p v w` does not vanish at `r`, then
`j''(r) + K j(r) = 0`, where `K` is the sectional curvature at `exp_p (r v)` of the plane spanned
by `d(exp_p)_(r v)(r w)` and `d(exp_p)_(r v) v`.

```lean
TauCeti.Manifold.deriv_deriv_polarJacobian_add_sectionalCurvature_mul.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] {p : M} {v w : TangentSpace I p}
  {r : ℝ} (hmem : r • v ∈ TauCeti.Manifold.expDomain I M p)
  (hj : TauCeti.Manifold.polarJacobian p v w r ≠ 0) (hv : ‖v‖ = 1) (hvw : inner ℝ v w = 0)
  (hdim : Module.finrank ℝ (TangentSpace I (TauCeti.Manifold.riemannianExp I M p (r • v))) = 2) :
  deriv (deriv (TauCeti.Manifold.polarJacobian p v w)) r +
      (CovariantDerivative.leviCivitaConnection I M).sectionalCurvature ⋯
          (TauCeti.Manifold.riemannianExp I M p (r • v))
          ((mfderiv% (TauCeti.Manifold.riemannianExp I M p) (r • v)) (r • w))
          ((mfderiv% (TauCeti.Manifold.riemannianExp I M p) (r • v)) v) *
        TauCeti.Manifold.polarJacobian p v w r =
    0
```

## Depends on

- [TauCeti.Manifold.polarJacobian](tauceti-manifold-polarjacobian.md)
- [TauCeti.Manifold.riemannianExp](../geodesics-the-exponential-map-and-the-hopf-rinow/tauceti-manifold-riemannianexp.md)

## Proof depends on

- [The Gauss lemma](../geodesics-the-exponential-map-and-the-hopf-rinow/the-gauss-lemma.md)
- [The Koszul formula](../../part-02/manifold/part-03/the-koszul-formula.md)
- [TauCeti.Manifold.IsJacobiFieldOn](tauceti-manifold-isjacobifieldon.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.deriv_deriv_polarJacobian_add_sectionalCurvature_mul`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Gauss/Polar/JacobiEquation.html#TauCeti.Manifold.deriv_deriv_polarJacobian_add_sectionalCurvature_mul).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.deriv_deriv_polarJacobian_add_sectionalCurvature_mul`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Gauss/Polar/JacobiEquation.html#TauCeti.Manifold.deriv_deriv_polarJacobian_add_sectionalCurvature_mul)
- [Source of `TauCeti.Manifold.deriv_deriv_polarJacobian_add_sectionalCurvature_mul` in TauCeti/Geometry/Manifold/Riemannian/Geodesic/Gauss/Polar/JacobiEquation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Gauss/Polar/JacobiEquation.lean#L96)
- [Tau Ceti roadmap status: Curvature, Jacobi fields, submanifolds, and Bochner geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RiemannianGeometry/STATUS.md)
