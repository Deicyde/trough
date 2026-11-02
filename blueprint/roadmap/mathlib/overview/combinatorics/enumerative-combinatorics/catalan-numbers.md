---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: catalan
mathlib_file: Mathlib/Combinatorics/Enumerative/Catalan/Basic.lean
---

# Catalan numbers

The recursive definition of the sequence of Catalan numbers:
`catalan (n + 1) = ∑ i : Fin n.succ, catalan i * catalan (n - i)`

```lean
catalan : ℕ → ℕ
```

## Depends on

- [Array](../../data-structures/list-like-structures/array.md)
- [Finite set](../../data-structures/sets/finite-set.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)
- [Set](../../data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `catalan`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Enumerative/Catalan/Basic.html#catalan)
- [Source of `catalan` in Mathlib/Combinatorics/Enumerative/Catalan/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Enumerative/Catalan/Basic.lean#L50)
- [Mathlib overview: Combinatorics › Enumerative combinatorics](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L504)
