---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.integral_sum_hessian_sq_add_ricci
statement: formalized
proof: formalized
---

# The integrated Bochner identity

For a compactly supported smooth function on a
boundaryless manifold, `∫ (|Hess f|² + Ric(grad f, grad f)) = ∫ (Δ f)²`.
Both integrands are integrable, and the identity holds in every pointwise orthonormal basis.

```lean
TauCeti.Manifold.integral_sum_hessian_sq_add_ricci.{u_1, u_2, u_3, u_4} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M] [I.Boundaryless] [MeasurableSpace M]
  [BorelSpace M] [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x]
  [IsContinuousRiemannianBundle E fun x => TangentSpace I x] {f : M → ℝ} {ι : Type u_4} [Fintype ι]
  [SigmaCompactSpace M] (hf : ContMDiff I (modelWithCornersSelf ℝ ℝ) (↑⊤) f)
  (hfc : HasCompactSupport f) (b : (x : M) → OrthonormalBasis ι ℝ (TangentSpace I x)) :
  ∫ (x : M),
      ∑ i, ∑ j, TauCeti.Manifold.hessian I f x ((b x) i) ((b x) j) ^ 2 +
        (((CovariantDerivative.leviCivitaConnection I M).ricciTensor x)
            (TauCeti.Manifold.mgradient I f x))
          (TauCeti.Manifold.mgradient I f x) ∂TauCeti.riemannianVolume I M =
    ∫ (x : M), TauCeti.Manifold.laplaceBeltrami I f x ^ 2 ∂TauCeti.riemannianVolume I M
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Bochner formula](../part-01/the-bochner-formula.md)
- [The divergence theorem on a manifold without boundary](../part-01/the-divergence-theorem-on-a-manifold-without-bou.md)
- [Green's first identity on a manifold without boundary](../part-01/greens-first-identity-on-a-manifold-without-boun.md)
- [The Koszul formula](the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.integral_sum_hessian_sq_add_ricci`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Bochner/Integral.html#TauCeti.Manifold.integral_sum_hessian_sq_add_ricci).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.integral_sum_hessian_sq_add_ricci`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Bochner/Integral.html#TauCeti.Manifold.integral_sum_hessian_sq_add_ricci)
- [Source of `TauCeti.Manifold.integral_sum_hessian_sq_add_ricci` in TauCeti/Geometry/Manifold/Riemannian/Bochner/Integral.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Riemannian/Bochner/Integral.lean#L99)
