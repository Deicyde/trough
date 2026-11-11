---
declaration: theorem
origin: cited
lean: TauCeti.cartan_poincare_of_bigradedExtPoincareMatrix_isDiagonal_of_semisimple
statement: formalized
proof: formalized
---

# The Cartan--Poincare identity over a semisimple degree-zero part

If `A` is
finite-dimensional and nonnegatively graded, its degree-zero part is semisimple, the chosen
simples are concentrated in degree zero, and their full bigraded Ext Poincare matrix is diagonal,
then `C^T * P(-q) = diagonal (fun i ↦ gdim(eᵢ • Sᵢ))`.

The diagonal entries are nonzero and need not be one; for projective covers of degree-zero
simples they are the constants `dim_k End_A(Sᵢ)`. The semisimplicity hypothesis supplies minimal
projective resolutions with finite-dimensional terms, so no resolutions or minimality witnesses
occur in the public statement.

```lean
TauCeti.cartan_poincare_of_bigradedExtPoincareMatrix_isDiagonal_of_semisimple.{uk, uA, uI}
  {k : Type uk} [Field k] {A : Type uA} [Ring A] [Algebra k A] {𝒜 : ℤ → Submodule k A}
  [GradedAlgebra 𝒜] [CategoryTheory.HasExt (TauCeti.GradedModuleCat 𝒜)] {I : Type uI}
  [Module.Finite k A] [Fintype I] [DecidableEq I]
  (S : I → (TauCeti.gradedFiniteModules 𝒜).FullSubcategory) {e : I → A}
  (he : ∀ (i : I), IsIdempotentElem (e i)) (he₀ : ∀ (i : I), e i ∈ 𝒜 0)
  (hI : ∀ (i : I), Ideal.IsHomogeneous 𝒜 (Ideal.span {e i}))
  (hne : Pairwise fun i j => TauCeti.GradedModuleCat.smulGradedDimension (e i) (S j).obj = 0)
  (hself : ∀ (i : I), TauCeti.GradedModuleCat.smulGradedDimension (e i) (S i).obj ≠ 0)
  (hS : TauCeti.IsExhaustiveGradedSimpleFamily S)
  (bP :
    Module.Basis I (LaurentPolynomial ℤ)
      (TauCeti.LaurentK0 (TauCeti.gradedFiniteProjectiveModulesExactStructure 𝒜)))
  (hbP :
    ∀ (i : I),
      bP i =
        TauCeti.LaurentK0.of (TauCeti.gradedFiniteProjectiveModulesExactStructure 𝒜)
          { obj := TauCeti.GradedModuleCat.ofIdeal 𝒜 (Ideal.span {e i}) ⋯, property := ⋯ })
  [IsSemisimpleRing ↥(𝒜 0)]
  (h :
    TauCeti.IsGradedEulerAdmissibleOn (TauCeti.gradedFiniteModules 𝒜)
      (TauCeti.gradedFiniteModules 𝒜))
  (hneg : ∀ p < 0, 𝒜 p = ⊥) (hconc : ∀ (i : I) (p : ℤ), p ≠ 0 → (S i).obj.grading.piece ℤ p = ⊥)
  {b : ℕ}
  (hb :
    ∀ (i j : I),
      TauCeti.IsGradedExtBoundedBy (TauCeti.GradedModuleCat.shift 𝒜) (S i).obj (S j).obj b)
  (hdiag :
    ∀ (i j : I),
      TauCeti.Bigraded.IsDiagonal
        (TauCeti.bigradedExtPoincareMatrix (fun i => (S i).obj) ⋯ b i j)) :
  (TauCeti.gradedCartanMatrix 𝒜 bP
          (TauCeti.gradedSimpleClassBasisOfNeZero S he he₀ hne hself hS)).transpose *
      (TauCeti.diagonalExtPoincareMatrix k (fun i => (S i).obj) b).map
        ⇑(Polynomial.eval₂RingHom LaurentPolynomial.C (-LaurentPolynomial.T 1)) =
    Matrix.diagonal fun i => TauCeti.GradedModuleCat.smulGradedDimension (e i) (S i).obj
```

## Depends on

- [The graded Cartan matrix in a projective basis `bP` and a module basis `bM`](the-graded-cartan-matrix-in-a-projective-basis-b.md)

## Proof depends on

- [The dual Noether isomorphism](../../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The general-field Cartan--Poincaré identity](../category/the-general-field-cartan-poincare-identity.md)
- [The Noether isomorphism for exact categories](../../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)
- [TauCeti.GradedProjectiveResolution.IsLinear](tauceti-gradedprojectiveresolution-islinear.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.cartan_poincare_of_bigradedExtPoincareMatrix_isDiagonal_of_semisimple`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/ExtEuler/Linearity.html#TauCeti.cartan_poincare_of_bigradedExtPoincareMatrix_isDiagonal_of_semisimple).

## Sources

- [Tau Ceti documentation: `TauCeti.cartan_poincare_of_bigradedExtPoincareMatrix_isDiagonal_of_semisimple`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/ExtEuler/Linearity.html#TauCeti.cartan_poincare_of_bigradedExtPoincareMatrix_isDiagonal_of_semisimple)
- [Source of `TauCeti.cartan_poincare_of_bigradedExtPoincareMatrix_isDiagonal_of_semisimple` in TauCeti/Algebra/Category/GradedModuleCat/CartanMap/ExtEuler/Linearity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/ExtEuler/Linearity.lean#L122)
