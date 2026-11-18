---
declaration: module
origin: cited
lean: SMRHN.PermGroup, SMRHN.chargeMap, SMRHN.repCharges, SMRHN.repCharges_toSpecies, SMRHN.toSpecies_sum_invariant, SMRHN.accGrav_invariant, SMRHN.accSU2_invariant, SMRHN.accSU3_invariant
statement: formalized
proof: formalized
---

# Permutations of SM charges with RHN.

The module `Physlib.Particles.BeyondTheStandardModel.RHN.AnomalyCancellation.Permutations`, [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Permutations.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Permutations.lean): 12 declarations (1 instance with no name), 4 with a docstring.

> We define the group of permutations for the SM charges with RHN.

**`SMRHN.PermGroup`**, a def, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Permutations.lean#L29).

> The group of `Sₙ` permutations for each species.

```lean
def PermGroup (n : ℕ)
```

**An instance with no name**, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Permutations.lean#L35).

> The instance of a group on `PermGroup n` through the target space `Equiv.Perm (Fin n)`.

```lean
instance : Group (PermGroup n)
```

**`SMRHN.chargeMap`**, a def, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Permutations.lean#L39).

> The image of an element of `permGroup n` under the representation on charges.

```lean
def chargeMap (f : PermGroup n) : (SMνCharges n).Charges →ₗ[ℚ] (SMνCharges n).Charges
```

**`SMRHN.repCharges`**, a def, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Permutations.lean#L47).

> The representation of `(permGroup n)` acting on the vector space of charges.

```lean
def repCharges {n : ℕ} : Representation ℚ (PermGroup n) (SMνCharges n).Charges
```

**`SMRHN.repCharges_toSpecies`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Permutations.lean#L64).

```lean
lemma repCharges_toSpecies (f : PermGroup n) (S : (SMνCharges n).Charges) (j : Fin 6) :
    toSpecies j (repCharges f S) = toSpecies j S ∘ f⁻¹ j
```

**`SMRHN.toSpecies_sum_invariant`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Permutations.lean#L68).

```lean
lemma toSpecies_sum_invariant (m : ℕ) (f : PermGroup n) (S : (SMνCharges n).Charges) (j : Fin 6) :
    ∑ i, ((fun a => a ^ m) ∘ toSpecies j (repCharges f S)) i =
    ∑ i, ((fun a => a ^ m) ∘ toSpecies j S) i
```

**`SMRHN.accGrav_invariant`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Permutations.lean#L75).

```lean
lemma accGrav_invariant (f : PermGroup n) (S : (SMνCharges n).Charges) :
    accGrav (repCharges f S) = accGrav S
```

**`SMRHN.accSU2_invariant`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Permutations.lean#L80).

```lean
lemma accSU2_invariant (f : PermGroup n) (S : (SMνCharges n).Charges) :
    accSU2 (repCharges f S) = accSU2 S
```

**`SMRHN.accSU3_invariant`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Permutations.lean#L85).

```lean
lemma accSU3_invariant (f : PermGroup n) (S : (SMνCharges n).Charges) :
    accSU3 (repCharges f S) = accSU3 S
```

**`SMRHN.accYY_invariant`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Permutations.lean#L90).

```lean
lemma accYY_invariant (f : PermGroup n) (S : (SMνCharges n).Charges) :
    accYY (repCharges f S) = accYY S
```

**`SMRHN.accQuad_invariant`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Permutations.lean#L94).

```lean
lemma accQuad_invariant (f : PermGroup n) (S : (SMνCharges n).Charges) :
    accQuad (repCharges f S) = accQuad S
```

**`SMRHN.accCube_invariant`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Permutations.lean#L98).

```lean
lemma accCube_invariant (f : PermGroup n) (S : (SMνCharges n).Charges) :
    accCube (repCharges f S) = accCube S
```

## Depends on

- [Anomaly cancellation conditions for the Standard Model with right-handed neutrinos](rhn-anomalycancellation-basic.md)

## Sources

- [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Permutations.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Permutations.lean)
