---
declaration: module
origin: cited
lean: SpeedOfLight, SpeedOfLight.instPositiveRealUnitCore, SpeedOfLight.positiveRealUnitCore_val, SpeedOfLight.val_pos, SpeedOfLight.val_nonneg, SpeedOfLight.val_ne_zero, SpeedOfLight.instHasDim, speedOfLight
statement: formalized
proof: formalized
---

# The Speed of Light

The module `Physlib.Relativity.SpeedOfLight`, [Physlib/Relativity/SpeedOfLight.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SpeedOfLight.lean): 17 declarations (2 instances with no name), 8 with a docstring.

> The speed of light in a vacuum, in the format of `Physlib/Units/Constants.lean`.

## i. Overview

> The speed of light has the dimension `L T⁻¹`, and its value in SI units is exact. Section F adds
> the instance of one and the speed of light as a dimensioned quantity.

## ii. Key results

> - `SpeedOfLight` : The speed of light in a chosen but arbitrary system of units.
> - `speedOfLight` : The speed of light in our world, `299792458 m s⁻¹`.
> - `SpeedOfLight.toWithDim` : The speed of light as a quantity with the dimension of
>   length over time.
> - `SpeedOfLight.toWithDim_scaleUnit` : The map `toWithDim` commutes with changes of units.

## iv. References

> * The defining value of the speed of light. [ref: bipm\_si\_brochure\_2019]

## A. The type

**`SpeedOfLight`**, a structure, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SpeedOfLight.lean#L56).

> The speed of light in a vacuum, in a chosen but arbitrary system of units.

```lean
structure SpeedOfLight where
  /-- The underlying value of the speed of light. -/
  val : ℝ
  pos : 0 < val
```

## B. Instances

**`SpeedOfLight.instPositiveRealUnitCore`**, an instance, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SpeedOfLight.lean#L69).

```lean
instance instPositiveRealUnitCore : PositiveRealUnitCore SpeedOfLight
```

**An instance with no name**, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SpeedOfLight.lean#L76).

```lean
instance : Coe SpeedOfLight ℝ
```

**`SpeedOfLight.positiveRealUnitCore_val`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SpeedOfLight.lean#L79).

```lean
lemma positiveRealUnitCore_val (c : SpeedOfLight) : PositiveRealUnitCore.val c = c.val
```

## C. Positivity

**`SpeedOfLight.val_pos`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SpeedOfLight.lean#L88).

```lean
lemma val_pos (c : SpeedOfLight) : 0 < (c : ℝ)
```

**`SpeedOfLight.val_nonneg`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SpeedOfLight.lean#L91).

```lean
lemma val_nonneg (c : SpeedOfLight) : 0 ≤ (c : ℝ)
```

**`SpeedOfLight.val_ne_zero`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SpeedOfLight.lean#L94).

```lean
lemma val_ne_zero (c : SpeedOfLight) : (c : ℝ) ≠ 0
```

## D. The dimension

**`SpeedOfLight.instHasDim`**, an instance, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SpeedOfLight.lean#L103).

> The speed of light has the dimension `L T⁻¹`.

```lean
instance instHasDim : HasDim SpeedOfLight
```

## E. The value in our world

**`speedOfLight`**, a def, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SpeedOfLight.lean#L115).

> The speed of light in our world, `299792458 m s⁻¹`, exact.

```lean
noncomputable def speedOfLight : Dimensionful SpeedOfLight
```

**`speedOfLight_in_SI`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SpeedOfLight.lean#L119).

```lean
lemma speedOfLight_in_SI : speedOfLight SI = ⟨299792458, by norm_num⟩
```

## F. Specific to the speed of light

### F.1. The instance of one

> We define the instance of one for `SpeedOfLight` to be the speed of light equal to `1`.
> This is useful when we are working in units where the speed of light is equal to one.

**An instance with no name**, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SpeedOfLight.lean#L135).

```lean
instance : One SpeedOfLight
```

**`SpeedOfLight.val_one`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SpeedOfLight.lean#L138).

```lean
lemma val_one : (1 : SpeedOfLight).val = 1
```

### F.2. As a dimensioned quantity

**`SpeedOfLight.toWithDim`**, a def, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SpeedOfLight.lean#L149).

> The speed of light as a quantity carrying the dimension of length over time,
> in nonnegative real values. The underlying value is the same as that of the
> `SpeedOfLight`.

```lean
def toWithDim (c : SpeedOfLight) : WithDim (L𝓭 * T𝓭⁻¹) ℝ≥0
```

**`SpeedOfLight.toWithDim_val`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SpeedOfLight.lean#L154).

> The underlying value of the speed of light as a dimensioned quantity agrees with
> the original value.

```lean
lemma toWithDim_val (c : SpeedOfLight) : (c.toWithDim.val : ℝ) = c.val
```

**`SpeedOfLight.toWithDim_val_pos`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SpeedOfLight.lean#L158).

> The speed of light as a dimensioned quantity is positive.

```lean
lemma toWithDim_val_pos (c : SpeedOfLight) : 0 < c.toWithDim.val
```

**`SpeedOfLight.scaleUnit_val`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SpeedOfLight.lean#L164).

> Scaling a speed of light multiplies its value by the scale factor of the
> dimension of length over time.

```lean
lemma scaleUnit_val (c : SpeedOfLight) (u1 u2 : LTMCTUnitChoices) :
    (scaleUnit u1 u2 c).val = (u1.dimScale u2 (L𝓭 * T𝓭⁻¹) : ℝ) * c.val
```

**`SpeedOfLight.toWithDim_scaleUnit`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SpeedOfLight.lean#L169).

> The map `toWithDim` commutes with changes of units.

```lean
lemma toWithDim_scaleUnit (c : SpeedOfLight) (u1 u2 : LTMCTUnitChoices) :
    (scaleUnit u1 u2 c).toWithDim = scaleUnit u1 u2 c.toWithDim
```

## Depends on

- [Physlib.Units.WithDim.Basic](../units/withdim/basic.md)

## Sources

- [Physlib/Relativity/SpeedOfLight.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SpeedOfLight.lean)
