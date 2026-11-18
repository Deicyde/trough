---
declaration: module
origin: cited
lean: leviCivitaSymbol, leviCivitaSymbol_eq_det, leviCivitaSymbol_id, leviCivitaSymbol_perm, leviCivitaSymbol_comp_swap, leviCivitaSymbol_swap_comp, leviCivitaSymbol_eq_zero_of_eq, leviCivitaSymbol_eq_zero_of_not_injective
statement: formalized
proof: formalized
---

# The Levi-Civita symbol in general dimension

The module `Physlib.Mathematics.LeviCivita.Basic`, [Physlib/Mathematics/LeviCivita/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/LeviCivita/Basic.lean): 10 declarations, 10 with a docstring.

## i. Overview

> This module defines the Levi-Civita symbol `leviCivitaSymbol` on a general finite index
> type `ι`: for `g : ι → ι` it is the sign of `g` when `g` is a permutation and `0`
> otherwise. Taking `ι = Fin d` gives the Levi-Civita symbol `ε_{i₁ ⋯ i_d}` in dimension
> `d`, normalized by `ε_{0 1 ⋯ (d-1)} = 1`.
>
> The definition is the `generalizedKroneckerDelta` of `g` against the identity, i.e. the
> determinant of the matrix of Kronecker deltas `δ[g i, j]`, so the basic properties are
> inherited from the determinant: the value `1` on the identity, antisymmetry under
> transposition of two indices, vanishing on repeated indices, and the sign of a
> permutation via `Matrix.det_permutation`.

## ii. Key results

> - `leviCivitaSymbol` : the Levi-Civita symbol on a finite index type, valued in `ℤ`.
> - `leviCivitaSymbol_id` : the normalization `ε_{0 1 ⋯ (d-1)} = 1`.
> - `leviCivitaSymbol_perm` : on a permutation `σ` the symbol is the sign of `σ`.
> - `leviCivitaSymbol_comp_swap` : antisymmetry under transposition of two indices.
> - `leviCivitaSymbol_swap_comp` : antisymmetry under transposition of two index values.
> - `leviCivitaSymbol_eq_zero_iff` : the symbol vanishes exactly on repeated indices.
> - `leviCivitaSymbol_eq_prod_prod_Ioi` : on `Fin n` the symbol is the product over pairs
>   `i < j` of the sign of `g j - g i`.

## iv. References

> * https://en.wikipedia.org/wiki/Levi-Civita\_symbol. [ref: wiki\_levi\_civita\_symbol]

## A. Definition

**`leviCivitaSymbol`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/LeviCivita/Basic.lean#L70).

> The Levi-Civita symbol on a finite index type `ι`: `leviCivitaSymbol g` is the sign
> of `g` when `g : ι → ι` is a permutation, and `0` otherwise. It is the generalized
> Kronecker delta of `g` against the identity, i.e. the determinant of the matrix of
> Kronecker deltas `δ[g i, j]`.
>
> For `ι = Fin d` this is the Levi-Civita symbol `ε_{i₁ ⋯ i_d}` in dimension `d`,
> normalized by `ε_{0 1 ⋯ (d-1)} = 1`.

```lean
def leviCivitaSymbol (g : ι → ι) : ℤ
```

**`leviCivitaSymbol_eq_det`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/LeviCivita/Basic.lean#L75).

> The Levi-Civita symbol as the determinant of the matrix of Kronecker deltas
> `δ[g i, j]`.

```lean
lemma leviCivitaSymbol_eq_det (g : ι → ι) :
    leviCivitaSymbol g = Matrix.det (fun i j => ((kroneckerDelta (g i) j : ℕ) : ℤ))
```

**`leviCivitaSymbol_id`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/LeviCivita/Basic.lean#L81).

> The Levi-Civita symbol of the identity, i.e. `ε_{0 1 ⋯ (d-1)}`, is `1`.

```lean
lemma leviCivitaSymbol_id : leviCivitaSymbol (id : ι → ι) = 1
```

## B. Value on permutations

**`leviCivitaSymbol_perm`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/LeviCivita/Basic.lean#L95).

> The Levi-Civita symbol of a permutation `σ` is the sign of `σ`.

```lean
lemma leviCivitaSymbol_perm (σ : Equiv.Perm ι) :
    leviCivitaSymbol ⇑σ = (Equiv.Perm.sign σ : ℤ)
```

## C. Antisymmetry

**`leviCivitaSymbol_comp_swap`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/LeviCivita/Basic.lean#L110).

> The Levi-Civita symbol is antisymmetric under transposition of two of its indices:
> precomposing with the swap of two distinct index positions negates it.

```lean
lemma leviCivitaSymbol_comp_swap (g : ι → ι) {i j : ι} (hij : i ≠ j) :
    leviCivitaSymbol (g ∘ Equiv.swap i j) = - leviCivitaSymbol g
```

**`leviCivitaSymbol_swap_comp`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/LeviCivita/Basic.lean#L118).

> The Levi-Civita symbol is antisymmetric under transposition of two index values:
> postcomposing with the swap of two distinct values exchanges those two values wherever
> they occur and negates it.

```lean
lemma leviCivitaSymbol_swap_comp (g : ι → ι) {i j : ι} (hij : i ≠ j) :
    leviCivitaSymbol (Equiv.swap i j ∘ g) = - leviCivitaSymbol g
```

## D. Vanishing on repeated indices

**`leviCivitaSymbol_eq_zero_of_eq`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/LeviCivita/Basic.lean#L135).

> The Levi-Civita symbol vanishes on a repeated index: if two distinct index positions
> `i ≠ j` carry the same value, the symbol is zero.

```lean
lemma leviCivitaSymbol_eq_zero_of_eq {g : ι → ι} {i j : ι} (hij : i ≠ j) (h : g i = g j) :
    leviCivitaSymbol g = 0
```

**`leviCivitaSymbol_eq_zero_of_not_injective`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/LeviCivita/Basic.lean#L141).

> The Levi-Civita symbol vanishes on maps which are not injective.

```lean
lemma leviCivitaSymbol_eq_zero_of_not_injective {g : ι → ι} (h : ¬ Function.Injective g) :
    leviCivitaSymbol g = 0
```

**`leviCivitaSymbol_eq_zero_iff`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/LeviCivita/Basic.lean#L149).

> The Levi-Civita symbol vanishes exactly on maps with a repeated index, i.e. on maps
> which are not injective.

```lean
lemma leviCivitaSymbol_eq_zero_iff {g : ι → ι} :
    leviCivitaSymbol g = 0 ↔ ¬ Function.Injective g
```

## E. Closed form on `Fin n`

**`leviCivitaSymbol_eq_prod_prod_Ioi`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/LeviCivita/Basic.lean#L166).

> On `Fin n` the Levi-Civita symbol is the product over pairs `i < j` of the sign of
> `g j - g i`. Unlike the determinant defining `leviCivitaSymbol`, this product is cheap to
> evaluate, e.g. by `decide`.

```lean
lemma leviCivitaSymbol_eq_prod_prod_Ioi {n : ℕ} (g : Fin n → Fin n) :
    leviCivitaSymbol g =
      ∏ i, ∏ j ∈ Finset.Ioi i, (if g i < g j then 1 else if g i = g j then 0 else -1)
```

## Depends on

- [Kronecker delta](../kroneckerdelta/basic.md)

## Sources

- [Physlib/Mathematics/LeviCivita/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/LeviCivita/Basic.lean)
