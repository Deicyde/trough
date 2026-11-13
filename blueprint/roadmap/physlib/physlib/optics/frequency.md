---
declaration: module
origin: cited
lean: Frequency
statement: formalized
proof: formalized
---

# Frequency

The module `Physlib.Optics.Frequency`, [Physlib/Optics/Frequency.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Optics/Frequency.lean): 1 declaration, 1 with a docstring.

> In this module we define the type `Frequency`, corresponding to the frequency of a wave
> carrying the dimension of inverse time.

## i. Overview

> The type `Frequency` is `WithDim T𝓭⁻¹ ℝ≥0`, i.e., a nonnegative real number tagged with
> the dimension of inverse time.

## ii. Key results

> - `Frequency` : The type of frequencies of waves.

## iv. References

> - https://en.wikipedia.org/wiki/Frequency
> - https://en.wikipedia.org/wiki/Wavelength

## A. The Frequency type

**`Frequency`**, an abbrev, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Optics/Frequency.lean#L50).

> The type `Frequency` represents the measure of of how often sinusodial components
> of a wave repeat per unit time, i.e. a nonnegative real number carrying the dimension
> of inverse time, in a given (but arbitrary) set of units.

```lean
abbrev Frequency : Type
```

## Depends on

- [Physlib.Units.WithDim.Basic](../units/withdim/basic.md)

## Sources

- [Physlib/Optics/Frequency.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Optics/Frequency.lean)
