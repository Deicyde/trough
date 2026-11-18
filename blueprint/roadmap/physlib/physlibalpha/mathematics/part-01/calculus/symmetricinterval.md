---
declaration: module
origin: cited
lean: SymmetricInterval.integral_symm_even, SymmetricInterval.hasDerivAt_convolution
statement: formalized
proof: formalized
---

# Integrals over a symmetric interval

The module `PhyslibAlpha.Mathematics.Calculus.SymmetricInterval`, [PhyslibAlpha/Mathematics/Calculus/SymmetricInterval.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Calculus/SymmetricInterval.lean): 2 declarations, 2 with a docstring.

> An even function integrates over `[-τ, τ]` to twice its integral over `[0, τ]`. A convolution with
> a continuous weight over `[-τ, τ]` is differentiated under the integral.

## i. Overview

> Both statements are used for the radial Bessel kernel. The weight is a continuous real function.
> The convolved function is complex valued and continuously differentiable.

## ii. Key results

> - `SymmetricInterval.integral_symm_even` : the integral of an even function.
> - `SymmetricInterval.hasDerivAt_convolution` : differentiation of a convolution over `[-τ, τ]`.

## iv. References

> None.

## A. Even functions

> - `SymmetricInterval.integral_symm_even` : the integral of an even function.

## B. Convolution

> - `SymmetricInterval.hasDerivAt_convolution` : differentiation of a convolution over `[-τ, τ]`.

**`SymmetricInterval.integral_symm_even`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Calculus/SymmetricInterval.lean#L55).

> The integral of an even continuous function over a symmetric interval.

```lean
lemma integral_symm_even {f : ℝ → ℂ} (hf : Continuous f) (he : ∀ x, f (-x) = f x) (τ : ℝ) :
    ∫ x in (-τ)..τ, f x = 2 * ∫ x in (0 : ℝ)..τ, f x
```

**`SymmetricInterval.hasDerivAt_convolution`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Calculus/SymmetricInterval.lean#L67).

> **Differentiation of a convolution over a bounded interval.**

```lean
lemma hasDerivAt_convolution {τ : ℝ} (hτ : 0 ≤ τ) (w : ℝ → ℝ) (hw : Continuous w) (f : ℝ → ℂ)
    (hf : ContDiff ℝ 1 f) (ρ : ℝ) :
    HasDerivAt (fun r : ℝ => ∫ u in (-τ)..τ, (w u : ℂ) * f (r + u))
      (∫ u in (-τ)..τ, (w u : ℂ) * deriv f (ρ + u)) ρ
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/Calculus/SymmetricInterval.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Calculus/SymmetricInterval.lean)
