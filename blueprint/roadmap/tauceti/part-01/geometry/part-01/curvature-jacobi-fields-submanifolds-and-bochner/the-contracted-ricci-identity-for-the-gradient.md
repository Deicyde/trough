---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.sum_inner_secondCovariantDerivative_mgradient_self
statement: formalized
proof: formalized
---

# The contracted Ricci identity for the gradient

In every orthonormal basis `eᵢ` of the
tangent space at `x`, `∑ᵢ ⟪∇²(grad f)(eᵢ, eᵢ), w⟫ = d(Δ f)(w) + Ric(w, grad f)`, where
`Δ = div ∘ grad` is `TauCeti.Manifold.laplaceBeltrami`. Equivalently, the rough Laplacian of
`grad f` is `grad Δ f + Ric(grad f)`.

```lean
TauCeti.Manifold.sum_inner_secondCovariantDerivative_mgradient_self.{u_1, u_2, u_3, u_4}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] {f : M → ℝ}
  (hf : ContMDiff I (modelWithCornersSelf ℝ ℝ) (↑⊤) f) (x : M) {ι : Type u_4} [Fintype ι]
  (b : OrthonormalBasis ι ℝ (TangentSpace I x)) (w : TangentSpace I x) :
  ∑ i,
      inner ℝ
        ((((CovariantDerivative.leviCivitaConnection I M).secondCovariantDerivative
              (CovariantDerivative.leviCivitaConnection I M) (TauCeti.Manifold.mgradient I f) x)
            (b i))
          (b i))
        w =
    (d% (TauCeti.Manifold.laplaceBeltrami I f) x) w +
      (((CovariantDerivative.leviCivitaConnection I M).ricciTensor x) w)
        (TauCeti.Manifold.mgradient I f x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Koszul formula](../../part-02/manifold/part-02/the-koszul-formula.md)
- [The Ricci identity](../../part-02/manifold/part-03/the-ricci-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.sum_inner_secondCovariantDerivative_mgradient_self`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Bochner/Basic.html#TauCeti.Manifold.sum_inner_secondCovariantDerivative_mgradient_self).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.sum_inner_secondCovariantDerivative_mgradient_self`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Bochner/Basic.html#TauCeti.Manifold.sum_inner_secondCovariantDerivative_mgradient_self)
- [Source of `TauCeti.Manifold.sum_inner_secondCovariantDerivative_mgradient_self` in TauCeti/Geometry/Manifold/Riemannian/Bochner/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Riemannian/Bochner/Basic.lean#L125)
