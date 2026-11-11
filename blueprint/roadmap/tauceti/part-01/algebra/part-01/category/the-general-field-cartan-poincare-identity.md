---
declaration: theorem
origin: cited
lean: TauCeti.gradedCartanMatrix_transpose_mul_diagonalExtPoincareMatrix_map_eq_diagonal
statement: formalized
proof: formalized
---

# The general-field Cartan--Poincaré identity

Let `C` be the
graded Cartan matrix in a projective basis of classes `[A eᵢ]` and the module basis
`[Sⱼ]`, with `gdim(eᵢ • Sⱼ) = 0` for `i ≠ j`. Suppose every pair of finite graded modules is
graded Euler-admissible, that every `Sᵢ` is concentrated in internal degree zero and has a linear
graded projective resolution, and that `b` bounds the cohomological support of Ext between any two
`Sᵢ`.
Then `Cᵀ · P(-q) = diagonal (fun i ↦ gdim(eᵢ • Sᵢ))`, where `P` is the diagonal Ext
Poincaré matrix truncated below `b`. Concentration makes these diagonal entries constant.

```lean
TauCeti.gradedCartanMatrix_transpose_mul_diagonalExtPoincareMatrix_map_eq_diagonal.{uk, uA, uI}
  {k : Type uk} [Field k] {A : Type uA} [Ring A] [Algebra k A] {𝒜 : ℤ → Submodule k A}
  [GradedAlgebra 𝒜] [Module.Finite k A] [CategoryTheory.HasExt (TauCeti.GradedModuleCat 𝒜)]
  {I : Type uI} [Fintype I] [DecidableEq I]
  (S : I → (TauCeti.gradedFiniteModules 𝒜).FullSubcategory) {e : I → A}
  (he : ∀ (i : I), IsIdempotentElem (e i)) (he₀ : ∀ (i : I), e i ∈ 𝒜 0)
  (hI : ∀ (i : I), Ideal.IsHomogeneous 𝒜 (Ideal.span {e i}))
  (hne : Pairwise fun i j => TauCeti.GradedModuleCat.smulGradedDimension (e i) (S j).obj = 0)
  (bP :
    Module.Basis I (LaurentPolynomial ℤ)
      (TauCeti.LaurentK0 (TauCeti.gradedFiniteProjectiveModulesExactStructure 𝒜)))
  (hbP :
    ∀ (i : I),
      bP i =
        TauCeti.LaurentK0.of (TauCeti.gradedFiniteProjectiveModulesExactStructure 𝒜)
          { obj := TauCeti.GradedModuleCat.ofIdeal 𝒜 (Ideal.span {e i}) ⋯, property := ⋯ })
  (bM :
    Module.Basis I (LaurentPolynomial ℤ)
      (TauCeti.LaurentK0 (TauCeti.gradedFiniteModulesExactStructure 𝒜)))
  (hbM : ∀ (i : I), bM i = TauCeti.LaurentK0.of (TauCeti.gradedFiniteModulesExactStructure 𝒜) (S i))
  (h :
    TauCeti.IsGradedEulerAdmissibleOn (TauCeti.gradedFiniteModules 𝒜)
      (TauCeti.gradedFiniteModules 𝒜))
  (hlin : ∀ (i : I), ∃ r, r.IsLinear)
  (hconc : ∀ (i : I) (p : ℤ), p ≠ 0 → (S i).obj.grading.piece ℤ p = ⊥) {b : ℕ}
  (hb :
    ∀ (i j : I),
      TauCeti.IsGradedExtBoundedBy (TauCeti.GradedModuleCat.shift 𝒜) (S i).obj (S j).obj b) :
  (TauCeti.gradedCartanMatrix 𝒜 bP bM).transpose *
      (TauCeti.diagonalExtPoincareMatrix k (fun i => (S i).obj) b).map
        ⇑(Polynomial.eval₂RingHom LaurentPolynomial.C (-LaurentPolynomial.T 1)) =
    Matrix.diagonal fun i => TauCeti.GradedModuleCat.smulGradedDimension (e i) (S i).obj
```

## Depends on

- [The graded Cartan matrix in a projective basis `bP` and a module basis `bM`](../grothendieck-groups-cartan-maps-and-euler-forms/the-graded-cartan-matrix-in-a-projective-basis-b.md)
- [TauCeti.GradedProjectiveResolution.IsLinear](../grothendieck-groups-cartan-maps-and-euler-forms/tauceti-gradedprojectiveresolution-islinear.md)

## Proof depends on

- [The dual Noether isomorphism](../../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Noether isomorphism for exact categories](../../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.gradedCartanMatrix_transpose_mul_diagonalExtPoincareMatrix_map_eq_diagonal`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/ExtEuler/Poincare.html#TauCeti.gradedCartanMatrix_transpose_mul_diagonalExtPoincareMatrix_map_eq_diagonal).

## Sources

- [Tau Ceti documentation: `TauCeti.gradedCartanMatrix_transpose_mul_diagonalExtPoincareMatrix_map_eq_diagonal`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/ExtEuler/Poincare.html#TauCeti.gradedCartanMatrix_transpose_mul_diagonalExtPoincareMatrix_map_eq_diagonal)
- [Source of `TauCeti.gradedCartanMatrix_transpose_mul_diagonalExtPoincareMatrix_map_eq_diagonal` in TauCeti/Algebra/Category/GradedModuleCat/CartanMap/ExtEuler/Poincare.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/ExtEuler/Poincare.lean#L117)
