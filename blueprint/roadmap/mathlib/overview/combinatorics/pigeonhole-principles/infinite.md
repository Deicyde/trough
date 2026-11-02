---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Finite.exists_infinite_fiber
mathlib_file: Mathlib/Data/Fintype/Pigeonhole.lean
---

# Infinite

The strong pigeonhole principle for infinitely many pigeons in
finitely many pigeonholes.  If there are infinitely many pigeons in
finitely many pigeonholes, then there is a pigeonhole with infinitely
many pigeons.

See also: `Finite.exists_ne_map_eq_of_infinite`

```lean
Finite.exists_infinite_fiber.{u_1, u_2} {α : Type u_1} {β : Type u_2} [Infinite α] [Finite β]
  (f : α → β) : ∃ y, Infinite ↑(f ⁻¹' {y})
```

## Depends on

- [Array](../../data-structures/list-like-structures/array.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)
- [Set](../../data-structures/sets/set.md)

## Proof depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Integer](../../general-algebra/numbers/integer.md)

## Sources

- [Mathlib documentation: `Finite.exists_infinite_fiber`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Fintype/Pigeonhole.html#Finite.exists_infinite_fiber)
- [Source of `Finite.exists_infinite_fiber` in Mathlib/Data/Fintype/Pigeonhole.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Data/Fintype/Pigeonhole.lean#L80)
- [Mathlib overview: Combinatorics › Pigeonhole principles](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L499)
