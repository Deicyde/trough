---
declaration: module
origin: cited
lean: TauCeti.IsPositiveDefinite.real_smul, TauCeti.IsPositiveDefinite.sum_smul, TauCeti.IsPositiveDefinite.sum_const_mul, TauCeti.IsPositiveDefinite.sum_real_smul, TauCeti.IsPositiveDefinite.sum_real_const_mul, TauCeti.IsPositiveDefinite.pow, TauCeti.IsPositiveDefinite.sum_smul_apply_of_apply_eq_one, TauCeti.IsPositiveDefinite.sum_smul_apply_eq_one
statement: formalized
proof: formalized
---

# Weighted closure for positive-definite functions

The module `PhyslibAlpha.Mathematics.TauCeti.Analysis.PositiveDefinite.Function.Closure`, [PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Closure.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Closure.lean): 22 declarations, 22 with a docstring.

> This file adds the weighted finite-mixture and Schur-power API for `TauCeti.IsPositiveDefinite`, the
> positive-definite-function predicate on an involutive additive monoid.

## i. Overview

> This file adds the weighted finite-mixture and Schur-power API for
> `TauCeti.IsPositiveDefinite`, the positive-definite-function predicate on an involutive additive
> monoid. The basic file already proves binary sums, nonnegative complex scalar multiples, pointwise
> products, and unweighted finite sums/products. Here we package the forms used by examples and
> finite approximations: finite nonnegative weighted sums, real-weighted variants, and powers. The
> weighted sum API is available in scalar (`•`) notation.
>
> This advances `TauCetiRoadmap/OneParameterSemigroups/README.md`, Part C, the positive-definite
> functions API asking for closure under sums and products before the Bochner and BCR representation
> milestones. No external formalization is vendored.

## ii. Key results

> * `TauCeti.IsPositiveDefinite.real_smul`: nonnegative real scalar multiplication.
> * `TauCeti.IsPositiveDefinite.sum_smul`: finite nonnegative weighted sums.
> * `TauCeti.IsPositiveDefinite.sum_real_smul`: finite nonnegative real-weighted sums.
> * `TauCeti.IsPositiveDefinite.pow`: Schur powers of a positive-definite function.
> * `TauCeti.IsPositiveDefinite.sum_smul_apply_zero_of_apply_zero_eq_one`: normalized finite
>   mixtures evaluate at the origin as the sum of their weights.

## iv. References

> * C. Berg, J. P. R. Christensen, P. Ressel, *Harmonic Analysis on Semigroups* (GTM 100, 1984),
>   Chapter 3.

## A. Development

**`TauCeti.IsPositiveDefinite.real_smul`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Closure.lean#L61).

> Positive-definite functions are closed under multiplication by a nonnegative real scalar.

```lean
lemma real_smul {r : ℝ} {F : M → ℂ} (hr : 0 ≤ r) (hF : IsPositiveDefinite F) :
    IsPositiveDefinite (fun x => r • F x)
```

**`TauCeti.IsPositiveDefinite.sum_smul`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Closure.lean#L68).

> Finite nonnegative complex-weighted sums of positive-definite functions are positive
> definite. This is the finite-mixture form used when the weights are already complex scalars with
> nonnegative real value.

```lean
lemma sum_smul {ι : Type*} {s : Finset ι} {w : ι → ℂ} {F : ι → M → ℂ}
    (hw : ∀ i ∈ s, 0 ≤ w i) (hF : ∀ i ∈ s, IsPositiveDefinite (F i)) :
    IsPositiveDefinite (fun x => ∑ i ∈ s, w i • F i x)
```

**`TauCeti.IsPositiveDefinite.sum_const_mul`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Closure.lean#L76).

> Finite nonnegative complex-weighted sums, written using multiplication rather than scalar
> notation.

```lean
lemma sum_const_mul {ι : Type*} {s : Finset ι} {w : ι → ℂ} {F : ι → M → ℂ}
    (hw : ∀ i ∈ s, 0 ≤ w i) (hF : ∀ i ∈ s, IsPositiveDefinite (F i)) :
    IsPositiveDefinite (fun x => ∑ i ∈ s, w i * F i x)
```

**`TauCeti.IsPositiveDefinite.sum_real_smul`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Closure.lean#L82).

> Finite nonnegative real-weighted sums of positive-definite functions are positive definite.

```lean
lemma sum_real_smul {ι : Type*} {s : Finset ι} {w : ι → ℝ} {F : ι → M → ℂ}
    (hw : ∀ i ∈ s, 0 ≤ w i) (hF : ∀ i ∈ s, IsPositiveDefinite (F i)) :
    IsPositiveDefinite (fun x => ∑ i ∈ s, w i • F i x)
```

**`TauCeti.IsPositiveDefinite.sum_real_const_mul`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Closure.lean#L89).

> Finite nonnegative real-weighted sums, written with the real weight coerced to `ℂ` and
> multiplied in the codomain.

```lean
lemma sum_real_const_mul {ι : Type*} {s : Finset ι} {w : ι → ℝ} {F : ι → M → ℂ}
    (hw : ∀ i ∈ s, 0 ≤ w i) (hF : ∀ i ∈ s, IsPositiveDefinite (F i)) :
    IsPositiveDefinite (fun x => ∑ i ∈ s, (w i : ℂ) * F i x)
```

**`TauCeti.IsPositiveDefinite.pow`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Closure.lean#L95).

> Schur powers of a positive-definite function are positive definite.

```lean
lemma pow {F : M → ℂ} (hF : IsPositiveDefinite F) (n : ℕ) :
    IsPositiveDefinite (fun x => F x ^ n)
```

**`TauCeti.IsPositiveDefinite.sum_smul_apply_of_apply_eq_one`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Closure.lean#L105).

> If each summand in a finite complex-weighted sum is normalized at a point, then the sum's
> value at that point is the sum of the weights.

```lean
lemma sum_smul_apply_of_apply_eq_one {ι : Type*} {s : Finset ι} {w : ι → ℂ}
    {F : ι → N → ℂ} {x : N} (hFx : ∀ i ∈ s, F i x = 1) : (∑ i ∈ s, w i • F i x) = ∑ i ∈ s, w i
```

**`TauCeti.IsPositiveDefinite.sum_smul_apply_eq_one`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Closure.lean#L113).

> A finite complex-weighted sum of functions normalized at a point is normalized at that point
> when the weights sum to `1`.

```lean
lemma sum_smul_apply_eq_one {ι : Type*} {s : Finset ι} {w : ι → ℂ}
    {F : ι → N → ℂ} {x : N} (hFx : ∀ i ∈ s, F i x = 1) (hw_sum : ∑ i ∈ s, w i = 1) :
    (fun y => ∑ i ∈ s, w i • F i y) x = 1
```

**`TauCeti.IsPositiveDefinite.sum_const_mul_apply_of_apply_eq_one`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Closure.lean#L121).

> If each summand in a finite complex-weighted sum is normalized at a point, then the sum's
> multiplication-form value at that point is the sum of the weights.

```lean
lemma sum_const_mul_apply_of_apply_eq_one {ι : Type*} {s : Finset ι} {w : ι → ℂ}
    {F : ι → N → ℂ} {x : N} (hFx : ∀ i ∈ s, F i x = 1) : (∑ i ∈ s, w i * F i x) = ∑ i ∈ s, w i
```

**`TauCeti.IsPositiveDefinite.sum_const_mul_apply_eq_one`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Closure.lean#L128).

> A finite complex-weighted sum, in multiplication form, of functions normalized at a point is
> normalized at that point when the weights sum to `1`.

```lean
lemma sum_const_mul_apply_eq_one {ι : Type*} {s : Finset ι} {w : ι → ℂ}
    {F : ι → N → ℂ} {x : N} (hFx : ∀ i ∈ s, F i x = 1) (hw_sum : ∑ i ∈ s, w i = 1) :
    (fun y => ∑ i ∈ s, w i * F i y) x = 1
```

**`TauCeti.IsPositiveDefinite.sum_real_smul_apply_of_apply_eq_one`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Closure.lean#L136).

> If each summand in a finite real-weighted sum is normalized at a point, then the sum's value at
> that point is the complex coercion of the sum of the real weights.

```lean
lemma sum_real_smul_apply_of_apply_eq_one {ι : Type*} {s : Finset ι} {w : ι → ℝ}
    {F : ι → N → ℂ} {x : N} (hFx : ∀ i ∈ s, F i x = 1) :
    (∑ i ∈ s, w i • F i x) = ((∑ i ∈ s, w i : ℝ) : ℂ)
```

**`TauCeti.IsPositiveDefinite.sum_real_smul_apply_eq_one`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Closure.lean#L144).

> A finite real-weighted sum of functions normalized at a point is normalized at that point when
> the weights sum to `1`.

```lean
lemma sum_real_smul_apply_eq_one {ι : Type*} {s : Finset ι} {w : ι → ℝ}
    {F : ι → N → ℂ} {x : N} (hFx : ∀ i ∈ s, F i x = 1) (hw_sum : ∑ i ∈ s, w i = 1) :
    (fun y => ∑ i ∈ s, w i • F i y) x = 1
```

**`TauCeti.IsPositiveDefinite.sum_real_const_mul_apply_of_apply_eq_one`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Closure.lean#L152).

> If each summand in a finite real-weighted sum is normalized at a point, then the sum's
> multiplication-form value at that point is the complex coercion of the sum of the real weights.

```lean
lemma sum_real_const_mul_apply_of_apply_eq_one {ι : Type*} {s : Finset ι}
    {w : ι → ℝ} {F : ι → N → ℂ} {x : N} (hFx : ∀ i ∈ s, F i x = 1) :
    (∑ i ∈ s, (w i : ℂ) * F i x) = ((∑ i ∈ s, w i : ℝ) : ℂ)
```

**`TauCeti.IsPositiveDefinite.sum_real_const_mul_apply_eq_one`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Closure.lean#L160).

> A finite real-weighted sum, in multiplication form, of functions normalized at a point is
> normalized at that point when the weights sum to `1`.

```lean
lemma sum_real_const_mul_apply_eq_one {ι : Type*} {s : Finset ι} {w : ι → ℝ}
    {F : ι → N → ℂ} {x : N} (hFx : ∀ i ∈ s, F i x = 1) (hw_sum : ∑ i ∈ s, w i = 1) :
    (fun y => ∑ i ∈ s, (w i : ℂ) * F i y) x = 1
```

**`TauCeti.IsPositiveDefinite.sum_smul_apply_zero_of_apply_zero_eq_one`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Closure.lean#L172).

> If each summand in a finite complex-weighted sum is normalized at the origin, then the sum's
> value at the origin is the sum of the weights.

```lean
lemma sum_smul_apply_zero_of_apply_zero_eq_one {ι : Type*} {s : Finset ι}
    {w : ι → ℂ} {F : ι → N → ℂ} (hF0 : ∀ i ∈ s, F i 0 = 1) :
    (∑ i ∈ s, w i • F i 0) = ∑ i ∈ s, w i
```

**`TauCeti.IsPositiveDefinite.sum_smul_apply_zero_eq_one`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Closure.lean#L179).

> A finite complex-weighted sum of functions normalized at the origin is normalized when the
> weights sum to `1`.

```lean
lemma sum_smul_apply_zero_eq_one {ι : Type*} {s : Finset ι} {w : ι → ℂ}
    {F : ι → N → ℂ} (hF0 : ∀ i ∈ s, F i 0 = 1) (hw_sum : ∑ i ∈ s, w i = 1) :
    (fun x => ∑ i ∈ s, w i • F i x) 0 = 1
```

**`TauCeti.IsPositiveDefinite.sum_const_mul_apply_zero_of_apply_zero_eq_one`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Closure.lean#L186).

> If each summand in a finite complex-weighted sum is normalized at the origin, then the
> sum's multiplication-form value at the origin is the sum of the weights.

```lean
lemma sum_const_mul_apply_zero_of_apply_zero_eq_one {ι : Type*} {s : Finset ι}
    {w : ι → ℂ} {F : ι → N → ℂ} (hF0 : ∀ i ∈ s, F i 0 = 1) :
    (∑ i ∈ s, w i * F i 0) = ∑ i ∈ s, w i
```

**`TauCeti.IsPositiveDefinite.sum_const_mul_apply_zero_eq_one`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Closure.lean#L193).

> A finite complex-weighted sum, in multiplication form, of functions normalized at the origin is
> normalized when the weights sum to `1`.

```lean
lemma sum_const_mul_apply_zero_eq_one {ι : Type*} {s : Finset ι} {w : ι → ℂ}
    {F : ι → N → ℂ} (hF0 : ∀ i ∈ s, F i 0 = 1) (hw_sum : ∑ i ∈ s, w i = 1) :
    (fun x => ∑ i ∈ s, w i * F i x) 0 = 1
```

**`TauCeti.IsPositiveDefinite.sum_real_smul_apply_zero_of_apply_zero_eq_one`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Closure.lean#L200).

> If each summand in a finite real-weighted sum is normalized at the origin, then the sum's value
> at the origin is the complex coercion of the sum of the real weights.

```lean
lemma sum_real_smul_apply_zero_of_apply_zero_eq_one {ι : Type*} {s : Finset ι}
    {w : ι → ℝ} {F : ι → N → ℂ} (hF0 : ∀ i ∈ s, F i 0 = 1) :
    (∑ i ∈ s, w i • F i 0) = ((∑ i ∈ s, w i : ℝ) : ℂ)
```

**`TauCeti.IsPositiveDefinite.sum_real_smul_apply_zero_eq_one`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Closure.lean#L207).

> A finite real-weighted sum of functions normalized at the origin is normalized when the weights
> sum to `1`.

```lean
lemma sum_real_smul_apply_zero_eq_one {ι : Type*} {s : Finset ι} {w : ι → ℝ}
    {F : ι → N → ℂ} (hF0 : ∀ i ∈ s, F i 0 = 1) (hw_sum : ∑ i ∈ s, w i = 1) :
    (fun x => ∑ i ∈ s, w i • F i x) 0 = 1
```

**`TauCeti.IsPositiveDefinite.sum_real_const_mul_apply_zero_of_apply_zero_eq_one`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Closure.lean#L214).

> If each summand in a finite real-weighted sum is normalized at the origin, then the sum's
> multiplication-form value at the origin is the complex coercion of the sum of the real weights.

```lean
lemma sum_real_const_mul_apply_zero_of_apply_zero_eq_one {ι : Type*} {s : Finset ι}
    {w : ι → ℝ} {F : ι → N → ℂ} (hF0 : ∀ i ∈ s, F i 0 = 1) :
    (∑ i ∈ s, (w i : ℂ) * F i 0) = ((∑ i ∈ s, w i : ℝ) : ℂ)
```

**`TauCeti.IsPositiveDefinite.sum_real_const_mul_apply_zero_eq_one`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Closure.lean#L221).

> A finite real-weighted sum, in multiplication form, of functions normalized at the origin is
> normalized when the weights sum to `1`.

```lean
lemma sum_real_const_mul_apply_zero_eq_one {ι : Type*} {s : Finset ι} {w : ι → ℝ}
    {F : ι → N → ℂ} (hF0 : ∀ i ∈ s, F i 0 = 1) (hw_sum : ∑ i ∈ s, w i = 1) :
    (fun x => ∑ i ∈ s, (w i : ℂ) * F i x) 0 = 1
```

## Depends on

- [Positive-definite functions on an involutive additive monoid](../part-01/analysis-positivedefinite-basic.md)

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Closure.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Closure.lean)
