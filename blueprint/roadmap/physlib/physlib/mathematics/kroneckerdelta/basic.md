---
declaration: module
origin: cited
lean: KroneckerDelta.kroneckerDelta, KroneckerDelta.eq_one_of_same, KroneckerDelta.eq_zero_of_ne, KroneckerDelta.eq_of_coe, KroneckerDelta.eq_zero_of_not, KroneckerDelta.kroneckerDelta_finSumFinEquiv, KroneckerDelta.smul_of_eq_zero, KroneckerDelta.smul_eq_zero_iff
statement: formalized
proof: formalized
---

# Kronecker delta

The module `Physlib.Mathematics.KroneckerDelta.Basic`, [Physlib/Mathematics/KroneckerDelta/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Basic.lean): 23 declarations, 5 with a docstring.

## i. Overview

> This module defines the Kronecker delta `kroneckerDelta i j` (notation `δ[i,j]`), equal to
> `1` when `i = j` and `0` otherwise, together with its behaviour under scalar multiplication,
> symmetrization, and finite sums. It also defines the `generalizedKroneckerDelta`, the
> determinant of a matrix of Kronecker deltas.

## ii. Key results

> - `kroneckerDelta` : the Kronecker delta on a type with decidable equality.
> - `generalizedKroneckerDelta` : the determinant form `det (δ[μᵢ, νⱼ])`.

## iv. References

> * None.

## A. The Kronecker delta

**`KroneckerDelta.kroneckerDelta`**, a def, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Basic.lean#L51).

> The Kronecker delta function, `ite (i = j) 1 0`.

```lean
def kroneckerDelta (i j : α) : ℕ
```

**`KroneckerDelta.eq_one_of_same`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Basic.lean#L57).

```lean
lemma eq_one_of_same (i : α) : δ[i,i] = 1
```

**`KroneckerDelta.eq_zero_of_ne`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Basic.lean#L60).

```lean
lemma eq_zero_of_ne {i j : α} (h : i ≠ j) : δ[i,j] = 0
```

**`KroneckerDelta.eq_of_coe`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Basic.lean#L63).

```lean
lemma eq_of_coe {p : α → Prop} (i j : Subtype p) : δ[(i : α),j] = δ[i,j]
```

**`KroneckerDelta.eq_zero_of_not`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Basic.lean#L68).

```lean
lemma eq_zero_of_not {p : α → Prop} {i j : α} (hi : ¬p i) (hj : p j) : δ[i,j] = 0
```

**`KroneckerDelta.kroneckerDelta_finSumFinEquiv`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Basic.lean#L72).

> The Kronecker delta is invariant under the component-index equivalence `finSumFinEquiv`.

```lean
lemma kroneckerDelta_finSumFinEquiv (a b : Fin 1 ⊕ Fin 3) :
    kroneckerDelta (finSumFinEquiv a) (finSumFinEquiv b) = kroneckerDelta a b
```

## B. Conditions for smul to vanish

**`KroneckerDelta.smul_of_eq_zero`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Basic.lean#L82).

```lean
lemma smul_of_eq_zero [AddMonoid M] (i j : α) {f : α → α → M} (hf : f i i = 0) :
    δ[i,j] • f i j = 0
```

**`KroneckerDelta.smul_eq_zero_iff`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Basic.lean#L88).

```lean
lemma smul_eq_zero_iff [AddMonoid M] (i j : α) (f : α → α → M) :
    δ[i,j] • f i j = 0 ↔ i ≠ j ∨ f i i = 0
```

**`KroneckerDelta.smul_eq_zero_iff'`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Basic.lean#L94).

```lean
lemma smul_eq_zero_iff' [AddMonoid M] (i : α) (f : α → α → M) :
    (∀ j : α, δ[i,j] • f i j = 0) ↔ f i i = 0
```

**`KroneckerDelta.smul_eq_zero_iff''`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Basic.lean#L99).

```lean
lemma smul_eq_zero_iff'' [AddMonoid M] (f : α → α → M) :
    (∀ i j : α, δ[i,j] • f i j = 0) ↔ ∀ i : α, f i i = 0
```

## C. Symmetrization

**`KroneckerDelta.symm`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Basic.lean#L109).

```lean
lemma symm (i j : α) : δ[i,j] = δ[j,i]
```

**`KroneckerDelta.smul_symm`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Basic.lean#L111).

```lean
lemma smul_symm [AddMonoid M] (i j : α) (f : α → α → M) : δ[i,j] • f j i = δ[i,j] • f i j
```

**`KroneckerDelta.symmetrize`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Basic.lean#L116).

```lean
lemma symmetrize [AddMonoid M] (i j : α) (f : α → α → M) :
    δ[i,j] • (f i j + f j i) = (2 * δ[i,j]) • f i j
```

**`KroneckerDelta.symmetrize'`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Basic.lean#L122).

```lean
lemma symmetrize' [AddCommMonoid M] {K : Type*} [Semifield K] [CharZero K] [Module K M]
    (i j : α) (f : α → α → M) : δ[i,j] • (2 : K)⁻¹ • (f i j + f j i) = δ[i,j] • f i j
```

**`KroneckerDelta.smul_sub_eq_zero`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Basic.lean#L130).

```lean
lemma smul_sub_eq_zero [AddGroup M] (i j : α) (f : α → α → M) : δ[i,j] • (f i j - f j i) = 0
```

## D. Sums

**`KroneckerDelta.sum_mul`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Basic.lean#L147).

```lean
lemma sum_mul [Fintype α] (i j : α) : ∑ k : α, δ[i,k] * δ[k,j] = δ[i,j]
```

**`KroneckerDelta.sum_smul`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Basic.lean#L151).

```lean
lemma sum_smul [Fintype α] (i : α) (f : α → M) : ∑ j : α, δ[i,j] • f j = f i
```

**`KroneckerDelta.sum_sum_smul_eq_zero`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Basic.lean#L154).

```lean
lemma sum_sum_smul_eq_zero [Fintype α] {f : α → α → M} (hf : ∀ i : α, f i i = 0) :
    ∑ i : α, ∑ j : α, δ[i,j] • f i j = 0
```

**`KroneckerDelta.finset_sum_smul`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Basic.lean#L158).

```lean
lemma finset_sum_smul (s : Finset α) (i : α) (f : α → M) :
    ∑ j ∈ s, δ[i,j] • f j = if i ∈ s then f i else 0
```

**`KroneckerDelta.finset_sum_sum_smul_eq_zero`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Basic.lean#L162).

```lean
lemma finset_sum_sum_smul_eq_zero {s s' : Finset α} {f : α → α → M}
    (hf : ∀ i ∈ s ∩ s', f i i = 0) : ∑ i ∈ s, ∑ j ∈ s', δ[i,j] • f i j = 0
```

## E. The generalized Kronecker delta

**`KroneckerDelta.generalizedKroneckerDelta`**, a def, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Basic.lean#L186).

> Generalized Kronecker delta:
> `δ^{μ₁...μₙ}_{ν₁...νₙ} = det (δ[μᵢ, νⱼ])`.
>
> This is defined for any finite type `α` with decidable equality.

```lean
def generalizedKroneckerDelta {α ι : Type} [DecidableEq α]
    [DecidableEq ι] [Fintype ι]
    (μ : ι → α) (ν : ι → α) : ℤ
```

**`KroneckerDelta.generalizedKroneckerDelta_swap`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Basic.lean#L193).

> Swapping two of the upper indices of the generalized Kronecker delta negates it.
> This is one row transposition of the underlying determinant.

```lean
lemma generalizedKroneckerDelta_swap {α ι : Type} [DecidableEq α] [DecidableEq ι] [Fintype ι]
    (μ ν : ι → α) {i j : ι} (hij : i ≠ j) :
    generalizedKroneckerDelta (μ ∘ Equiv.swap i j) ν = - generalizedKroneckerDelta μ ν
```

**`KroneckerDelta.generalizedKroneckerDelta_comp_perm`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Basic.lean#L205).

> Simultaneously reindexing the upper and lower slots of a generalized Kronecker delta by the
> same permutation leaves it unchanged.

```lean
lemma generalizedKroneckerDelta_comp_perm {α ι : Type} [DecidableEq α] [DecidableEq ι]
    [Fintype ι] (μ ν : ι → α) (e : Equiv.Perm ι) :
    generalizedKroneckerDelta (μ ∘ e) (ν ∘ e) = generalizedKroneckerDelta μ ν
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/KroneckerDelta/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Basic.lean)
