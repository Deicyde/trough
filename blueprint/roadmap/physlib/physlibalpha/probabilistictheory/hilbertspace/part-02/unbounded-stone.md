---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.expFunction_hasDerivAt, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.expFunction_slope_tendsto, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.expFunction_sub_one_norm_le, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.expFunction_slope_norm_le, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.expFunction_slope_sub_derivative_norm_le, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.expSlope, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.expSlope_measurable, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.expSlope_tendsto
statement: formalized
proof: formalized
---

# Differentiating the exponential multiplier

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.Stone`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Stone.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Stone.lean): 16 declarations, 1 with a docstring.

> Difference quotients of `exp(i t T) x` converge to `i T x` for `x` of finite second moment.

## i. Overview

> The functions `λ ↦ exp(i t λ)` are differentiable in `t` with derivative `i λ exp(i t λ)`, and their
> difference quotients are dominated by `|λ|`. Integrating against a spectral measure, the difference
> quotients of `exp(i t T) x` converge for `x` of finite second moment.

## ii. Key results

> - `expFunction_hasDerivAt` : the derivative of `t ↦ exp(i t λ)`.
> - `expFunction_slope_norm_le` : the difference quotients are bounded by `|λ|`.
> - `expSlope` : the difference quotient `t⁻¹ (exp(i t λ) - 1)`.
> - `expIntegral_inner_slope_tendsto_complexWeakIntegral` : the difference quotients converge weakly.
> - `expIntegral_strong_slope_tendsto` : for `x` in the maximal domain, the difference quotients of
>   `exp(i t T) x` converge in norm to `i T x`.

## iv. References

> * None.

## A. The exponential function and its difference quotients

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.expFunction_hasDerivAt`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Stone.lean#L63).

```lean
lemma expFunction_hasDerivAt (r : ℝ) :
    HasDerivAt (fun t : ℝ => expFunction t r) (Complex.I * (r : ℂ)) 0
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.expFunction_slope_tendsto`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Stone.lean#L92).

```lean
lemma expFunction_slope_tendsto (r : ℝ) :
    Filter.Tendsto
      (fun t : ℝ => t⁻¹ • (expFunction t r - expFunction 0 r))
      (𝓝[≠] (0 : ℝ)) (𝓝 (Complex.I * (r : ℂ)))
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.expFunction_sub_one_norm_le`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Stone.lean#L98).

```lean
lemma expFunction_sub_one_norm_le (t r : ℝ) (ht : |t * r| ≤ 1) :
    ‖expFunction t r - 1‖ ≤ 2 * |t * r|
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.expFunction_slope_norm_le`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Stone.lean#L106).

```lean
lemma expFunction_slope_norm_le {t r : ℝ} (ht : t ≠ 0) (_htsmall : |t| ≤ 1) :
    ‖t⁻¹ • (expFunction t r - 1)‖ ≤ 2 * |r|
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.expFunction_slope_sub_derivative_norm_le`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Stone.lean#L137).

```lean
lemma expFunction_slope_sub_derivative_norm_le {t r : ℝ} (ht : t ≠ 0)
    (htsmall : |t| ≤ 1) :
    ‖t⁻¹ • (expFunction t r - 1) - Complex.I * (r : ℂ)‖ ≤ 3 * |r|
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.expSlope`**, a def, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Stone.lean#L150).

> The difference quotient `t⁻¹(exp(itr) - 1)` of `expFunction`.

```lean
def expSlope (t r : ℝ) : ℂ
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.expSlope_measurable`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Stone.lean#L153).

```lean
lemma expSlope_measurable (t : ℝ) : Measurable (expSlope t)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.expSlope_tendsto`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Stone.lean#L158).

```lean
lemma expSlope_tendsto (r : ℝ) :
    Filter.Tendsto (fun t : ℝ => expSlope t r) (𝓝[≠] (0 : ℝ))
      (𝓝 (Complex.I * (r : ℂ)))
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.expSlope_sub_derivative_measurable`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Stone.lean#L163).

```lean
lemma expSlope_sub_derivative_measurable (t : ℝ) :
    Measurable (fun r : ℝ => expSlope t r - Complex.I * (r : ℂ))
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.expSlope_sub_derivative_norm_le`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Stone.lean#L168).

```lean
lemma expSlope_sub_derivative_norm_le {t r : ℝ} (ht : t ≠ 0)
    (htsmall : |t| ≤ 1) :
    ‖expSlope t r - Complex.I * (r : ℂ)‖ ≤ 3 * |r|
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.vectorMeasure_expSlope_sub_derivative_tendsto`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Stone.lean#L173).

```lean
lemma vectorMeasure_expSlope_sub_derivative_tendsto
    {μ : MeasureTheory.VectorMeasure ℝ ℂ} (hxi : μ.Integrable id) :
    Filter.Tendsto
      (fun t : ℝ => ∫ᵛ r, expSlope t r - Complex.I * (r : ℂ) ∂[
        ContinuousLinearMap.lsmul ℝ ℂ (E := ℂ); μ])
      (𝓝[≠] (0 : ℝ)) (𝓝 0)
```

## B. Weak convergence of the difference quotients

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_inner_eq_complexWeakIntegral`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Stone.lean#L218).

```lean
lemma maximalSpectralIntegral_inner_eq_complexWeakIntegral
    (μS : WOTSpectralMeasure ℝ H) (x : H)
    (hx : x ∈ (maximalSpectralIntegral μS).domain) (y : H)
    (hfi : (μS.scalarMeasure x y).Integrable id) :
    ⟪y, (maximalSpectralIntegral μS) ⟨x, hx⟩⟫_ℂ =
      μS.complexWeakIntegral (fun r : ℝ => (r : ℂ)) x y
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.expIntegral_inner_slope_tendsto_complexWeakIntegral`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Stone.lean#L228).

```lean
lemma expIntegral_inner_slope_tendsto_complexWeakIntegral
    (μS : WOTSpectralMeasure ℝ H) (x y : H)
    (hfi : (μS.scalarMeasure x y).Integrable id) :
    Filter.Tendsto
      (fun t : ℝ => t⁻¹ •
        (⟪y, expIntegral μS t x⟫_ℂ - ⟪y, x⟫_ℂ))
      (𝓝[≠] (0 : ℝ))
      (𝓝 (μS.complexWeakIntegral (fun r : ℝ => Complex.I * (r : ℂ)) x y))
```

## C. Strong convergence of the difference quotients

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral_sub_maximal_norm_sq`**, a lemma, [line 383](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Stone.lean#L383).

```lean
lemma boundedIntegral_sub_maximal_norm_sq
    (μS : WOTSpectralMeasure ℝ H) {g : ℝ → ℂ} (hg : Measurable g)
    (hgb : ∃ C : ℝ, ∀ r, ‖g r‖ ≤ C)
    (x : H) (hx : x ∈ (maximalSpectralIntegral μS).domain) :
    ENNReal.ofReal (‖boundedIntegral μS g hg hgb x -
      Complex.I • (maximalSpectralIntegral μS) ⟨x, hx⟩‖ ^ 2) =
      ∫⁻ r, ENNReal.ofReal (‖g r - Complex.I * (r : ℂ)‖ ^ 2)
        ∂μS.diagonalMeasure x
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.expIntegral_slope_eq_boundedIntegral`**, a lemma, [line 518](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Stone.lean#L518).

```lean
lemma expIntegral_slope_eq_boundedIntegral
    (μS : WOTSpectralMeasure ℝ H) (t : ℝ) (x : H)
    (hgb : ∃ C : ℝ, ∀ r, ‖expSlope t r‖ ≤ C) :
    t⁻¹ • (expIntegral μS t x - x) =
      boundedIntegral μS (expSlope t) (expSlope_measurable t) hgb x
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.expIntegral_strong_slope_tendsto`**, a lemma, [line 555](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Stone.lean#L555).

```lean
lemma expIntegral_strong_slope_tendsto
    (μS : WOTSpectralMeasure ℝ H) (x : H)
    (hx : x ∈ (maximalSpectralIntegral μS).domain) :
    Filter.Tendsto
      (fun t : ℝ => t⁻¹ • (expIntegral μS t x - x))
      (𝓝[≠] (0 : ℝ))
      (𝓝 (Complex.I • (maximalSpectralIntegral μS) ⟨x, hx⟩))
```

## Depends on

- [Integrating unbounded functions against a spectral measure](../part-03/unbounded-spectralintegral-construction.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Stone.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Stone.lean)
