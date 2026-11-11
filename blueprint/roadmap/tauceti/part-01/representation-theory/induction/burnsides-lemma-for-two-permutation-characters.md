---
declaration: theorem
origin: cited
lean: TauCeti.sum_character_ofMulAction_mul_character_ofMulAction_eq_card_orbits_mul_card_group
statement: formalized
proof: formalized
---

# Burnside's lemma for two permutation characters

The unnormalized sum
`∑ g, χ_X(g) · χ_Y(g⁻¹)` is the number of orbits of `G` on `X × Y` times the order of `G`.

This form carries no division, so it holds over any field.

```lean
TauCeti.sum_character_ofMulAction_mul_character_ofMulAction_eq_card_orbits_mul_card_group.{u, v, w,
    z}
  (k : Type u) {G : Type v} [Field k] [Group G] [Fintype G] (X : Type w) (Y : Type z)
  [MulAction G X] [MulAction G Y] [Finite X] [Finite Y] :
  ∑ g,
      (Representation.ofMulAction k G X).character g *
        (Representation.ofMulAction k G Y).character g⁻¹ =
    ↑(Nat.card (MulAction.orbitRel.Quotient G (X × Y))) * ↑(Nat.card G)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Burnside's lemma on a product](../../group-theory/other-results/burnsides-lemma-on-a-product.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.sum_character_ofMulAction_mul_character_ofMulAction_eq_card_orbits_mul_card_group`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/DoubleCosetPairing.html#TauCeti.sum_character_ofMulAction_mul_character_ofMulAction_eq_card_orbits_mul_card_group).

## Sources

- [Tau Ceti documentation: `TauCeti.sum_character_ofMulAction_mul_character_ofMulAction_eq_card_orbits_mul_card_group`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/DoubleCosetPairing.html#TauCeti.sum_character_ofMulAction_mul_character_ofMulAction_eq_card_orbits_mul_card_group)
- [Source of `TauCeti.sum_character_ofMulAction_mul_character_ofMulAction_eq_card_orbits_mul_card_group` in TauCeti/RepresentationTheory/Induction/DoubleCosetPairing.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Induction/DoubleCosetPairing.lean#L88)
