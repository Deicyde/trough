---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.simpleIntegral, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.simpleIntegral_inner, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.simpleIntegral_norm_sq, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.simpleIntegral_norm_sq_eq_lintegral, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.simpleIntegral_norm_sq_le, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.simpleIntegral_norm_le, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.simpleIntegral_const, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.spectralCLM
statement: formalized
proof: formalized
---

# Integrating bounded functions against a spectral measure

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.BoundedIntegral`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean): 28 declarations, 4 with a docstring.

> The integral of a bounded measurable function against a weak spectral measure.

## i. Overview

> For a weak spectral measure `μ` and a bounded measurable `f`, the operator `∫ f dμ` is defined in
> three steps. A simple function `f` has the finite sum `∑ z • μ (f⁻¹{z})`. Its norm is controlled by
> the sup norm of `f`, so for a uniform limit of simple functions the finite sums converge in operator
> norm. Every bounded measurable function is such a limit, which gives the integral.

## ii. Key results

> - `simpleIntegral` : the integral of a simple function.
> - `simpleIntegral_norm_le` : the integral of a simple function is bounded by its sup norm.
> - `simpleIntegral_piecewise_indicator` : `∫ 𝟙_S dμ = μ S`.
> - `boundedIntegral` : the integral of a bounded measurable function.

## iv. References

> * None.

## A. The simple-function integral

> The integral of a simple function is a finite sum. It is defined in the weak operator topology,
> since a weak spectral measure need not have finite variation in operator norm.

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.simpleIntegral`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L68).

> The weak-operator integral of a complex-valued simple function.

```lean
noncomputable def simpleIntegral (f : SimpleFunc α ℂ) : H →WOT[ℂ] H
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.simpleIntegral_inner`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L71).

```lean
lemma simpleIntegral_inner (f : SimpleFunc α ℂ) (x y : H) :
    ⟪y, simpleIntegral μS f x⟫_ℂ =
      ∑ z ∈ f.range, z * μS.scalarMeasure x y (f ⁻¹' {z})
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.simpleIntegral_norm_sq`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L80).

```lean
lemma simpleIntegral_norm_sq (f : SimpleFunc α ℂ) (x : H) :
    ENNReal.ofReal (‖simpleIntegral μS f x‖ ^ 2) =
      ∑ z ∈ f.range, ENNReal.ofReal (‖z‖ ^ 2) *
        (μS.diagonalMeasure x) (f ⁻¹' {z})
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.simpleIntegral_norm_sq_eq_lintegral`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L148).

```lean
lemma simpleIntegral_norm_sq_eq_lintegral (f : SimpleFunc α ℂ) (x : H) :
    ENNReal.ofReal (‖simpleIntegral μS f x‖ ^ 2) =
      ∫⁻ z, ENNReal.ofReal (‖f z‖ ^ 2) ∂μS.diagonalMeasure x
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.simpleIntegral_norm_sq_le`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L160).

```lean
lemma simpleIntegral_norm_sq_le (f : SimpleFunc α ℂ) (x : H) {C : ℝ}
    (hC : ∀ z ∈ f.range, ‖z‖ ^ 2 ≤ C ^ 2) :
    ENNReal.ofReal (‖simpleIntegral μS f x‖ ^ 2) ≤
      ENNReal.ofReal (C ^ 2 * ‖x‖ ^ 2)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.simpleIntegral_norm_le`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L181).

```lean
lemma simpleIntegral_norm_le (f : SimpleFunc α ℂ) (x : H) {C : ℝ}
    (hC : 0 ≤ C) (hCf : ∀ z ∈ f.range, ‖z‖ ≤ C) :
    ‖simpleIntegral μS f x‖ ≤ C * ‖x‖
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.simpleIntegral_const`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L195).

```lean
lemma simpleIntegral_const [Nonempty α] (c : ℂ) :
    simpleIntegral μS (SimpleFunc.const α c) = c • (1 : H →WOT[ℂ] H)
```

## B. Uniform approximation and the limiting integral

> The WOT type is a topological copy of the bounded-operator space; its underlying normed operator
> is still available through `toCLM`. The finite estimate above therefore gives a norm completion
> for any explicitly supplied uniformly convergent simple approximation. Keeping the approximation
> sequence as an argument makes the analytic hypotheses visible at this low level.

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.spectralCLM`**, a def, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L216).

> The real-linear map `z ↦ z • μS(S)`, as a bounded operator, for each `z : ℂ`.

```lean
def spectralCLM (S : Set α) : ℂ →L[ℝ] (H →L[ℂ] H)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.spectralCLM_apply`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L219).

```lean
lemma spectralCLM_apply (S : Set α) (z : ℂ) :
    spectralCLM μS S z = z • ContinuousLinearMapWOT.toCLM (μS S)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.spectralCLM_finMeasAdditive`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L223).

```lean
lemma spectralCLM_finMeasAdditive (μ : Measure α) :
    FinMeasAdditive μ (spectralCLM μS)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.simpleFunc_integrable_dirac`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L231).

```lean
lemma simpleFunc_integrable_dirac (f : SimpleFunc α ℂ) [Nonempty α] :
    Integrable f (Measure.dirac (Classical.choice (inferInstance : Nonempty α)))
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.simpleIntegral_eq_setToSimpleFunc`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L238).

```lean
lemma simpleIntegral_eq_setToSimpleFunc (f : SimpleFunc α ℂ) (_μ : Measure α) :
    ContinuousLinearMapWOT.toCLM (simpleIntegral μS f) = f.setToSimpleFunc (spectralCLM μS)
```

> The integral of an indicator is the value of the spectral measure.

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.simpleIntegral_piecewise_indicator`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L260).

```lean
lemma simpleIntegral_piecewise_indicator {S : Set α} (hS : MeasurableSet S) :
    simpleIntegral μS
        (SimpleFunc.piecewise S hS (SimpleFunc.const α (1 : ℂ))
          (SimpleFunc.const α (0 : ℂ))) = μS S
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.simpleIntegral_add`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L272).

```lean
lemma simpleIntegral_add [Nonempty α] (f g : SimpleFunc α ℂ) :
    simpleIntegral μS (f + g) = simpleIntegral μS f + simpleIntegral μS g
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.simpleIntegral_neg`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L283).

```lean
lemma simpleIntegral_neg [Nonempty α] (f : SimpleFunc α ℂ) :
    simpleIntegral μS (-f) = -simpleIntegral μS f
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.simpleIntegral_sub`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L293).

```lean
lemma simpleIntegral_sub [Nonempty α] (f g : SimpleFunc α ℂ) :
    simpleIntegral μS (f - g) = simpleIntegral μS f - simpleIntegral μS g
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.simpleIntegral_mul`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L297).

```lean
lemma simpleIntegral_mul [Nonempty α] (f g : SimpleFunc α ℂ) :
    simpleIntegral μS (f * g) = simpleIntegral μS f * simpleIntegral μS g
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.simpleIntegral_star`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L342).

```lean
lemma simpleIntegral_star [Nonempty α] (f : SimpleFunc α ℂ) :
    simpleIntegral μS (star f) = star (simpleIntegral μS f)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.simpleIntegral_toCLM_norm_le`**, a lemma, [line 378](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L378).

```lean
lemma simpleIntegral_toCLM_norm_le (f : SimpleFunc α ℂ) {C : ℝ}
    (hC : 0 ≤ C) (hCf : ∀ z ∈ f.range, ‖z‖ ≤ C) :
    ‖ContinuousLinearMapWOT.toCLM (simpleIntegral μS f)‖ ≤ C
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.simpleIntegral_toCLM_diff_norm_le`**, a lemma, [line 385](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L385).

```lean
lemma simpleIntegral_toCLM_diff_norm_le [Nonempty α] (f g : SimpleFunc α ℂ) {C : ℝ}
    (hC : 0 ≤ C) (hfg : ∀ x, ‖f x - g x‖ ≤ C) :
    ‖ContinuousLinearMapWOT.toCLM (simpleIntegral μS f) -
        ContinuousLinearMapWOT.toCLM (simpleIntegral μS g)‖ ≤ C
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.simpleIntegral_toCLM_cauchySeq`**, a lemma, [line 395](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L395).

```lean
lemma simpleIntegral_toCLM_cauchySeq [Nonempty α] {f : α → ℂ} {s : ℕ → SimpleFunc α ℂ}
    (hs : ∀ ε > 0, ∃ N, ∀ n ≥ N, ∀ x, ‖s n x - f x‖ < ε) :
    CauchySeq (fun n => ContinuousLinearMapWOT.toCLM (simpleIntegral μS (s n)))
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegralOfUniformApprox`**, a def, [line 419](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L419).

> The bounded operator integral obtained from an explicit uniformly convergent simple
> approximation. The limit is taken in the normed space of bounded operators and then viewed in the
> WOT copy.

```lean
noncomputable def boundedIntegralOfUniformApprox [Nonempty α]
    (f : α → ℂ) (s : ℕ → SimpleFunc α ℂ)
    (_hs : ∀ ε > 0, ∃ N, ∀ n ≥ N, ∀ x, ‖s n x - f x‖ < ε) :
    H →WOT[ℂ] H
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegralOfUniformApprox_eq_limUnder`**, a lemma, [line 427](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L427).

```lean
lemma boundedIntegralOfUniformApprox_eq_limUnder
    [Nonempty α]
    (f : α → ℂ) (s : ℕ → SimpleFunc α ℂ)
    (hs : ∀ ε > 0, ∃ N, ∀ n ≥ N, ∀ x, ‖s n x - f x‖ < ε) :
    ContinuousLinearMapWOT.toCLM (boundedIntegralOfUniformApprox μS f s hs) =
      Filter.atTop.limUnder
        (fun n => ContinuousLinearMapWOT.toCLM (simpleIntegral μS (s n)))
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegralOfUniformApprox_norm_le`**, a lemma, [line 436](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L436).

```lean
lemma boundedIntegralOfUniformApprox_norm_le
    [Nonempty α]
    (f : α → ℂ) (s : ℕ → SimpleFunc α ℂ)
    (hs : ∀ ε > 0, ∃ N, ∀ n ≥ N, ∀ x, ‖s n x - f x‖ < ε)
    {C : ℝ} (hC : ∀ n x, ‖s n x‖ ≤ C) :
    ‖ContinuousLinearMapWOT.toCLM (boundedIntegralOfUniformApprox μS f s hs)‖ ≤ C
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegralOfUniformApprox_eq_of_uniform_approx`**, a lemma, [line 461](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L461).

```lean
lemma boundedIntegralOfUniformApprox_eq_of_uniform_approx
    [Nonempty α]
    {f : α → ℂ} {s t : ℕ → SimpleFunc α ℂ}
    (hs : ∀ ε > 0, ∃ N, ∀ n ≥ N, ∀ x, ‖s n x - f x‖ < ε)
    (ht : ∀ ε > 0, ∃ N, ∀ n ≥ N, ∀ x, ‖t n x - f x‖ < ε)
    (hst : ∀ ε > 0, ∃ N, ∀ n ≥ N, ∀ x, ‖s n x - t n x‖ < ε) :
    boundedIntegralOfUniformApprox μS f s hs =
      boundedIntegralOfUniformApprox μS f t ht
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegralOfUniformApprox_eq_of_same_target`**, a lemma, [line 514](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L514).

```lean
lemma boundedIntegralOfUniformApprox_eq_of_same_target
    [Nonempty α]
    {f : α → ℂ} {s t : ℕ → SimpleFunc α ℂ}
    (hs : ∀ ε > 0, ∃ N, ∀ n ≥ N, ∀ x, ‖s n x - f x‖ < ε)
    (ht : ∀ ε > 0, ∃ N, ∀ n ≥ N, ∀ x, ‖t n x - f x‖ < ε) :
    boundedIntegralOfUniformApprox μS f s hs =
      boundedIntegralOfUniformApprox μS f t ht
```

## C. The canonical integral

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.exists_uniform_simple_approx`**, a lemma, [line 538](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L538).

```lean
lemma exists_uniform_simple_approx [Nonempty α] {f : α → ℂ} (hf : Measurable f)
    (hbdd : ∃ C, ∀ x, ‖f x‖ ≤ C) :
    ∃ s : ℕ → SimpleFunc α ℂ,
      (∀ ε > 0, ∃ N, ∀ n ≥ N, ∀ x, ‖s n x - f x‖ < ε) ∧
      ∃ C, ∀ n x, ‖s n x‖ ≤ C
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral`**, a def, [line 605](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean#L605).

> The weak-operator-topology integral of a bounded measurable `f : α → ℂ` against `μS`,
> defined as the limit of simple-function integrals under uniform approximation.

```lean
noncomputable def boundedIntegral [Nonempty α] (f : α → ℂ) (hf : Measurable f)
    (hbdd : ∃ C, ∀ x, ‖f x‖ ≤ C) : H →WOT[ℂ] H
```

## Depends on

- [Scalar and diagonal measures of a spectral measure](unbounded-scalarmeasure.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegral.lean)
