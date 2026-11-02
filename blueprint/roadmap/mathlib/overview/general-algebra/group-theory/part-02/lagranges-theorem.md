---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Subgroup.card_subgroup_dvd_card
mathlib_file: Mathlib/GroupTheory/Coset/Card.lean
---

# Lagrange's theorem

**Lagrange's Theorem**: The order of a subgroup divides the order of its ambient group.

[Wikidata Q505798](https://www.wikidata.org/wiki/Q505798)

```lean
Subgroup.card_subgroup_dvd_card.{u_1} {α : Type u_1} [Group α] (s : Subgroup α) :
  Nat.card ↥s ∣ Nat.card α
```

## Depends on

- [Cardinal](../../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Ring morphism](../../rings/ring-morphism.md)
- [Subgroup](../part-01/subgroup.md)

## Proof depends on

- [Cantor’s Theorem](../../../../hundred-theorems/part-04/cantors-theorem.md)
- [Characteristic zero](../../field-theory/characteristic-zero.md)
- [Finite set](../../../data-structures/sets/finite-set.md)
- [Group action](../part-01/group-action.md)
- [Orbit](../../../../undergraduate/group-theory/basic-definitions/orbit.md)
- [Ordered ring](../../rings/ordered-ring.md)
- [Schroeder-Bernstein Theorem](../../../../hundred-theorems/part-02/schroeder-bernstein-theorem.md)

## Sources

- [Mathlib documentation: `Subgroup.card_subgroup_dvd_card`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Coset/Card.html#Subgroup.card_subgroup_dvd_card)
- [Source of `Subgroup.card_subgroup_dvd_card` in Mathlib/GroupTheory/Coset/Card.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/Coset/Card.lean#L66)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L59)
- [Freek Wiedijk's 100 theorems, no. 71](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L358)
- [1000+ theorems list: Q505798](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L506)
- [1000+ theorems project: Q505798](https://1000-plus.github.io/?length=-1#Q505798)
- [Wikipedia: Lagrange's theorem (group theory)](https://en.wikipedia.org/wiki/Lagrange's_theorem_%28group_theory%29)
- [Wikidata: Q505798](https://www.wikidata.org/wiki/Q505798)
