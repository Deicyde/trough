---
declaration: module
origin: cited
lean: ProbabilisticTheory.IsOneParameterGroup, ProbabilisticTheory.IsOneParameterGroup.left_inv, ProbabilisticTheory.IsOneParameterGroup.right_inv, ProbabilisticTheory.IsOneParameterGroup.bijective
statement: formalized
proof: formalized
---

# One-parameter groups

The module `PhyslibAlpha.ProbabilisticTheory.Dynamics.OneParameterGroup`, [PhyslibAlpha/ProbabilisticTheory/Dynamics/OneParameterGroup.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Dynamics/OneParameterGroup.lean): 4 declarations, 2 with a docstring.

> Defines one-parameter groups `α : ℝ → E → E` satisfying `α 0 = id` and the group law.

## i. Overview

> A one-parameter group is a family `α : ℝ → E → E` with `α 0 = id` and `α (s + t) = α s ∘ α t`. It is
> stated for an arbitrary type `E`; preservation of structure and continuity are separate conditions.

## ii. Key results

> - `IsOneParameterGroup` : one-parameter groups.

## iv. References

> * None.

## A. The group law

**`ProbabilisticTheory.IsOneParameterGroup`**, a structure, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Dynamics/OneParameterGroup.lean#L44).

> `α : ℝ → E → E` is a one-parameter group of (not-yet-specified-as-anything) transformations of
> `E`: `α 0 = id` and `α (s + t) = α s ∘ α t`. Nothing about linearity, order, a product, or
> continuity is assumed — those are independent, composable hypotheses to add at the point of use.

```lean
structure IsOneParameterGroup {E : Type*} (α : ℝ → E → E) : Prop where
  /-- Evolving for zero time does nothing. -/
  map_zero : ∀ a : E, α 0 a = a
  /-- Evolving for `s` then `t` is the same as evolving for `s + t`. -/
  map_add : ∀ s t a, α (s + t) a = α s (α t a)
```

**`ProbabilisticTheory.IsOneParameterGroup.left_inv`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Dynamics/OneParameterGroup.lean#L57).

> Every time-`t` map has a two-sided inverse, `α (-t)`: an immediate consequence of the group
> law, recorded once here rather than re-derived at each point of use.

```lean
lemma left_inv (t : ℝ) (a : E) : α (-t) (α t a) = a
```

**`ProbabilisticTheory.IsOneParameterGroup.right_inv`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Dynamics/OneParameterGroup.lean#L61).

```lean
lemma right_inv (t : ℝ) (a : E) : α t (α (-t) a) = a
```

**`ProbabilisticTheory.IsOneParameterGroup.bijective`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Dynamics/OneParameterGroup.lean#L65).

```lean
lemma bijective (t : ℝ) : Function.Bijective (α t)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Dynamics/OneParameterGroup.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Dynamics/OneParameterGroup.lean)
