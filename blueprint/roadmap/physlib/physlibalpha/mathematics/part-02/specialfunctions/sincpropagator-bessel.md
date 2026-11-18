---
declaration: module
origin: cited
lean: Real.momentFormula, Real.momentFormula_succ, Real.moment_eq, Real.besselSq, Real.summable_pow_div_factorial_sq, Real.summable_even_pow_div_factorial, Real.hasSum_besselSq, Real.moment_scaled
statement: formalized
proof: formalized
---

# The Bessel function `J₀` and the massive sine propagation function on the line

The module `PhyslibAlpha.Mathematics.SpecialFunctions.SincPropagator.Bessel`, [PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean): 24 declarations, 15 with a docstring.

> The sine propagation function with mass is the cosine transform of the Bessel kernel on the
> interval `[-r, r]`.

## i. Overview

> The Bessel function `J₀` is defined by its power series. The kernel `½ J₀ (m √(r² - u²))` on the
> interval `[-r, r]` has the cosine transform `sin (r √(k² + m²)) / √(k² + m²)`. This is the retarded
> Green function of the Klein–Gordon equation in one space dimension. The proof expands both sides in
> power series in `m²`. The moments of `(1 - s²)ⁿ` are computed by a recurrence. The derivative of
> the series in `y = z²` is expressed by the Bessel function `J₁`.

## ii. Key results

> - `moment_eq` : the moments of `(1 - s²)ⁿ`.
> - `besselSq` : `J₀ (√y)` as a power series in `y`.
> - `integral_besselSq_cos` : the cosine transform of the Bessel kernel.
> - `besselJ1` : the Bessel function `J₁`.
> - `mul_besselSqDeriv_eq_besselJ1` : the tail of the Green function in terms of `J₁`.

## iv. References

> None.

## A. Moments

> - `moment_eq` : the moments of `(1 - s²)ⁿ`.
> - `moment_scaled` : the moments of `(r² - u²)ⁿ` on `[-r, r]`.

## B. The Bessel series

> - `besselSq` : `J₀ (√y)` as a power series in `y`.
> - `continuousOn_besselSq` : the Bessel series is continuous on bounded sets.

## C. The cosine transform

> - `hasSum_integral_besselSq_cos` : the cosine transform as a double series.
> - `hasSum_integral_besselSq_cos_series` : the cosine transform as a series in `k² + M`.
> - `integral_besselSq_cos` : the cosine transform of the Bessel kernel.

## D. The derivative and `J₁`

> - `besselSqDeriv` : the derivative of the Bessel series.
> - `hasDerivAt_besselSq` : the derivative of the Bessel series.
> - `besselJ1` : the Bessel function `J₁`.
> - `besselSqDeriv_sq` : the derivative at `z²` in terms of `J₁`.
> - `mul_besselSqDeriv_eq_besselJ1` : the tail of the Green function in terms of `J₁`.

**`Real.momentFormula`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean#L81).

> The closed form of the moments of `(1 - s²)ⁿ`.

```lean
def momentFormula (n j : ℕ) : ℝ
```

**`Real.momentFormula_succ`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean#L84).

```lean
lemma momentFormula_succ (n j : ℕ) :
    momentFormula (n + 1) j = momentFormula n j - momentFormula n (j + 1)
```

**`Real.moment_eq`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean#L118).

> The moments of `(1 - s²)ⁿ` on `[-1, 1]`.

```lean
lemma moment_eq (n j : ℕ) :
    ∫ s in (-1 : ℝ)..1, (1 - s ^ 2) ^ n * s ^ (2 * j) = momentFormula n j
```

**`Real.besselSq`**, a def, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean#L148).

> `J₀ (√y)` as a power series in `y`: `∑ (-y / 4)ⁿ / (n !)²`.

```lean
def besselSq (y : ℝ) : ℝ
```

**`Real.summable_pow_div_factorial_sq`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean#L150).

```lean
lemma summable_pow_div_factorial_sq (a : ℝ) : Summable fun n : ℕ => a ^ n / (n ! : ℝ) ^ 2
```

**`Real.summable_even_pow_div_factorial`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean#L159).

```lean
lemma summable_even_pow_div_factorial (x : ℝ) :
    Summable fun j : ℕ => x ^ (2 * j) / ((2 * j) ! : ℝ)
```

**`Real.hasSum_besselSq`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean#L163).

```lean
lemma hasSum_besselSq (y : ℝ) : HasSum (fun n : ℕ => (-y / 4) ^ n / (n ! : ℝ) ^ 2) (besselSq y)
```

**`Real.moment_scaled`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean#L167).

> The moments of `(r² - u²)ⁿ` on `[-r, r]`.

```lean
lemma moment_scaled {r : ℝ} (hr : 0 ≤ r) (n j : ℕ) :
    ∫ u in (-r)..r, (r ^ 2 - u ^ 2) ^ n * u ^ (2 * j) =
      r ^ (2 * n + 2 * j + 1) * momentFormula n j
```

**`Real.hasSum_integral_besselSq_cos`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean#L187).

> The cosine transform of the Bessel kernel as a double series.

```lean
lemma hasSum_integral_besselSq_cos {r : ℝ} (hr : 0 ≤ r) (k M : ℝ) :
    HasSum (fun p : ℕ × ℕ => (-M / 4) ^ p.1 / (p.1 ! : ℝ) ^ 2 *
      ((-1) ^ p.2 * k ^ (2 * p.2) / ((2 * p.2) ! : ℝ)) *
        (r ^ (2 * p.1 + 2 * p.2 + 1) * momentFormula p.1 p.2))
      (∫ u in (-r)..r, besselSq (M * (r ^ 2 - u ^ 2)) * Real.cos (k * u))
```

**`Real.coeff_eq`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean#L260).

> The coefficient of the double series, simplified.

```lean
lemma coeff_eq (r k M : ℝ) (n j : ℕ) :
    (-M / 4) ^ n / (n ! : ℝ) ^ 2 * ((-1) ^ j * k ^ (2 * j) / ((2 * j) ! : ℝ)) *
        (r ^ (2 * n + 2 * j + 1) * momentFormula n j) =
      2 * (-1) ^ (n + j) * r ^ (2 * (n + j) + 1) / ((2 * (n + j) + 1) ! : ℝ) *
        (((n + j).choose n : ℝ) * M ^ n * (k ^ 2) ^ j)
```

**`Real.hasSum_integral_besselSq_cos_series`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean#L279).

> **The cosine transform of the Bessel kernel as a series in the frequency squared.**

```lean
lemma hasSum_integral_besselSq_cos_series {r : ℝ} (hr : 0 ≤ r) (k M : ℝ) :
    HasSum (fun N : ℕ => 2 * ((-1) ^ N * (k ^ 2 + M) ^ N * r ^ (2 * N + 1) /
      ((2 * N + 1) ! : ℝ)))
      (∫ u in (-r)..r, besselSq (M * (r ^ 2 - u ^ 2)) * Real.cos (k * u))
```

**`Real.hasSum_sincPropagator_series`**, a lemma, [line 311](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean#L311).

> The sine propagation function as a power series in the frequency squared.

```lean
lemma hasSum_sincPropagator_series (r a : ℝ) (ha : 0 ≤ a) :
    HasSum (fun N : ℕ => (-1) ^ N * a ^ N * r ^ (2 * N + 1) / ((2 * N + 1) ! : ℝ))
      (Real.sincPropagator r (Real.sqrt a))
```

**`Real.integral_besselSq_cos`**, a lemma, [line 333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean#L333).

> **The cosine transform of the Bessel kernel.** For `r ≥ 0` and `k² + M ≥ 0`
> `∫_{-r}^{r} J₀ (√M √(r² - u²)) cos (k u) du = 2 sin (r √(k² + M)) / √(k² + M)`.

```lean
lemma integral_besselSq_cos {r : ℝ} (hr : 0 ≤ r) (k M : ℝ) (h : 0 ≤ k ^ 2 + M) :
    ∫ u in (-r)..r, besselSq (M * (r ^ 2 - u ^ 2)) * Real.cos (k * u) =
      2 * Real.sincPropagator r (Real.sqrt (k ^ 2 + M))
```

**`Real.continuousOn_besselSq`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean#L342).

> The Bessel series is continuous on bounded sets.

```lean
lemma continuousOn_besselSq (R : ℝ) : ContinuousOn besselSq (Set.Icc (-R) R)
```

**`Real.besselSqDeriv`**, a def, [line 354](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean#L354).

> The termwise derivative of the Bessel series.

```lean
def besselSqDeriv (y : ℝ) : ℝ
```

**`Real.summable_besselSqDeriv_bound`**, a lemma, [line 356](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean#L356).

```lean
lemma summable_besselSqDeriv_bound (a : ℝ) (ha : 0 ≤ a) :
    Summable fun n : ℕ => (n : ℝ) * (1 / 4) * a ^ (n - 1) / (n ! : ℝ) ^ 2
```

**`Real.hasDerivAt_besselSq`**, a lemma, [line 372](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean#L372).

> **The derivative of the Bessel series.**

```lean
lemma hasDerivAt_besselSq (y : ℝ) : HasDerivAt besselSq (besselSqDeriv y) y
```

**`Real.continuous_besselSqDeriv`**, a lemma, [line 396](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean#L396).

```lean
lemma continuous_besselSqDeriv : Continuous besselSqDeriv
```

**`Real.besselJ1`**, a def, [line 415](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean#L415).

> The Bessel function `J₁` by its power series.

```lean
def besselJ1 (z : ℝ) : ℝ
```

**`Real.summable_besselSqDeriv`**, a lemma, [line 418](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean#L418).

```lean
lemma summable_besselSqDeriv (y : ℝ) :
    Summable fun n : ℕ => (n : ℝ) * (-1 / 4) * (-y / 4) ^ (n - 1) / (n ! : ℝ) ^ 2
```

**`Real.besselSqDeriv_sq`**, a lemma, [line 428](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean#L428).

> The derivative of the Bessel series is `-J₁ (z) / (2 z)` at `y = z²`.

```lean
lemma besselSqDeriv_sq {z : ℝ} (hz : z ≠ 0) : besselSqDeriv (z ^ 2) = -besselJ1 z / (2 * z)
```

**`Real.continuous_besselSq`**, a lemma, [line 455](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean#L455).

```lean
lemma continuous_besselSq : Continuous besselSq
```

**`Real.besselSq_zero`**, a lemma, [line 458](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean#L458).

```lean
lemma besselSq_zero : besselSq 0 = 1
```

**`Real.mul_besselSqDeriv_eq_besselJ1`**, a lemma, [line 467](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean#L467).

> **The Bessel tail in terms of `J₁`.** For `|u| < τ` the derivative of the Bessel series at
> `m² (τ² - u²)` is `J₁ (m √(τ² - u²)) / √(τ² - u²)` up to the factor `-1 / (2 m)`.

```lean
lemma mul_besselSqDeriv_eq_besselJ1 {m τ u : ℝ} (hm : m ≠ 0) (hu : |u| < τ) (c : ℝ) :
    2 * m ^ 2 * (c * besselSqDeriv (m ^ 2 * (τ ^ 2 - u ^ 2))) =
      -(m * (c * (besselJ1 (m * Real.sqrt (τ ^ 2 - u ^ 2)) / Real.sqrt (τ ^ 2 - u ^ 2))))
```

## Depends on

- [The sine propagation function `t ↦ sin (ω t) / ω`](sincpropagator-basic.md)

## Sources

- [PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Bessel.lean)
