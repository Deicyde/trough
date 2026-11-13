---
declaration: module
origin: cited
lean: exists_units_constants_eq_one
statement: formalized
proof: formalized
---

# Physical constants

The module `Physlib.Units.Constants`, [Physlib/Units/Constants.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Constants.lean): 1 declaration, 1 with a docstring.

> An index of the physical constants in Physlib, and the format of their files.

## i. Overview

> Each constant has its own file, which this module imports. Use these constants instead of defining
> new ones or writing out their values: a result in any units takes the type, such as
> `c : SpeedOfLight`, and the value in our world is `speedOfLight`. A new constant gets a file in the
> format of section A, an import above, a row in the table below and an `example` in section B.

## ii. Key results

> | Constant | Dimension | Value in SI units |
> |---|---|---|
> | `speedOfLight` | `L T⁻¹` | `299792458 m s⁻¹`, exact |
> | `boltzmannConstant` | `M L² T⁻² Θ⁻¹` | `1.380649 × 10⁻²³ J K⁻¹`, exact |
>
> Not yet in this format: `Constants.h`, `Constants.ℏ` and `ChargeUnit.elementaryCharge`.
>
> - `exists_units_constants_eq_one` : There are units in which the speed of light and the Boltzmann
>   constant are `1`.

## iv. References

> * The defining constants of the SI. [ref: bipm\_si\_brochure\_2019]

## A. The format of a constant

> The file of a constant with type `X` and value `x` has these sections, as in
> `Physlib/Relativity/SpeedOfLight.lean`.
>
> | Section | Contents |
> |---|---|
> | A. The type | `structure X` with fields `val : ℝ` and `pos : 0 < val` |
> | B. Instances | `X.instPositiveRealUnitCore`, `Coe X ℝ`, `X.positiveRealUnitCore_val` |
> | C. Positivity | `X.val_pos`, `X.val_nonneg`, `X.val_ne_zero` |
> | D. The dimension | `X.instHasDim` |
> | E. The value in our world | `x : Dimensionful X` and `x_in_SI` |
> | F. Specific to this constant | Optional, for example `One` or other forms of the constant |
>
> The value `x` is `X` in lower camel case, defined by `toDimensionful SI`, and `x_in_SI` is proved by
> `toDimensionful_apply_self`. The docstring of `x` gives the number with its SI unit, followed by
> `exact` or, for a measured constant, the CODATA edition.

## B. Checked values

> One `example` for each row of the table, giving the dimension and the value in SI units. Lean
> checks these against the definitions; it does not read the table.

## C. Planck units

> Planck units are units in which `c`, `ℏ`, `G` and `k_B` are all `1`; so far the lemma below covers
> `c` and `k_B`. Constants with independent dimensions can always be `1` together, while constants
> with dependent dimensions can only if their dimensionless ratios are `1`. So the lemma does not
> extend to every constant: `h` cannot join `ℏ`, and the electron mass cannot join `c`, `ℏ` and `G`.

**`exists_units_constants_eq_one`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Constants.lean#L100).

> There are units in which the speed of light and the Boltzmann constant are `1`.

```lean
lemma exists_units_constants_eq_one : ∃ u : LTMCTUnitChoices,
    (speedOfLight u).val = 1 ∧ (boltzmannConstant u).val = 1
```

## Depends on

- [The Speed of Light](../relativity/speedoflight.md)
- [Boltzmann constant](../statisticalmechanics/boltzmannconstant.md)

## Sources

- [Physlib/Units/Constants.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Constants.lean)
