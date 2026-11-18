---
declaration: module
origin: cited
lean: SpaceTimeAlgebra.taylorSeries, SpaceTimeAlgebra.coeff_taylorSeries, SpaceTimeAlgebra.constantCoeff_iteratedPDeriv_taylorSeries, SpaceTimeAlgebra.taylorSeries_add, SpaceTimeAlgebra.taylorSeries_const_smul, SpaceTimeAlgebra.taylorSeries_deriv
statement: formalized
proof: formalized
---

# Taylor series of functions on spacetime

The module `Physlib.SpaceAndTime.SpaceTime.SpaceTimeAlgebra.TaylorSeries`, [Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/TaylorSeries.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/TaylorSeries.lean): 6 declarations, 3 with a docstring.

## i. Overview

> The Taylor series of a complex-valued function `f` on spacetime at a point `x₀` is the element of
> the spacetime algebra whose base-point derivative values are the iterated derivatives of `f` at
> `x₀`. For smooth `f` it is additive and `ℂ`-homogeneous in `f`, and it takes the derivative of `f`
> along a direction to the formal partial derivative of the series along the same direction.

## ii. Key results

> - `SpaceTimeAlgebra.taylorSeries` : the Taylor series of a function at a point.
> - `SpaceTimeAlgebra.constantCoeff_iteratedPDeriv_taylorSeries` : derivative values of `f` at `x₀`.
> - `SpaceTimeAlgebra.taylorSeries_deriv` : derivatives become formal partial derivatives.

## iv. References

> * None.

## A. The Taylor series of a function

> The iterated derivatives `iteratedDeriv s f` of a function are indexed by multisets of directions,
> like the iterated formal partial derivatives of a series. The Taylor series of `f` at `x₀` is the
> series `ofDerivValues` built from their values at `x₀`, so that its coefficient of `x^s` is
> `(∂^s f)(x₀)` divided by `s!` and the base point of the spacetime algebra is identified with `x₀`.
> For smooth functions, iterated derivatives distribute over sums and scalar multiples, and so does
> the Taylor series.

**`SpaceTimeAlgebra.taylorSeries`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/TaylorSeries.lean#L59).

> The Taylor series at `x₀` of a complex-valued function on spacetime.

```lean
noncomputable def taylorSeries (x₀ : SpaceTime) (f : SpaceTime → ℂ) : SpaceTimeAlgebra
```

**`SpaceTimeAlgebra.coeff_taylorSeries`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/TaylorSeries.lean#L62).

```lean
lemma coeff_taylorSeries (x₀ : SpaceTime) (f : SpaceTime → ℂ) (m : (Fin 1 ⊕ Fin 3) →₀ ℕ) :
    coeff m (taylorSeries x₀ f) =
      ((∏ ν, (m ν).factorial : ℕ) : ℂ)⁻¹ * iteratedDeriv (Finsupp.toMultiset m) f x₀
```

**`SpaceTimeAlgebra.constantCoeff_iteratedPDeriv_taylorSeries`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/TaylorSeries.lean#L68).

> The base-point derivative values of `taylorSeries x₀ f` are the derivatives of `f` at `x₀`.

```lean
lemma constantCoeff_iteratedPDeriv_taylorSeries (x₀ : SpaceTime) (f : SpaceTime → ℂ)
    (s : Multiset (Fin 1 ⊕ Fin 3)) :
    constantCoeff (iteratedPDeriv s (taylorSeries x₀ f)) = iteratedDeriv s f x₀
```

**`SpaceTimeAlgebra.taylorSeries_add`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/TaylorSeries.lean#L76).

```lean
lemma taylorSeries_add (x₀ : SpaceTime) {f g : SpaceTime → ℂ} (hf : ContDiff ℝ ∞ f)
    (hg : ContDiff ℝ ∞ g) :
    taylorSeries x₀ (f + g) = taylorSeries x₀ f + taylorSeries x₀ g
```

**`SpaceTimeAlgebra.taylorSeries_const_smul`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/TaylorSeries.lean#L83).

```lean
lemma taylorSeries_const_smul (x₀ : SpaceTime) (c : ℂ) {f : SpaceTime → ℂ}
    (hf : ContDiff ℝ ∞ f) :
    taylorSeries x₀ (c • f) = c • taylorSeries x₀ f
```

## B. Taylor series of derivatives

> Applying `∂^s` after `∂_μ` is the same as applying `∂^(μ ::ₘ s)`, both for smooth functions and
> for series. Hence the Taylor series of `∂_μ f` and the formal partial derivative `pderiv μ` of the
> Taylor series of `f` have the same base-point derivative values, namely `(∂^(μ ::ₘ s) f)(x₀)` at
> each `s`. A series is determined by its base-point derivative values, so the two are equal.

**`SpaceTimeAlgebra.taylorSeries_deriv`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/TaylorSeries.lean#L102).

> The Taylor series of a derivative is the formal partial derivative of the Taylor series.

```lean
lemma taylorSeries_deriv (x₀ : SpaceTime) (μ : Fin 1 ⊕ Fin 3) {f : SpaceTime → ℂ}
    (hf : ContDiff ℝ ∞ f) :
    taylorSeries x₀ (∂_ μ f) = pderiv μ (taylorSeries x₀ f)
```

## Depends on

- [Derivatives on SpaceTime](derivatives.md)
- [The spacetime algebra](spacetimealgebra-basic.md)

## Sources

- [Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/TaylorSeries.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/TaylorSeries.lean)
