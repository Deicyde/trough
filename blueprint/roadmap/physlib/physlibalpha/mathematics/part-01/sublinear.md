---
declaration: module
origin: cited
lean: map_zero_of_sublinear, smul_le_of_sublinear, exists_linearMap_le_eq_of_sublinear
statement: formalized
proof: formalized
---

# Linear minorants of sublinear functionals

The module `PhyslibAlpha.Mathematics.Sublinear`, [PhyslibAlpha/Mathematics/Sublinear.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Sublinear.lean): 3 declarations, 2 with a docstring.

> A sublinear functional has a linear minorant attaining it at any given point (Hahn–Banach).

## i. Overview

> A sublinear functional is the largest of the linear functionals below it. At every point the
> Hahn–Banach theorem gives a linear functional below it that agrees with it there.

## ii. Key results

> - `exists_linearMap_le_eq_of_sublinear` proves that a linear functional below a sublinear functional
>   can be chosen to agree with it at a given point.

## iv. References

> * None.

## A. Linear minorants

**`map_zero_of_sublinear`**, a lemma, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Sublinear.lean#L47).

```lean
lemma map_zero_of_sublinear : N 0 = 0
```

**`smul_le_of_sublinear`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Sublinear.lean#L54).

> A sublinear functional dominates the multiples of its value at a point.

```lean
lemma smul_le_of_sublinear (c : ℝ) (x : V) : c * N x ≤ N (c • x)
```

**`exists_linearMap_le_eq_of_sublinear`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Sublinear.lean#L66).

> **Hahn–Banach**: a sublinear functional has a linear minorant attaining it at `x`.

```lean
lemma exists_linearMap_le_eq_of_sublinear (x : V) :
    ∃ g : V →ₗ[ℝ] ℝ, (∀ y, g y ≤ N y) ∧ g x = N x
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/Sublinear.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Sublinear.lean)
