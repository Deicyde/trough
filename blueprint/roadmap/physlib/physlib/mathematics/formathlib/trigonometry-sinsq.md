---
declaration: module
origin: cited
lean: Real.sin_sq_lt_one, Real.sin_half_sq_lt_one
statement: formalized
proof: formalized
---

# Strict bounds on the square of the sine

The module `Physlib.Mathematics.ForMathlib.Trigonometry.SinSq`, [Physlib/Mathematics/ForMathlib/Trigonometry/SinSq.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Trigonometry/SinSq.lean): 2 declarations, 2 with a docstring.

> …

## i. Overview

> Mathlib bounds the square of the sine by `sin x ^ 2 ≤ 1` for every real `x` (`Real.sin_sq_le_one`),
> with equality exactly at the odd multiples of `π / 2`. This file records the strict form of that
> bound, `sin x ^ 2 < 1` on the open interval `|x| < π / 2`, where the cosine is positive and
> `1 - sin² x = cos² x`, together with its half-angle form `sin (θ / 2) ^ 2 < 1` for `|θ| < π`.
>
> Physlib uses the half-angle form for the simple pendulum: the parameter `sin² (θ₀ / 2)` of the
> period formula lies in the domain `m < 1` of the complete elliptic integral `Real.completeEllipticK`
> for every libration amplitude `|θ₀| < π`.

## ii. Key results

> - `Real.sin_sq_lt_one` : `sin x ^ 2 < 1` for `|x| < π / 2`.
> - `Real.sin_half_sq_lt_one` : `sin (θ / 2) ^ 2 < 1` for `|θ| < π`.

## iv. References

> * Landau & Lifshitz, Mechanics, 3rd ed., §11, Problem 1 (the pendulum period, whose parameter is
>   `sin² (θ₀ / 2)`). [ref: landau\_mechanics]

## A. Strict bounds on the square of the sine

> On `|x| < π / 2` the cosine is positive, so `1 - sin² x = cos² x` is positive; the half-angle form
> follows by applying this at `x = θ / 2`.

**`Real.sin_sq_lt_one`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Trigonometry/SinSq.lean#L55).

> `sin x ^ 2 < 1` for `|x| < π / 2`: the cosine is positive there, and `1 - sin² x = cos² x`.

```lean
lemma sin_sq_lt_one {x : ℝ} (h : |x| < π / 2) : sin x ^ 2 < 1
```

**`Real.sin_half_sq_lt_one`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Trigonometry/SinSq.lean#L63).

> The half-angle form of `sin_sq_lt_one`: `sin (θ / 2) ^ 2 < 1` for `|θ| < π`. For the pendulum
> this says that the parameter `sin² (θ₀ / 2)` of the period formula lies in the domain of
> `completeEllipticK` for every libration amplitude `|θ₀| < π`.

```lean
lemma sin_half_sq_lt_one {θ : ℝ} (h : |θ| < π) : sin (θ / 2) ^ 2 < 1
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/ForMathlib/Trigonometry/SinSq.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Trigonometry/SinSq.lean)
