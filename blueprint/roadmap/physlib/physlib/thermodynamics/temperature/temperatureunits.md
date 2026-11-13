---
declaration: module
origin: cited
lean: TemperatureUnit, TemperatureUnit.kelvin, TemperatureUnit.nanokelvin, TemperatureUnit.microkelvin, TemperatureUnit.millikelvin, TemperatureUnit.absoluteFahrenheit
statement: formalized
proof: formalized
---

# Units on Temperature

The module `Physlib.Thermodynamics.Temperature.TemperatureUnits`, [Physlib/Thermodynamics/Temperature/TemperatureUnits.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/TemperatureUnits.lean): 7 declarations (1 instance with no name), 6 with a docstring.

> A unit of temperature corresponds to a choice of translationally-invariant
> metric on the temperature manifold (to be defined diffeomorphic to `ℝ≥0`).
> Such a choice is (non-canonically) equivalent to a
> choice of positive real number. We define the type `TemperatureUnit` to be equivalent to the
> positive reals.
>
> On `TemperatureUnit` there is an instance of division giving a real number, corresponding to the
> ratio of the two scales of temperature unit.
>
> To define specific temperature units, we first state the existence of a
> a given temperature unit, and then construct all other temperature units from it.
> We choose to state the
> existence of the temperature unit of kelvin, and construct all other temperature units from that.

**`TemperatureUnit`**, a structure, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/TemperatureUnits.lean#L35).

> The choices of translationally-invariant metrics on the temperature-manifold.
> Such a choice corresponds to a choice of units for temperature.

```lean
structure TemperatureUnit where
  /-- The underlying scale of the unit. -/
  val : ℝ
  property : 0 < val
```

**An instance with no name**, [line 40](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/TemperatureUnits.lean#L40).

```lean
instance : PositiveRealUnitCore TemperatureUnit
```

## Specific choices of temperature units

> To define a specific temperature units.
> We first define the notion of a kelvin to correspond to the temperature unit with underlying value
> equal to `1`. This is really down to a choice in the isomorphism between the set of metrics
> on the temperature manifold and the positive reals.
>
> Once we have defined kelvin, we can define other temperature units by scaling kelvin.

**`TemperatureUnit.kelvin`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/TemperatureUnits.lean#L66).

> The definition of a temperature unit of kelvin.

```lean
def kelvin : TemperatureUnit
```

**`TemperatureUnit.nanokelvin`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/TemperatureUnits.lean#L69).

> The temperature unit of degrees nanokelvin (10^(-9) kelvin).

```lean
noncomputable def nanokelvin : TemperatureUnit
```

**`TemperatureUnit.microkelvin`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/TemperatureUnits.lean#L72).

> The temperature unit of degrees microkelvin (10^(-6) kelvin).

```lean
noncomputable def microkelvin : TemperatureUnit
```

**`TemperatureUnit.millikelvin`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/TemperatureUnits.lean#L75).

> The temperature unit of degrees millikelvin (10^(-3) kelvin).

```lean
noncomputable def millikelvin : TemperatureUnit
```

**`TemperatureUnit.absoluteFahrenheit`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/TemperatureUnits.lean#L79).

> The temperature unit of degrees fahrenheit ((5/9) of a kelvin).
> Note, this is fahrenheit starting at `0` absolute temperature.

```lean
noncomputable def absoluteFahrenheit : TemperatureUnit
```

## Depends on

- [A. Shared arithmetic for positive-real unit types](../../units/positiverealunit.md)

## Sources

- [Physlib/Thermodynamics/Temperature/TemperatureUnits.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/TemperatureUnits.lean)
