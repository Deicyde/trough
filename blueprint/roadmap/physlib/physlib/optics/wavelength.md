---
declaration: module
origin: cited
lean: Wavelength, Wavelength.ofFrequency, Wavelength.ofFrequency_val, Wavelength.ofFrequency_pos, Wavelength.ofFrequency_mul, Wavelength.ofFrequency_scaleUnit, Frequency.ofWavelength, Frequency.ofWavelength_val
statement: formalized
proof: formalized
---

# Wavelength

The module `Physlib.Optics.Wavelength`, [Physlib/Optics/Wavelength.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Optics/Wavelength.lean): 15 declarations, 13 with a docstring.

> In this module we define the type `Wavelength`, corresponding to the wavelength of a wave
> carrying the dimension of length, and relate it to the type `Frequency` through the
> propagation speed of the wave via the relation `c = λ * ν`.

## i. Overview

> The type `Wavelength` is `WithDim L𝓭 ℝ≥0`, i.e., a nonnegative real number tagged with
> the dimension of length.
>
> For a wave of frequency `ν > 0` propagating at a speed `c` (e.g. the speed of light),
> the associated wavelength is `λ = c / ν`, and conversely a wave of wavelength `λ > 0`
> has frequency `ν = c / λ`. These two constructions are inverse to one another.

## ii. Key results

> - `Wavelength` : The type of wavelengths of waves.
> - `Wavelength.ofFrequency` : The wavelength `c / ν` associated with a positive frequency.
> - `Frequency.ofWavelength` : The frequency `c / λ` associated with a positive wavelength.
> - `Wavelength.ofFrequency_mul` : The relation `λ * ν = c`.
> - `Frequency.ofWavelength_mul` : The relation `ν * λ = c`.
> - `Wavelength.ofFrequency_ofWavelength` and `Frequency.ofWavelength_ofFrequency` : The
>   two constructions are inverse to one another.
> - `Wavelength.ofFrequency_scaleUnit` and `Frequency.ofWavelength_scaleUnit` : The
>   constructions commute with changes of units.
> - `speedEqWavelengthMulFrequency_isDimensionallyCorrect` : The relation `c = λ * ν` is
>   dimensionally correct.

## iv. References

> - https://en.wikipedia.org/wiki/Wavelength

## A. The Wavelength type

**`Wavelength`**, an abbrev, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Optics/Wavelength.lean#L70).

> The type `Wavelength` represents the distance between consecutive
> corresponding points of the same phase on the wave, such as two adjacent
> crests, troughs, or zero crossings, i.e. a nonnegative real number
> carrying the dimension of length.

```lean
abbrev Wavelength : Type
```

## B. Wavelength from frequency

**`Wavelength.ofFrequency`**, a def, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Optics/Wavelength.lean#L82).

> The wavelength of a wave of frequency `ν` propagating at a speed `c`,
> given by `λ = c / ν`.

```lean
noncomputable def ofFrequency (c : WithDim (L𝓭 * T𝓭⁻¹) ℝ≥0) (ν : Frequency) (_ν_pos : 0 < ν.val) :
    Wavelength
```

**`Wavelength.ofFrequency_val`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Optics/Wavelength.lean#L86).

```lean
lemma ofFrequency_val (c : WithDim (L𝓭 * T𝓭⁻¹) ℝ≥0) (ν : Frequency) (hν : 0 < ν.val) :
    (ofFrequency c ν hν).val = c.val / ν.val
```

**`Wavelength.ofFrequency_pos`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Optics/Wavelength.lean#L91).

> Positivity of the wavelength associated with a positive frequency and a positive
> speed.

```lean
lemma ofFrequency_pos (c : WithDim (L𝓭 * T𝓭⁻¹) ℝ≥0) (hc : 0 < c.val) (ν : Frequency)
    (hν : 0 < ν.val) : 0 < (ofFrequency c ν hν).val
```

**`Wavelength.ofFrequency_mul`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Optics/Wavelength.lean#L96).

> The wavelength associated with a frequency satisfies `λ * ν = c`.

```lean
lemma ofFrequency_mul (c : WithDim (L𝓭 * T𝓭⁻¹) ℝ≥0) (ν : Frequency) (hν : 0 < ν.val) :
    (ofFrequency c ν hν).val * ν.val = c.val
```

**`Wavelength.ofFrequency_scaleUnit`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Optics/Wavelength.lean#L103).

> The wavelength associated with a frequency scales with units as a wavelength should:
> changing the units from `u1` to `u2` rescales the resulting wavelength by the scale factor
> of the dimension of length.

```lean
lemma ofFrequency_scaleUnit (c : WithDim (L𝓭 * T𝓭⁻¹) ℝ≥0) (ν : Frequency) (hν : 0 < ν.val)
    (u1 u2 : LTMCTUnitChoices) :
    ofFrequency (scaleUnit u1 u2 c) (scaleUnit u1 u2 ν) (WithDim.scaleUnit_val_pos ν hν u1 u2) =
      scaleUnit u1 u2 (ofFrequency c ν hν)
```

## C. Frequency from wavelength

**`Frequency.ofWavelength`**, a def, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Optics/Wavelength.lean#L123).

> The frequency of a wave of wavelength `w` propagating at a speed `c`,
> given by `ν = c / w`. We can't use `λ` due to Lean anon function.

```lean
noncomputable def ofWavelength (c : WithDim (L𝓭 * T𝓭⁻¹) ℝ≥0) (w : Wavelength) (_w_pos : 0 < w.val) :
    Frequency
```

**`Frequency.ofWavelength_val`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Optics/Wavelength.lean#L127).

```lean
lemma ofWavelength_val (c : WithDim (L𝓭 * T𝓭⁻¹) ℝ≥0) (w : Wavelength) (w_pos : 0 < w.val) :
    (ofWavelength c w w_pos).val = c.val / w.val
```

**`Frequency.ofWavelength_pos`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Optics/Wavelength.lean#L132).

> Positivity of the frequency associated with a positive wavelength and a positive
> speed.

```lean
lemma ofWavelength_pos (c : WithDim (L𝓭 * T𝓭⁻¹) ℝ≥0) (c_pos : 0 < c.val) (w : Wavelength)
    (hw : 0 < w.val) : 0 < (ofWavelength c w hw).val
```

**`Frequency.ofWavelength_mul`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Optics/Wavelength.lean#L137).

> The frequency associated with a wavelength satisfies `ν * λ = c`.

```lean
lemma ofWavelength_mul (c : WithDim (L𝓭 * T𝓭⁻¹) ℝ≥0) (w : Wavelength) (w_pos : 0 < w.val) :
    (ofWavelength c w w_pos).val * w.val = c.val
```

**`Frequency.ofWavelength_scaleUnit`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Optics/Wavelength.lean#L144).

> The frequency associated with a wavelength scales with units as a frequency should:
> changing the units from `u1` to `u2` rescales the resulting frequency by the scale factor
> of the dimension of inverse time.

```lean
lemma ofWavelength_scaleUnit (c : WithDim (L𝓭 * T𝓭⁻¹) ℝ≥0) (w : Wavelength) (w_pos : 0 < w.val)
    (u1 u2 : LTMCTUnitChoices) :
    ofWavelength (scaleUnit u1 u2 c) (scaleUnit u1 u2 w)
      (WithDim.scaleUnit_val_pos w w_pos u1 u2) =
      scaleUnit u1 u2 (ofWavelength c w w_pos)
```

## D. Round trips

**`Frequency.ofWavelength_ofFrequency`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Optics/Wavelength.lean#L161).

> Converting a wavelength to a frequency and back recovers the wavelength.

```lean
lemma ofWavelength_ofFrequency (c : WithDim (L𝓭 * T𝓭⁻¹) ℝ≥0) (hc : 0 < c.val)
    (ν : Frequency) (hν : 0 < ν.val) :
    ofWavelength c (Wavelength.ofFrequency c ν hν)
      (Wavelength.ofFrequency_pos c hc ν hν) = ν
```

**`Wavelength.ofFrequency_ofWavelength`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Optics/Wavelength.lean#L175).

> Converting a frequency to a wavelength and back recovers the frequency.

```lean
lemma ofFrequency_ofWavelength (c : WithDim (L𝓭 * T𝓭⁻¹) ℝ≥0) (hc : 0 < c.val)
    (w : Wavelength) (hw : 0 < w.val) :
    ofFrequency c (Frequency.ofWavelength c w hw)
      (Frequency.ofWavelength_pos c hc w hw) = w
```

## E. Dimensional correctness

**`SpeedEqWavelengthMulFrequency`**, a def, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Optics/Wavelength.lean#L194).

> The relation `c = λ * ν` between a speed `c`, a wavelength `λ` and a frequency `ν`,
> stated on real-valued quantities carrying the dimensions of speed, length and inverse time
> respectively.

```lean
def SpeedEqWavelengthMulFrequency (c : WithDim (L𝓭 * T𝓭⁻¹) ℝ) (w : WithDim L𝓭 ℝ)
    (ν : WithDim T𝓭⁻¹ ℝ) : Prop
```

**`speedEqWavelengthMulFrequency_isDimensionallyCorrect`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Optics/Wavelength.lean#L200).

> The relation `c = λ * ν` is dimensionally correct: it holds in one system of units if and
> only if it holds in every system of units.

```lean
lemma speedEqWavelengthMulFrequency_isDimensionallyCorrect :
    IsDimensionallyCorrect SpeedEqWavelengthMulFrequency
```

## Depends on

- [Frequency](frequency.md)

## Sources

- [Physlib/Optics/Wavelength.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Optics/Wavelength.lean)
