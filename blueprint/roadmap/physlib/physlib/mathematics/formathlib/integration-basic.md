---
declaration: module
origin: cited
lean: Integration.integral_withDensity_ofReal_eq_integral_smul
statement: formalized
proof: formalized
---

# Basic integration results

The module `Physlib.Mathematics.ForMathlib.Integration.Basic`, [Physlib/Mathematics/ForMathlib/Integration/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Integration/Basic.lean): 1 declaration, 1 with a docstring.

> Basic results related to integration not in Mathlib.

## i. Overview

> Mathlib's `MeasureTheory.integral_withDensity_eq_integral_smul` converts an integral against a
> measure `μ.withDensity f` into an integral against `μ`, but it takes the density as an
> `NNReal`-valued function.
>
> This file contains the version of that lemma for densities given as real-valued functions.

## ii. Key results

> - `Integration.integral_withDensity_ofReal_eq_integral_smul` : for measurable `f ≥ 0`,
>   `∫ x, g x ∂(μ.withDensity fun x => ENNReal.ofReal (f x)) = ∫ x, f x • g x ∂μ`.

## iv. References

## A. Integrals against a real-valued density

**`Integration.integral_withDensity_ofReal_eq_integral_smul`**, a lemma, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Integration/Basic.lean#L47).

> Integrating `g` against the measure with real-valued density `f` (taken through
> `ENNReal.ofReal`) is integrating `f x • g x` against the original measure, for measurable
> `f` that is everywhere nonnegative. This is the `ℝ`-valued form of
> `integral_withDensity_eq_integral_smul`, which takes an `NNReal`-valued density.

```lean
lemma integral_withDensity_ofReal_eq_integral_smul {α : Type*} [MeasurableSpace α]
    {μ : Measure α} {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    {f : α → ℝ} (hf : Measurable f) (hf0 : ∀ x, 0 ≤ f x) (g : α → E) :
    ∫ x, g x ∂(μ.withDensity fun x => ENNReal.ofReal (f x)) = ∫ x, f x • g x ∂μ
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/ForMathlib/Integration/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Integration/Basic.lean)
