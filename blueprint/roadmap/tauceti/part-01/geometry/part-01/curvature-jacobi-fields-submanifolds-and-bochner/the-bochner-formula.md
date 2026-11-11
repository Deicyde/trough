---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.laplaceBeltrami_norm_sq_mgradient
statement: formalized
proof: formalized
---

# The Bochner formula

For a smooth function `f` and every orthonormal basis `eᵢ` of the
tangent space at `x`,
`Δ |grad f|² = 2 ∑ᵢⱼ Hess f(eᵢ, eⱼ)² + 2 d(Δ f)(grad f) + 2 Ric(grad f, grad f)`,
where `Δ = div ∘ grad` is `TauCeti.Manifold.laplaceBeltrami` and `Ric` is the Ricci tensor of the
Levi-Civita connection. For the nonnegative Laplacian `Δ⁺ = -Δ` this is
`Δ⁺ |df|² + 2 |Hess f|² + 2 Ric(grad f, grad f) = 2 ⟨df, d Δ⁺ f⟩`.

```lean
TauCeti.Manifold.laplaceBeltrami_norm_sq_mgradient.{u_1, u_2, u_3, u_4} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] {f : M → ℝ}
  (hf : ContMDiff I (modelWithCornersSelf ℝ ℝ) (↑⊤) f) (x : M) {ι : Type u_4} [Fintype ι]
  (b : OrthonormalBasis ι ℝ (TangentSpace I x)) :
  TauCeti.Manifold.laplaceBeltrami I (fun y => ‖TauCeti.Manifold.mgradient I f y‖ ^ 2) x =
    2 * ∑ i, ∑ j, TauCeti.Manifold.hessian I f x (b i) (b j) ^ 2 +
        2 * (d% (TauCeti.Manifold.laplaceBeltrami I f) x) (TauCeti.Manifold.mgradient I f x) +
      2 *
        (((CovariantDerivative.leviCivitaConnection I M).ricciTensor x)
            (TauCeti.Manifold.mgradient I f x))
          (TauCeti.Manifold.mgradient I f x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The contracted Ricci identity for the gradient](the-contracted-ricci-identity-for-the-gradient.md)
- [The Koszul formula](../../part-02/manifold/part-02/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.laplaceBeltrami_norm_sq_mgradient`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Bochner/Basic.html#TauCeti.Manifold.laplaceBeltrami_norm_sq_mgradient).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.laplaceBeltrami_norm_sq_mgradient`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Bochner/Basic.html#TauCeti.Manifold.laplaceBeltrami_norm_sq_mgradient)
- [Source of `TauCeti.Manifold.laplaceBeltrami_norm_sq_mgradient` in TauCeti/Geometry/Manifold/Riemannian/Bochner/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Riemannian/Bochner/Basic.lean#L165)
- [Tau Ceti roadmap status: Curvature, Jacobi fields, submanifolds, and Bochner geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RiemannianGeometry/STATUS.md)
