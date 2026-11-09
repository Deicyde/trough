---
declaration: theorem
origin: cited
lean: TauCeti.natCard_nsmul_eq_sum_artinCoeff_indK0_resK0
statement: formalized
proof: formalized
---

# Artin's induction identity for every virtual class over every field

Multiplying by
`|G|` expresses a class as the Artin-coefficient sum of its induced restrictions.

```lean
TauCeti.natCard_nsmul_eq_sum_artinCoeff_indK0_resK0.{u} (k G : Type u) [Field k] [Group G]
  [Finite G] (x : TauCeti.ExactK0 (TauCeti.finiteModulesExactStructure (MonoidAlgebra k G))) :
  Nat.card G • x =
    ∑ᶠ (C : Subgroup G),
      (C.artinCoeff * ↑(Nat.card ↥C)) • (TauCeti.indK0 k C) ((TauCeti.resK0 k C.subtype) x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Artin's identity in `G₀(k[G])` over every field, written as induction of the unit from subgroups](artins-identity-in-g0-k-g-over-every-field-writt.md)
- [The dual Noether isomorphism](../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Noether isomorphism for exact categories](../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.natCard_nsmul_eq_sum_artinCoeff_indK0_resK0`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/GrothendieckGroup/GroupAlgebra/Artin.html#TauCeti.natCard_nsmul_eq_sum_artinCoeff_indK0_resK0).

## Sources

- [Tau Ceti documentation: `TauCeti.natCard_nsmul_eq_sum_artinCoeff_indK0_resK0`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/GrothendieckGroup/GroupAlgebra/Artin.html#TauCeti.natCard_nsmul_eq_sum_artinCoeff_indK0_resK0)
- [Source of `TauCeti.natCard_nsmul_eq_sum_artinCoeff_indK0_resK0` in TauCeti/RepresentationTheory/GrothendieckGroup/GroupAlgebra/Artin.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/GrothendieckGroup/GroupAlgebra/Artin.lean#L130)
