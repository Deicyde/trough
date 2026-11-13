---
declaration: module
origin: cited
lean: TauCeti.isPositiveDefinite_iff_posSemidef, TauCeti.IsPositiveDefinite.posSemidef_sub, TauCeti.isPositiveDefinite_iff_posSemidef_sub
statement: formalized
proof: formalized
---

# The positive-definite function ↔ positive-definite kernel correspondence

The module `PhyslibAlpha.Mathematics.TauCeti.Analysis.PositiveDefinite.Function.Kernel`, [PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Kernel.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Kernel.lean): 3 declarations, 3 with a docstring.

> A positive-definite function `F : M → ℂ` on an involutive additive monoid and a positive-definite
> kernel `K : M → M → ℂ` are two views of the same data, linked by the assignment `K(a, b) = F(a +
> b⋆)`.

## i. Overview

> A positive-definite function `F : M → ℂ` on an involutive additive monoid and a positive-definite
> kernel `K : M → M → ℂ` are two views of the same data, linked by the assignment
> `K(a, b) = F(a + b⋆)`. This file records the forward and reverse correspondence, packages them
> as an iff, and records the translation-invariant group specialization.
>
> Both sides express nonnegativity of finite quadratic forms; the two-variable kernel is viewed
> directly as a matrix and tested with Mathlib's `Matrix.PosSemidef` predicate.
>
> Under the negation involution `a⋆ = -a` the kernel takes the familiar translation-invariant shape
> `K(a, b) = F(a - b)`, the form in which positive definiteness is usually stated on groups such as
> `ℝᵈ` or a real inner-product space. We record that specialization as a corollary parameterized by
> the hypothesis `star a = -a` (Mathlib pins no such `StarAddMonoid` instance, since `star` is the
> identity on a real vector space, so the negation involution is supplied as a side hypothesis rather
> than an instance).
>
> This advances the `OneParameterSemigroups` roadmap, Part C ("Positive-definite functions and
> Bochner's theorem", `TauCetiRoadmap/OneParameterSemigroups/README.md`): the `API to develop` bullet
> "the PD-function ↔ PD-kernel equivalence (`K(a, b) = F(a + b⋆)`; `F(a − b)` for a group)".
> The function-side predicate `IsPositiveDefinite` lives in Tau Ceti, while the kernel side uses
> Mathlib's `Matrix.PosSemidef`; this file connects them and records the group form. No Mathlib code
> is vendored.

## ii. Key results

> * `TauCeti.isPositiveDefinite_iff_posSemidef`: the equivalence of the two predicates,
>   packaging the two halves.
> * `TauCeti.IsPositiveDefinite.posSemidef_sub` and
>   `TauCeti.isPositiveDefinite_iff_posSemidef_sub`: the subtraction form
>   `K(a, b) = F(a - b)` under the negation involution `star a = -a`.

## iv. References

> * C. Berg, J. P. R. Christensen, P. Ressel, *Harmonic Analysis on Semigroups* (GTM 100, 1984),
>   Chapter 3.

## A. Development

**`TauCeti.isPositiveDefinite_iff_posSemidef`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Kernel.lean#L72).

> A function `F` on an involutive additive monoid is positive definite if and only if the
> two-variable kernel `K(a, b) = F(a + b⋆)` is positive definite.

```lean
lemma isPositiveDefinite_iff_posSemidef :
    IsPositiveDefinite F ↔ Matrix.PosSemidef (fun a b => F (a + star b))
```

**`TauCeti.IsPositiveDefinite.posSemidef_sub`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Kernel.lean#L83).

> Under the negation involution `a⋆ = -a`, a positive-definite function `F` gives the
> translation-invariant positive-definite kernel `K(a, b) = F(a - b)`. This is the form in which
> positive definiteness is usually stated on groups such as `ℝᵈ` or a real inner-product space.

```lean
lemma posSemidef_sub (hstar : ∀ a : G, star a = -a) (hF : IsPositiveDefinite F) :
    Matrix.PosSemidef (fun a b => F (a - b))
```

**`TauCeti.isPositiveDefinite_iff_posSemidef_sub`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Kernel.lean#L97).

> Under the negation involution `a⋆ = -a`, `F` is positive definite if and only if the
> translation-invariant kernel `K(a, b) = F(a - b)` is positive definite.

```lean
lemma isPositiveDefinite_iff_posSemidef_sub (hstar : ∀ a : G, star a = -a) :
    IsPositiveDefinite F ↔ Matrix.PosSemidef (fun a b => F (a - b))
```

## Depends on

- [Positive-definite functions on an involutive additive monoid](../part-01/analysis-positivedefinite-basic.md)

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Kernel.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Function/Kernel.lean)
