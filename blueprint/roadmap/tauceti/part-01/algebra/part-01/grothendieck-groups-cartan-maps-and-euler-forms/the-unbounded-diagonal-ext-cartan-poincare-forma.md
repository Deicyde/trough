---
declaration: theorem
origin: cited
lean: TauCeti.gradedCartanMatrix_trunc_transpose_mul_diagonalExtPowerSeries_eq_diagonal
statement: formalized
proof: formalized
---

# The unbounded diagonal-Ext Cartan–Poincaré formal power-series identity

Suppose `A` is
nonnegatively graded and every member of the exhaustive degree-zero simple family `Sᵢ` admits a
linear graded projective resolution (possibly of infinite length, with no minimality or semisimple
degree-zero assumption). Let `P_diag` be the formal power-series matrix with `(i, j)` entry
`∑ n, dim_k Extⁿ(Sᵢ, Sⱼ{n}) tⁿ`. Then
`C_psᵀ * P_diag(-q) = diagonal (fun i ↦ dim_k(eᵢ • (Sᵢ)₀))`.

```lean
TauCeti.gradedCartanMatrix_trunc_transpose_mul_diagonalExtPowerSeries_eq_diagonal.{uk, uA, uI}
  {k : Type uk} [Field k] {A : Type uA} [Ring A] [Algebra k A] {𝒜 : ℤ → Submodule k A}
  [GradedAlgebra 𝒜] [Module.Finite k A] [CategoryTheory.HasExt (TauCeti.GradedModuleCat 𝒜)]
  {I : Type uI} [Fintype I] [DecidableEq I]
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
  (hlin : ∀ (i : I), ∃ r, r.IsLinear) (hneg : ∀ p < 0, 𝒜 p = ⊥)
  (hconc : ∀ (i : I) (p : ℤ), p ≠ 0 → (S i).obj.grading.piece p = ⊥) :
  (((TauCeti.gradedCartanMatrix 𝒜 bP
              (TauCeti.gradedSimpleClassBasisOfNeZero S he he₀ hne hself hS)).map
          fun p => ↑(LaurentPolynomial.trunc p)).transpose *
      Matrix.of fun i j =>
        (PowerSeries.rescale (-1))
          (PowerSeries.mk fun n =>
            ↑(Module.finrank k
                (TauCeti.GradedExt (TauCeti.GradedModuleCat.shift 𝒜) (S i).obj (S j).obj n ↑n)))) =
    Matrix.diagonal fun i => PowerSeries.C ↑(Module.finrank k ↥(e i • (S i).obj.grading.piece 0))
```

## Depends on

- [The graded Cartan matrix in a projective basis `bP` and a module basis `bM`](the-graded-cartan-matrix-in-a-projective-basis-b.md)

## Proof depends on

- [The dual Noether isomorphism](../../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Noether isomorphism for exact categories](../../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)
- [TauCeti.Bigraded.eulerPowerSeries](tauceti-bigraded-eulerpowerseries.md)
- [TauCeti.bigradedExtPoincarePowerSeries](tauceti-bigradedextpoincarepowerseries.md)
- [The weighted graded Cartan coefficient formula](../../part-02/category/the-weighted-graded-cartan-coefficient-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.gradedCartanMatrix_trunc_transpose_mul_diagonalExtPowerSeries_eq_diagonal`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/ExtEuler/PowerSeries.html#TauCeti.gradedCartanMatrix_trunc_transpose_mul_diagonalExtPowerSeries_eq_diagonal).

## Sources

- [Tau Ceti documentation: `TauCeti.gradedCartanMatrix_trunc_transpose_mul_diagonalExtPowerSeries_eq_diagonal`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/ExtEuler/PowerSeries.html#TauCeti.gradedCartanMatrix_trunc_transpose_mul_diagonalExtPowerSeries_eq_diagonal)
- [Source of `TauCeti.gradedCartanMatrix_trunc_transpose_mul_diagonalExtPowerSeries_eq_diagonal` in TauCeti/Algebra/Category/GradedModuleCat/CartanMap/ExtEuler/PowerSeries.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/ExtEuler/PowerSeries.lean#L452)
