---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Fintype.exists_lt_card_fiber_of_mul_lt_card
mathlib_file: Mathlib/Combinatorics/Pigeonhole.lean
---

# Strong pigeonhole principle

The strong pigeonhole principle for finitely many pigeons and pigeonholes.
There is a pigeonhole with at least as many pigeons as
the ceiling of the average number of pigeons across all pigeonholes.
("The maximum is at least the mean" specialized to integers.)

More formally, given a function `f` between finite types `α` and `β` and a number `n` such that
`card β * n < card α`, there exists an element `y : β` such that its preimage has more than `n`
elements.

```lean
Fintype.exists_lt_card_fiber_of_mul_lt_card.{u, v} {α : Type u} {β : Type v} [DecidableEq β]
  [Fintype α] [Fintype β] (f : α → β) {n : ℕ} (hn : Fintype.card β * n < Fintype.card α) :
  ∃ y, n < {x | f x = y}.card
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)
- [Set](../../data-structures/sets/set.md)

## Proof depends on

- [Array](../../data-structures/list-like-structures/array.md)
- [Integer](../../general-algebra/numbers/integer.md)

## Sources

- [Mathlib documentation: `Fintype.exists_lt_card_fiber_of_mul_lt_card`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Pigeonhole.html#Fintype.exists_lt_card_fiber_of_mul_lt_card)
- [Source of `Fintype.exists_lt_card_fiber_of_mul_lt_card` in Mathlib/Combinatorics/Pigeonhole.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Pigeonhole.lean#L383)
- [Mathlib overview: Combinatorics › Pigeonhole principles](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L500)
