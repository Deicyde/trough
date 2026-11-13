---
declaration: module
origin: cited
lean: ProbabilisticTheory.AlgState.apply_nonneg, ProbabilisticTheory.AlgState.star_dotProduct_covarianceMatrixForm_mulVec, ProbabilisticTheory.AlgState.covarianceForm_sub_covarianceForm_map, ProbabilisticTheory.AlgState.covarianceForm_map_le, ProbabilisticTheory.AlgState.covarianceMatrixForm_map_le, Matrix.sq_sum_le_sum_sq, Matrix.kadison, ProbabilisticTheory.AlgState.covarianceForm_map_le_of_positive
statement: formalized
proof: formalized
---

# Covariances do not decrease under unital maps

The module `PhyslibAlpha.ProbabilisticTheory.StarAlgebra.CovarianceFormUnitalMap`, [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceFormUnitalMap.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceFormUnitalMap.lean): 15 declarations, 13 with a docstring.

## i. Overview

> Let `Φ : A → B` be a linear map of unital `*`-algebras, `ω` a state on `B` and `ω'` the state
> `ω ∘ Φ` on `A`. The map `Φ` moves observables (Heisenberg picture), and `ω'` is the state `ω`
> after the dual map. We compare the covariance forms `C` of the two states.
>
> * **Schwarz maps.** If `Φ(X)⋆ Φ(X) ≤ Φ(X⋆ X)`, the Kadison–Schwarz inequality, which holds for
>   completely positive unital maps, then `C_ω(Φ X, Φ X) ≤ C_ω'(X, X)`: the difference is
>   `ω(Φ(X⋆ X) - Φ(X)⋆ Φ(X))`. Taking `X = ∑ cⱼ Xⱼ`, the same holds for the quadratic form of the
>   matrix of covariances of a family at every complex `c`, so commutator part included.
> * **Positive maps of matrices.** Kadison's inequality `Φ(A)² ≤ Φ(A²)` for Hermitian `A` gives
>   the same bound for Hermitian matrices, and for the matrix of covariances of Hermitian matrices
>   at real `c`. Writing `A = ∑ λₖ Pₖ` with orthogonal projections, `Qₖ = Φ(Pₖ)` are positive with
>   `∑ Qₖ = 1`, and `Φ(A²) - Φ(A)² = ∑ₖ (λₖ - Φ A) Qₖ (λₖ - Φ A)`.
> * **The gap.** The transpose of `2 × 2` matrices is positive and unital, but the bound fails for
>   the non-Hermitian matrix `E₀₁`.

## ii. Key results

> - `AlgState.apply_nonneg` : on a star-ordered ring a state is nonnegative on nonnegative elements.
> - `AlgState.covarianceForm_map_le` : a Schwarz inequality for `Φ` bounds the covariance form.
> - `AlgState.covarianceMatrixForm_map_le` : Schwarz maps do not decrease the matrix of
>   covariances.
> - `Matrix.kadison` : Kadison's inequality for positive unital maps of matrices.
> - `AlgState.covarianceForm_map_le_of_positive` : positive unital maps do not decrease the
>   covariance form of Hermitian matrices.
> - `AlgState.covarianceMatrixForm_map_le_of_positive` : nor the matrix of covariances of
>   Hermitian matrices at real coefficients.
> - `Matrix.transposeMap_gap` : the transpose is positive and unital but increases the covariance
>   form of `E₀₁` after the map.

## iv. References

> * R. V. Kadison, *A generalized Schwarz inequality and algebraic invariants for operator
>   algebras*, Ann. of Math. 56 (1952), 494–503.
> * M.-D. Choi, *A Schwarz inequality for positive linear maps on C*-algebras*, Illinois J. Math.
>   18 (1974), 565–574.

## A. Positivity of a state

**`ProbabilisticTheory.AlgState.apply_nonneg`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceFormUnitalMap.lean#L78).

> On a star-ordered ring a state is nonnegative on every nonnegative element.

```lean
lemma apply_nonneg {a : A} (ha : 0 ≤ a) : 0 ≤ ω a
```

## B. Schwarz maps

**`ProbabilisticTheory.AlgState.star_dotProduct_covarianceMatrixForm_mulVec`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceFormUnitalMap.lean#L100).

> The quadratic form of the matrix of covariances at `c` is the covariance form of `∑ cⱼ aⱼ`
> with itself.

```lean
lemma star_dotProduct_covarianceMatrixForm_mulVec {ι : Type*} [Fintype ι] (ω : AlgState A)
    (a : ι → A) (c : ι → ℂ) :
    star c ⬝ᵥ (ω.covarianceMatrixForm a a *ᵥ c) =
      ω.covarianceForm (∑ j, c j • a j) (∑ j, c j • a j)
```

**`ProbabilisticTheory.AlgState.covarianceForm_sub_covarianceForm_map`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceFormUnitalMap.lean#L114).

> Pulling the observable through `Φ` and pushing the state differ by the value of `ω` on
> `Φ(X⋆ X) - Φ(X)⋆ Φ(X)`.

```lean
lemma covarianceForm_sub_covarianceForm_map (hω' : ∀ x, ω' x = ω (Φ x)) (X : A) :
    ω'.covarianceForm X X - ω.covarianceForm (Φ X) (Φ X) =
      ω (Φ (star X * X) - star (Φ X) * Φ X)
```

**`ProbabilisticTheory.AlgState.covarianceForm_map_le`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceFormUnitalMap.lean#L126).

> **A Schwarz inequality for `Φ` bounds the covariance form**: if
> `Φ(X)⋆ Φ(X) ≤ Φ(X⋆ X)`, then `C_ω(Φ X, Φ X) ≤ C_ω'(X, X)`.

```lean
lemma covarianceForm_map_le (hω' : ∀ x, ω' x = ω (Φ x)) {X : A}
    (h : star (Φ X) * Φ X ≤ Φ (star X * X)) :
    ω.covarianceForm (Φ X) (Φ X) ≤ ω'.covarianceForm X X
```

**`ProbabilisticTheory.AlgState.covarianceMatrixForm_map_le`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceFormUnitalMap.lean#L134).

> **Maps satisfying the Schwarz inequality do not decrease the matrix of covariances.** The
> hypothesis holds for completely positive unital maps.

```lean
lemma covarianceMatrixForm_map_le {ι : Type*} [Fintype ι] (hω' : ∀ x, ω' x = ω (Φ x))
    (hΦ : ∀ X, star (Φ X) * Φ X ≤ Φ (star X * X)) (a : ι → A) (c : ι → ℂ) :
    star c ⬝ᵥ (ω.covarianceMatrixForm (Φ ∘ a) (Φ ∘ a) *ᵥ c) ≤
      star c ⬝ᵥ (ω'.covarianceMatrixForm a a *ᵥ c)
```

## C. Kadison's inequality

**`Matrix.sq_sum_le_sum_sq`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceFormUnitalMap.lean#L157).

> With positive `Qₖ` summing to `1`, `(∑ λₖ Qₖ)² ≤ ∑ λₖ² Qₖ`.

```lean
lemma sq_sum_le_sum_sq {ι : Type*} [Fintype ι] (Q : ι → Matrix m m ℂ)
    (hQ : ∀ k, (Q k).PosSemidef) (h1 : ∑ k, Q k = 1) (c : ι → ℝ) :
    (∑ k, (c k : ℂ) • Q k) * ∑ k, (c k : ℂ) • Q k ≤ ∑ k, ((c k : ℂ) * c k) • Q k
```

**`Matrix.kadison`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceFormUnitalMap.lean#L184).

> **Kadison's inequality**: for a positive unital map and Hermitian `A`,
> `Φ(A)² ≤ Φ(A²)`.

```lean
lemma kadison (Φ : Matrix n n ℂ →ₚ₁[ℂ] Matrix m m ℂ) {A : Matrix n n ℂ}
    (hA : A.IsHermitian) : (Φ A)ᴴ * Φ A ≤ Φ (Aᴴ * A)
```

## D. Positive maps of matrices

**`ProbabilisticTheory.AlgState.covarianceForm_map_le_of_positive`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceFormUnitalMap.lean#L243).

> **Positive unital maps do not decrease the covariance form of Hermitian matrices.**

```lean
lemma covarianceForm_map_le_of_positive (hω' : ∀ x, ω' x = ω (Φ x)) {X : Matrix n n ℂ}
    (hX : X.IsHermitian) : ω.covarianceForm (Φ X) (Φ X) ≤ ω'.covarianceForm X X
```

**`ProbabilisticTheory.AlgState.covarianceMatrixForm_map_le_of_positive`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceFormUnitalMap.lean#L249).

> **Positive unital maps do not decrease the matrix of covariances** of Hermitian matrices at
> real coefficients.

```lean
lemma covarianceMatrixForm_map_le_of_positive {ι : Type*} [Fintype ι]
    (hω' : ∀ x, ω' x = ω (Φ x)) {a : ι → Matrix n n ℂ} (ha : ∀ i, (a i).IsHermitian)
    (c : ι → ℝ) :
    star (fun i => (c i : ℂ)) ⬝ᵥ (ω.covarianceMatrixForm (Φ ∘ a) (Φ ∘ a) *ᵥ fun i => (c i : ℂ)) ≤
      star (fun i => (c i : ℂ)) ⬝ᵥ (ω'.covarianceMatrixForm a a *ᵥ fun i => (c i : ℂ))
```

## E. The transpose

**`Matrix.stateZero`**, a def, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceFormUnitalMap.lean#L270).

> The state `X ↦ X₀₀` of `2 × 2` matrices, the vector state of `|0⟩`.

```lean
def stateZero : ProbabilisticTheory.AlgState (Matrix (Fin 2) (Fin 2) ℂ)
```

**`Matrix.stateZero_apply`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceFormUnitalMap.lean#L281).

```lean
lemma stateZero_apply (X : Matrix (Fin 2) (Fin 2) ℂ) : stateZero X = X 0 0
```

**`Matrix.transposeMap`**, a def, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceFormUnitalMap.lean#L284).

> The transpose of `2 × 2` matrices.

```lean
noncomputable def transposeMap : Matrix (Fin 2) (Fin 2) ℂ →ₚ₁[ℂ] Matrix (Fin 2) (Fin 2) ℂ
```

**`Matrix.transposeMap_apply`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceFormUnitalMap.lean#L290).

```lean
lemma transposeMap_apply (X : Matrix (Fin 2) (Fin 2) ℂ) : transposeMap X = Xᵀ
```

**`Matrix.stateZero_transposeMap`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceFormUnitalMap.lean#L293).

> The state `X ↦ X₀₀` is unchanged by the transpose.

```lean
lemma stateZero_transposeMap (X : Matrix (Fin 2) (Fin 2) ℂ) :
    stateZero X = stateZero (transposeMap X)
```

**`Matrix.transposeMap_gap`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceFormUnitalMap.lean#L298).

> **The transpose is positive and unital, but the bound fails for `E₀₁`**: for positive maps
> it holds only on Hermitian matrices.

```lean
lemma transposeMap_gap :
    ¬ stateZero.covarianceForm (transposeMap (single 0 1 1)) (transposeMap (single 0 1 1)) ≤
      stateZero.covarianceForm (single 0 1 1) (single 0 1 1)
```

## Depends on

- [The covariance form of a state and its symmetries](covarianceform.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceFormUnitalMap.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceFormUnitalMap.lean)
