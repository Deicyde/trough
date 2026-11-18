---
declaration: module
origin: cited
lean: ParametricIntegral.contDiffOn_integral, ParametricIntegral.norm_iteratedFDeriv_integral_le, ParametricIntegral.continuous_iteratedFDeriv_partial
statement: formalized
proof: formalized
---

# Smoothness of parametric integrals

The module `PhyslibAlpha.Mathematics.Calculus.ParametricIntegral`, [PhyslibAlpha/Mathematics/Calculus/ParametricIntegral.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Calculus/ParametricIntegral.lean): 3 declarations, 2 with a docstring.

## i. Overview

> An integral of a smooth family of functions is smooth when the derivatives have an integrable bound.

## ii. Key results

> - `continuous_iteratedFDeriv_partial` : The derivatives in the first variable of a jointly smooth
>   function are jointly continuous.
> - `norm_iteratedFDeriv_integral_le` : Uniform integrable domination bounds every derivative of a
>   parametric integral.
> - `contDiffOn_integral`

## iv. References

> None.

## A. Smoothness of parametric integrals

> Lemmas: `contDiffOn_integral`, `norm_iteratedFDeriv_integral_le`,
> `continuous_iteratedFDeriv_partial`.

**`ParametricIntegral.contDiffOn_integral`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Calculus/ParametricIntegral.lean#L52).

```lean
lemma contDiffOn_integral {P α : Type u} [NormedAddCommGroup P] [NormedSpace ℝ P]
    [MeasurableSpace α]
    (μ : Measure α)
    {U : Set P} (hU : IsOpen U) (n : ℕ) :
    ∀ (F : Type u) [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] (H : P → α → F),
    (∀ a, ContDiff ℝ n fun p => H p a) →
    (∀ k ≤ n, ∀ p, AEStronglyMeasurable (fun a => iteratedFDeriv ℝ k (fun q => H q a) p) μ) →
    (∀ k ≤ n, ∃ b : α → ℝ, Integrable b μ ∧
      ∀ᵐ a ∂μ, ∀ p ∈ U, ‖iteratedFDeriv ℝ k (fun q => H q a) p‖ ≤ b a) →
    ContDiffOn ℝ n (fun p => ∫ a, H p a ∂μ) U
```

**`ParametricIntegral.norm_iteratedFDeriv_integral_le`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Calculus/ParametricIntegral.lean#L121).

> Uniform integrable domination bounds every derivative of a parametric integral.

```lean
lemma norm_iteratedFDeriv_integral_le {P α : Type u} [NormedAddCommGroup P] [NormedSpace ℝ P]
    [MeasurableSpace α] (μ : Measure α) (n : ℕ) :
    ∀ (F : Type u) [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F]
      (H : P → α → F) (b : ℕ → α → ℝ),
    (∀ a, ContDiff ℝ ∞ (fun p => H p a)) →
    (∀ k p, AEStronglyMeasurable (fun a => iteratedFDeriv ℝ k (fun q => H q a) p) μ) →
    (∀ k, Integrable (b k) μ) →
    (∀ k, ∀ᵐ a ∂μ, ∀ p, ‖iteratedFDeriv ℝ k (fun q => H q a) p‖ ≤ b k a) →
    ∀ p, ‖iteratedFDeriv ℝ n (fun q => ∫ a, H q a ∂μ) p‖ ≤ ∫ a, b n a ∂μ
```

**`ParametricIntegral.continuous_iteratedFDeriv_partial`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Calculus/ParametricIntegral.lean#L170).

> The derivatives in the first variable of a jointly smooth function are jointly continuous.

```lean
lemma continuous_iteratedFDeriv_partial {P α F : Type*} [NormedAddCommGroup P] [NormedSpace ℝ P]
    [NormedAddCommGroup α] [NormedSpace ℝ α] [NormedAddCommGroup F] [NormedSpace ℝ F]
    (H : P × α → F) (hH : ContDiff ℝ ∞ H) (k : ℕ) :
    Continuous fun z : P × α => iteratedFDeriv ℝ k (fun q => H (q, z.2)) z.1
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/Calculus/ParametricIntegral.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Calculus/ParametricIntegral.lean)
