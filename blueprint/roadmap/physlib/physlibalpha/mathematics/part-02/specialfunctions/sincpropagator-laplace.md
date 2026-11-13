---
declaration: module
origin: cited
lean: Real.integral_exp_mul_sincPropagator, Real.integral_exp_mul_sincPropagator_zero, Real.integral_exp_mul_sincPropagator_all
statement: formalized
proof: formalized
---

# The Laplace transform of the sine propagation function

The module `PhyslibAlpha.Mathematics.SpecialFunctions.SincPropagator.Laplace`, [PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Laplace.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Laplace.lean): 3 declarations, 3 with a docstring.

> The transform of `t ↦ sin (ω t) / ω` over the positive half line is `1 / (ω² - z²)`.

## i. Overview

> The retarded Green function of the oscillator is the sine propagation function on the positive
> half line. Its Fourier transform in time exists for frequencies in the upper half plane. It
> equals `1 / (ω² - z²)`. The value at `ω = 0` is the transform of the identity function.

## ii. Key results

> - `integral_exp_mul_sincPropagator` : the transform for a nonzero frequency.
> - `integral_exp_mul_sincPropagator_zero` : the transform for zero frequency.

## iv. References

> None.

## A. The transform

> - `integral_exp_mul_sincPropagator` : the transform for a nonzero frequency.

**`Real.integral_exp_mul_sincPropagator`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Laplace.lean#L50).

> The Laplace transform of the sine propagation function for a nonzero frequency.

```lean
lemma integral_exp_mul_sincPropagator {ω : ℝ} (hω : ω ≠ 0) {z : ℂ} (hz : 0 < z.im) :
    ∫ t in Set.Ioi (0 : ℝ), Complex.exp (I * z * t) * (t.sincPropagator ω : ℂ) =
      1 / ((ω : ℂ) ^ 2 - z ^ 2)
```

**`Real.integral_exp_mul_sincPropagator_zero`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Laplace.lean#L93).

> The Laplace transform of the sine propagation function at zero frequency.

```lean
lemma integral_exp_mul_sincPropagator_zero {z : ℂ} (hz : 0 < z.im) :
    ∫ t in Set.Ioi (0 : ℝ), Complex.exp (I * z * t) * (t.sincPropagator 0 : ℂ) =
      1 / ((0 : ℂ) ^ 2 - z ^ 2)
```

**`Real.integral_exp_mul_sincPropagator_all`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Laplace.lean#L157).

> The Laplace transform of the sine propagation function for every frequency.

```lean
lemma integral_exp_mul_sincPropagator_all (ω : ℝ) {z : ℂ} (hz : 0 < z.im) :
    ∫ t in Set.Ioi (0 : ℝ), Complex.exp (I * z * t) * (t.sincPropagator ω : ℂ) =
      1 / ((ω : ℂ) ^ 2 - z ^ 2)
```

## Depends on

- [The sine propagation function `t ↦ sin (ω t) / ω`](sincpropagator-basic.md)

## Sources

- [PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Laplace.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Laplace.lean)
