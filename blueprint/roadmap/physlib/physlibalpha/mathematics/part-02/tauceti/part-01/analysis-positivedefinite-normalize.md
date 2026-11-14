---
declaration: module
origin: cited
lean: TauCeti.IsPositiveDefinite.normalize, TauCeti.IsPositiveDefinite.normalize_apply_zero, TauCeti.IsPositiveDefinite.norm_normalize_apply_le_one_of_add_star_eq_zero, TauCeti.IsPositiveDefinite.norm_normalize_apply_le_one_of_star_eq_neg, TauCeti.IsPositiveDefinite.norm_normalize_apply_le_one_of_forall_star_eq_neg
statement: formalized
proof: formalized
---

# Normalizing positive-definite functions

The module `PhyslibAlpha.Mathematics.TauCeti.Analysis.PositiveDefinite.Normalize`, [PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Normalize.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Normalize.lean): 5 declarations, 5 with a docstring; 1 private, not shown.

> This file records the standard normalization step for positive-definite functions: if `F : M → ℂ` is
> positive definite and `F 0 ≠ 0`, then multiplying by the reciprocal of the nonnegative real number
> `(F 0).re` gives a positive-definite function whose value at the origin is `1`.

## i. Overview

> This file records the standard normalization step for positive-definite functions: if
> `F : M → ℂ` is positive definite and `F 0 ≠ 0`, then multiplying by the reciprocal of the
> nonnegative real number `(F 0).re` gives a positive-definite function whose value at the origin
> is `1`.
>
> This is part of the normalization API requested in Part C of the `OneParameterSemigroups`
> roadmap ("Positive-definite functions and Bochner's theorem"). Normalized positive-definite
> functions are the convenient form for characteristic functions and for the later Bochner and
> GNS/Kolmogorov constructions: after normalization, the general bound `‖F a‖ ≤ (F 0).re` becomes
> the familiar `‖F a‖ ≤ 1`.
>
> The file deliberately keeps the hypotheses unbundled. It proves lemmas about the explicit
> normalized function rather than introducing a new bundled predicate.

## ii. Key results

> * `TauCeti.IsPositiveDefinite.normalize`: multiplying by `((F 0).re)⁻¹` preserves
>   positive-definiteness.
> * `TauCeti.IsPositiveDefinite.normalize_apply_zero`: the normalized function has value `1` at
>   the origin.
> * `TauCeti.IsPositiveDefinite.norm_normalize_apply_le_one_of_add_star_eq_zero` and
>   `TauCeti.IsPositiveDefinite.norm_normalize_apply_le_one_of_star_eq_neg`: normalized functions
>   are bounded by `1` on the usual group-like points.

## iv. References

> * C. Berg, J. P. R. Christensen, P. Ressel, *Harmonic Analysis on Semigroups* (GTM 100, 1984),
>   Chapter 3.

## A. Development

**`TauCeti.IsPositiveDefinite.normalize`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Normalize.lean#L73).

> Multiplying a positive-definite function by the reciprocal of its real value at the origin
> preserves positive-definiteness. If `F 0 = 0` this gives the zero scaling; the separate
> `normalize_apply_zero` lemma below records the useful nonzero case.

```lean
lemma normalize (hF : IsPositiveDefinite F) :
    IsPositiveDefinite (fun x => (((F 0).re)⁻¹ : ℂ) * F x)
```

**`TauCeti.IsPositiveDefinite.normalize_apply_zero`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Normalize.lean#L79).

> The normalized positive-definite function has value `1` at the origin.

```lean
lemma normalize_apply_zero (hF : IsPositiveDefinite F) (h0 : F 0 ≠ 0) :
    (((F 0).re)⁻¹ : ℂ) * F 0 = 1
```

**`TauCeti.IsPositiveDefinite.norm_normalize_apply_le_one_of_add_star_eq_zero`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Normalize.lean#L88).

> At points satisfying `a + star a = 0`, the normalized positive-definite function is bounded
> by `1`. When `F 0 = 0` the normalizing scalar is `0`, so the bound holds trivially.

```lean
lemma norm_normalize_apply_le_one_of_add_star_eq_zero (hF : IsPositiveDefinite F)
    (a : M) (ha : a + star a = 0) :
    ‖(((F 0).re)⁻¹ : ℂ) * F a‖ ≤ 1
```

**`TauCeti.IsPositiveDefinite.norm_normalize_apply_le_one_of_star_eq_neg`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Normalize.lean#L108).

> Under the negation involution, the normalized positive-definite function is bounded by `1` at
> every point.

```lean
lemma norm_normalize_apply_le_one_of_star_eq_neg (hH : IsPositiveDefinite H)
    (a : G) (hstar_a : star a = -a) :
    ‖(((H 0).re)⁻¹ : ℂ) * H a‖ ≤ 1
```

**`TauCeti.IsPositiveDefinite.norm_normalize_apply_le_one_of_forall_star_eq_neg`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Normalize.lean#L115).

> If the involution is negation everywhere, the normalized positive-definite function is
> uniformly bounded by `1`.

```lean
lemma norm_normalize_apply_le_one_of_forall_star_eq_neg (hH : IsPositiveDefinite H)
    (hstar : ∀ a : G, star a = -a) (a : G) :
    ‖(((H 0).re)⁻¹ : ℂ) * H a‖ ≤ 1
```

## Depends on

- [Positive-definite functions on an involutive additive monoid](analysis-positivedefinite-basic.md)

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Normalize.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Normalize.lean)
