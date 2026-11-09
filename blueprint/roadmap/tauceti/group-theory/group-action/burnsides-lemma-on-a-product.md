---
declaration: theorem
origin: cited
lean: TauCeti.sum_card_fixedBy_mul_card_fixedBy_eq_card_orbits_mul_card_group
statement: formalized
proof: formalized
---

# Burnside's lemma on a product

For a finite group `G` acting on two finite sets `X` and
`Y`, the sum over `g : G` of the product of the two fixed-point counts is the number of orbits of
`G` on `X × Y`, times the order of `G`.

```lean
TauCeti.sum_card_fixedBy_mul_card_fixedBy_eq_card_orbits_mul_card_group.{u_1, u_2, u_3}
  {G : Type u_1} (X : Type u_2) (Y : Type u_3) [Group G] [MulAction G X] [MulAction G Y] [Fintype G]
  [Finite X] [Finite Y] :
  ∑ g, Nat.card ↑(MulAction.fixedBy X g) * Nat.card ↑(MulAction.fixedBy Y g) =
    Nat.card (MulAction.orbitRel.Quotient G (X × Y)) * Nat.card G
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.sum_card_fixedBy_mul_card_fixedBy_eq_card_orbits_mul_card_group`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAction/Burnside.html#TauCeti.sum_card_fixedBy_mul_card_fixedBy_eq_card_orbits_mul_card_group).

## Sources

- [Tau Ceti documentation: `TauCeti.sum_card_fixedBy_mul_card_fixedBy_eq_card_orbits_mul_card_group`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAction/Burnside.html#TauCeti.sum_card_fixedBy_mul_card_fixedBy_eq_card_orbits_mul_card_group)
- [Source of `TauCeti.sum_card_fixedBy_mul_card_fixedBy_eq_card_orbits_mul_card_group` in TauCeti/GroupTheory/GroupAction/Burnside.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/GroupAction/Burnside.lean#L113)
