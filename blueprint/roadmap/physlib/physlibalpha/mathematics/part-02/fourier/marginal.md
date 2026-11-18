---
declaration: module
origin: cited
lean: EuclideanProd.fourier_marginal, EuclideanProd.exists_bound_marginal, EuclideanProd.continuous_marginal, EuclideanProd.integrable_marginal, EuclideanProd.fourier_eq_integral_integral
statement: formalized
proof: formalized
---

# The marginal of a Schwartz function on a Euclidean product

The module `PhyslibAlpha.Mathematics.Fourier.Marginal`, [PhyslibAlpha/Mathematics/Fourier/Marginal.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/Marginal.lean): 5 declarations, 5 with a docstring.

> The integral of a Schwartz function over the second factor is continuous and integrable. Its
> Fourier transform is the restriction of the transform to the first factor.

## i. Overview

> A Schwartz function on `WithLp 2 (E × F)` decays faster than every power in the second variable,
> uniformly in the first. The marginal over `F` is therefore a continuous integrable function on
> `E`. Its Fourier transform at `ξ` is the transform of the original function at `(ξ, 0)`.

## ii. Key results

> - `EuclideanProd.fourier_marginal` : the transform of the marginal is the restriction of the
>   transform.
> - `EuclideanProd.continuous_marginal` : the marginal of a Schwartz function is continuous.
> - `EuclideanProd.integrable_marginal` : the marginal of a Schwartz function is integrable.
> - `EuclideanProd.fourier_eq_integral_integral` : the transform is the iterated transform.

## iv. References

> None.

## A. The transform of the marginal

> - `EuclideanProd.fourier_marginal` : the transform of the marginal is the restriction of the
>   transform.

## B. The marginal of a Schwartz function

> - `EuclideanProd.exists_bound_marginal` : a Schwartz function decays in the extra variables.
> - `EuclideanProd.continuous_marginal` : the marginal of a Schwartz function is continuous.
> - `EuclideanProd.integrable_marginal` : the marginal of a Schwartz function is integrable.

## C. The iterated transform

> - `EuclideanProd.fourier_eq_integral_integral` : the transform is the iterated transform.

**`EuclideanProd.fourier_marginal`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/Marginal.lean#L74).

> **The transform of the marginal.** The Fourier transform of the integral over `F` is the
> restriction of the transform to the frequencies `(ξ, 0)`.

```lean
lemma fourier_marginal {φ : WithLp 2 (E × F) → ℂ} (hφ : Integrable φ) (ξ : E) :
    ∫ x : E, (𝐞 (-inner ℝ x ξ) : ℂ) • ∫ y : F, φ (WithLp.toLp 2 (x, y)) =
      ∫ z, (𝐞 (-inner ℝ z (WithLp.toLp 2 (ξ, (0 : F)))) : ℂ) • φ z
```

**`EuclideanProd.exists_bound_marginal`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/Marginal.lean#L98).

> A Schwartz function decays in the extra variables, uniformly in the others.

```lean
lemma exists_bound_marginal (h : 𝓢(WithLp 2 (E × F), ℂ)) :
    ∃ C : ℝ, ∀ (x : E) (y : F), ‖h (WithLp.toLp 2 (x, y))‖ ≤
      C * (1 + ‖y‖) ^ (-((Module.finrank ℝ F + 1 : ℕ) : ℝ))
```

**`EuclideanProd.continuous_marginal`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/Marginal.lean#L108).

> The marginal of a Schwartz function is continuous.

```lean
lemma continuous_marginal (h : 𝓢(WithLp 2 (E × F), ℂ)) :
    Continuous fun x : E => ∫ y : F, h (WithLp.toLp 2 (x, y))
```

**`EuclideanProd.integrable_marginal`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/Marginal.lean#L121).

> The marginal of a Schwartz function is integrable.

```lean
lemma integrable_marginal (h : 𝓢(WithLp 2 (E × F), ℂ)) :
    Integrable fun x : E => ∫ y : F, h (WithLp.toLp 2 (x, y))
```

**`EuclideanProd.fourier_eq_integral_integral`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/Marginal.lean#L128).

> **The iterated form of the Fourier transform.** The transform on the Euclidean product is the
> transform in the first variable of the transform in the second.

```lean
lemma fourier_eq_integral_integral (g : 𝓢(WithLp 2 (E × F), ℂ)) (ζ : E) (ξ : F) :
    𝓕 g (WithLp.toLp 2 (ζ, ξ)) = ∫ x : E, 𝐞 (-(inner ℝ x ζ)) •
      ∫ y : F, 𝐞 (-(inner ℝ y ξ)) • g (WithLp.toLp 2 (x, y))
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Proof depends on

- [Pointwise polynomial decay of Schwartz functions](../distribution/schwartzpointwise.md)
- [Integration over the Euclidean product](../measuretheory/euclideanprod.md)

## Sources

- [PhyslibAlpha/Mathematics/Fourier/Marginal.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/Marginal.lean)
