---
declaration: theorem
origin: cited
lean: TauCeti.natCard_nsmul_one_eq_sum_artinCoeff_indK0
statement: formalized
proof: formalized
---

# Artin's identity in `G₀(k[G])` over every field, written as induction of the unit from subgroups

No division by the group order is required.

```lean
TauCeti.natCard_nsmul_one_eq_sum_artinCoeff_indK0.{u} (k G : Type u) [Field k] [Group G]
  [Finite G] :
  Nat.card G • 1 = ∑ᶠ (C : Subgroup G), (C.artinCoeff * ↑(Nat.card ↥C)) • (TauCeti.indK0 k C) 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Artin's signed permutation identity in the exact Grothendieck group over every field](artins-signed-permutation-identity-in-the-exact.md)
- [The dual Noether isomorphism](../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Noether isomorphism for exact categories](../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.natCard_nsmul_one_eq_sum_artinCoeff_indK0`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/GrothendieckGroup/GroupAlgebra/Artin.html#TauCeti.natCard_nsmul_one_eq_sum_artinCoeff_indK0).

## Sources

- [Tau Ceti documentation: `TauCeti.natCard_nsmul_one_eq_sum_artinCoeff_indK0`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/GrothendieckGroup/GroupAlgebra/Artin.html#TauCeti.natCard_nsmul_one_eq_sum_artinCoeff_indK0)
- [Source of `TauCeti.natCard_nsmul_one_eq_sum_artinCoeff_indK0` in TauCeti/RepresentationTheory/GrothendieckGroup/GroupAlgebra/Artin.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/GrothendieckGroup/GroupAlgebra/Artin.lean#L121)
