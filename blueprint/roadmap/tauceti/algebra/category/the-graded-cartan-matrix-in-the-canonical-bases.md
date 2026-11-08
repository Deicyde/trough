---
declaration: theorem
origin: cited
lean: TauCeti.coeff_zero_gradedCartanMatrix_gradedIdempotentProjectiveBasis
statement: formalized
proof: formalized
---

# The graded Cartan matrix in the canonical bases is the identity modulo `q`

the constant
term of its `(i, j)` entry is `1` if `i = j` and `0` otherwise.

```lean
TauCeti.coeff_zero_gradedCartanMatrix_gradedIdempotentProjectiveBasis.{uk, uA, uI} {k : Type uk}
  [Field k] {A : Type uA} [Ring A] [Algebra k A] [Module.Finite k A] {𝒜 : ℤ → Submodule k A}
  [GradedAlgebra 𝒜] {I : Type uI} [Fintype I] {e : I → A} (he : CompleteOrthogonalIdempotents e)
  (he₀ : ∀ (i : I), e i ∈ 𝒜 0) (hI : ∀ (i : I), Ideal.IsHomogeneous 𝒜 (Ideal.span {e i}))
  (hneg : ∀ p < 0, 𝒜 p = ⊥) (hspan : 𝒜 0 ≤ Submodule.span k (Set.range e))
  (hne : ∀ (i : I), e i ≠ 0) [DecidableEq I] (i j : I) :
  (TauCeti.gradedCartanMatrix 𝒜 (TauCeti.gradedIdempotentProjectiveBasis he he₀ hI hneg hspan hne)
          (TauCeti.gradedIdempotentHeadBasis hneg he he₀ hspan hne) i j).coeff
      0 =
    if i = j then 1 else 0
```

## Depends on

- [The graded Cartan matrix in a projective basis `bP` and a module basis `bM`](../grothendieck-groups-cartan-maps-and-euler-forms/part-01/the-graded-cartan-matrix-in-a-projective-basis-b.md)
- [The graded projectives `A eᵢ` form a basis of `K₀^gr(proj A)` over `ℤ[q,q⁻¹]`, for a nonnegatively graded finite-dimensional algebra whose degree-zero piece is spanned by a complete family of orthogonal nonzero idempotents `eᵢ`](../grothendieck-groups-cartan-maps-and-euler-forms/part-01/the-graded-projectives-a-ei-form-a-basis-of-k0-g.md)

## Proof depends on

- [The dual Noether isomorphism](../../category-theory/exact/the-dual-noether-isomorphism.md)
- [Jacobson's lemma](../../category-theory/preadditive/jacobsons-lemma.md)
- [The Noether isomorphism for exact categories](../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)
- [TauCeti.isLocalRing_end_of_indecomposable](../../category-theory/preadditive/tauceti-islocalring-end-of-indecomposable.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.coeff_zero_gradedCartanMatrix_gradedIdempotentProjectiveBasis`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Idempotent/Matrix.html#TauCeti.coeff_zero_gradedCartanMatrix_gradedIdempotentProjectiveBasis).

## Sources

- [Tau Ceti documentation: `TauCeti.coeff_zero_gradedCartanMatrix_gradedIdempotentProjectiveBasis`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Idempotent/Matrix.html#TauCeti.coeff_zero_gradedCartanMatrix_gradedIdempotentProjectiveBasis)
- [Source of `TauCeti.coeff_zero_gradedCartanMatrix_gradedIdempotentProjectiveBasis` in TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Idempotent/Matrix.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Idempotent/Matrix.lean#L109)
