---
declaration: module
origin: cited
lean: TauCeti.IsPositiveDefinite.norm_sub_sq_le_two_mul_map_zero_re_mul_re_sub_of_add_star_eq_zero, TauCeti.IsPositiveDefinite.norm_sub_sq_le_two_mul_map_zero_re_mul_norm_sub_of_add_star_eq_zero, TauCeti.IsPositiveDefinite.norm_sub_sq_le_two_mul_map_zero_re_mul_re_sub_of_star_eq_neg, TauCeti.IsPositiveDefinite.norm_sub_sq_le_two_mul_map_zero_re_mul_re_sub_of_forall_star_eq_neg, TauCeti.IsPositiveDefinite.norm_sub_sq_le_two_mul_map_zero_re_mul_norm_sub_of_star_eq_neg, TauCeti.IsPositiveDefinite.norm_sub_sq_le_two_mul_map_zero_re_mul_norm_sub_of_forall_star_eq_neg, TauCeti.IsPositiveDefinite.uniformContinuous_of_continuousAt_zero_of_forall_star_eq_neg
statement: formalized
proof: formalized
---

# Continuity of positive-definite functions

The module `PhyslibAlpha.Mathematics.TauCeti.Analysis.PositiveDefinite.Continuity`, [PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Continuity.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Continuity.lean): 7 declarations, 7 with a docstring; 5 private, not shown.

> This file records the standard continuity upgrade for positive-definite functions on a seminormed
> additive group with the negation involution.

## i. Overview

> This file records the standard continuity upgrade for positive-definite functions on a seminormed
> additive group with the negation involution. A positive-definite function that is continuous at
> the origin is uniformly continuous. The file also records the local estimates
> `‖F x - F y‖² ≤ 2 F(0).re ((F 0).re - (F (x + star y)).re)` and
> `‖F x - F y‖² ≤ 2 F(0).re ‖F (x + star y) - F 0‖` at points satisfying
> `x + star x = 0` and `y + star y = 0`, together with their specializations to additive groups
> whose involution is negation.
>
> This advances Part C of the `OneParameterSemigroups` roadmap, whose positive-definite-function
> API asks for the basic fact "continuity at `0` ⇒ uniform continuity" before Bochner's theorem.

## ii. Key results

> In the namespace `TauCeti.IsPositiveDefinite`:
>
> * `norm_sub_sq_le_two_mul_map_zero_re_mul_re_sub_of_star_eq_neg`:
>   the local real-part continuity estimate.
> * `norm_sub_sq_le_two_mul_map_zero_re_mul_re_sub_of_add_star_eq_zero`:
>   the monoid-level local real-part continuity estimate.
> * `norm_sub_sq_le_two_mul_map_zero_re_mul_norm_sub_of_star_eq_neg`:
>   the local norm-valued continuity estimate.
> * `norm_sub_sq_le_two_mul_map_zero_re_mul_norm_sub_of_add_star_eq_zero`:
>   the monoid-level local norm-valued continuity estimate.
> * `norm_sub_sq_le_two_mul_map_zero_re_mul_re_sub_of_forall_star_eq_neg` and
>   `norm_sub_sq_le_two_mul_map_zero_re_mul_norm_sub_of_forall_star_eq_neg`:
>   specializations to a globally negating involution.
> * `uniformContinuous_of_continuousAt_zero_of_forall_star_eq_neg`:
>   continuity at `0` implies uniform continuity.

## iv. References

> * C. Berg, J. P. R. Christensen, P. Ressel, *Harmonic Analysis on Semigroups* (GTM 100, 1984),
>   Chapter 3.

## A. Development

**`TauCeti.IsPositiveDefinite.norm_sub_sq_le_two_mul_map_zero_re_mul_re_sub_of_add_star_eq_zero`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Continuity.lean#L161).

> The local monoid-level real-part form of the standard positive-definite continuity estimate.

```lean
lemma norm_sub_sq_le_two_mul_map_zero_re_mul_re_sub_of_add_star_eq_zero
    (hF : IsPositiveDefinite F) {x y : E} (hx : x + star x = 0) (hy : y + star y = 0) :
    ‖F x - F y‖ ^ 2
      ≤ 2 * (F 0).re * ((F 0).re - (F (x + star y)).re)
```

**`TauCeti.IsPositiveDefinite.norm_sub_sq_le_two_mul_map_zero_re_mul_norm_sub_of_add_star_eq_zero`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Continuity.lean#L197).

> The local monoid-level norm-valued form of the standard positive-definite continuity
> estimate.

```lean
lemma norm_sub_sq_le_two_mul_map_zero_re_mul_norm_sub_of_add_star_eq_zero
    (hF : IsPositiveDefinite F) {x y : E} (hx : x + star x = 0) (hy : y + star y = 0) :
    ‖F x - F y‖ ^ 2 ≤ 2 * (F 0).re * ‖F (x + star y) - F 0‖
```

**`TauCeti.IsPositiveDefinite.norm_sub_sq_le_two_mul_map_zero_re_mul_re_sub_of_star_eq_neg`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Continuity.lean#L217).

> The local real-part form of the standard positive-definite continuity estimate.

```lean
lemma norm_sub_sq_le_two_mul_map_zero_re_mul_re_sub_of_star_eq_neg (hF : IsPositiveDefinite F)
    {x y : E} (hx : star x = -x) (hy : star y = -y) :
    ‖F x - F y‖ ^ 2
      ≤ 2 * (F 0).re * ((F 0).re - (F (x - y)).re)
```

**`TauCeti.IsPositiveDefinite.norm_sub_sq_le_two_mul_map_zero_re_mul_re_sub_of_forall_star_eq_neg`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Continuity.lean#L228).

> The real-part form of the standard positive-definite continuity estimate under a globally
> negating involution.

```lean
lemma norm_sub_sq_le_two_mul_map_zero_re_mul_re_sub_of_forall_star_eq_neg
    (hF : IsPositiveDefinite F) (hstar : ∀ x : E, star x = -x) (x y : E) :
    ‖F x - F y‖ ^ 2
      ≤ 2 * (F 0).re * ((F 0).re - (F (x - y)).re)
```

**`TauCeti.IsPositiveDefinite.norm_sub_sq_le_two_mul_map_zero_re_mul_norm_sub_of_star_eq_neg`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Continuity.lean#L235).

> The local norm-valued form of the standard positive-definite continuity estimate.

```lean
lemma norm_sub_sq_le_two_mul_map_zero_re_mul_norm_sub_of_star_eq_neg (hF : IsPositiveDefinite F)
    {x y : E} (hx : star x = -x) (hy : star y = -y) :
    ‖F x - F y‖ ^ 2 ≤ 2 * (F 0).re * ‖F (x - y) - F 0‖
```

**`TauCeti.IsPositiveDefinite.norm_sub_sq_le_two_mul_map_zero_re_mul_norm_sub_of_forall_star_eq_neg`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Continuity.lean#L245).

> The norm-valued form of the standard positive-definite continuity estimate under a globally
> negating involution.

```lean
lemma norm_sub_sq_le_two_mul_map_zero_re_mul_norm_sub_of_forall_star_eq_neg
    (hF : IsPositiveDefinite F) (hstar : ∀ x : E, star x = -x) (x y : E) :
    ‖F x - F y‖ ^ 2 ≤ 2 * (F 0).re * ‖F (x - y) - F 0‖
```

**`TauCeti.IsPositiveDefinite.uniformContinuous_of_continuousAt_zero_of_forall_star_eq_neg`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Continuity.lean#L258).

> A positive-definite function on a seminormed additive group with the negation involution is
> uniformly continuous as soon as it is continuous at the origin.

```lean
lemma uniformContinuous_of_continuousAt_zero_of_forall_star_eq_neg (hF : IsPositiveDefinite F)
    (hstar : ∀ x : E, star x = -x) (hcont : ContinuousAt F 0) :
    UniformContinuous F
```

## Depends on

- [Positive-definite functions on an involutive additive monoid](analysis-positivedefinite-basic.md)

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Continuity.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Continuity.lean)
