---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: IsLowerSet.le_card_inter_finset
mathlib_file: Mathlib/Combinatorics/SetFamily/HarrisKleitman.lean
---

# Harris-Kleitman inequality

**Harris-Kleitman inequality**: Any two lower sets of finsets correlate.

```lean
IsLowerSet.le_card_inter_finset.{u_1} {α : Type u_1} [DecidableEq α] {𝒜 ℬ : Finset (Finset α)}
  [Fintype α] (h𝒜 : IsLowerSet ↑𝒜) (hℬ : IsLowerSet ↑ℬ) :
  𝒜.card * ℬ.card ≤ 2 ^ Fintype.card α * (𝒜 ∩ ℬ).card
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)
- [Set](../../data-structures/sets/set.md)

## Proof depends on

- [Ordered ring](../../general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `IsLowerSet.le_card_inter_finset`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SetFamily/HarrisKleitman.html#IsLowerSet.le_card_inter_finset)
- [Source of `IsLowerSet.le_card_inter_finset` in Mathlib/Combinatorics/SetFamily/HarrisKleitman.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/SetFamily/HarrisKleitman.lean#L92)
- [Mathlib overview: Combinatorics › Set families](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L510)
