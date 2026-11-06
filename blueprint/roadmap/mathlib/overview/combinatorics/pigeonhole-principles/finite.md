# Finite

The pigeonhole principle for finitely many pigeons and pigeonholes.
This is the `Fintype` version of `Finset.exists_ne_map_eq_of_card_lt_of_maps_to`.

```lean
Fintype.exists_ne_map_eq_of_card_lt.{u_1, u_2} {α : Type u_1} {β : Type u_2} [Fintype α] [Fintype β]
  (f : α → β) (h : Fintype.card β < Fintype.card α) : ∃ x y, x ≠ y ∧ f x = f y
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Fintype.exists_ne_map_eq_of_card_lt`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Fintype/Pigeonhole.html#Fintype.exists_ne_map_eq_of_card_lt)
- [Source of `Fintype.exists_ne_map_eq_of_card_lt` in Mathlib/Data/Fintype/Pigeonhole.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Data/Fintype/Pigeonhole.lean#L44)
- [Mathlib overview: Combinatorics › Pigeonhole principles](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L498)
