---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Finset.card_biUnion_le_of_intersecting
mathlib_file: Mathlib/Combinatorics/SetFamily/Kleitman.lean
---

# Kleitman's theorem

**Kleitman's theorem**. An intersecting family on `n` elements contains at most `2ⁿ⁻¹` sets, and
each further intersecting family takes at most half of the sets that are in no previous family.

```lean
Finset.card_biUnion_le_of_intersecting.{u_1, u_2} {ι : Type u_1} {α : Type u_2} [Fintype α]
  [DecidableEq α] [Nonempty α] (s : Finset ι) (f : ι → Finset (Finset α))
  (hf : ∀ i ∈ s, (↑(f i)).Intersecting) :
  (s.biUnion f).card ≤ 2 ^ Fintype.card α - 2 ^ (Fintype.card α - s.card)
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)
- [Set](../../data-structures/sets/set.md)

## Proof depends on

- [Maximum size of an intersecting family](maximum-size-of-an-intersecting-family.md)
- [Ordered ring](../../general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `Finset.card_biUnion_le_of_intersecting`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SetFamily/Kleitman.html#Finset.card_biUnion_le_of_intersecting)
- [Source of `Finset.card_biUnion_le_of_intersecting` in Mathlib/Combinatorics/SetFamily/Kleitman.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/SetFamily/Kleitman.lean#L37)
- [Mathlib overview: Combinatorics › Set families](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L517)
