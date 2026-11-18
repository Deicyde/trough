---
declaration: module
origin: cited
lean: Real.sqrtCoeff, Real.radius_sqrtCoeff, Real.cosSqrt, Real.sincSqrt, Real.cosSqrt_eq_sum, Real.sincSqrt_eq_sum, Real.analyticOnNhd_sqrtSum, Real.contDiff_cosSqrt
statement: formalized
proof: formalized
---

# `cos √y` and `sinc √y` as entire functions

The module `PhyslibAlpha.Mathematics.SpecialFunctions.SincPropagator.Series`, [PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean): 24 declarations, 5 with a docstring.

> The functions `cos √y` and `sinc √y` are even in `√y`.

## i. Overview

> The functions `cos √y` and `sinc √y` are even in `√y`. They are therefore power series in `y` with
> infinite radius, and smooth on all of `ℝ` although `√` is not differentiable at `0`.
> This file defines them by their series and proves that they are smooth.
> It then proves that every derivative is bounded by `2⁻ʲ` on `[0, ∞)`.

## ii. Key results

> - `sqrtCoeff` : coefficients `(-1)ⁿ / (2n + k)!`
> - `cosSqrt` : `cos √y` as an entire function of `y`.
> - `sincSqrt` : `sinc √y` as an entire function of `y`.
> - `abs_iteratedDeriv_le` : All derivatives of `cos √y` and `sinc √y` are bounded by `2⁻ʲ` on
>   `[0, ∞)`.

## iv. References

> None.

## A. `cos √y` and `sinc √y` as entire functions

> - `sqrtCoeff` : coefficients `(-1)ⁿ / (2n + k)!`
> - `cosSqrt` : `cos √y` as an entire function of `y`.
> - `sincSqrt` : `sinc √y` as an entire function of `y`.
>
> Lemmas: `radius_sqrtCoeff`, `cosSqrt_eq_sum`, `sincSqrt_eq_sum`, `analyticOnNhd_sqrtSum`,
> `contDiff_cosSqrt`, `contDiff_sincSqrt`, `sqrt_pow_two_mul`, `cosSqrt_of_nonneg`,
> `sincSqrt_of_nonneg`, `analyticOnNhd_cosSqrt` and more.

**`Real.sqrtCoeff`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean#L66).

> coefficients `(-1)ⁿ / (2n + k)!`

```lean
def sqrtCoeff (k n : ℕ) : ℝ
```

**`Real.radius_sqrtCoeff`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean#L68).

```lean
lemma radius_sqrtCoeff (k : ℕ) : (ofScalars ℝ (sqrtCoeff k)).radius = ⊤
```

**`Real.cosSqrt`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean#L88).

> `cos √y` as an entire function of `y`.

```lean
def cosSqrt (y : ℝ) : ℝ
```

**`Real.sincSqrt`**, a def, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean#L91).

> `sinc √y` as an entire function of `y`.

```lean
def sincSqrt (y : ℝ) : ℝ
```

**`Real.cosSqrt_eq_sum`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean#L93).

```lean
lemma cosSqrt_eq_sum : cosSqrt = ofScalarsSum (E := ℝ) (sqrtCoeff 0)
```

**`Real.sincSqrt_eq_sum`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean#L96).

```lean
lemma sincSqrt_eq_sum : sincSqrt = ofScalarsSum (E := ℝ) (sqrtCoeff 1)
```

**`Real.analyticOnNhd_sqrtSum`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean#L99).

```lean
lemma analyticOnNhd_sqrtSum (k : ℕ) : AnalyticOnNhd ℝ (ofScalarsSum (E := ℝ) (sqrtCoeff k))
    Set.univ
```

**`Real.contDiff_cosSqrt`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean#L107).

```lean
lemma contDiff_cosSqrt : ContDiff ℝ ⊤ cosSqrt
```

**`Real.contDiff_sincSqrt`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean#L110).

```lean
lemma contDiff_sincSqrt : ContDiff ℝ ⊤ sincSqrt
```

**`Real.sqrt_pow_two_mul`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean#L113).

```lean
lemma sqrt_pow_two_mul {y : ℝ} (hy : 0 ≤ y) (n : ℕ) : √y ^ (2 * n) = y ^ n
```

**`Real.cosSqrt_of_nonneg`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean#L116).

```lean
lemma cosSqrt_of_nonneg {y : ℝ} (hy : 0 ≤ y) : cosSqrt y = cos (√y)
```

**`Real.sincSqrt_of_nonneg`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean#L122).

```lean
lemma sincSqrt_of_nonneg {y : ℝ} (hy : 0 ≤ y) : sincSqrt y = sinc (√y)
```

**`Real.analyticOnNhd_cosSqrt`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean#L135).

```lean
lemma analyticOnNhd_cosSqrt : AnalyticOnNhd ℝ cosSqrt Set.univ
```

**`Real.analyticOnNhd_sincSqrt`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean#L138).

```lean
lemma analyticOnNhd_sincSqrt : AnalyticOnNhd ℝ sincSqrt Set.univ
```

**`Real.hasDerivAt_cosSqrt_of_pos`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean#L141).

```lean
lemma hasDerivAt_cosSqrt_of_pos {y : ℝ} (hy : 0 < y) :
    HasDerivAt cosSqrt (-(1 / 2) * sincSqrt y) y
```

**`Real.deriv_cosSqrt`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean#L151).

```lean
lemma deriv_cosSqrt : deriv cosSqrt = fun y => -(1 / 2) * sincSqrt y
```

**`Real.cosSqrt_eq_sincSqrt_add_of_pos`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean#L161).

```lean
lemma cosSqrt_eq_sincSqrt_add_of_pos {y : ℝ} (hy : 0 < y) :
    cosSqrt y = sincSqrt y + 2 * y * deriv sincSqrt y
```

**`Real.hasDerivAt_integral_scale`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean#L177).

```lean
lemma hasDerivAt_integral_scale {G : ℝ → ℝ} (hG : ContDiff ℝ 1 G) (k : ℕ) (y : ℝ) :
    HasDerivAt (fun y => ∫ u in (0:ℝ)..1, u ^ k * G (u ^ 2 * y))
      (∫ u in (0:ℝ)..1, u ^ (k + 2) * deriv G (u ^ 2 * y)) y
```

**`Real.cosSqrt_eq_sincSqrt_add`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean#L230).

```lean
lemma cosSqrt_eq_sincSqrt_add (y : ℝ) :
    cosSqrt y = sincSqrt y + 2 * y * deriv sincSqrt y
```

**`Real.sincSqrt_eq_integral`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean#L242).

> `sinc √y` is the mean of `cos √(u² y)`.

```lean
lemma sincSqrt_eq_integral (y : ℝ) :
    sincSqrt y = ∫ u in (0:ℝ)..1, cosSqrt (u ^ 2 * y)
```

**`Real.iteratedDeriv_succ_cosSqrt`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean#L262).

```lean
lemma iteratedDeriv_succ_cosSqrt (j : ℕ) :
    iteratedDeriv (j + 1) cosSqrt = fun y => -(1 / 2) * iteratedDeriv j sincSqrt y
```

**`Real.contDiff_iteratedDeriv_cosSqrt`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean#L268).

```lean
lemma contDiff_iteratedDeriv_cosSqrt (j : ℕ) : ContDiff ℝ 1 (iteratedDeriv j cosSqrt)
```

**`Real.iteratedDeriv_sincSqrt`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean#L272).

```lean
lemma iteratedDeriv_sincSqrt (j : ℕ) :
    iteratedDeriv j sincSqrt = fun y => ∫ u in (0:ℝ)..1, u ^ (2 * j) * iteratedDeriv j cosSqrt (u ^
      2 * y)
```

**`Real.abs_iteratedDeriv_le`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean#L289).

> All derivatives of `cos √y` and `sinc √y` are bounded by `2⁻ʲ` on `[0, ∞)`.

```lean
lemma abs_iteratedDeriv_le (j : ℕ) {y : ℝ} (hy : 0 ≤ y) :
    |iteratedDeriv j cosSqrt y| ≤ (1 / 2) ^ j ∧ |iteratedDeriv j sincSqrt y| ≤ (1 / 2) ^ j
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Series.lean)
