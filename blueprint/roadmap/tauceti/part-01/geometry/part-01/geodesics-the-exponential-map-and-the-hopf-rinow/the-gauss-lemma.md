---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.inner_mfderiv_riemannianExp_radial, TauCeti.Manifold.inner_mfderiv_riemannianExp_model_space
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

## Proof depends on

- [The Koszul formula](../../part-02/manifold/part-02/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.inner_mfderiv_riemannianExp_radial`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Gauss/Basic.html#TauCeti.Manifold.inner_mfderiv_riemannianExp_radial).

## Other forms

**The Gauss lemma in an inner-product space.** Formalized in Tau Ceti as [`TauCeti.Manifold.inner_mfderiv_riemannianExp_model_space`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Euclidean.html#TauCeti.Manifold.inner_mfderiv_riemannianExp_model_space).

```lean
TauCeti.Manifold.inner_mfderiv_riemannianExp_model_space.{u_1} {F : Type u_1} [NormedAddCommGroup F]
  [InnerProductSpace ℝ F] [FiniteDimensional ℝ F] (p : F)
  (v w₁ w₂ : TangentSpace (modelWithCornersSelf ℝ F) p) :
  inner ℝ ((mfderiv% (TauCeti.Manifold.riemannianExp (modelWithCornersSelf ℝ F) F p) v) w₁)
      ((mfderiv% (TauCeti.Manifold.riemannianExp (modelWithCornersSelf ℝ F) F p) v) w₂) =
    inner ℝ w₁ w₂
```

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.inner_mfderiv_riemannianExp_radial`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Gauss/Basic.html#TauCeti.Manifold.inner_mfderiv_riemannianExp_radial)
- [Source of `TauCeti.Manifold.inner_mfderiv_riemannianExp_radial` in TauCeti/Geometry/Manifold/Riemannian/Geodesic/Gauss/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Gauss/Basic.lean#L145)
- [Tau Ceti roadmap status: Geodesics, the exponential map, and the Hopf–Rinow theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/HopfRinow/STATUS.md)
