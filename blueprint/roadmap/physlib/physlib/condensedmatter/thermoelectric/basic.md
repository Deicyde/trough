---
declaration: module
origin: cited
lean: CondensedMatter.ThermoelectricMaterial, CondensedMatter.ThermoelectricMaterial.powerFactor, CondensedMatter.ThermoelectricMaterial.powerFactor_pos, CondensedMatter.ThermoelectricMaterial.totalThermalConductivity, CondensedMatter.ThermoelectricMaterial.totalThermalConductivity_pos, CondensedMatter.ThermoelectricMaterial.figureOfMerit, CondensedMatter.ThermoelectricMaterial.figureOfMerit_eq, CondensedMatter.ThermoelectricMaterial.figureOfMerit_pos
statement: formalized
proof: formalized
---

# Thermoelectric figure of merit

The module `Physlib.CondensedMatter.Thermoelectric.Basic`, [Physlib/CondensedMatter/Thermoelectric/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Thermoelectric/Basic.lean): 9 declarations, 9 with a docstring.

## i. Overview

> A thermoelectric material converts a temperature difference into electrical
> power. In the linear-response (Onsager) regime, the coupled transport of
> charge and heat in an isotropic material is governed by the constitutive
> relations
>
>   J = σ (E − S ∇T),        q = T S J − κ ∇T,
>
> so a thermoelectric material is characterized by exactly four transport
> coefficients: the Seebeck coefficient `S`, the electrical conductivity `σ`,
> and the thermal conductivity `κ = κl + κe`, split into its lattice (phonon)
> and electronic contributions because the two channels respond independently
> to material design. These four coefficients are collected in the structure
> `ThermoelectricMaterial`, and everything in this file is stated on it.
>
> The performance of the material at absolute temperature `T` is captured by
> the dimensionless figure of merit
>
>   zT = σ S² T / (κl + κe),
>
> whose numerator groups into the power factor `PF = σ S²`. Temperature is a
> state variable, not a material property, so `T` enters as an argument rather
> than a field. The four coefficients of a real material are themselves
> temperature-dependent, so a `ThermoelectricMaterial` should be read as a
> material at an operating point, its coefficients evaluated at the same
> temperature at which `zT` is evaluated.
>
> In this file all quantities are real numbers in a fixed consistent system of
> units, following the convention of `Physlib.Thermodynamics.IdealGas.Basic`.

## ii. Key results

> - `ThermoelectricMaterial`: the four linear-response transport coefficients
>   of a thermoelectric material, with their physical sign constraints.
> - `powerFactor`: the thermoelectric power factor `σ S²`.
> - `totalThermalConductivity`: the total thermal conductivity `κl + κe`.
> - `figureOfMerit`: the dimensionless figure of merit `zT`.
> - `figureOfMerit_eq`: the flat form `zT = σ S² T / (κl + κe)`.
> - `figureOfMerit_pos`: positivity of `zT` for a material with a nonzero
>   Seebeck coefficient at positive temperature.
> - `figureOfMerit_le_of_le`: lowering the lattice thermal conductivity raises
>   `zT`, the phonon-glass electron-crystal design principle.

## iv. References

> * Ioffe, A.F., Semiconductor Thermoelements and Thermoelectric Cooling, Infosearch (1957).
>   [ref: ioffe\_1957]
> * Snyder, G.J., Toberer, E.S., Complex thermoelectric materials, Nature Materials 7, 105–114
>   (2008). [ref: snyder\_toberer\_2008]

## A. The thermoelectric material

> The four fields are the complete set of linear-response coefficients for
> coupled charge and heat transport in an isotropic material: no further
> material parameter enters the steady-state thermoelectric equations, and
> `zT` is a function of exactly these four together with the temperature.
> The sign constraints are physical: a thermoelectric material conducts
> charge (`0 < σ`) and its lattice conducts heat (`0 < κl`), while the
> electronic heat channel can be negligible but never negative (`0 ≤ κe`).
> The Seebeck coefficient is unconstrained: its sign records the carrier
> type (negative for electrons, positive for holes), and it vanishes at
> compensation points.

**`CondensedMatter.ThermoelectricMaterial`**, a structure, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Thermoelectric/Basic.lean#L102).

> A thermoelectric material in the linear-response regime, characterized by
> its four transport coefficients.

```lean
structure ThermoelectricMaterial where
  /-- The Seebeck coefficient `S`: the voltage developed per unit temperature
  difference. Its sign records the dominant carrier type. -/
  S : ℝ
  /-- The electrical conductivity `σ`. -/
  σ : ℝ
  /-- The lattice (phonon) contribution `κl` to the thermal conductivity. -/
  κl : ℝ
  /-- The electronic contribution `κe` to the thermal conductivity. -/
  κe : ℝ
  σ_pos : 0 < σ
  κl_pos : 0 < κl
  κe_nonneg : 0 ≤ κe
```

## B. The power factor

**`CondensedMatter.ThermoelectricMaterial.powerFactor`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Thermoelectric/Basic.lean#L125).

> The thermoelectric power factor `PF = σ S²` of a material.

```lean
def powerFactor (M : ThermoelectricMaterial) : ℝ
```

**`CondensedMatter.ThermoelectricMaterial.powerFactor_pos`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Thermoelectric/Basic.lean#L128).

> The power factor is positive when the Seebeck coefficient is nonzero.

```lean
lemma powerFactor_pos {M : ThermoelectricMaterial} (hS : M.S ≠ 0) :
    0 < M.powerFactor
```

## C. The total thermal conductivity

**`CondensedMatter.ThermoelectricMaterial.totalThermalConductivity`**, a def, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Thermoelectric/Basic.lean#L143).

> The total thermal conductivity `κl + κe` of a material, the sum of the
> lattice (phonon) and electronic contributions.

```lean
def totalThermalConductivity (M : ThermoelectricMaterial) : ℝ
```

**`CondensedMatter.ThermoelectricMaterial.totalThermalConductivity_pos`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Thermoelectric/Basic.lean#L146).

> The total thermal conductivity is positive.

```lean
lemma totalThermalConductivity_pos (M : ThermoelectricMaterial) :
    0 < M.totalThermalConductivity
```

## D. The figure of merit

**`CondensedMatter.ThermoelectricMaterial.figureOfMerit`**, a def, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Thermoelectric/Basic.lean#L158).

> The dimensionless thermoelectric figure of merit
> `zT = PF · T / (κl + κe)` of a material at absolute temperature `T`.

```lean
def figureOfMerit (M : ThermoelectricMaterial) (T : ℝ) : ℝ
```

### D.1. Equalities for the figure of merit

**`CondensedMatter.ThermoelectricMaterial.figureOfMerit_eq`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Thermoelectric/Basic.lean#L169).

> The figure of merit in its standard flat form
> `zT = σ S² T / (κl + κe)`.

```lean
lemma figureOfMerit_eq (M : ThermoelectricMaterial) (T : ℝ) :
    M.figureOfMerit T = M.σ * M.S ^ 2 * T / (M.κl + M.κe)
```

### D.2. Positivity of the figure of merit

**`CondensedMatter.ThermoelectricMaterial.figureOfMerit_pos`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Thermoelectric/Basic.lean#L182).

> The figure of merit is positive at positive temperature when the Seebeck
> coefficient is nonzero.

```lean
lemma figureOfMerit_pos {M : ThermoelectricMaterial} {T : ℝ}
    (hS : M.S ≠ 0) (hT : 0 < T) :
    0 < M.figureOfMerit T
```

### D.3. Monotonicity in the lattice thermal conductivity

**`CondensedMatter.ThermoelectricMaterial.figureOfMerit_le_of_le`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Thermoelectric/Basic.lean#L200).

> Lowering the lattice thermal conductivity raises the figure of merit: if
> `M.κl ≤ κl'` then the material with lattice conductivity `κl'` (all other
> coefficients equal) has the smaller `zT`. This is the phonon-glass
> electron-crystal design principle: scatter phonons without degrading
> electronic transport. Note the hypotheses: no condition on the Seebeck
> coefficient is needed, since monotonicity only requires the numerator
> `σ S² T` to be nonnegative.

```lean
lemma figureOfMerit_le_of_le (M : ThermoelectricMaterial) {κl' T : ℝ}
    (hpos : 0 < κl') (h : M.κl ≤ κl') (hT : 0 ≤ T) :
    figureOfMerit { M with κl := κl', κl_pos := hpos } T ≤ M.figureOfMerit T
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/CondensedMatter/Thermoelectric/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Thermoelectric/Basic.lean)
