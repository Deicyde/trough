---
declaration: module
origin: cited
lean: MSSM.PermGroup, MSSM.chargeMap, MSSM.chargeMap_toSpecies, MSSM.repCharges, MSSM.repCharges_toSMSpecies, MSSM.toSpecies_sum_invariant, MSSM.Hd_invariant, MSSM.Hu_invariant
statement: formalized
proof: formalized
---

# Permutations of MSSM charges and solutions

The module `Physlib.Particles.SuperSymmetry.MSSMNu.AnomalyCancellation.Permutations`, [Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Permutations.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Permutations.lean): 15 declarations (1 instance with no name), 4 with a docstring.

> The three family MSSM charges has a family permutation of S₃⁶. This file defines this group
> and its action on the MSSM.

**`MSSM.PermGroup`**, a def, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Permutations.lean#L31).

> The group of family permutations is `S₃⁶`

```lean
def PermGroup
```

**An instance with no name**, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Permutations.lean#L35).

> The type `PermGroup` has a group instances derived from the group instance of it's target.

```lean
instance : Group PermGroup
```

**`MSSM.chargeMap`**, a def, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Permutations.lean#L39).

> The image of an element of `permGroup` under the representation on charges.

```lean
def chargeMap (f : PermGroup) : MSSMCharges.Charges →ₗ[ℚ] MSSMCharges.Charges
```

**`MSSM.chargeMap_toSpecies`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Permutations.lean#L55).

```lean
lemma chargeMap_toSpecies (f : PermGroup) (S : MSSMCharges.Charges) (j : Fin 6) :
    toSMSpecies j (chargeMap f S) = toSMSpecies j S ∘ f j
```

**`MSSM.repCharges`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Permutations.lean#L62).

> The representation of `permGroup` acting on the vector space of charges.

```lean
def repCharges : Representation ℚ PermGroup (MSSMCharges).Charges
```

**`MSSM.repCharges_toSMSpecies`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Permutations.lean#L84).

```lean
lemma repCharges_toSMSpecies (f : PermGroup) (S : MSSMCharges.Charges) (j : Fin 6) :
    toSMSpecies j (repCharges f S) = toSMSpecies j S ∘ f⁻¹ j
```

**`MSSM.toSpecies_sum_invariant`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Permutations.lean#L88).

```lean
lemma toSpecies_sum_invariant (m : ℕ) (f : PermGroup) (S : MSSMCharges.Charges) (j : Fin 6) :
    ∑ i, ((fun a => a ^ m) ∘ toSMSpecies j (repCharges f S)) i =
    ∑ i, ((fun a => a ^ m) ∘ toSMSpecies j S) i
```

**`MSSM.Hd_invariant`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Permutations.lean#L94).

```lean
lemma Hd_invariant (f : PermGroup) (S : MSSMCharges.Charges) :
    Hd (repCharges f S) = Hd S
```

**`MSSM.Hu_invariant`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Permutations.lean#L97).

```lean
lemma Hu_invariant (f : PermGroup) (S : MSSMCharges.Charges) :
    Hu (repCharges f S) = Hu S
```

**`MSSM.accGrav_invariant`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Permutations.lean#L101).

```lean
lemma accGrav_invariant (f : PermGroup) (S : MSSMCharges.Charges) :
    accGrav (repCharges f S) = accGrav S
```

**`MSSM.accSU2_invariant`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Permutations.lean#L109).

```lean
lemma accSU2_invariant (f : PermGroup) (S : MSSMCharges.Charges) :
    accSU2 (repCharges f S) = accSU2 S
```

**`MSSM.accSU3_invariant`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Permutations.lean#L117).

```lean
lemma accSU3_invariant (f : PermGroup) (S : MSSMCharges.Charges) :
    accSU3 (repCharges f S) = accSU3 S
```

**`MSSM.accYY_invariant`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Permutations.lean#L123).

```lean
lemma accYY_invariant (f : PermGroup) (S : MSSMCharges.Charges) :
    accYY (repCharges f S) = accYY S
```

**`MSSM.accQuad_invariant`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Permutations.lean#L130).

```lean
lemma accQuad_invariant (f : PermGroup) (S : MSSMCharges.Charges) :
    accQuad (repCharges f S) = accQuad S
```

**`MSSM.accCube_invariant`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Permutations.lean#L137).

```lean
lemma accCube_invariant (f : PermGroup) (S : MSSMCharges.Charges) :
    accCube (repCharges f S) = accCube S
```

## Depends on

- [The MSSM with 3 families and RHNs](mssmnu-anomalycancellation-basic.md)

## Sources

- [Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Permutations.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Permutations.lean)
