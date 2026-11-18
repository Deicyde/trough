---
declaration: module
origin: cited
lean: SMCharges, SMSpecies, SMCharges.sum_SMSpecies_numberCharges_one, SMCharges.toSpeciesEquiv, SMCharges.toSpecies, SMCharges.toSpecies_apply_eq, SMCharges.charges_eq_toSpecies_eq, SMCharges.toSMSpecies_toSpecies_inv
statement: formalized
proof: formalized
---

# Anomaly cancellation conditions for the n-family SM.

The module `Physlib.Particles.StandardModel.AnomalyCancellation.Basic`, [Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean): 27 declarations, 23 with a docstring.

> We define the ACC system for the Standard Model with`n`-families and no RHN.

**`SMCharges`**, a def, [line 24](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean#L24).

> Associate to each (including RHN) SM fermion a set of charges

```lean
def SMCharges (n : ℕ) : ACCSystemCharges
```

**`SMSpecies`**, a def, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean#L28).

> The vector space associated with a single species of fermions.

```lean
def SMSpecies (n : ℕ) : ACCSystemCharges
```

**`SMCharges.sum_SMSpecies_numberCharges_one`**, a lemma, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean#L35).

```lean
lemma sum_SMSpecies_numberCharges_one {M} [AddCommMonoid M]
    (f : Fin (SMSpecies 1).numberCharges → M) :
    ∑ i, f i = f ⟨0, by simp⟩
```

**`SMCharges.toSpeciesEquiv`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean#L45).

> An equivalence between the set `(SMCharges n).charges` and the set
> `(Fin 5 → Fin n → ℚ)`.

```lean
def toSpeciesEquiv : (SMCharges n).Charges ≃ (Fin 5 → Fin (SMSpecies n).numberCharges → ℚ)
```

**`SMCharges.toSpecies`**, a def, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean#L51).

> For a given `i ∈ Fin 5`, the projection of a charge onto that species.

```lean
def toSpecies (i : Fin 5) : (SMCharges n).Charges →ₗ[ℚ] (SMSpecies n).Charges
```

**`SMCharges.toSpecies_apply_eq`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean#L56).

```lean
lemma toSpecies_apply_eq (i : Fin 5) (S : (SMCharges n).Charges) :
    toSpecies i S = fun j => toSpeciesEquiv S i j
```

**`SMCharges.charges_eq_toSpecies_eq`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean#L59).

```lean
lemma charges_eq_toSpecies_eq (S T : (SMCharges n).Charges) :
    S = T ↔ ∀ i, toSpecies i S = toSpecies i T
```

**`SMCharges.toSMSpecies_toSpecies_inv`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean#L66).

```lean
lemma toSMSpecies_toSpecies_inv (i : Fin 5) (f : Fin 5 → Fin n → ℚ) :
    (toSpecies i) (toSpeciesEquiv.symm f) = f i
```

**`SMCharges.Q`**, an abbrev, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean#L72).

> The `Q` charges as a map `Fin n → ℚ`.

```lean
abbrev Q
```

**`SMCharges.U`**, an abbrev, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean#L75).

> The `U` charges as a map `Fin n → ℚ`.

```lean
abbrev U
```

**`SMCharges.D`**, an abbrev, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean#L78).

> The `D` charges as a map `Fin n → ℚ`.

```lean
abbrev D
```

**`SMCharges.L`**, an abbrev, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean#L81).

> The `L` charges as a map `Fin n → ℚ`.

```lean
abbrev L
```

**`SMCharges.E`**, an abbrev, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean#L84).

> The `E` charges as a map `Fin n → ℚ`.

```lean
abbrev E
```

**`SMACCs.accGrav`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean#L96).

> The gravitational anomaly equation.

```lean
def accGrav : (SMCharges n).Charges →ₗ[ℚ] ℚ
```

**`SMACCs.accGrav_ext`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean#L115).

> Extensionality lemma for `accGrav`.

```lean
lemma accGrav_ext {S T : (SMCharges n).Charges}
    (hj : ∀ (j : Fin 5), ∑ i, (toSpecies j) S i = ∑ i, (toSpecies j) T i) :
    accGrav S = accGrav T
```

**`SMACCs.accSU2`**, a def, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean#L126).

> The `SU(2)` anomaly equation.

```lean
def accSU2 : (SMCharges n).Charges →ₗ[ℚ] ℚ
```

**`SMACCs.accSU2_ext`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean#L145).

> Extensionality lemma for `accSU2`.

```lean
lemma accSU2_ext {S T : (SMCharges n).Charges}
    (hj : ∀ (j : Fin 5), ∑ i, (toSpecies j) S i = ∑ i, (toSpecies j) T i) :
    accSU2 S = accSU2 T
```

**`SMACCs.accSU3`**, a def, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean#L156).

> The `SU(3)` anomaly equations.

```lean
def accSU3 : (SMCharges n).Charges →ₗ[ℚ] ℚ
```

**`SMACCs.accSU3_ext`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean#L175).

> Extensionality lemma for `accSU3`.

```lean
lemma accSU3_ext {S T : (SMCharges n).Charges}
    (hj : ∀ (j : Fin 5), ∑ i, (toSpecies j) S i = ∑ i, (toSpecies j) T i) :
    accSU3 S = accSU3 T
```

**`SMACCs.accYY`**, a def, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean#L186).

> The `Y²` anomaly equation.

```lean
def accYY : (SMCharges n).Charges →ₗ[ℚ] ℚ
```

**`SMACCs.accYY_ext`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean#L205).

> Extensionality lemma for `accYY`.

```lean
lemma accYY_ext {S T : (SMCharges n).Charges}
    (hj : ∀ (j : Fin 5), ∑ i, (toSpecies j) S i = ∑ i, (toSpecies j) T i) :
    accYY S = accYY T
```

**`SMACCs.quadBiLin`**, a def, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean#L217).

> The quadratic bilinear map.

```lean
def quadBiLin : BiLinearSymm (SMCharges n).Charges
```

**`SMACCs.accQuad`**, a def, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean#L251).

> The quadratic anomaly cancellation condition.

```lean
def accQuad : HomogeneousQuadratic (SMCharges n).Charges
```

**`SMACCs.accQuad_ext`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean#L256).

> Extensionality lemma for `accQuad`.

```lean
lemma accQuad_ext {S T : (SMCharges n).Charges}
    (h : ∀ j, ∑ i, ((fun a => a^2) ∘ toSpecies j S) i =
    ∑ i, ((fun a => a^2) ∘ toSpecies j T) i) :
    accQuad S = accQuad T
```

**`SMACCs.cubeTriLin`**, a def, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean#L270).

> The trilinear function defining the cubic.

```lean
def cubeTriLin : TriLinearSymm (SMCharges n).Charges
```

**`SMACCs.accCube`**, a def, [line 309](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean#L309).

> The cubic acc.

```lean
def accCube : HomogeneousCubic (SMCharges n).Charges
```

**`SMACCs.accCube_ext`**, a lemma, [line 313](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean#L313).

> Extensionality lemma for `accCube`.

```lean
lemma accCube_ext {S T : (SMCharges n).Charges}
    (h : ∀ j, ∑ i, ((fun a => a^3) ∘ toSpecies j S) i =
    ∑ i, ((fun a => a^3) ∘ toSpecies j T) i) :
    accCube S = accCube T
```

## Depends on

- [Anomaly cancellation conditions](../../qft/anomalycancellation/basic.md)

## Sources

- [Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/Basic.lean)
