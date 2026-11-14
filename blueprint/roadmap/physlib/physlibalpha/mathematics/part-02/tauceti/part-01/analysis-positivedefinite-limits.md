---
declaration: module
origin: cited
lean: TauCeti.IsPositiveDefinite.of_tendsto, TauCeti.IsPositiveDefinite.of_forall_tendsto, TauCeti.IsPositiveDefinite.of_seq_tendsto, TauCeti.IsPositiveDefinite.of_tendstoLocallyUniformly
statement: formalized
proof: formalized
---

# Limits of positive-definite functions

The module `PhyslibAlpha.Mathematics.TauCeti.Analysis.PositiveDefinite.Limits`, [PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Limits.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Limits.lean): 4 declarations, 4 with a docstring.

> This file derives pointwise- and locally-uniform-limit closure for `TauCeti.IsPositiveDefinite`, the
> positive-definite function predicate on an involutive additive monoid, from Mathlib's closedness
> theorem for the cone of positive-semidefinite matrices.

## i. Overview

> This file derives pointwise- and locally-uniform-limit closure for
> `TauCeti.IsPositiveDefinite`, the positive-definite function predicate on an involutive additive
> monoid, from Mathlib's closedness theorem for the cone of positive-semidefinite matrices.
>
> This is the limit-closure item from Part C of the `OneParameterSemigroups` roadmap. The result is
> about positive-definiteness alone for pointwise limits; as the roadmap notes, continuity needs an
> additional hypothesis. Mathlib's `TendstoLocallyUniformly.continuous` provides continuity of a
> locally uniform limit when the approximating functions are frequently continuous, while this file
> provides the positive-definiteness conclusion.

## ii. Key results

> * `TauCeti.IsPositiveDefinite.of_tendsto`: filter-level pointwise-limit closure for
>   positive-definite functions.
> * `TauCeti.IsPositiveDefinite.of_forall_tendsto`: the same result when every function in the
>   family is positive definite.
> * `TauCeti.IsPositiveDefinite.of_seq_tendsto`: the sequential `atTop` specialization.
> * `TauCeti.IsPositiveDefinite.of_tendstoLocallyUniformly`: locally uniform limits of eventually
>   positive-definite functions are positive definite.

## iv. References

> * C. Berg, J. P. R. Christensen, P. Ressel, *Harmonic Analysis on Semigroups* (GTM 100, 1984),
>   Chapter 3.

## A. Development

**`TauCeti.IsPositiveDefinite.of_tendsto`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Limits.lean#L67).

> Positive-definiteness is preserved under pointwise limits along a nontrivial filter. The
> hypothesis on positive-definiteness is eventual, so this applies equally to nets that are
> eventually positive definite.

```lean
lemma of_tendsto {ι : Type*} {l : Filter ι} [NeBot l] {F : ι → M → ℂ} {G : M → ℂ}
    (hF : ∀ᶠ i in l, IsPositiveDefinite (F i))
    (hlim : ∀ x : M, Tendsto (fun i => F i x) l (𝓝 (G x))) :
    IsPositiveDefinite G
```

**`TauCeti.IsPositiveDefinite.of_forall_tendsto`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Limits.lean#L78).

> A pointwise limit of a family of positive-definite functions is positive definite. This is the
> non-eventual form of `TauCeti.IsPositiveDefinite.of_tendsto`.

```lean
lemma of_forall_tendsto {ι : Type*} {l : Filter ι} [NeBot l] {F : ι → M → ℂ} {G : M → ℂ}
    (hF : ∀ i, IsPositiveDefinite (F i)) (hlim : ∀ x : M, Tendsto (fun i => F i x) l (𝓝 (G x))) :
    IsPositiveDefinite G
```

**`TauCeti.IsPositiveDefinite.of_seq_tendsto`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Limits.lean#L84).

> Sequential pointwise limits of eventually positive-definite functions are positive definite.

```lean
lemma of_seq_tendsto {F : ℕ → M → ℂ} {G : M → ℂ} (hF : ∀ᶠ n in atTop, IsPositiveDefinite (F n))
    (hlim : ∀ x : M, Tendsto (fun n => F n x) atTop (𝓝 (G x))) :
    IsPositiveDefinite G
```

**`TauCeti.IsPositiveDefinite.of_tendstoLocallyUniformly`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Limits.lean#L96).

> A locally uniform limit of eventually positive-definite functions is positive definite.
>
> Unlike continuity, positive-definiteness itself only needs pointwise convergence; local uniform
> convergence is converted to pointwise convergence before applying
> `TauCeti.IsPositiveDefinite.of_tendsto`.

```lean
lemma of_tendstoLocallyUniformly {ι : Type*} {l : Filter ι} [NeBot l] {F : ι → M → ℂ} {G : M → ℂ}
    (hF : ∀ᶠ i in l, IsPositiveDefinite (F i)) (hlim : TendstoLocallyUniformly F G l) :
    IsPositiveDefinite G
```

## Depends on

- [Positive-definite functions on an involutive additive monoid](analysis-positivedefinite-basic.md)

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Limits.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Limits.lean)
