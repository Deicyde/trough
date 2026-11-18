---
declaration: module
origin: cited
lean: generalizedKroneckerDelta_mul, generalizedKroneckerDelta_sum_snoc, sum_generalizedKroneckerDelta_self_card, sum_generalizedKroneckerDelta_cons_card, sum_generalizedKroneckerDelta_cons₂_card, sum_generalizedKroneckerDelta_self_eq_factorial, sum_generalizedKroneckerDelta_self, sum_generalizedKroneckerDelta_cons
statement: formalized
proof: formalized
---

# Contraction identities for the generalized Kronecker delta

The module `Physlib.Mathematics.KroneckerDelta.Contraction`, [Physlib/Mathematics/KroneckerDelta/Contraction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Contraction.lean): 13 declarations, 13 with a docstring; 3 private, not shown.

## i. Overview

> This file proves the combinatorial contraction facts for the `generalizedKroneckerDelta`
> (defined in `Physlib.Mathematics.KroneckerDelta.Basic`). Everything here is purely about the
> abstract generalized Kronecker delta on a finite type; no tensor or physics content appears.
> These facts are the reusable backbone of the Levi-Civita epsilon-epsilon contraction
> identities proved in `Physlib.Relativity.Tensors.LeviCivita.Contractions`.
>
> The central fact is that summing a `generalizedKroneckerDelta` over one shared index lowers
> its rank by one and multiplies it by `card α - n` (`generalizedKroneckerDelta_sum_snoc`).
> Iterating that fact gives the fully-, singly-, and doubly-free contractions over an arbitrary
> finite index type, with the falling product `(card α - m) (card α - m - 1) ⋯` for `m` free pairs
> (`sum_generalizedKroneckerDelta_self_card`, `sum_generalizedKroneckerDelta_cons_card`,
> `sum_generalizedKroneckerDelta_cons₂_card`), and `k!` for the full contraction when the index type
> has `k` elements (`sum_generalizedKroneckerDelta_self_eq_factorial`). Together with the product
> identity
> `generalizedKroneckerDelta μ ν = generalizedKroneckerDelta μ id * generalizedKroneckerDelta ν id`
> (`generalizedKroneckerDelta_mul`), their `Fin 4` instances `sum_generalizedKroneckerDelta_self`,
> `sum_generalizedKroneckerDelta_cons`, and `sum_generalizedKroneckerDelta_cons₂` give the
> contractions used for the Levi-Civita identities.
>
> The proof of `generalizedKroneckerDelta_sum_snoc` borders the delta matrix with the appended
> index (a Schur-complement reduction) and then applies the ring-general rank-one determinant
> update lemma `Matrix.det_add_rankOne`, which is proved here because Mathlib only provides the
> matrix determinant lemma when `det A` is a unit and Kronecker-delta matrices are singular.

## ii. Key results

> - `generalizedKroneckerDelta_sum_snoc` : summing over one shared index lowers the rank by one.
> - `sum_generalizedKroneckerDelta_self_card`, `sum_generalizedKroneckerDelta_cons_card`,
>   `sum_generalizedKroneckerDelta_cons₂_card` : the fully-, singly-, and doubly-free contractions
>   over any finite index type; `sum_generalizedKroneckerDelta_self_eq_factorial` : the full
>   contraction is `k!` when the type has `k` elements.
> - `sum_generalizedKroneckerDelta_mul_self`, `sum_generalizedKroneckerDelta_mul_cons`,
>   `sum_generalizedKroneckerDelta_mul_snoc`, `sum_generalizedKroneckerDelta_mul_cons₂` : the
>   fully-, singly-, and doubly-free symbol-level contractions over `Fin 4`.

## iv. References

> * None.

## A. The rank-one determinant update

## B. Contraction identities

**`generalizedKroneckerDelta_mul`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Contraction.lean#L147).

> The product of two Levi-Civita-type symbols is a generalized Kronecker delta:
> `δ^{μ}_{·} · δ^{ν}_{·} = δ^{μ}_{ν}`, where each single factor is a Kronecker matrix against the
> identity. This is the Lean form of `ε^{μ₁…μₙ} ε_{ν₁…νₙ} = δ^{μ₁…μₙ}_{ν₁…νₙ}`.

```lean
lemma generalizedKroneckerDelta_mul (μ ν : α → α) :
    generalizedKroneckerDelta μ id * generalizedKroneckerDelta ν id
      = generalizedKroneckerDelta μ ν
```

**`generalizedKroneckerDelta_sum_snoc`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Contraction.lean#L170).

> **Generalized Kronecker delta contraction.** Summing a `generalizedKroneckerDelta` over one
> shared index appended at the end lowers the rank by one and pulls out a factor of `card α - n`.
> This is the reusable combinatorial fact behind all epsilon-epsilon identities.

```lean
lemma generalizedKroneckerDelta_sum_snoc {n : ℕ} (μ ν : Fin n → α) :
    ∑ a : α, generalizedKroneckerDelta (Fin.snoc μ a) (Fin.snoc ν a)
      = ((Fintype.card α : ℤ) - n) * generalizedKroneckerDelta μ ν
```

**`sum_generalizedKroneckerDelta_self_card`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Contraction.lean#L225).

> **Full contraction over an arbitrary finite type.** Summing `δ^{h}_{h}` over all `k`-tuples
> `h` of indices gives the falling product `card α · (card α - 1) ⋯ (card α - k + 1)`.

```lean
lemma sum_generalizedKroneckerDelta_self_card (k : ℕ) :
    ∑ h : Fin k → α, generalizedKroneckerDelta h h
      = ∏ j ∈ Finset.range k, ((Fintype.card α : ℤ) - j)
```

**`sum_generalizedKroneckerDelta_cons_card`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Contraction.lean#L245).

> **Single contraction over an arbitrary finite type.** Contracting the last `k` of `k+1`
> index pairs leaves one free pair `σ, τ`, with the falling product
> `(card α - 1) (card α - 2) ⋯`.

```lean
lemma sum_generalizedKroneckerDelta_cons_card (σ τ : α) (k : ℕ) :
    ∑ h : Fin k → α,
        generalizedKroneckerDelta (Fin.cons σ h) (Fin.cons τ h)
      = (∏ j ∈ Finset.range k, ((Fintype.card α : ℤ) - 1 - j))
        * ((kroneckerDelta σ τ : ℕ) : ℤ)
```

**`sum_generalizedKroneckerDelta_cons₂_card`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Contraction.lean#L273).

> **Double contraction over an arbitrary finite type.** Contracting the last `k` of `k+2`
> index pairs leaves two free pairs, with value a `2×2` generalized Kronecker delta times the
> falling product `(card α - 2) (card α - 3) ⋯`.

```lean
lemma sum_generalizedKroneckerDelta_cons₂_card (ρ σ τ ω : α) (k : ℕ) :
    ∑ h : Fin k → α,
        generalizedKroneckerDelta (Fin.cons ρ (Fin.cons σ h)) (Fin.cons τ (Fin.cons ω h))
      = (∏ j ∈ Finset.range k, ((Fintype.card α : ℤ) - 2 - j))
        * generalizedKroneckerDelta ![ρ, σ] ![τ, ω]
```

**`sum_generalizedKroneckerDelta_self_eq_factorial`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Contraction.lean#L307).

> When the index type has exactly `k` elements, the full contraction is `k!`.

```lean
lemma sum_generalizedKroneckerDelta_self_eq_factorial {k : ℕ} (hk : Fintype.card α = k) :
    ∑ h : Fin k → α, generalizedKroneckerDelta h h = (k.factorial : ℤ)
```

**`sum_generalizedKroneckerDelta_self`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Contraction.lean#L318).

> **Full contraction.** Iterating the snoc contraction over all four indices:
> `∑_f δ^{f}_{f} = 4!`. Here `f` ranges over all maps `Fin 4 → Fin 4`. The `Fin 4` instance of
> `sum_generalizedKroneckerDelta_self_card`.

```lean
lemma sum_generalizedKroneckerDelta_self (k : ℕ) :
    ∑ h : Fin k → Fin 4, generalizedKroneckerDelta h h
      = ∏ j ∈ Finset.range k, ((4 : ℤ) - j)
```

**`sum_generalizedKroneckerDelta_cons`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Contraction.lean#L325).

> **Single contraction.** Contracting the last `k` of `k+1` index pairs leaves one free pair
> `σ, τ`, with the factorial factor `(4-1)(4-2)…`.

```lean
lemma sum_generalizedKroneckerDelta_cons (σ τ : Fin 4) (k : ℕ) :
    ∑ h : Fin k → Fin 4,
        generalizedKroneckerDelta (Fin.cons σ h) (Fin.cons τ h)
      = (∏ j ∈ Finset.range k, ((3 : ℤ) - j)) * ((kroneckerDelta σ τ : ℕ) : ℤ)
```

**`sum_generalizedKroneckerDelta_cons₂`**, a lemma, [line 333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Contraction.lean#L333).

> **Double contraction.** Contracting the last `k` of `k+2` index pairs leaves two free pairs,
> with value a `2×2` generalized Kronecker delta times the factorial factor.

```lean
lemma sum_generalizedKroneckerDelta_cons₂ (ρ σ τ ω : Fin 4) (k : ℕ) :
    ∑ h : Fin k → Fin 4,
        generalizedKroneckerDelta (Fin.cons ρ (Fin.cons σ h)) (Fin.cons τ (Fin.cons ω h))
      = (∏ j ∈ Finset.range k, ((2 : ℤ) - j))
        * generalizedKroneckerDelta ![ρ, σ] ![τ, ω]
```

**`sum_generalizedKroneckerDelta_mul_self`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Contraction.lean#L341).

> Symbol-level full contraction over `Fin 4 → Fin 4`.

```lean
lemma sum_generalizedKroneckerDelta_mul_self :
    ∑ g : Fin 4 → Fin 4,
      generalizedKroneckerDelta g id * generalizedKroneckerDelta g id = (24 : ℤ)
```

**`sum_generalizedKroneckerDelta_mul_cons`**, a lemma, [line 349](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Contraction.lean#L349).

> Symbol-level triple contraction, one free pair `σ, τ`.

```lean
lemma sum_generalizedKroneckerDelta_mul_cons (σ τ : Fin 4) :
    ∑ h : Fin 3 → Fin 4,
        generalizedKroneckerDelta (Fin.cons σ h) id
          * generalizedKroneckerDelta (Fin.cons τ h) id
      = 6 * ((kroneckerDelta σ τ : ℕ) : ℤ)
```

**`sum_generalizedKroneckerDelta_mul_snoc`**, a lemma, [line 360](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Contraction.lean#L360).

> Symbol-level triple contraction with the free index in the last slot.

```lean
lemma sum_generalizedKroneckerDelta_mul_snoc (σ τ : Fin 4) :
    ∑ h : Fin 3 → Fin 4,
        generalizedKroneckerDelta (Fin.snoc h σ) id * generalizedKroneckerDelta (Fin.snoc h τ) id =
      6 * ((kroneckerDelta σ τ : ℕ) : ℤ)
```

**`sum_generalizedKroneckerDelta_mul_cons₂`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Contraction.lean#L377).

> Symbol-level double contraction, two free pairs.

```lean
lemma sum_generalizedKroneckerDelta_mul_cons₂ (ρ σ τ ω : Fin 4) :
    ∑ h : Fin 2 → Fin 4,
        generalizedKroneckerDelta (Fin.cons ρ (Fin.cons σ h)) id
          * generalizedKroneckerDelta (Fin.cons τ (Fin.cons ω h)) id
      = 2 * (((kroneckerDelta ρ τ : ℕ) : ℤ) * ((kroneckerDelta σ ω : ℕ) : ℤ)
          - ((kroneckerDelta ρ ω : ℕ) : ℤ) * ((kroneckerDelta σ τ : ℕ) : ℤ))
```

## Depends on

- [Kronecker delta](basic.md)

## Sources

- [Physlib/Mathematics/KroneckerDelta/Contraction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/KroneckerDelta/Contraction.lean)
