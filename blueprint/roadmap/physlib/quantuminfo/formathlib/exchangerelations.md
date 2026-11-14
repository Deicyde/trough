---
declaration: module
origin: cited
lean: Finset.prod_apply_update, Finset.prod_update_const_mul, prod_apply_update_mul_prod_apply_update, eq_mul_prod_of_mul_update, exists_prod_of_mul_update, exists_prod_iff_mul_update
statement: formalized
proof: formalized
---

# Products of functions on a finite product

The module `QuantumInfo.ForMathlib.ExchangeRelations`, [QuantumInfo/ForMathlib/ExchangeRelations.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ExchangeRelations.lean): 6 declarations, 6 with a docstring.

> With at least one coordinate, a function `T` on a finite product `(i : ι) → κ i` is a product of
> functions of one variable exactly when it satisfies the exchange relations.

## i. Overview

> For a function `T : ((i : ι) → κ i) → K` with values in a field, the exchange relations say
> that for every coordinate `i`, values `a b : κ i` and points `x y`,
> `T (x[i ← a]) * T (y[i ← b]) = T (x[i ← b]) * T (y[i ← a])`, where `x[i ← a]` is `x` with
> coordinate `i` replaced by `a`. They say that all `2 × 2` minors of the one-coordinate
> flattenings of `T` vanish. The flattening at `i` has rows indexed by `κ i` and columns indexed
> by assignments to the remaining coordinates.
>
> If the index type `ι` is finite and nonempty, the exchange relations hold exactly when
> `T x = ∏ i, v i (x i)` for some functions `v i : κ i → K`. Nonemptiness is necessary: if `ι` is
> empty, the exchange relations are vacuous, so every function satisfies them, but an empty
> product is always `1`.
>
> For finite-dimensional tensors, these equations characterize the tensors of rank at most one,
> which form the affine cone over the Segre variety.
>
> This file is a temporary copy of results intended for Mathlib.

## ii. Key results

> - `exists_prod_iff_mul_update` : with at least one coordinate, `T` is a product of functions of
>   one variable if and only if it satisfies the exchange relations.

## iv. References

> - M. Michałek and B. Sturmfels, Invitation to Nonlinear Algebra, §9.2, p. 141.
>   [ref: michalek\_sturmfels\_2021]

## A. Product identities

**`Finset.prod_apply_update`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ExchangeRelations.lean#L70).

> Changing coordinate `i` of `x` to `a` changes only the factor indexed by `i` in
> `∏ j, v j (x j)`.

```lean
lemma Finset.prod_apply_update (v : (i : ι) → κ i → K) (x : (i : ι) → κ i) (i : ι)
    (a : κ i) : ∏ j, v j (update x i a j) = v i a * ∏ j ∈ Finset.univ.erase i, v j (x j)
```

**`Finset.prod_update_const_mul`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ExchangeRelations.lean#L77).

> Multiplying the function indexed by `i₀` by `c` multiplies `∏ i, v i (x i)` by `c`.

```lean
lemma Finset.prod_update_const_mul (v : (i : ι) → κ i → K) (c : K) (i₀ : ι)
    (x : (i : ι) → κ i) :
    ∏ i, update v i₀ (fun a ↦ c * v i₀ a) i (x i) = c * ∏ i, v i (x i)
```

**`prod_apply_update_mul_prod_apply_update`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ExchangeRelations.lean#L87).

> A product `x ↦ ∏ i, v i (x i)` of functions of one variable satisfies the exchange
> relations.

```lean
lemma prod_apply_update_mul_prod_apply_update (v : (i : ι) → κ i → K) (x y : (i : ι) → κ i)
    (i : ι) (a b : κ i) :
    (∏ j, v j (update x i a j)) * ∏ j, v j (update y i b j) =
      (∏ j, v j (update x i b j)) * ∏ j, v j (update y i a j)
```

## B. Factorization from the exchange relations

**`eq_mul_prod_of_mul_update`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ExchangeRelations.lean#L109).

> If `T` satisfies the exchange relations and `T x₀ ≠ 0`, then every `x` that agrees with `x₀`
> outside a finite set `s` of coordinates satisfies
> `T x = T x₀ * ∏ j ∈ s, T (update x₀ j (x j)) / T x₀`.

```lean
lemma eq_mul_prod_of_mul_update {T : ((i : ι) → κ i) → K}
    (hT : ∀ i (a b : κ i) x y, T (update x i a) * T (update y i b) =
      T (update x i b) * T (update y i a))
    {x₀ : (i : ι) → κ i} (h₀ : T x₀ ≠ 0) (s : Finset ι) :
    ∀ x : (i : ι) → κ i, (∀ j ∉ s, x j = x₀ j) →
      T x = T x₀ * ∏ j ∈ s, T (update x₀ j (x j)) / T x₀
```

**`exists_prod_of_mul_update`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ExchangeRelations.lean#L140).

> If `ι` is nonempty, a function on a finite product that satisfies the exchange relations
> factors as a product of functions of one variable.

```lean
lemma exists_prod_of_mul_update [Fintype ι] [Nonempty ι] {T : ((i : ι) → κ i) → K}
    (hT : ∀ i (a b : κ i) x y, T (update x i a) * T (update y i b) =
      T (update x i b) * T (update y i a)) :
    ∃ v : (i : ι) → κ i → K, ∀ x, T x = ∏ i, v i (x i)
```

**`exists_prod_iff_mul_update`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ExchangeRelations.lean#L156).

> If `ι` is nonempty, a function on a finite product factors as a product of functions of one
> variable if and only if it satisfies the exchange relations.

```lean
lemma exists_prod_iff_mul_update [Fintype ι] [Nonempty ι] {T : ((i : ι) → κ i) → K} :
    (∃ v : (i : ι) → κ i → K, ∀ x, T x = ∏ i, v i (x i)) ↔
      ∀ i (a b : κ i) x y, T (update x i a) * T (update y i b) =
        T (update x i b) * T (update y i a)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [QuantumInfo/ForMathlib/ExchangeRelations.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ExchangeRelations.lean)
