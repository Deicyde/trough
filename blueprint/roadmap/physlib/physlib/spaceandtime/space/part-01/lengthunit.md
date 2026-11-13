---
declaration: module
origin: cited
lean: LengthUnit, LengthUnit.meters, LengthUnit.femtometers, LengthUnit.picometers, LengthUnit.nanometers, LengthUnit.micrometers, LengthUnit.millimeters, LengthUnit.centimeters
statement: formalized
proof: formalized
---

# Units on Length

The module `Physlib.SpaceAndTime.Space.LengthUnit`, [Physlib/SpaceAndTime/Space/LengthUnit.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/LengthUnit.lean): 24 declarations (1 instance with no name), 23 with a docstring.

> A unit of length corresponds to a choice of translationally-invariant
> metric on the space manifold (to be defined). Such a choice is (non-canonically) equivalent to a
> choice of positive real number. We define the type `LengthUnit` to be equivalent to the
> positive reals.
>
> On `LengthUnit` there is an instance of division giving a real number, corresponding to the
> ratio of the two scales of length unit.
>
> To define specific length units, we first state the existence of a
> a given length unit, and then construct all other length units from it. We choose to state the
> existence of the length unit of meters, and construct all other length units from that.

## References

> * The BIPM SI Brochure, for the meter, the speed of light, and SI prefixes.
>   [ref: bipm\_si\_brochure\_2019]
> * NIST Handbook 44, Appendix C, for the international foot-based units and the international
>   nautical mile. [ref: nist\_hb44\_2023]
> * IAU 2012 Resolution B2, for the astronomical unit. [ref: iau\_2012\_resolution\_b2]
> * The IAU Style Manual recommendations, for the Julian year convention used in the light-year.
>   [ref: iau\_style\_manual\_units]
> * IAU 2015 Resolution B2, for the exact parsec convention. [ref: iau\_2015\_resolution\_b2]

**`LengthUnit`**, a structure, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/LengthUnit.lean#L42).

> The choices of translationally-invariant metrics on the space-manifold.
> Such a choice corresponds to a choice of units for length.

```lean
structure LengthUnit where
  /-- The underlying scale of the unit. -/
  val : ℝ
  property : 0 < val
```

**An instance with no name**, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/LengthUnit.lean#L47).

```lean
instance : PositiveRealUnitCore LengthUnit
```

## Specific choices of Length units

> To define a specific length units.
> We first define the notion of a meter to correspond to the length unit with underlying value
> equal to `1`. This is really down to a choice in the isomorphism between the set of metrics
> on the space manifold and the positive reals.
> From this choice of meters, we can define other length units by scaling meters.
>
> The references for the numerical definitions used below are:
> * the BIPM SI Brochure for the meter, the speed of light, and SI prefixes:
>   https://www.bipm.org/documents/d/guest/si-brochure-9-en-pdf [ref: bipm\_si\_brochure\_2019]
> * NIST Handbook 44, Appendix C, for the international foot-based units and
>   the international nautical mile:
>   https://doi.org/10.6028/NIST.HB.44-2023 [ref: nist\_hb44\_2023]
> * IAU 2012 Resolution B2 for the astronomical unit:
>   https://iauarchive.eso.org/static/resolutions/IAU2012\_English.pdf [ref: iau\_2012\_resolution\_b2]
> * the IAU Style Manual recommendations for the Julian year convention used in
>   the light-year:
>   https://iauarchive.eso.org/publications/proceedings\_rules/units/ [ref: iau\_style\_manual\_units]
> * IAU 2015 Resolution B2 for the exact parsec convention:
>   https://iauarchive.eso.org/static/resolutions/IAU2015\_English.pdf [ref: iau\_2015\_resolution\_b2]

**`LengthUnit.meters`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/LengthUnit.lean#L86).

> The definition of a length unit of meters.

```lean
def meters : LengthUnit
```

**`LengthUnit.femtometers`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/LengthUnit.lean#L89).

> The length unit of femtometers (10⁻¹⁵ of a meter).

```lean
noncomputable def femtometers : LengthUnit
```

**`LengthUnit.picometers`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/LengthUnit.lean#L92).

> The length unit of picometers (10⁻¹² of a meter).

```lean
noncomputable def picometers : LengthUnit
```

**`LengthUnit.nanometers`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/LengthUnit.lean#L95).

> The length unit of nanometers (10⁻⁹ of a meter).

```lean
noncomputable def nanometers : LengthUnit
```

**`LengthUnit.micrometers`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/LengthUnit.lean#L98).

> The length unit of micrometers (10⁻⁶ of a meter).

```lean
noncomputable def micrometers : LengthUnit
```

**`LengthUnit.millimeters`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/LengthUnit.lean#L101).

> The length unit of millimeters (10⁻³ of a meter).

```lean
noncomputable def millimeters : LengthUnit
```

**`LengthUnit.centimeters`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/LengthUnit.lean#L104).

> The length unit of centimeters (10⁻² of a meter).

```lean
noncomputable def centimeters : LengthUnit
```

**`LengthUnit.inches`**, a def, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/LengthUnit.lean#L107).

> The length unit of inch (0.0254 meters).

```lean
noncomputable def inches : LengthUnit
```

**`LengthUnit.links`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/LengthUnit.lean#L110).

> The length unit of link (0.201168 meters).

```lean
noncomputable def links : LengthUnit
```

**`LengthUnit.feet`**, a def, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/LengthUnit.lean#L113).

> The length unit of feet (0.3048 meters)

```lean
noncomputable def feet : LengthUnit
```

**`LengthUnit.yards`**, a def, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/LengthUnit.lean#L116).

> The length unit of a yard (0.9144 meters)

```lean
noncomputable def yards : LengthUnit
```

**`LengthUnit.rods`**, a def, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/LengthUnit.lean#L119).

> The length unit of a rod (5.0292 meters)

```lean
noncomputable def rods : LengthUnit
```

**`LengthUnit.chains`**, a def, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/LengthUnit.lean#L122).

> The length unit of a chain (20.1168 meters)

```lean
noncomputable def chains : LengthUnit
```

**`LengthUnit.furlongs`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/LengthUnit.lean#L125).

> The length unit of a furlong (201.168 meters)

```lean
noncomputable def furlongs : LengthUnit
```

**`LengthUnit.kilometers`**, a def, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/LengthUnit.lean#L128).

> The length unit of kilometers (10³ meters).

```lean
noncomputable def kilometers : LengthUnit
```

**`LengthUnit.miles`**, a def, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/LengthUnit.lean#L131).

> The length unit of a mile (1609.344 meters).

```lean
noncomputable def miles : LengthUnit
```

**`LengthUnit.nauticalMiles`**, a def, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/LengthUnit.lean#L134).

> The length unit of a nautical mile (1852 meters).

```lean
noncomputable def nauticalMiles : LengthUnit
```

**`LengthUnit.astronomicalUnits`**, a def, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/LengthUnit.lean#L137).

> The length unit of an astronomical unit (149,597,870,700 meters).

```lean
noncomputable def astronomicalUnits : LengthUnit
```

**`LengthUnit.lightYears`**, a def, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/LengthUnit.lean#L140).

> The length unit of a light year (9,460,730,472,580,800 meters).

```lean
noncomputable def lightYears : LengthUnit
```

**`LengthUnit.parsecs`**, a def, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/LengthUnit.lean#L143).

> The length unit of a parsec (648,000/π astronomicalUnits).

```lean
noncomputable def parsecs : LengthUnit
```

## Relations between length units

**`LengthUnit.miles_div_yards`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/LengthUnit.lean#L153).

> There are exactly 1760 yards in a mile.

```lean
lemma miles_div_yards : miles / yards = (⟨1760, by norm_num⟩ : ℝ≥0)
```

**`LengthUnit.furlongs_div_yards`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/LengthUnit.lean#L161).

> There are exactly 220 yards in a furlong.

```lean
lemma furlongs_div_yards : furlongs / yards = (⟨220, by norm_num⟩ : ℝ≥0)
```

## Depends on

- [A. Shared arithmetic for positive-real unit types](../../../units/positiverealunit.md)

## Sources

- [Physlib/SpaceAndTime/Space/LengthUnit.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/LengthUnit.lean)
