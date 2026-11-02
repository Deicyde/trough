---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MulAction.sum_card_fixedBy_eq_card_orbits_mul_card_group
mathlib_file: Mathlib/GroupTheory/GroupAction/Quotient.lean
---

# Burnside lemma

**Burnside's lemma** : given a finite group `G` acting on a type `X`, the sum the orders of the
stabilisers coincides with the number of orbits multiplied by the order of `G`.

[Wikidata Q1330377](https://www.wikidata.org/wiki/Q1330377)

```lean
MulAction.sum_card_fixedBy_eq_card_orbits_mul_card_group.{u, v} (G : Type u) (X : Type v) [Group G]
  [MulAction G X] [Fintype G] [(g : G) → Fintype ↑(MulAction.fixedBy X g)]
  [Fintype (Quotient (MulAction.orbitRel G X))] :
  ∑ g, Fintype.card ↑(MulAction.fixedBy X g) =
    Fintype.card (Quotient (MulAction.orbitRel G X)) * Fintype.card G
```

## Depends on

- [Finite set](../../../data-structures/sets/finite-set.md)
- [Group](group.md)
- [Group action](group-action.md)
- [Orbit](../../../../undergraduate/group-theory/basic-definitions/orbit.md)

## Proof depends on

- [Group morphism](group-morphism.md)
- [Quotient space (Basic definitions)](../../../../undergraduate/group-theory/basic-definitions/quotient-space.md)

## Sources

- [Mathlib documentation: `MulAction.sum_card_fixedBy_eq_card_orbits_mul_card_group`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Quotient.html#MulAction.sum_card_fixedBy_eq_card_orbits_mul_card_group)
- [Source of `MulAction.sum_card_fixedBy_eq_card_orbits_mul_card_group` in Mathlib/GroupTheory/GroupAction/Quotient.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/GroupAction/Quotient.lean#L260)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L37)
