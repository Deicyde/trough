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

## Sources

- [Mathlib documentation: `Set.Intersecting.is_max_iff_card_eq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SetFamily/Intersecting.html#Set.Intersecting.is_max_iff_card_eq)
- [Source of `Set.Intersecting.is_max_iff_card_eq` in Mathlib/Combinatorics/SetFamily/Intersecting.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Combinatorics/SetFamily/Intersecting.lean#L161)
- [Mathlib overview: Combinatorics › Set families](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L516)
