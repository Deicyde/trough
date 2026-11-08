---
declaration: def
origin: cited
lean: TauCeti.gradedIdempotentProjectiveBasis
statement: formalized
---

# The graded projectives `A eᵢ` form a basis of `K₀^gr(proj A)` over `ℤ[q,q⁻¹]`, for a nonnegatively graded finite-dimensional algebra whose degree-zero piece is spanned by a complete family of orthogonal nonzero idempotents `eᵢ`

Its basis vector at `i` is the class `[A eᵢ]`. This
is the projective counterpart of the head basis `TauCeti.gradedIdempotentHeadBasis`, and the case of
`TauCeti.gradedIdempotentProjectiveBasisOfPrimitive` where each `eᵢ` is primitive by
`TauCeti.isPrimitiveIdempotent_of_gradeZero_le_span` and the `A eᵢ` are pairwise nonisomorphic by
`TauCeti.isEmpty_linearEquiv_span_singleton_of_gradeZero_le_span`.

```lean
TauCeti.gradedIdempotentProjectiveBasis.{uk, uA, uI} {k : Type uk} [Field k] {A : Type uA} [Ring A]
  [Algebra k A] {𝒜 : ℤ → Submodule k A} [GradedAlgebra 𝒜] {I : Type uI} [Fintype I] {e : I → A}
  (he : CompleteOrthogonalIdempotents e) (he₀ : ∀ (i : I), e i ∈ 𝒜 0)
  (hI : ∀ (i : I), Ideal.IsHomogeneous 𝒜 (Ideal.span {e i})) [Module.Finite k A]
  (hneg : ∀ p < 0, 𝒜 p = ⊥) (hspan : 𝒜 0 ≤ Submodule.span k (Set.range e))
  (hne : ∀ (i : I), e i ≠ 0) :
  Module.Basis I (LaurentPolynomial ℤ)
    (TauCeti.LaurentK0 (TauCeti.gradedFiniteProjectiveModulesExactStructure 𝒜))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The dual Noether isomorphism](../../../category-theory/exact/the-dual-noether-isomorphism.md)
- [Jacobson's lemma](../../../category-theory/preadditive/jacobsons-lemma.md)
- [The Noether isomorphism for exact categories](../../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)
- [TauCeti.isLocalRing_end_of_indecomposable](../../../category-theory/preadditive/tauceti-islocalring-end-of-indecomposable.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.gradedIdempotentProjectiveBasis`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Idempotent/Projective/Basic.html#TauCeti.gradedIdempotentProjectiveBasis).

## Sources

- [Tau Ceti documentation: `TauCeti.gradedIdempotentProjectiveBasis`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Idempotent/Projective/Basic.html#TauCeti.gradedIdempotentProjectiveBasis)
- [Source of `TauCeti.gradedIdempotentProjectiveBasis` in TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Idempotent/Projective/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Idempotent/Projective/Basic.lean#L417)
- [Tau Ceti roadmap status: Grothendieck groups, Cartan maps, and Euler forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GrothendieckEulerForms/STATUS.md)
