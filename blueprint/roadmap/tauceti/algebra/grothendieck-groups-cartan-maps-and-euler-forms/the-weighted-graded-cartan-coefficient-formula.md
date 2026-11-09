---
declaration: theorem
origin: cited
lean: TauCeti.finrank_smul_simple_piece_zero_mul_coeff_gradedCartanMatrix
statement: formalized
proof: formalized
---

# The weighted graded Cartan coefficient formula

A coefficient in a column `[A f]`,
multiplied by `dim_k(eᵢ • (Sᵢ)₀)`, is the corresponding graded corner dimension.

```lean
TauCeti.finrank_smul_simple_piece_zero_mul_coeff_gradedCartanMatrix.{uk, uA, uI, uJ} {k : Type uk}
  [Field k] {A : Type uA} [Ring A] [Algebra k A] [Module.Finite k A] {𝒜 : ℤ → Submodule k A}
  {I : Type uI} (S : I → (TauCeti.gradedFiniteModules 𝒜).FullSubcategory) {e : I → A}
  (he : ∀ (i : I), IsIdempotentElem (e i)) (he₀ : ∀ (i : I), e i ∈ 𝒜 0)
  (hne : Pairwise fun i j => TauCeti.GradedModuleCat.smulGradedDimension (e i) (S j).obj = 0)
  (hself : ∀ (i : I), TauCeti.GradedModuleCat.smulGradedDimension (e i) (S i).obj ≠ 0)
  (hS : TauCeti.IsExhaustiveGradedSimpleFamily S) [GradedAlgebra 𝒜] {J : Type uJ} [Fintype J]
  [Finite I]
  (bP :
    Module.Basis J (LaurentPolynomial ℤ)
      (TauCeti.LaurentK0 (TauCeti.gradedFiniteProjectiveModulesExactStructure 𝒜)))
  {f : A} (hf : IsIdempotentElem f) (hF : Ideal.IsHomogeneous 𝒜 (Ideal.span {f})) (j : J)
  (hj :
    bP j =
      TauCeti.LaurentK0.of (TauCeti.gradedFiniteProjectiveModulesExactStructure 𝒜)
        { obj := TauCeti.GradedModuleCat.ofIdeal 𝒜 (Ideal.span {f}) hF, property := ⋯ })
  (i : I) (hconc : ∀ (p : ℤ), p ≠ 0 → (S i).obj.grading.piece ℤ p = ⊥) (p : ℤ) :
  ↑(Module.finrank k ↥(e i • (S i).obj.grading.piece ℤ 0)) *
      (TauCeti.gradedCartanMatrix 𝒜 bP
            (TauCeti.gradedSimpleClassBasisOfNeZero S he he₀ hne hself hS) i j).coeff
        p =
    ↑(Module.finrank k ↥(TauCeti.cornerSubmodule k (e i) f ⊓ 𝒜 p))
```

## Depends on

- [The graded Cartan matrix in a projective basis `bP` and a module basis `bM`](the-graded-cartan-matrix-in-a-projective-basis-b.md)

## Proof depends on

- [The dual Noether isomorphism](../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Noether isomorphism for exact categories](../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.finrank_smul_simple_piece_zero_mul_coeff_gradedCartanMatrix`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Coefficients.html#TauCeti.finrank_smul_simple_piece_zero_mul_coeff_gradedCartanMatrix).

## Sources

- [Tau Ceti documentation: `TauCeti.finrank_smul_simple_piece_zero_mul_coeff_gradedCartanMatrix`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Coefficients.html#TauCeti.finrank_smul_simple_piece_zero_mul_coeff_gradedCartanMatrix)
- [Source of `TauCeti.finrank_smul_simple_piece_zero_mul_coeff_gradedCartanMatrix` in TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Coefficients.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Coefficients.lean#L110)
