---
declaration: module
origin: cited
lean: Space.iteratedDeriv, Space.iteratedDeriv_zero, Space.iteratedDeriv_increment_zero, Space.iteratedDeriv_single, Space.iteratedDeriv_add, Space.iteratedDeriv_const_smul, Space.iteratedDeriv_contDiff, Space.tsupport_deriv_subset
statement: formalized
proof: formalized
---

# Iterated derivatives on `Space d`

The module `Physlib.SpaceAndTime.Space.Derivatives.Iterated`, [Physlib/SpaceAndTime/Space/Derivatives/Iterated.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Iterated.lean): 11 declarations, 6 with a docstring; 5 private, not shown.

## i. Overview

> This module defines iterated coordinate derivatives on `Space d` indexed by multi-indices.
>
> The implementation is intentionally modest. A multi-index is first expanded into a canonical list
> of coordinate directions, and the iterated derivative is then defined by repeated application of
> `Space.deriv` along that list.

## ii. Key results

> - `Space.iteratedDeriv` : iterated coordinate derivatives on `Space d`.
> - `∂^[I] f` : notation for the iterated derivative indexed by the multi-index `I`.
> - `Space.iteratedDeriv_add`, `Space.iteratedDeriv_const_smul` :
>   algebraic compatibility for smooth scalar-valued functions.
> - `Space.iteratedDeriv_contDiff` : smooth scalar-valued functions remain smooth after
>   iterated coordinate differentiation.
> - `Space.tsupport_iteratedDeriv_subset` :
>   the support of an iterated spatial derivative is contained in that of the original function.

## iv. References

> * None.

## A. Iterated derivatives on `Space d`

**`Space.iteratedDeriv`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Iterated.lean#L58).

> The iterated coordinate derivative on `Space d` indexed by a multi-index.

```lean
noncomputable def iteratedDeriv [AddCommGroup M] [Module ℝ M] [TopologicalSpace M]
    (I : MultiIndex d) (f : Space d → M) : Space d → M
```

**`Space.iteratedDeriv_zero`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Iterated.lean#L94).

```lean
lemma iteratedDeriv_zero [AddCommGroup M] [Module ℝ M] [TopologicalSpace M]
    (f : Space d → M) : ∂^[0] f = f
```

**`Space.iteratedDeriv_increment_zero`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Iterated.lean#L99).

```lean
lemma iteratedDeriv_increment_zero [NeZero d] [AddCommGroup M] [Module ℝ M] [TopologicalSpace M]
    (I : MultiIndex d) (f : Space d → M) :
    ∂^[MultiIndex.increment I 0] f = ∂[0] (∂^[I] f)
```

**`Space.iteratedDeriv_single`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Iterated.lean#L106).

```lean
lemma iteratedDeriv_single [AddCommGroup M] [Module ℝ M] [TopologicalSpace M]
    (i : Fin d) (f : Space d → M) :
    ∂^[MultiIndex.increment 0 i] f = ∂[i] f
```

**`Space.iteratedDeriv_add`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Iterated.lean#L111).

```lean
lemma iteratedDeriv_add (I : MultiIndex d) {f g : Space d → ℝ}
    (hf : ContDiff ℝ ∞ f) (hg : ContDiff ℝ ∞ g) :
    ∂^[I] (f + g) = ∂^[I] f + ∂^[I] g
```

**`Space.iteratedDeriv_const_smul`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Iterated.lean#L116).

```lean
lemma iteratedDeriv_const_smul (I : MultiIndex d) (c : ℝ) {f : Space d → ℝ}
    (hf : ContDiff ℝ ∞ f) :
    ∂^[I] (c • f) = c • ∂^[I] f
```

**`Space.iteratedDeriv_contDiff`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Iterated.lean#L122).

> Iterated spatial derivatives preserve smoothness for scalar-valued functions.

```lean
lemma iteratedDeriv_contDiff (I : MultiIndex d) {f : Space d → ℝ}
    (hf : ContDiff ℝ ∞ f) :
    ContDiff ℝ ∞ (∂^[I] f)
```

**`Space.tsupport_deriv_subset`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Iterated.lean#L129).

> The topological support of a spatial derivative is contained in that of the original
> function.

```lean
lemma tsupport_deriv_subset (i : Fin d) {f : Space d → ℝ} :
    tsupport (deriv i f) ⊆ tsupport f
```

**`Space.deriv_iteratedDeriv_commute`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Iterated.lean#L147).

> An extra spatial derivative commutes with iterated spatial derivatives for smooth
> scalar-valued functions.

```lean
lemma deriv_iteratedDeriv_commute (i : Fin d) (I : MultiIndex d) {f : Space d → ℝ}
    (hf : ContDiff ℝ ∞ f) :
    deriv i (∂^[I] f) = ∂^[I] (deriv i f)
```

**`Space.tsupport_iteratedDeriv_subset`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Iterated.lean#L160).

> The topological support of an iterated spatial derivative is contained in that of the
> original function.

```lean
lemma tsupport_iteratedDeriv_subset (I : MultiIndex d) {f : Space d → ℝ} :
    tsupport (∂^[I] f) ⊆ tsupport f
```

**`Space.iteratedDeriv_eq_zero_of_notMem_tsupport`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Iterated.lean#L166).

> An iterated spatial derivative vanishes outside the topological support of the original
> function.

```lean
lemma iteratedDeriv_eq_zero_of_notMem_tsupport (I : MultiIndex d) {f : Space d → ℝ} {x : Space d}
    (hx : x ∉ tsupport f) :
    ∂^[I] f x = 0
```

## Depends on

- [Derivatives on Space](derivatives-basic.md)
- [Multi-indices](../part-02/derivatives-multiindex.md)

## Sources

- [Physlib/SpaceAndTime/Space/Derivatives/Iterated.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Iterated.lean)
