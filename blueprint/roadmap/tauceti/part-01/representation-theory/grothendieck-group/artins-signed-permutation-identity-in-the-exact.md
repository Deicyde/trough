---
declaration: theorem
origin: cited
lean: TauCeti.natCard_nsmul_permK0_quotient_top_eq_sum_artinCoeff
statement: formalized
proof: formalized
---

# Artin's signed permutation identity in the exact Grothendieck group over every field

```lean
TauCeti.natCard_nsmul_permK0_quotient_top_eq_sum_artinCoeff.{u} (k G : Type u) [Field k] [Group G]
  [Finite G] :
  Nat.card G • TauCeti.permK0 k G (G ⧸ ⊤) =
    ∑ᶠ (C : Subgroup G), (C.artinCoeff * ↑(Nat.card ↥C)) • TauCeti.permK0 k G (G ⧸ C)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Artin's identity for fixed points](../../group-theory/other-results/part-01/artins-identity-for-fixed-points.md)
- [The dual Noether isomorphism](../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Noether isomorphism for exact categories](../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.natCard_nsmul_permK0_quotient_top_eq_sum_artinCoeff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/GrothendieckGroup/GroupAlgebra/Artin.html#TauCeti.natCard_nsmul_permK0_quotient_top_eq_sum_artinCoeff).

## Sources

- [Tau Ceti documentation: `TauCeti.natCard_nsmul_permK0_quotient_top_eq_sum_artinCoeff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/GrothendieckGroup/GroupAlgebra/Artin.html#TauCeti.natCard_nsmul_permK0_quotient_top_eq_sum_artinCoeff)
- [Source of `TauCeti.natCard_nsmul_permK0_quotient_top_eq_sum_artinCoeff` in TauCeti/RepresentationTheory/GrothendieckGroup/GroupAlgebra/Artin.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/GrothendieckGroup/GroupAlgebra/Artin.lean#L92)
