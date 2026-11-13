---
declaration: module
origin: cited
lean: PositiveLinearMap.majorantSet, PositiveLinearMap.majorant, PositiveLinearMap.majorantSet_nonempty, PositiveLinearMap.sub_le_smul, PositiveLinearMap.m_nonneg, PositiveLinearMap.bddBelow_majorantSet, PositiveLinearMap.majorant_le, PositiveLinearMap.majorant_add_le
statement: formalized
proof: formalized
---

# Positive majorants

The module `PhyslibAlpha.Mathematics.Order.PositiveDual.Majorant`, [PhyslibAlpha/Mathematics/Order/PositiveDual/Majorant.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Majorant.lean): 12 declarations, 4 with a docstring.

> A positive functional of weight at most m at u that dominates P - N, via Hahn–Banach.

## i. Overview

> Fix an order unit `u` and two positive functionals `P` and `N`. If `P - N` is at most
> `m` on the order interval `[0, u]`, then `P` lies below `π + N` for a positive functional `π` with
> `π u ≤ m`. The functional `π` comes from Hahn–Banach, applied to a gauge that measures how much
> `P - N` can exceed `m` times the multiple of `u` needed to dominate an element.

## ii. Key results

> - `PositiveLinearMap.majorant` : the majorant gauge.
> - `PositiveLinearMap.exists_le_add_of_forall_le` : a positive functional of weight at most `m` at
>   `u` that makes up for `P - N`.

## iv. References

> * None.

## A. The majorant gauge

**`PositiveLinearMap.majorantSet`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Majorant.lean#L54).

> The values `m t - P a + N a` over all `t ≥ 0` and `a ≥ 0` with `x + a ≤ t • u`.

```lean
def majorantSet (m : ℝ) (x : E) : Set ℝ
```

**`PositiveLinearMap.majorant`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Majorant.lean#L59).

> The majorant gauge.

```lean
noncomputable def majorant (m : ℝ) (x : E) : ℝ
```

**`PositiveLinearMap.majorantSet_nonempty`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Majorant.lean#L65).

```lean
lemma majorantSet_nonempty (x : E) : (majorantSet u P N m x).Nonempty
```

**`PositiveLinearMap.sub_le_smul`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Majorant.lean#L70).

```lean
lemma sub_le_smul {a : E} {s : ℝ} (hs : 0 ≤ s) (ha : 0 ≤ a) (has : a ≤ s • u) :
    P a - N a ≤ s * m
```

**`PositiveLinearMap.m_nonneg`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Majorant.lean#L81).

```lean
lemma m_nonneg : 0 ≤ m
```

**`PositiveLinearMap.bddBelow_majorantSet`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Majorant.lean#L83).

```lean
lemma bddBelow_majorantSet (x : E) : BddBelow (majorantSet u P N m x)
```

**`PositiveLinearMap.majorant_le`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Majorant.lean#L95).

```lean
lemma majorant_le {x : E} {r : ℝ} (hr : r ∈ majorantSet u P N m x) : majorant u P N m x ≤ r
```

**`PositiveLinearMap.majorant_add_le`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Majorant.lean#L98).

```lean
lemma majorant_add_le (x y : E) :
    majorant u P N m (x + y) ≤ majorant u P N m x + majorant u P N m y
```

**`PositiveLinearMap.majorantSet_smul`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Majorant.lean#L116).

```lean
lemma majorantSet_smul {c : ℝ} (hc : 0 < c) (x : E) :
    majorantSet u P N m (c • x) = c • majorantSet u P N m x
```

**`PositiveLinearMap.majorant_smul`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Majorant.lean#L133).

```lean
lemma majorant_smul {c : ℝ} (hc : 0 < c) (x : E) :
    majorant u P N m (c • x) = c * majorant u P N m x
```

## B. Positive majorants

**`PositiveLinearMap.exists_le_majorant`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Majorant.lean#L141).

> A linear functional below the majorant gauge.

```lean
lemma exists_le_majorant : ∃ g : E →ₗ[ℝ] ℝ, ∀ x, g x ≤ majorant u P N m x
```

**`PositiveLinearMap.exists_le_add_of_forall_le`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Majorant.lean#L155).

> If `P - N` is at most `m` on `[0, u]`, then `P ≤ π + N` for a positive functional `π` with
> `π u ≤ m`.

```lean
lemma exists_le_add_of_forall_le : ∃ π : E →ₚ[ℝ] ℝ, (∀ f, 0 ≤ f → P f ≤ π f + N f) ∧ π u ≤ m
```

## Depends on

- [Strong units](strongunit.md)

## Sources

- [PhyslibAlpha/Mathematics/Order/PositiveDual/Majorant.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Majorant.lean)
