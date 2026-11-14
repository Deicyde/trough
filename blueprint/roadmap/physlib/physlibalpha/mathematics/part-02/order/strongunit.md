---
declaration: module
origin: cited
lean: IsStrongUnit, IsStrongUnit.exists_two_sided, IsStrongUnit.isDirectedOrder, IsStrongUnit.ne_zero, IsOrderUnit, IsOrderUnit.exists_two_sided, IsOrderUnit.isDirectedOrder, IsOrderUnit.exists_forall_le_smul
statement: formalized
proof: formalized
---

# Strong units

The module `PhyslibAlpha.Mathematics.Order.StrongUnit`, [PhyslibAlpha/Mathematics/Order/StrongUnit.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/StrongUnit.lean): 9 declarations, 8 with a docstring.

> Strong units and order units of ordered abelian groups, and the directed order they induce.

## i. Overview

> A strong unit of an ordered abelian group is an element `u` such that every element lies below some
> natural multiple of `u`; an order unit is a nonnegative strong unit. A group with a nonnegative
> strong unit is directed: any two elements lie below a common multiple of `u`. In a nontrivial
> group a strong unit is nonzero.

## ii. Key results

> - `IsStrongUnit` : every element lies below a natural multiple of `u`.
> - `IsStrongUnit.exists_two_sided` : every element lies between opposite multiples of `u`.
> - `IsStrongUnit.isDirectedOrder` : a nonnegative strong unit makes the order directed.
> - `IsStrongUnit.ne_zero` : a strong unit of a nontrivial group is nonzero.
> - `IsOrderUnit` : a nonnegative strong unit.

## iv. References

> * None.

## A. Strong units

**`IsStrongUnit`**, a def, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/StrongUnit.lean#L51).

> A strong unit: every element lies below some natural multiple of `u`.

```lean
def IsStrongUnit : Prop
```

**`IsStrongUnit.exists_two_sided`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/StrongUnit.lean#L56).

> Every element lies between two opposite multiples of a nonnegative strong unit.

```lean
lemma exists_two_sided (hunit : IsStrongUnit u) (hu : 0 ≤ u) (x : G) :
    ∃ n : ℕ, -(n • u) ≤ x ∧ x ≤ n • u
```

**`IsStrongUnit.isDirectedOrder`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/StrongUnit.lean#L65).

> A nonnegative strong unit makes the order directed.

```lean
lemma isDirectedOrder (hunit : IsStrongUnit u) (hu : 0 ≤ u) : IsDirectedOrder G
```

**`IsStrongUnit.ne_zero`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/StrongUnit.lean#L73).

> A strong unit of a nontrivial group is nonzero.

```lean
lemma ne_zero [Nontrivial G] (hunit : IsStrongUnit u) : u ≠ 0
```

## B. Order units

**`IsOrderUnit`**, a structure, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/StrongUnit.lean#L86).

> An order unit: a nonnegative strong unit.

```lean
structure IsOrderUnit (u : G) : Prop where
  /-- An order unit is nonnegative. -/
  nonneg : 0 ≤ u
  /-- Every element lies below a natural multiple of an order unit. -/
  isStrongUnit : IsStrongUnit u
```

**`IsOrderUnit.exists_two_sided`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/StrongUnit.lean#L98).

> Every element lies between two opposite multiples of an order unit.

```lean
lemma exists_two_sided (x : G) : ∃ n : ℕ, -(n • u) ≤ x ∧ x ≤ n • u
```

**`IsOrderUnit.isDirectedOrder`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/StrongUnit.lean#L101).

```lean
lemma isDirectedOrder : IsDirectedOrder G
```

**`IsOrderUnit.exists_forall_le_smul`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/StrongUnit.lean#L108).

> Finitely many elements lie below a common nonnegative multiple of an order unit.

```lean
lemma exists_forall_le_smul {ι : Type*} [Fintype ι] (x : ι → G) :
    ∃ μ : ℝ, 0 ≤ μ ∧ ∀ i, x i ≤ μ • u
```

**`IsOrderUnit.nonneg_of_smul_nonneg`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/StrongUnit.lean#L119).

> A multiple of an order unit of a nontrivial space is nonnegative only for a nonnegative
> factor.

```lean
lemma nonneg_of_smul_nonneg [Nontrivial G] {c : ℝ} (h : 0 ≤ c • u) : 0 ≤ c
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/Order/StrongUnit.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/StrongUnit.lean)
