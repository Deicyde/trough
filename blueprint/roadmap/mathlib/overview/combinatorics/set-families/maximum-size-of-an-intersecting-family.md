---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Set.Intersecting.is_max_iff_card_eq
mathlib_file: Mathlib/Combinatorics/SetFamily/Intersecting.lean
---

# Maximum size of an intersecting family

Mathlib states this as `Set.Intersecting.is_max_iff_card_eq`.

```lean
Set.Intersecting.is_max_iff_card_eq.{u_1} {α : Type u_1} [BooleanAlgebra α] [Nontrivial α]
  [Fintype α] {s : Finset α} (hs : (↑s).Intersecting) :
  (∀ (t : Finset α), (↑t).Intersecting → s ⊆ t → s = t) ↔ 2 * s.card = Fintype.card α
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)
- [Set](../../data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `Set.Intersecting.is_max_iff_card_eq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SetFamily/Intersecting.html#Set.Intersecting.is_max_iff_card_eq)
- [Source of `Set.Intersecting.is_max_iff_card_eq` in Mathlib/Combinatorics/SetFamily/Intersecting.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/SetFamily/Intersecting.lean#L161)
- [Mathlib overview: Combinatorics › Set families](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L516)
