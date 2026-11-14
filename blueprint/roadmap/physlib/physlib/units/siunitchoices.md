---
declaration: module
origin: cited
lean: CurrentUnit, CurrentUnit.amperes, CurrentUnit.milliamperes, AmountUnit, AmountUnit.moles, LuminousIntensityUnit, LuminousIntensityUnit.candelas, prod_univ_ISQDimensionBase
statement: formalized
proof: formalized
---

# A typed unit choice over the ISQ base quantities (the SI units)

The module `Physlib.Units.SIUnitChoices`, [Physlib/Units/SIUnitChoices.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/SIUnitChoices.lean): 16 declarations (4 instances with no name), 12 with a docstring.

> `LTMCTUnitChoices` is the typed unit choice over PhysLib's default dimension basis
> `LTMCTDimensionBase`. This module gives the *second* typed unit choice — over the
> seven ISQ base quantities `ISQDimensionBase` — realised through the basis-generic
> `UnitMagnitudeCatalog` / `UnitSystem` machinery of `Physlib.Units.UnitSystem`. It is the concrete
> payoff of parametrising the unit side: the same generic layer produces a fully *typed*
> unit choice over a different basis, and the scaling homomorphism comes for free from
> `UnitScale.dimScale` — nothing is re-proved by hand.
>
> The ISQ base quantities are length, mass, time, electric current, thermodynamic
> temperature, amount of substance and luminous intensity. Four of the corresponding typed
> unit types already exist (`LengthUnit`, `MassUnit`, `TimeUnit`, `TemperatureUnit`); the
> remaining three — `CurrentUnit`, `AmountUnit`, `LuminousIntensityUnit` — are introduced
> here. They follow the `LengthUnit` convention of a positive-real magnitude and support
> rescaling and unit-ratio laws through `PositiveRealUnitCore`. Following PhysLib's
> layout, these types may ultimately live under the relevant physics directories.
>
> `SIUnitChoices := UnitSystem ISQDimensionBase` is then the typed SI unit choice, and
> `SIUnitChoices.SI` is the coherent SI choice (metre, kilogram, second, ampere, kelvin,
> mole, candela). Contrast `SIUnitChoices` (current-based, seven typed slots) with
> `LTMCTUnitChoices` (charge-based, five typed slots): the machinery supports both, and the
> `Dimension.ltmctToISQ` / `Dimension.isqToLTMCT` bridge relates their bases.

## Typed unit types for the ISQ base quantities not already present

**`CurrentUnit`**, a structure, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/SIUnitChoices.lean#L51).

> A unit of electric current — a choice of positive-real magnitude. The SI coherent
> choice is the ampere.

```lean
structure CurrentUnit where
  /-- The underlying scale of the unit. -/
  val : ℝ
  property : 0 < val
```

**An instance with no name**, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/SIUnitChoices.lean#L56).

```lean
instance : PositiveRealUnitCore CurrentUnit
```

**`CurrentUnit.amperes`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/SIUnitChoices.lean#L68).

> The SI coherent unit of electric current, the ampere.

```lean
def amperes : CurrentUnit
```

**`CurrentUnit.milliamperes`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/SIUnitChoices.lean#L71).

> One milliampere, equal to `10⁻³` amperes.

```lean
noncomputable def milliamperes : CurrentUnit
```

**`AmountUnit`**, a structure, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/SIUnitChoices.lean#L78).

> A unit of amount of substance — a choice of positive-real magnitude. The SI coherent
> choice is the mole.

```lean
structure AmountUnit where
  /-- The underlying scale of the unit. -/
  val : ℝ
  property : 0 < val
```

**An instance with no name**, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/SIUnitChoices.lean#L83).

```lean
instance : PositiveRealUnitCore AmountUnit
```

**`AmountUnit.moles`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/SIUnitChoices.lean#L95).

> The SI coherent unit of amount of substance, the mole.

```lean
def moles : AmountUnit
```

**`LuminousIntensityUnit`**, a structure, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/SIUnitChoices.lean#L101).

> A unit of luminous intensity — a choice of positive-real magnitude. The SI coherent
> choice is the candela.

```lean
structure LuminousIntensityUnit where
  /-- The underlying scale of the unit. -/
  val : ℝ
  property : 0 < val
```

**An instance with no name**, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/SIUnitChoices.lean#L106).

```lean
instance : PositiveRealUnitCore LuminousIntensityUnit
```

**`LuminousIntensityUnit.candelas`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/SIUnitChoices.lean#L118).

> The SI coherent unit of luminous intensity, the candela.

```lean
def candelas : LuminousIntensityUnit
```

## The ISQ `UnitMagnitudeCatalog` instance

> Each ISQ base quantity is assigned its typed unit type; the magnitude layer is the
> positive-real `val`, exactly as for the `LTMCTDimensionBase` instance.

**An instance with no name**, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/SIUnitChoices.lean#L131).

```lean
noncomputable instance : UnitMagnitudeCatalog ISQDimensionBase
```

## Folding over the ISQ base quantities

**`prod_univ_ISQDimensionBase`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/SIUnitChoices.lean#L159).

> The product over the seven ISQ base quantities, in canonical enumeration order — the
> `ISQDimensionBase` companion to `prod_univ_LTMCTDimensionBase`, a reusable fact about the
> `Fintype` enumeration for folding `Finset.prod` over the ISQ basis.

```lean
lemma prod_univ_ISQDimensionBase {M : Type} [CommMonoid M] (f : ISQDimensionBase → M) :
    ∏ b, f b = f .length * f .mass * f .time * f .current * f .temperature
      * f .amount * f .luminousIntensity
```

## `SIUnitChoices`

**`SIUnitChoices`**, an abbrev, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/SIUnitChoices.lean#L178).

> A **typed SI unit choice**: a typed unit at every ISQ base quantity. This is the
> seven-slot, current-based sibling of the five-slot, charge-based `LTMCTUnitChoices`,
> produced by the same basis-generic `UnitSystem` / `UnitMagnitudeCatalog` machinery.

```lean
abbrev SIUnitChoices
```

**`SIUnitChoices.SI`**, a def, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/SIUnitChoices.lean#L183).

> The coherent SI unit choice: metre, kilogram, second, ampere, kelvin, mole, candela.

```lean
noncomputable def SI : SIUnitChoices
```

**`SIUnitChoices.dimScale`**, a def, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/SIUnitChoices.lean#L194).

> The dimension-scaling homomorphism over the ISQ basis, obtained *for free* from the
> generic `UnitScale.dimScale` fold — no per-basis hand-rolling.

```lean
noncomputable def dimScale (u1 u2 : SIUnitChoices) : Dimension ISQDimensionBase →* ℝ≥0
```

**`SIUnitChoices.dimScale_self`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/SIUnitChoices.lean#L202).

> A quantity of ISQ dimension does not rescale between a unit choice and itself.

```lean
lemma dimScale_self (u : SIUnitChoices) (d : Dimension ISQDimensionBase) :
    dimScale u u d = 1
```

## Depends on

- [The ISQ base quantities](isqdimensionbase.md)
- [Unit systems, parametrised in a dimension basis](unitsystem.md)

## Sources

- [Physlib/Units/SIUnitChoices.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/SIUnitChoices.lean)
