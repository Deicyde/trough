---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.inner_mfderiv_riemannianExp_radial
statement: formalized
proof: formalized
---

# The Gauss lemma

The differential of the Riemannian exponential map preserves the inner
product with the radial direction at every vector in its natural domain.

```lean
TauCeti.Manifold.inner_mfderiv_riemannianExp_radial.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [FiniteDimensional ℝ E] [Bundle.RiemannianBundle fun x => TangentSpace I x] [IsManifold I (↑⊤) M]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] [I.Boundaryless] [T2Space M]
  {p : M} {v w : TangentSpace I p} (hv : v ∈ TauCeti.Manifold.expDomain I M p) :
  inner ℝ ((mfderiv% (TauCeti.Manifold.riemannianExp I M p) v) v)
      ((mfderiv% (TauCeti.Manifold.riemannianExp I M p) v) w) =
    inner ℝ v w
```

## Depends on

- [TauCeti.Manifold.riemannianExp](tauceti-manifold-riemannianexp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.inner_mfderiv_riemannianExp_radial`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Gauss/Basic.html#TauCeti.Manifold.inner_mfderiv_riemannianExp_radial).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.inner_mfderiv_riemannianExp_radial`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Gauss/Basic.html#TauCeti.Manifold.inner_mfderiv_riemannianExp_radial)
- [Source of `TauCeti.Manifold.inner_mfderiv_riemannianExp_radial` in TauCeti/Geometry/Manifold/Riemannian/Geodesic/Gauss/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Gauss/Basic.lean#L142)
- [Tau Ceti roadmap status: Geodesics, the exponential map, and the Hopf–Rinow theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/HopfRinow/STATUS.md)
