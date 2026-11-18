---
declaration: module
origin: cited
lean: SchwartzMap.integral_char_smul_fourier, SchwartzMap.integral_char_mul_fourier, SchwartzMap.integrable_char_mul_fourier
statement: formalized
proof: formalized
---

# Fourier inversion for Schwartz functions on the line

The module `PhyslibAlpha.Mathematics.Fourier.Inversion`, [PhyslibAlpha/Mathematics/Fourier/Inversion.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/Inversion.lean): 3 declarations, 3 with a docstring.

> A Schwartz function on the line is the integral of its transform against the exponential.

## i. Overview

> Mathlib states Fourier inversion for the Fourier multiplier on the Schwartz space. This file
> unfolds it to the pointwise integral with the character `𝐞 (y * ξ)`. The integrand is integrable
> because the transform is.

## ii. Key results

> - `SchwartzMap.integral_char_smul_fourier` : the pointwise inversion formula.
> - `SchwartzMap.integral_char_mul_fourier` : the same with the product in place of the scalar action.
> - `SchwartzMap.integrable_char_mul_fourier` : the integrand is integrable.

## iv. References

> None.

## A. Pointwise inversion

> - `SchwartzMap.integral_char_smul_fourier` : the pointwise inversion formula.
> - `SchwartzMap.integral_char_mul_fourier` : the same with the product.
> - `SchwartzMap.integrable_char_mul_fourier` : the integrand is integrable.

**`SchwartzMap.integral_char_smul_fourier`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/Inversion.lean#L53).

> **Fourier inversion on the line.**

```lean
lemma integral_char_smul_fourier (g : 𝓢(ℝ, ℂ)) (y : ℝ) :
    ∫ ξ : ℝ, (𝐞 (y * ξ) : ℂ) • 𝓕 g ξ = g y
```

**`SchwartzMap.integral_char_mul_fourier`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/Inversion.lean#L62).

> Fourier inversion on the line with the product in place of the scalar action.

```lean
lemma integral_char_mul_fourier (g : 𝓢(ℝ, ℂ)) (y : ℝ) :
    ∫ ξ : ℝ, (𝐞 (y * ξ) : ℂ) * 𝓕 g ξ = g y
```

**`SchwartzMap.integrable_char_mul_fourier`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/Inversion.lean#L67).

> The integrand of Fourier inversion is integrable.

```lean
lemma integrable_char_mul_fourier (g : 𝓢(ℝ, ℂ)) (y : ℝ) :
    Integrable fun ξ : ℝ => (𝐞 (y * ξ) : ℂ) * 𝓕 g ξ
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/Fourier/Inversion.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/Inversion.lean)
