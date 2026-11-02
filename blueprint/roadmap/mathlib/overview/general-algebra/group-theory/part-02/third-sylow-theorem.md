---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: card_sylow_modEq_one
mathlib_file: Mathlib/GroupTheory/Sylow.lean
---

# Third Sylow theorem

A generalization of **Sylow's third theorem**.
If the number of Sylow `p`-subgroups is finite, then it is congruent to `1` modulo `p`.

```lean
card_sylow_modEq_one.{u_1} (p : ℕ) (G : Type u_1) [Group G] [Fact (Nat.Prime p)]
  [Finite (Sylow p G)] : Nat.card (Sylow p G) ≡ 1 [MOD p]
```

## Depends on

- [Cardinal](../../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Irreducible element](../../divisibility-in-integral-domains/irreducible-element.md)
- [Ring morphism](../../rings/ring-morphism.md)
- [Subgroup](../part-01/subgroup.md)

## Proof depends on

- [Finite set](../../../data-structures/sets/finite-set.md)
- [Group action](../part-01/group-action.md)

## Sources

- [Mathlib documentation: `card_sylow_modEq_one`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#card_sylow_modEq_one)
- [Source of `card_sylow_modEq_one` in Mathlib/GroupTheory/Sylow.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/Sylow.lean#L373)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L62)
