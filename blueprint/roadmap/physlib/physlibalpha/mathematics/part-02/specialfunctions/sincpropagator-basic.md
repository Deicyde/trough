---
declaration: module
origin: cited
lean: Real.sincPropagator, Real.sincPropagator_zero_left, Real.sincPropagator_zero_right, Real.sincPropagator_eq_sin_div, Real.sincPropagator_neg_left, Real.abs_sincPropagator_le, Real.hasDerivAt_sincPropagator, Real.hasDerivAt_cos_mul
statement: formalized
proof: formalized
---

# The sine propagation function `t ↦ sin (ω t) / ω`

The module `PhyslibAlpha.Mathematics.SpecialFunctions.SincPropagator.Basic`, [PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Basic.lean): 11 declarations, 1 with a docstring.

> The function `sincPropagator t ω = sin (ω t) / ω` solves `u'' + ω² u = 0` with `u 0 = 0` and
> `u' 0 = 1`.

## i. Overview

> The function `sincPropagator t ω = sin (ω t) / ω` solves `u'' + ω² u = 0` with `u 0 = 0` and
> `u' 0 = 1`. It is the time dependence of every free wave with frequency `ω`.
> Writing it as `t * sinc (ω t)` removes the case `ω = 0`, where it equals `t`.
> Together with the cosine it forms the one-parameter group of the harmonic oscillator.
> The group law is proved in `Exponential.lean` from the exponential of the generator.

## ii. Key results

> - `sincPropagator` : The function `sin (ω t) / ω`, with the value `t` at `ω = 0`.
> - `sincPropagator_zero_left`
> - `sincPropagator_zero_right`
> - `sincPropagator_eq_sin_div`

## iv. References

> None.

## A. The sine propagation function `t ↦ sin (ω t) / ω`

> - `sincPropagator` : The function `sin (ω t) / ω`, with the value `t` at `ω = 0`.
>
> Lemmas: `sincPropagator_zero_left`, `sincPropagator_zero_right`, `sincPropagator_eq_sin_div`,
> `sincPropagator_neg_left`, `abs_sincPropagator_le`, `hasDerivAt_sincPropagator`,
> `hasDerivAt_cos_mul`, `continuous_sincPropagator`.

## B. Equivalent forms of the sine propagation function

> Lemmas: `sinc_abs`, `sincPropagator_eq_mul_sincSqrt`.

**`Real.sincPropagator`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Basic.lean#L65).

> The function `sin (ω t) / ω`, with the value `t` at `ω = 0`.

```lean
def sincPropagator (t ω : ℝ) : ℝ
```

**`Real.sincPropagator_zero_left`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Basic.lean#L68).

```lean
lemma sincPropagator_zero_left (ω : ℝ) : sincPropagator 0 ω = 0
```

**`Real.sincPropagator_zero_right`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Basic.lean#L71).

```lean
lemma sincPropagator_zero_right (t : ℝ) : sincPropagator t 0 = t
```

**`Real.sincPropagator_eq_sin_div`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Basic.lean#L73).

```lean
lemma sincPropagator_eq_sin_div {ω : ℝ} (hω : ω ≠ 0) (t : ℝ) :
    sincPropagator t ω = sin (ω * t) / ω
```

**`Real.sincPropagator_neg_left`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Basic.lean#L81).

```lean
lemma sincPropagator_neg_left (t ω : ℝ) : sincPropagator (-t) ω = - sincPropagator t ω
```

**`Real.abs_sincPropagator_le`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Basic.lean#L84).

```lean
lemma abs_sincPropagator_le (t ω : ℝ) : |sincPropagator t ω| ≤ |t|
```

**`Real.hasDerivAt_sincPropagator`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Basic.lean#L88).

```lean
lemma hasDerivAt_sincPropagator (ω t : ℝ) : HasDerivAt (fun s => sincPropagator s ω) (cos (ω * t))
    t
```

**`Real.hasDerivAt_cos_mul`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Basic.lean#L99).

```lean
lemma hasDerivAt_cos_mul (ω t : ℝ) :
    HasDerivAt (fun s => cos (ω * s)) (-ω ^ 2 * sincPropagator t ω) t
```

**`Real.continuous_sincPropagator`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Basic.lean#L107).

```lean
lemma continuous_sincPropagator : Continuous fun p : ℝ × ℝ => sincPropagator p.1 p.2
```

**`Real.sinc_abs`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Basic.lean#L111).

```lean
lemma sinc_abs (x : ℝ) : sinc |x| = sinc x
```

**`Real.sincPropagator_eq_mul_sincSqrt`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Basic.lean#L114).

```lean
lemma sincPropagator_eq_mul_sincSqrt (t ω : ℝ) :
    sincPropagator t ω = t * sincSqrt (t ^ 2 * ω ^ 2)
```

## Depends on

- [`cos √y` and `sinc √y` as entire functions](sincpropagator-series.md)

## Sources

- [PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Basic.lean)
