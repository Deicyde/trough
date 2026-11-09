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
- [Source of `catalan` in Mathlib/Combinatorics/Enumerative/Catalan/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Combinatorics/Enumerative/Catalan/Basic.lean#L50)
- [Mathlib overview: Combinatorics › Enumerative combinatorics](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L504)
