---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Multiset.prod_X_add_C_eq_sum_esymm
mathlib_file: Mathlib/RingTheory/Polynomial/Vieta.lean
---

# Vieta's formulas

A sum version of **Vieta's formula** for `Multiset`: the product of the linear terms `X + λ`
where `λ` runs through a multiset `s` is equal to a linear combination of the symmetric functions
`esymm s` of the `λ`'s .

```lean
Multiset.prod_X_add_C_eq_sum_esymm.{u_1} {R : Type u_1} [CommSemiring R] (s : Multiset R) :
  (Multiset.map (fun r => Polynomial.X + Polynomial.C r) s).prod =
    ∑ j ∈ Finset.range (s.card + 1), Polynomial.C (s.esymm j) * Polynomial.X ^ (s.card - j)
```

## Depends on

- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Polynomial in one indeterminate](../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-one-indeterminate.md)

## Proof depends on

- [Array](../../../overview/data-structures/list-like-structures/array.md)
- [Integer](../../../overview/general-algebra/numbers/integer.md)

## Sources

- [Mathlib documentation: `Multiset.prod_X_add_C_eq_sum_esymm`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Vieta.html#Multiset.prod_X_add_C_eq_sum_esymm)
- [Source of `Multiset.prod_X_add_C_eq_sum_esymm` in Mathlib/RingTheory/Polynomial/Vieta.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/Polynomial/Vieta.lean#L37)
- [1000+ theorems list: Q570779](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L566)
- [1000+ theorems project: Q570779](https://1000-plus.github.io/?length=-1#Q570779)
- [Wikipedia: Vieta's formulas](https://en.wikipedia.org/wiki/Vieta's_formulas)
- [Wikidata: Q570779](https://www.wikidata.org/wiki/Q570779)
