---
declaration: theorem
origin: cited
lean: TauCeti.adjoin_symplecticCrossing_symplecticCupCap_eq_centralizer_of_charZero
statement: formalized
proof: formalized
---

# Brauer duality for the symplectic group on two strands in characteristic zero, for instance over `ℂ`

the unit `2` has no nontrivial power equal to `1`.

```lean
TauCeti.adjoin_symplecticCrossing_symplecticCupCap_eq_centralizer_of_charZero.{u_1} {K : Type u_1}
  [Field K] [CharZero K] {n : ℕ} :
  K[TauCeti.symplecticCrossing K n, TauCeti.symplecticCupCap K n] =
    Subalgebra.centralizer K (Set.range ⇑((TauCeti.stdSymplecticRep K n).tensorPower 2))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Brauer duality for the symplectic group on two strands](brauer-duality-for-the-symplectic-group-on-two-s.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.adjoin_symplecticCrossing_symplecticCupCap_eq_centralizer_of_charZero`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/BrauerGenerators/Symplectic/TwoStrands.html#TauCeti.adjoin_symplecticCrossing_symplecticCupCap_eq_centralizer_of_charZero).

## Sources

- [Tau Ceti documentation: `TauCeti.adjoin_symplecticCrossing_symplecticCupCap_eq_centralizer_of_charZero`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/BrauerGenerators/Symplectic/TwoStrands.html#TauCeti.adjoin_symplecticCrossing_symplecticCupCap_eq_centralizer_of_charZero)
- [Source of `TauCeti.adjoin_symplecticCrossing_symplecticCupCap_eq_centralizer_of_charZero` in TauCeti/RepresentationTheory/ClassicalGroups/BrauerGenerators/Symplectic/TwoStrands.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/ClassicalGroups/BrauerGenerators/Symplectic/TwoStrands.lean#L671)
