---
declaration: module
origin: cited
lean: ProbabilisticTheory.AlgState.fluctuationMap, ProbabilisticTheory.AlgState.fluctuationMap_apply, ProbabilisticTheory.AlgState.covarianceForm, ProbabilisticTheory.AlgState.covarianceForm_apply, ProbabilisticTheory.AlgState.covarianceForm_smul_left, ProbabilisticTheory.AlgState.covarianceForm_smul_right, ProbabilisticTheory.AlgState.covarianceForm_sum_left, ProbabilisticTheory.AlgState.covarianceForm_sum_right
statement: formalized
proof: formalized
---

# The covariance form of a state and its symmetries

The module `PhyslibAlpha.ProbabilisticTheory.StarAlgebra.CovarianceForm`, [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceForm.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceForm.lean): 18 declarations, 12 with a docstring.

## i. Overview

> A state `ω` on a unital `*`-algebra `A` has the covariance form
> `C(a, b) = ω(a⋆ b) - conj (ω a) ω(b)`, the inner product of the fluctuations `a - ω(a)` and
> `b - ω(b)` in the pre-Hilbert space of the state. It is antilinear in `a` and linear in `b`. For
> observables, `C(a, b) = Cov(a, b) + i ω⟨⁅a, b⁆⟩`, so `C` contains both matrices `Σ` and `Ω` of
> Robertson's relation.
>
> If `ω` is invariant under a `⋆`-automorphism `σ`, then `C(σ a, σ b) = C(a, b)`. If `σ` acts on
> two finite families of elements by the matrices `R` and `S`, the matrix of covariances `M`
> satisfies `Rᴴ M S = M`. When `R` is unitary this says `M S = R M`, so `M` is an intertwining map,
> and by Schur's lemma it vanishes when a group acts on the two families by inequivalent
> irreducible representations. For one-dimensional representations this says that elements
> transforming with different characters have covariance zero. With `ℤ/2` it gives the vanishing of
> the covariance between an even and an odd element; with translations it gives the vanishing of
> the covariance between different crystal momenta.

## ii. Key results

> - `AlgState.covarianceForm` : the covariance form `C(a, b) = ω(a⋆ b) - conj (ω a) ω(b)`.
> - `AlgState.covarianceForm_selfAdjoint` : `C(a, b) = Cov(a, b) + i ω⟨⁅a, b⁆⟩` for observables.
> - `AlgState.covarianceForm_map` : a symmetry of the state preserves `C`.
> - `AlgState.posSemidef_covarianceMatrixForm` : the matrix of `C` on a family is positive
>   semidefinite.
> - `AlgState.conjTranspose_mul_covarianceMatrixForm_mul` : `Rᴴ M S = M`.
> - `AlgState.covarianceForm_eq_zero_of_character` : elements transforming with different
>   unitary characters have covariance zero.
> - `AlgState.covarianceMatrixForm_eq_zero_of_irreducible` : **Schur's lemma** for covariances,
>   families transforming under inequivalent irreducible unitary representations have covariance
>   zero.

## iv. References

> * E. Wigner, Group Theory and its Application to the Quantum Mechanics of Atomic Spectra,
>   Chapter 21.

## A. The covariance form

**`ProbabilisticTheory.AlgState.fluctuationMap`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceForm.lean#L74).

> The fluctuation `a - ω(a)` of an element, as a linear map.

```lean
def fluctuationMap : A →ₗ[ℂ] A
```

**`ProbabilisticTheory.AlgState.fluctuationMap_apply`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceForm.lean#L79).

```lean
lemma fluctuationMap_apply (a : A) : ω.fluctuationMap a = a - ω a • 1
```

**`ProbabilisticTheory.AlgState.covarianceForm`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceForm.lean#L83).

> The covariance form `C(a, b) = ω(a⋆ b) - conj (ω a) ω(b)`, the inner product of the
> fluctuations in the pre-Hilbert space of the state.

```lean
noncomputable def covarianceForm (a b : A) : ℂ
```

**`ProbabilisticTheory.AlgState.covarianceForm_apply`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceForm.lean#L86).

```lean
lemma covarianceForm_apply (a b : A) :
    ω.covarianceForm a b = ω (star a * b) - star (ω a) * ω b
```

**`ProbabilisticTheory.AlgState.covarianceForm_smul_left`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceForm.lean#L98).

```lean
lemma covarianceForm_smul_left (c : ℂ) (a b : A) :
    ω.covarianceForm (c • a) b = star c * ω.covarianceForm a b
```

**`ProbabilisticTheory.AlgState.covarianceForm_smul_right`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceForm.lean#L103).

```lean
lemma covarianceForm_smul_right (c : ℂ) (a b : A) :
    ω.covarianceForm a (c • b) = c * ω.covarianceForm a b
```

**`ProbabilisticTheory.AlgState.covarianceForm_sum_left`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceForm.lean#L107).

```lean
lemma covarianceForm_sum_left {ι : Type*} (s : Finset ι) (a : ι → A) (b : A) :
    ω.covarianceForm (∑ i ∈ s, a i) b = ∑ i ∈ s, ω.covarianceForm (a i) b
```

**`ProbabilisticTheory.AlgState.covarianceForm_sum_right`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceForm.lean#L111).

```lean
lemma covarianceForm_sum_right {ι : Type*} (s : Finset ι) (a : A) (b : ι → A) :
    ω.covarianceForm a (∑ i ∈ s, b i) = ∑ i ∈ s, ω.covarianceForm a (b i)
```

**`ProbabilisticTheory.AlgState.covarianceForm_selfAdjoint`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceForm.lean#L116).

> For observables, `C(a, b) = Cov(a, b) + i ω⟨⁅a, b⁆⟩`.

```lean
lemma covarianceForm_selfAdjoint (a b : selfAdjoint A) :
    ω.covarianceForm a b = ω.covariance a b + Complex.I * ω.bracket a b
```

## B. Symmetries

**`ProbabilisticTheory.AlgState.covarianceForm_map`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceForm.lean#L132).

> **A symmetry of the state preserves the covariance form**: `C(σ a, σ b) = C(a, b)`.

```lean
lemma covarianceForm_map (a b : A) : ω.covarianceForm (σ a) (σ b) = ω.covarianceForm a b
```

**`ProbabilisticTheory.AlgState.covarianceForm_eq_zero_of_smul`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceForm.lean#L138).

> Elements multiplied by `χ` and `χ'` under a symmetry, with `conj χ · χ' ≠ 1`, have
> covariance zero.

```lean
lemma covarianceForm_eq_zero_of_smul {a b : A} {χ χ' : ℂ} (ha : σ a = χ • a) (hb : σ b = χ' • b)
    (h : star χ * χ' ≠ 1) : ω.covarianceForm a b = 0
```

**`ProbabilisticTheory.AlgState.covarianceForm_eq_zero_of_neg`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceForm.lean#L146).

> **An even and an odd element have covariance zero.**

```lean
lemma covarianceForm_eq_zero_of_neg {a b : A} (ha : σ a = a) (hb : σ b = -b) :
    ω.covarianceForm a b = 0
```

**`ProbabilisticTheory.AlgState.covarianceForm_eq_zero_of_character`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceForm.lean#L160).

> **Elements transforming with different unitary characters have covariance zero.** If
> `α g a = χ g • a` and `α g b = χ' g • b` with `|χ g| = 1` and `χ ≠ χ'`, then `C(a, b) = 0`.

```lean
lemma covarianceForm_eq_zero_of_character {a b : A} {χ χ' : Γ → ℂ} (hχ : ∀ g, ‖χ g‖ = 1)
    (ha : ∀ g, α g a = χ g • a) (hb : ∀ g, α g b = χ' g • b) (hne : χ ≠ χ') :
    ω.covarianceForm a b = 0
```

## C. Matrices of covariances

**`ProbabilisticTheory.AlgState.covarianceMatrixForm`**, a def, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceForm.lean#L179).

> The matrix `M_ik = C(a_i, b_k)` of covariances of two families.

```lean
noncomputable def covarianceMatrixForm (a : ι → A) (b : κ → A) : Matrix ι κ ℂ
```

**`ProbabilisticTheory.AlgState.posSemidef_covarianceMatrixForm`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceForm.lean#L185).

> **The matrix of covariances of a family is positive semidefinite**, being a Gram matrix.

```lean
lemma posSemidef_covarianceMatrixForm (a : ι → A) : (ω.covarianceMatrixForm a a).PosSemidef
```

**`ProbabilisticTheory.AlgState.conjTranspose_mul_covarianceMatrixForm_mul`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceForm.lean#L195).

> **A symmetry of the state preserves the matrix of covariances**: if `σ` acts on the two
> families by the matrices `R` and `S`, then `Rᴴ M S = M`.

```lean
lemma conjTranspose_mul_covarianceMatrixForm_mul (σ : A ≃⋆ₐ[ℂ] A) (hω : ∀ x, ω (σ x) = ω x)
    {a : ι → A} {b : κ → A} {R : Matrix ι ι ℂ} {S : Matrix κ κ ℂ}
    (ha : ∀ i, σ (a i) = ∑ j, R j i • a j) (hb : ∀ k, σ (b k) = ∑ l, S l k • b l) :
    Rᴴ * ω.covarianceMatrixForm a b * S = ω.covarianceMatrixForm a b
```

## D. Schur's lemma

**`ProbabilisticTheory.AlgState.covarianceMatrixForm_isIntertwining`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceForm.lean#L221).

> If `α` acts on the families `a` and `b` by `ρ` and `π`, with `ρ` unitary, then the matrix of
> covariances intertwines `π` with `ρ`.

```lean
lemma covarianceMatrixForm_isIntertwining {a : ι → A} {b : κ → A}
    (hρ : ∀ g, LinearMap.toMatrix' (ρ g) ∈ unitaryGroup ι ℂ)
    (ha : ∀ g i, α g (a i) = ∑ j, LinearMap.toMatrix' (ρ g) j i • a j)
    (hb : ∀ g k, α g (b k) = ∑ l, LinearMap.toMatrix' (π g) l k • b l) (g : Γ) :
    toLin' (ω.covarianceMatrixForm a b) ∘ₗ π g =
      ρ g ∘ₗ toLin' (ω.covarianceMatrixForm a b)
```

**`ProbabilisticTheory.AlgState.covarianceMatrixForm_eq_zero_of_irreducible`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceForm.lean#L246).

> **Schur's lemma for covariances.** If a group of symmetries of the state acts on the family
> `a` by the irreducible unitary representation `ρ` and on the family `b` by the irreducible
> representation `π`, and `π` and `ρ` are not equivalent, then `C(a_i, b_k) = 0` for all `i, k`.

```lean
lemma covarianceMatrixForm_eq_zero_of_irreducible [ρ.IsIrreducible] [π.IsIrreducible]
    [IsEmpty (π.Equiv ρ)] {a : ι → A} {b : κ → A}
    (hρ : ∀ g, LinearMap.toMatrix' (ρ g) ∈ unitaryGroup ι ℂ)
    (ha : ∀ g i, α g (a i) = ∑ j, LinearMap.toMatrix' (ρ g) j i • a j)
    (hb : ∀ g k, α g (b k) = ∑ l, LinearMap.toMatrix' (π g) l k • b l) :
    ω.covarianceMatrixForm a b = 0
```

## Depends on

- [Uncertainty relations for states on a `*`-algebra](stateuncertainty.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceForm.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/CovarianceForm.lean)
