---
declaration: module
origin: cited
lean: SM.PermGroup, SM.chargeMap, SM.repCharges, SM.repCharges_toSpecies, SM.toSpecies_sum_invariant, SM.accGrav_invariant, SM.accSU2_invariant, SM.accSU3_invariant
statement: formalized
proof: formalized
---

# Permutations of SM with no RHN.

The module `Physlib.Particles.StandardModel.AnomalyCancellation.Permutations`, [Physlib/Particles/StandardModel/AnomalyCancellation/Permutations.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Permutations.lean): 12 declarations (1 instance with no name), 12 with a docstring.

> We define the group of permutations for the SM charges with no RHN.

**`SM.PermGroup`**, a def, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Permutations.lean#L31).

> The group of `Sₙ` permutations for each species.

```lean
def PermGroup (n : ℕ)
```

**An instance with no name**, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Permutations.lean#L38).

> The type `PermGroup n` inherits the instance of a group from it's
> target space `Equiv.Perm`.

```lean
instance : Group (PermGroup n)
```

**`SM.chargeMap`**, a def, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Permutations.lean#L42).

> The image of an element of `permGroup n` under the representation on charges.

```lean
def chargeMap (f : PermGroup n) : (SMCharges n).Charges →ₗ[ℚ] (SMCharges n).Charges
```

**`SM.repCharges`**, a def, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Permutations.lean#L49).

> The representation of `(permGroup n)` acting on the vector space of charges.

```lean
def repCharges {n : ℕ} : Representation ℚ (PermGroup n) (SMCharges n).Charges
```

**`SM.repCharges_toSpecies`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Permutations.lean#L69).

> The species charges of a set of charges acted on by a family permutation is the permutation
> of those species charges with the corresponding part of the family permutation.

```lean
lemma repCharges_toSpecies (f : PermGroup n) (S : (SMCharges n).Charges) (j : Fin 5) :
    toSpecies j (repCharges f S) = toSpecies j S ∘ f⁻¹ j
```

**`SM.toSpecies_sum_invariant`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Permutations.lean#L75).

> The sum over every charge in any species to some power `m` is invariant under the group
> action.

```lean
lemma toSpecies_sum_invariant (m : ℕ) (f : PermGroup n) (S : (SMCharges n).Charges) (j : Fin 5) :
    ∑ i, ((fun a => a ^ m) ∘ toSpecies j (repCharges f S)) i =
    ∑ i, ((fun a => a ^ m) ∘ toSpecies j S) i
```

**`SM.accGrav_invariant`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Permutations.lean#L83).

> The gravitational anomaly equations is invariant under family permutations.

```lean
lemma accGrav_invariant (f : PermGroup n) (S : (SMCharges n).Charges) :
    accGrav (repCharges f S) = accGrav S
```

**`SM.accSU2_invariant`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Permutations.lean#L89).

> The `SU(2)` anomaly equation is invariant under family permutations.

```lean
lemma accSU2_invariant (f : PermGroup n) (S : (SMCharges n).Charges) :
    accSU2 (repCharges f S) = accSU2 S
```

**`SM.accSU3_invariant`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Permutations.lean#L95).

> The `SU(3)` anomaly equation is invariant under family permutations.

```lean
lemma accSU3_invariant (f : PermGroup n) (S : (SMCharges n).Charges) :
    accSU3 (repCharges f S) = accSU3 S
```

**`SM.accYY_invariant`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Permutations.lean#L102).

> The `Y²` anomaly equation is invariant under family permutations.

```lean
lemma accYY_invariant (f : PermGroup n) (S : (SMCharges n).Charges) :
    accYY (repCharges f S) = accYY S
```

**`SM.accQuad_invariant`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Permutations.lean#L108).

> The quadratic anomaly equation is invariant under family permutations.

```lean
lemma accQuad_invariant (f : PermGroup n) (S : (SMCharges n).Charges) :
    accQuad (repCharges f S) = accQuad S
```

**`SM.accCube_invariant`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Permutations.lean#L114).

> The cubic anomaly equation is invariant under family permutations.

```lean
lemma accCube_invariant (f : PermGroup n) (S : (SMCharges n).Charges) :
    accCube (repCharges f S) = accCube S
```

## Depends on

- [Anomaly cancellation conditions for the n-family SM.](anomalycancellation-basic.md)

## Sources

- [Physlib/Particles/StandardModel/AnomalyCancellation/Permutations.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Permutations.lean)
