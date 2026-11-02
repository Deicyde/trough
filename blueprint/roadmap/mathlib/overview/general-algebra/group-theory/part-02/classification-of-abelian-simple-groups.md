---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: CommGroup.is_simple_iff_prime_card
mathlib_file: Mathlib/GroupTheory/SpecificGroups/Cyclic.lean
---

# Classification of abelian simple groups

Mathlib states this as `CommGroup.is_simple_iff_prime_card`.

```lean
CommGroup.is_simple_iff_prime_card.{u_1} {α : Type u_1} [CommGroup α] :
  IsSimpleGroup α ↔ Nat.Prime (Nat.card α)
```

## Depends on

- [Cardinal](../../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Irreducible element](../../divisibility-in-integral-domains/irreducible-element.md)
- [Ring morphism](../../rings/ring-morphism.md)
- [Simple group](../part-01/simple-group.md)

## Proof depends on

- [Characteristic zero](../../field-theory/characteristic-zero.md)
- [Cyclic group](../part-01/cyclic-group.md)
- [Lagrange's theorem](lagranges-theorem.md)
- [Order of an element](../../../../undergraduate/group-theory/basic-definitions/order-of-an-element.md)

## Sources

- [Mathlib documentation: `CommGroup.is_simple_iff_prime_card`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Cyclic.html#CommGroup.is_simple_iff_prime_card)
- [Source of `CommGroup.is_simple_iff_prime_card` in Mathlib/GroupTheory/SpecificGroups/Cyclic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/SpecificGroups/Cyclic.lean#L272)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L57)
