---
declaration: module
origin: cited
lean: FourierIntegral.fourierInvIntegral_eq_fourier, FourierIntegral.laplacian_fourierInvIntegral, FourierIntegral.iteratedDeriv_fourierChar, FourierIntegral.norm_iteratedFDeriv_fourierChar, FourierIntegral.contDiff_fourierChar_real, FourierIntegral.norm_iteratedFDeriv_char_le, FourierIntegral.norm_iteratedFDeriv_timeShift_le, FourierIntegral.char_pow_mul_decay_le
statement: formalized
proof: formalized
---

# Fourier integrals and their derivatives

The module `PhyslibAlpha.Mathematics.Fourier.Integral`, [PhyslibAlpha/Mathematics/Fourier/Integral.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/Integral.lean): 9 declarations, 5 with a docstring.

## i. Overview

> Derivative bounds for the Fourier character and the Laplacian of an inverse Fourier integral.

## ii. Key results

> - `laplacian_fourierInvIntegral` : The Laplacian of the inverse Fourier integral of `h` is the
>   integral of `-(2π)² ‖ξ‖² h`.
> - `char_pow_mul_decay_le` : Polynomial factors from spatial derivatives are absorbed by additional
>   Fourier decay.
> - `fourierInvIntegral_eq_fourier` : The inverse Fourier integral is the Fourier integral of the
>   reflected function.
> - `norm_iteratedFDeriv_timeShift_le` : The derivatives of a time translate are bounded by those of
>   the function.

## iv. References

> None.

## A. The Laplacian of an inverse Fourier integral

> Lemmas: `fourierInvIntegral_eq_fourier`, `laplacian_fourierInvIntegral`.

## B. Derivative bounds for the Fourier character and for time translates

> Lemmas: `iteratedDeriv_fourierChar`, `norm_iteratedFDeriv_fourierChar`, `contDiff_fourierChar_real`,
> `norm_iteratedFDeriv_char_le`, `norm_iteratedFDeriv_timeShift_le`, `char_pow_mul_decay_le`.

## C. Smoothness of the retarded solution

> Lemmas: `contDiff_char_pair`.

**`FourierIntegral.fourierInvIntegral_eq_fourier`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/Integral.lean#L75).

> The inverse Fourier integral is the Fourier integral of the reflected function.

```lean
lemma fourierInvIntegral_eq_fourier (h : E → F) (x : E) :
    ∫ ξ : E, (𝐞 (inner ℝ ξ x) : ℂ) • h ξ = 𝓕 (fun v => h (-v)) x
```

**`FourierIntegral.laplacian_fourierInvIntegral`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/Integral.lean#L82).

> The Laplacian of the inverse Fourier integral of `h` is the integral of `-(2π)² ‖ξ‖² h`.

```lean
lemma laplacian_fourierInvIntegral {h : E → F} (hm : AEStronglyMeasurable h volume)
    (hi : ∀ n : ℕ, n ≤ 2 → Integrable (fun ξ : E => ‖ξ‖ ^ n * ‖h ξ‖)) (x : E) :
    Δ (fun y : E => ∫ ξ : E, (𝐞 (inner ℝ ξ y) : ℂ) • h ξ) x =
      ∫ ξ : E, (-((2 * π) ^ 2 * ‖ξ‖ ^ 2 : ℝ) : ℂ) • ((𝐞 (inner ℝ ξ x) : ℂ) • h ξ)
```

**`FourierIntegral.iteratedDeriv_fourierChar`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/Integral.lean#L141).

```lean
lemma iteratedDeriv_fourierChar (i : ℕ) :
    iteratedDeriv i (fun r : ℝ => (𝐞 r : ℂ)) = fun r => (2 * π * Complex.I) ^ i * (𝐞 r : ℂ)
```

**`FourierIntegral.norm_iteratedFDeriv_fourierChar`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/Integral.lean#L154).

```lean
lemma norm_iteratedFDeriv_fourierChar (i : ℕ) (r : ℝ) :
    ‖iteratedFDeriv ℝ i (fun r : ℝ => (𝐞 r : ℂ)) r‖ = (2 * π) ^ i
```

**`FourierIntegral.contDiff_fourierChar_real`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/Integral.lean#L159).

```lean
lemma contDiff_fourierChar_real : ContDiff ℝ ∞ (fun r : ℝ => (𝐞 r : ℂ))
```

**`FourierIntegral.norm_iteratedFDeriv_char_le`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/Integral.lean#L168).

> The derivatives of `(t, x) ↦ 𝐞 ⟪ξ, x⟫` are bounded by `(2π‖ξ‖)ⁱ`.

```lean
lemma norm_iteratedFDeriv_char_le (ξ : E) (i : ℕ) (q : ℝ × E) :
    ‖iteratedFDeriv ℝ i (fun q : ℝ × E => (𝐞 (inner ℝ ξ q.2) : ℂ)) q‖ ≤ (2 * π * ‖ξ‖) ^ i
```

**`FourierIntegral.norm_iteratedFDeriv_timeShift_le`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/Integral.lean#L194).

> The derivatives of a time translate are bounded by those of the function.

```lean
lemma norm_iteratedFDeriv_timeShift_le (g : ℝ → F) (hg : ContDiff ℝ ∞ g) (r : ℝ) (j : ℕ)
    (q : ℝ × E) :
    ‖iteratedFDeriv ℝ j (fun q : ℝ × E => g (q.1 - r)) q‖ ≤ ‖iteratedDeriv j g (q.1 - r)‖
```

**`FourierIntegral.char_pow_mul_decay_le`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/Integral.lean#L214).

> Polynomial factors from spatial derivatives are absorbed by additional Fourier decay.

```lean
lemma char_pow_mul_decay_le {E : Type*} [NormedAddCommGroup E] (ξ : E) (i N : ℕ) :
    (2 * π * ‖ξ‖) ^ i * (1 + ‖ξ‖) ^ (-((i + N : ℕ) : ℝ)) ≤
      (2 * π) ^ i * (1 + ‖ξ‖) ^ (-(N : ℝ))
```

**`FourierIntegral.contDiff_char_pair`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/Integral.lean#L234).

```lean
lemma contDiff_char_pair : ContDiff ℝ ∞ fun w : (ℝ × E) × (ℝ × E) =>
    (𝐞 (inner ℝ w.2.2 w.1.2) : ℂ)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/Fourier/Integral.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/Integral.lean)
