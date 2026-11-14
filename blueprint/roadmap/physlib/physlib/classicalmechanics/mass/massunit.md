---
declaration: module
origin: cited
lean: MassUnit, MassUnit.kilograms, MassUnit.micrograms, MassUnit.milligrams, MassUnit.grams, MassUnit.ounces, MassUnit.pounds, MassUnit.stones
statement: formalized
proof: formalized
---

# Units on Mass

The module `Physlib.ClassicalMechanics.Mass.MassUnit`, [Physlib/ClassicalMechanics/Mass/MassUnit.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Mass/MassUnit.lean): 18 declarations (1 instance with no name), 14 with a docstring.

> A unit of mass corresponds to a choice of translationally-invariant
> metric on the mass manifold (to be defined diffeomorphic to `ℝ≥0`).
> Such a choice is (non-canonically) equivalent to a
> choice of positive real number. We define the type `MassUnit` to be equivalent to the
> positive reals.
>
> On `MassUnit` there is an instance of division giving a real number, corresponding to the
> ratio of the two scales of mass unit.
>
> To define specific mass units, we first state the existence of a
> a given mass unit, and then construct all other mass units from it. We choose to state the
> existence of the mass unit of kilograms, and construct all other mass units from that.

## References

> * The numerical value used for the nominal solar mass. [ref: nominal\_solar\_mass\_article]

**`MassUnit`**, a structure, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Mass/MassUnit.lean#L38).

> The choices of translationally-invariant metrics on the mass-manifold.
> Such a choice corresponds to a choice of units for mass.

```lean
structure MassUnit where
  /-- The underlying scale of the unit. -/
  val : ℝ
  property : 0 < val
```

**An instance with no name**, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Mass/MassUnit.lean#L43).

```lean
instance : PositiveRealUnitCore MassUnit
```

## Specific choices of mass units

> To define a specific mass units.
> We first define the notion of a kilogram to correspond to the mass unit with underlying value
> equal to `1`. This is really down to a choice in the isomorphism between the set of metrics
> on the mass manifold and the positive reals.
> From this choice of kilograms, we can define other length units by scaling kilograms.

**`MassUnit.kilograms`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Mass/MassUnit.lean#L68).

> The definition of a mass unit of kilograms.

```lean
def kilograms : MassUnit
```

**`MassUnit.micrograms`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Mass/MassUnit.lean#L71).

> The mass unit of a microgram (10^(-9) of a kilogram).

```lean
noncomputable def micrograms : MassUnit
```

**`MassUnit.milligrams`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Mass/MassUnit.lean#L74).

> The mass unit of milligram (10^(-6) of a kilogram).

```lean
noncomputable def milligrams : MassUnit
```

**`MassUnit.grams`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Mass/MassUnit.lean#L77).

> The mass unit of grams (10^(-3) of a kilogram).

```lean
noncomputable def grams : MassUnit
```

**`MassUnit.ounces`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Mass/MassUnit.lean#L80).

> The mass unit of (avoirdupois) ounces (0.028 349 523 125 of a kilogram).

```lean
noncomputable def ounces : MassUnit
```

**`MassUnit.pounds`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Mass/MassUnit.lean#L83).

> The mass unit of (avoirdupois) pounds (0.453 592 37 of a kilogram).

```lean
noncomputable def pounds : MassUnit
```

**`MassUnit.stones`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Mass/MassUnit.lean#L86).

> The mass unit of stones (14 pounds).

```lean
noncomputable def stones : MassUnit
```

**`MassUnit.quarters`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Mass/MassUnit.lean#L89).

> The mass unit of a quarter (28 pounds).

```lean
noncomputable def quarters : MassUnit
```

**`MassUnit.hundredweights`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Mass/MassUnit.lean#L92).

> The mass unit of hundredweights (112 pounds).

```lean
noncomputable def hundredweights : MassUnit
```

**`MassUnit.shortTons`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Mass/MassUnit.lean#L95).

> The mass unit of short tons (2000 pounds).

```lean
noncomputable def shortTons : MassUnit
```

**`MassUnit.metricTons`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Mass/MassUnit.lean#L98).

> The mass unit of metric tons (1000 kilograms).

```lean
noncomputable def metricTons : MassUnit
```

**`MassUnit.longTons`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Mass/MassUnit.lean#L101).

> The mass unit of long tons (2240 pounds). Also called shortweight tons.

```lean
noncomputable def longTons : MassUnit
```

**`MassUnit.nominalSolarMasses`**, a def, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Mass/MassUnit.lean#L105).

> The mass unit of nominal solar masses (1.988416 × 10 ^ 30 kilograms).
> See: https://iopscience.iop.org/article/10.3847/0004-6256/152/2/41 [ref: nominal\_solar\_mass\_article]

```lean
noncomputable def nominalSolarMasses : MassUnit
```

## Relations between mass units

**`MassUnit.pounds_div_ounces`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Mass/MassUnit.lean#L113).

```lean
lemma pounds_div_ounces : pounds / ounces = (16 : ℝ≥0)
```

**`MassUnit.shortTons_div_kilograms`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Mass/MassUnit.lean#L119).

```lean
lemma shortTons_div_kilograms : shortTons / kilograms = (907.18474 : ℝ≥0)
```

**`MassUnit.longTons_div_kilograms`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Mass/MassUnit.lean#L122).

```lean
lemma longTons_div_kilograms : longTons / kilograms = (1016.0469088 : ℝ≥0)
```

## Depends on

- [A. Shared arithmetic for positive-real unit types](../../units/positiverealunit.md)

## Sources

- [Physlib/ClassicalMechanics/Mass/MassUnit.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Mass/MassUnit.lean)
