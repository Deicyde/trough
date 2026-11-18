---
declaration: module
origin: cited
lean: SMνCharges, SMνSpecies, SMνCharges.sum_one, SMνCharges.toSpeciesEquiv, SMνCharges.toSpecies, SMνCharges.charges_eq_toSpecies_eq, SMνCharges.toSMSpecies_toSpecies_inv, SMνCharges.toSpecies_one
statement: formalized
proof: formalized
---

# Anomaly cancellation conditions for the Standard Model with right-handed neutrinos

The module `Physlib.Particles.BeyondTheStandardModel.RHN.AnomalyCancellation.Basic`, [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean): 36 declarations, 24 with a docstring.

> This directory is related to the anomaly cancellation conditions (ACCs) for the Standard Model with
> right-handed neutrinos (SMν).

**`SMνCharges`**, a def, [line 25](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L25).

> The vector space of charges corresponding to the SM fermions with RHN.

```lean
def SMνCharges (n : ℕ) : ACCSystemCharges
```

**`SMνSpecies`**, a def, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L29).

> The vector spaces of charges of one species of fermions in the SM.

```lean
def SMνSpecies (n : ℕ) : ACCSystemCharges
```

**`SMνCharges.sum_one`**, a lemma, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L36).

```lean
lemma sum_one  [AddCommMonoid M] (f : Fin (SMνSpecies 1).numberCharges → M) :
    ∑ i, f i = f ⟨0, by simp⟩
```

**`SMνCharges.toSpeciesEquiv`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L45).

> An equivalence between `(SMνCharges n).charges` and `(Fin 6 → Fin n → ℚ)`
> splitting the charges into species.

```lean
def toSpeciesEquiv : (SMνCharges n).Charges ≃ (Fin 6 → Fin n → ℚ)
```

**`SMνCharges.toSpecies`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L50).

> Given an `i ∈ Fin 6`, the projection of charges onto a given species.

```lean
def toSpecies (i : Fin 6) : (SMνCharges n).Charges →ₗ[ℚ] (SMνSpecies n).Charges
```

**`SMνCharges.charges_eq_toSpecies_eq`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L55).

```lean
lemma charges_eq_toSpecies_eq (S T : (SMνCharges n).Charges) :
    S = T ↔ ∀ i, toSpecies i S = toSpecies i T
```

**`SMνCharges.toSMSpecies_toSpecies_inv`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L62).

```lean
lemma toSMSpecies_toSpecies_inv (i : Fin 6) (f : Fin 6 → Fin n → ℚ) :
    (toSpecies i) (toSpeciesEquiv.symm f) = f i
```

**`SMνCharges.toSpecies_one`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L67).

```lean
lemma toSpecies_one (S : (SMνCharges 1).Charges) (j : Fin 6) :
    toSpecies j S ⟨0, zero_lt_succ 0⟩ = S j
```

**`SMνCharges.Q`**, an abbrev, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L78).

> The `Q` charges as a map `Fin n → ℚ`.

```lean
abbrev Q
```

**`SMνCharges.U`**, an abbrev, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L80).

> The `U` charges as a map `Fin n → ℚ`.

```lean
abbrev U
```

**`SMνCharges.D`**, an abbrev, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L82).

> The `D` charges as a map `Fin n → ℚ`.

```lean
abbrev D
```

**`SMνCharges.L`**, an abbrev, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L84).

> The `L` charges as a map `Fin n → ℚ`.

```lean
abbrev L
```

**`SMνCharges.E`**, an abbrev, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L86).

> The `E` charges as a map `Fin n → ℚ`.

```lean
abbrev E
```

**`SMνCharges.N`**, an abbrev, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L88).

> The `N` charges as a map `Fin n → ℚ`.

```lean
abbrev N
```

**`SMνACCs.accGrav`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L100).

> The gravitational anomaly equation.

```lean
def accGrav : (SMνCharges n).Charges →ₗ[ℚ] ℚ
```

**`SMνACCs.accGrav_decomp`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L118).

```lean
lemma accGrav_decomp (S : (SMνCharges n).Charges) :
    accGrav S = 6 * ∑ i, Q S i + 3 * ∑ i, U S i + 3 * ∑ i, D S i + 2 * ∑ i, L S i + ∑ i, E S i +
      ∑ i, N S i
```

**`SMνACCs.accGrav_ext`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L127).

> Extensionality lemma for `accGrav`.

```lean
lemma accGrav_ext {S T : (SMνCharges n).Charges}
    (hj : ∀ (j : Fin 6), ∑ i, (toSpecies j) S i = ∑ i, (toSpecies j) T i) :
    accGrav S = accGrav T
```

**`SMνACCs.accSU2`**, a def, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L135).

> The `SU(2)` anomaly equation.

```lean
def accSU2 : (SMνCharges n).Charges →ₗ[ℚ] ℚ
```

**`SMνACCs.accSU2_decomp`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L153).

```lean
lemma accSU2_decomp (S : (SMνCharges n).Charges) :
    accSU2 S = 3 * ∑ i, Q S i + ∑ i, L S i
```

**`SMνACCs.accSU2_ext`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L161).

> Extensionality lemma for `accSU2`.

```lean
lemma accSU2_ext {S T : (SMνCharges n).Charges}
    (hj : ∀ (j : Fin 6), ∑ i, (toSpecies j) S i = ∑ i, (toSpecies j) T i) :
    accSU2 S = accSU2 T
```

**`SMνACCs.accSU3`**, a def, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L169).

> The `SU(3)` anomaly equations.

```lean
def accSU3 : (SMνCharges n).Charges →ₗ[ℚ] ℚ
```

**`SMνACCs.accSU3_decomp`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L187).

```lean
lemma accSU3_decomp (S : (SMνCharges n).Charges) :
    accSU3 S = 2 * ∑ i, Q S i + ∑ i, U S i + ∑ i, D S i
```

**`SMνACCs.accSU3_ext`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L195).

> Extensionality lemma for `accSU3`.

```lean
lemma accSU3_ext {S T : (SMνCharges n).Charges}
    (hj : ∀ (j : Fin 6), ∑ i, (toSpecies j) S i = ∑ i, (toSpecies j) T i) :
    accSU3 S = accSU3 T
```

**`SMνACCs.accYY`**, a def, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L203).

> The `Y²` anomaly equation.

```lean
def accYY : (SMνCharges n).Charges →ₗ[ℚ] ℚ
```

**`SMνACCs.accYY_decomp`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L222).

```lean
lemma accYY_decomp (S : (SMνCharges n).Charges) :
    accYY S = ∑ i, Q S i + 8 * ∑ i, U S i + 2 * ∑ i, D S i + 3 * ∑ i, L S i + 6 * ∑ i, E S i
```

**`SMνACCs.accYY_ext`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L230).

> Extensionality lemma for `accYY`.

```lean
lemma accYY_ext {S T : (SMνCharges n).Charges}
    (hj : ∀ (j : Fin 6), ∑ i, (toSpecies j) S i = ∑ i, (toSpecies j) T i) :
    accYY S = accYY T
```

**`SMνACCs.quadBiLin`**, a def, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L239).

> The quadratic bilinear map.

```lean
def quadBiLin : BiLinearSymm (SMνCharges n).Charges
```

**`SMνACCs.quadBiLin_decomp`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L268).

```lean
lemma quadBiLin_decomp (S T : (SMνCharges n).Charges) :
    quadBiLin S T = ∑ i, Q S i * Q T i - 2 * ∑ i, U S i * U T i +
        ∑ i, D S i * D T i - ∑ i, L S i * L T i + ∑ i, E S i * E T i
```

**`SMνACCs.accQuad`**, a def, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L280).

> The quadratic anomaly cancellation condition.

```lean
def accQuad : HomogeneousQuadratic (SMνCharges n).Charges
```

**`SMνACCs.accQuad_decomp`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L283).

```lean
lemma accQuad_decomp (S : (SMνCharges n).Charges) :
    accQuad S = ∑ i, (Q S i)^2 - 2 * ∑ i, (U S i)^2 + ∑ i, (D S i)^2 - ∑ i, (L S i)^2
    + ∑ i, (E S i)^2
```

**`SMνACCs.accQuad_ext`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L292).

> Extensionality lemma for `accQuad`.

```lean
lemma accQuad_ext {S T : (SMνCharges n).Charges}
    (h : ∀ j, ∑ i, ((fun a => a^2) ∘ toSpecies j S) i =
    ∑ i, ((fun a => a^2) ∘ toSpecies j T) i) :
    accQuad S = accQuad T
```

**`SMνACCs.cubeTriLin`**, a def, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L302).

> The symmetric trilinear form used to define the cubic acc.

```lean
def cubeTriLin : TriLinearSymm (SMνCharges n).Charges
```

**`SMνACCs.cubeTriLin_decomp`**, a lemma, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L336).

```lean
lemma cubeTriLin_decomp (S T R : (SMνCharges n).Charges) :
    cubeTriLin S T R = 6 * ∑ i, (Q S i * Q T i * Q R i) + 3 * ∑ i, (U S i * U T i * U R i) +
      3 * ∑ i, (D S i * D T i * D R i) + 2 * ∑ i, (L S i * L T i * L R i) +
      ∑ i, (E S i * E T i * E R i) + ∑ i, (N S i * N T i * N R i)
```

**`SMνACCs.accCube`**, a def, [line 347](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L347).

> The cubic ACC.

```lean
def accCube : HomogeneousCubic (SMνCharges n).Charges
```

**`SMνACCs.accCube_decomp`**, a lemma, [line 349](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L349).

```lean
lemma accCube_decomp (S : (SMνCharges n).Charges) :
    accCube S = 6 * ∑ i, (Q S i)^3 + 3 * ∑ i, (U S i)^3 + 3 * ∑ i, (D S i)^3 + 2 * ∑ i, (L S i)^3 +
      ∑ i, (E S i)^3 + ∑ i, (N S i)^3
```

**`SMνACCs.accCube_ext`**, a lemma, [line 358](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean#L358).

> Extensionality lemma for `accCube`.

```lean
lemma accCube_ext {S T : (SMνCharges n).Charges}
    (h : ∀ j, ∑ i, ((fun a => a^3) ∘ toSpecies j S) i =
    ∑ i, ((fun a => a^3) ∘ toSpecies j T) i) :
    accCube S = accCube T
```

## Depends on

- [Anomaly cancellation conditions](../../qft/anomalycancellation/basic.md)

## Sources

- [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Basic.lean)
