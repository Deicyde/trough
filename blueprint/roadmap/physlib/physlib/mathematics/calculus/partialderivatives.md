---
declaration: module
origin: cited
lean: fderiv_partial_snd, fderiv_partial_thd, fderiv_apply_zero_prod, deriv_fderiv_apply_comm
statement: formalized
proof: formalized
---

# Partial derivatives on products

The module `Physlib.Mathematics.Calculus.PartialDerivatives`, [Physlib/Mathematics/Calculus/PartialDerivatives.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/PartialDerivatives.lean): 4 declarations, 4 with a docstring.

> Splitting derivatives of functions on `X × Y × Z` and of families `H : ℝ × ℝ → F`.

## i. Overview

> The derivative of `f (a, y, z)` splits into partial derivatives, and mixed derivatives of `H (s, τ)`
> commute.

## ii. Key results

> - `fderiv_apply_zero_prod`: splitting of the derivative of `f (a, y, z)`
> - `deriv_fderiv_apply_comm`: commutation of mixed derivatives of `H (s, τ)`

## iv. References

> * None.

## A. Functions on a triple product

**`fderiv_partial_snd`**, a lemma, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/PartialDerivatives.lean#L49).

> The derivative in the middle argument of `f` as a restriction of the total derivative.

```lean
lemma fderiv_partial_snd {f : X × Y × Z → F} {a : X} {y : Y} {z : Z}
    (hf : DifferentiableAt ℝ f (a, y, z)) :
    fderiv ℝ (fun y' ↦ f (a, y', z)) y = (fderiv ℝ f (a, y, z)).comp
      ((0 : Y →L[ℝ] X).prod ((ContinuousLinearMap.id ℝ Y).prod (0 : Y →L[ℝ] Z)))
```

**`fderiv_partial_thd`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/PartialDerivatives.lean#L57).

> The derivative in the last argument of `f` as a restriction of the total derivative.

```lean
lemma fderiv_partial_thd {f : X × Y × Z → F} {a : X} {y : Y} {z : Z}
    (hf : DifferentiableAt ℝ f (a, y, z)) :
    fderiv ℝ (fun z' ↦ f (a, y, z')) z = (fderiv ℝ f (a, y, z)).comp
      ((0 : Z →L[ℝ] X).prod ((0 : Z →L[ℝ] Y).prod (ContinuousLinearMap.id ℝ Z)))
```

**`fderiv_apply_zero_prod`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/PartialDerivatives.lean#L65).

> The total derivative of `f` on `(0, u, w)` splits into its middle and last partials.

```lean
lemma fderiv_apply_zero_prod {f : X × Y × Z → F} {a : X} {y : Y} {z : Z}
    (hf : DifferentiableAt ℝ f (a, y, z)) (u : Y) (w : Z) :
    fderiv ℝ f (a, y, z) (0, u, w) =
      fderiv ℝ (fun y' ↦ f (a, y', z)) y u + fderiv ℝ (fun z' ↦ f (a, y, z')) z w
```

## B. Two-parameter families

**`deriv_fderiv_apply_comm`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/PartialDerivatives.lean#L81).

> Mixed partial derivatives of a two-parameter family, `C²` at the point, commute.

```lean
lemma deriv_fderiv_apply_comm {s τ : ℝ} (hH : ContDiffAt ℝ 2 H (s, τ)) :
    deriv (fun σ ↦ fderiv ℝ H (s, σ) (1, 0)) τ =
      fderiv ℝ (fun p ↦ fderiv ℝ H p (0, 1)) (s, τ) (1, 0)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/Calculus/PartialDerivatives.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/PartialDerivatives.lean)
