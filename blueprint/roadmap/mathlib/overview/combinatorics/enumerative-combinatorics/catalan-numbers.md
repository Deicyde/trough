# Catalan numbers

The recursive definition of the sequence of Catalan numbers:
`catalan (n + 1) = ∑ i : Fin n.succ, catalan i * catalan (n - i)`

```lean
catalan : ℕ → ℕ
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `catalan`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Enumerative/Catalan/Basic.html#catalan)
- [Source of `catalan` in Mathlib/Combinatorics/Enumerative/Catalan/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Combinatorics/Enumerative/Catalan/Basic.lean#L49)
- [Mathlib overview: Combinatorics › Enumerative combinatorics](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L504)
