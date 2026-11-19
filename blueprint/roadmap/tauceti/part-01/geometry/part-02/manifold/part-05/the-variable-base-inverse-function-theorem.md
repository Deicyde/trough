---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.isLocalDiffeomorphAt_prodMk_proj_riemannianExp_zeroSection
statement: formalized
proof: formalized
---

# The variable-base inverse function theorem

The map `(x, v) ↦ (x, exp_x v)` from the
tangent bundle to `M × M` is a local diffeomorphism at every zero vector.

```lean
TauCeti.Manifold.isLocalDiffeomorphAt_prodMk_proj_riemannianExp_zeroSection.{u_1, u_2, u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M] [T2Space M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] (p : M) :
  IsLocalDiffeomorphAt I.tangent (I.prod I) (↑⊤)
    (fun z => (z.proj, TauCeti.Manifold.riemannianExp I M z.proj z.snd))
    (Bundle.zeroSection E (TangentSpace I) p)
```

## Depends on

- [TauCeti.Manifold.riemannianExp](../../../part-01/geodesics-the-exponential-map-and-the-hopf-rinow/tauceti-manifold-riemannianexp.md)

## Proof depends on

- [The inverse function theorem for manifolds](../part-02/the-inverse-function-theorem-for-manifolds.md)
- [The Koszul formula](../part-03/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.isLocalDiffeomorphAt_prodMk_proj_riemannianExp_zeroSection`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Exponential/VariableBase.html#TauCeti.Manifold.isLocalDiffeomorphAt_prodMk_proj_riemannianExp_zeroSection).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.isLocalDiffeomorphAt_prodMk_proj_riemannianExp_zeroSection`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Exponential/VariableBase.html#TauCeti.Manifold.isLocalDiffeomorphAt_prodMk_proj_riemannianExp_zeroSection)
- [Source of `TauCeti.Manifold.isLocalDiffeomorphAt_prodMk_proj_riemannianExp_zeroSection` in TauCeti/Geometry/Manifold/Riemannian/Geodesic/Exponential/VariableBase.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Exponential/VariableBase.lean#L130)
