---
declaration: theorem
origin: cited
lean: TauCeti.sum_artinCoeff_mul_card_fixedBy
statement: formalized
proof: formalized
---

# Artin's identity for fixed points

weighting the permutation character of `G ⧸ C` by
`C.artinCoeff * |C|` and summing over all subgroups gives `|G|`, at every `g : G`.

```lean
TauCeti.sum_artinCoeff_mul_card_fixedBy.{u_1} {G : Type u_1} [Group G] [Finite G] (g : G) :
  ∑ᶠ (C : Subgroup G), C.artinCoeff * ↑(Nat.card ↥C) * ↑(Nat.card ↑(MulAction.fixedBy (G ⧸ C) g)) =
    ↑(Nat.card G)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.sum_artinCoeff_mul_card_fixedBy`](https://taucetiproject.org/docs/TauCeti/GroupTheory/ArtinCoefficient.html#TauCeti.sum_artinCoeff_mul_card_fixedBy).

## Sources

- [Tau Ceti documentation: `TauCeti.sum_artinCoeff_mul_card_fixedBy`](https://taucetiproject.org/docs/TauCeti/GroupTheory/ArtinCoefficient.html#TauCeti.sum_artinCoeff_mul_card_fixedBy)
- [Source of `TauCeti.sum_artinCoeff_mul_card_fixedBy` in TauCeti/GroupTheory/ArtinCoefficient.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/ArtinCoefficient.lean#L235)
