---
declaration: module
origin: cited
lean: PositiveLinearMap.nnsmul_apply, PositiveLinearMap.dominator, PositiveLinearMap.le_dominator, PositiveLinearMap.dominator_nonneg, PositiveLinearMap.instPartialOrder, PositiveLinearMap.le_def, PositiveLinearMap.zero_le, PositiveLinearMap.le_add_right
statement: formalized
proof: formalized
---

# Positive functionals

The module `PhyslibAlpha.Mathematics.Order.PositiveDual.Basic`, [PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean): 26 declarations (1 instance with no name), 8 with a docstring.

> Positive functionals on an ordered vector space, their order, and extension from the cone.

## i. Overview

> A positive functional on an ordered real vector space `E` is a linear functional that is
> nonnegative on the positive cone. When the order is directed, every element is a difference of
> two nonnegative ones, so positive functionals are determined by their values on the cone. They are
> then ordered by comparing these values: `ψ ≤ φ` when `φ - ψ` is positive again.
>
> Conversely, a nonnegative function on the cone that is additive and positively homogeneous there
> extends uniquely to a positive functional.

## ii. Key results

> - `PositiveLinearMap.instPartialOrder` : positive functionals ordered on the positive cone.
> - `PositiveLinearMap.subOfLE` : the difference of two positive functionals, one below the other.
> - `PositiveLinearMap.eq_zero_of_map_eq_zero` : a positive functional vanishing at an order unit
>   vanishes.
> - `PositiveLinearMap.ofCone` : a nonnegative, additive, positively homogeneous function on the
>   cone as a positive functional.

## iv. References

> * None.

## A. Scaling positive functionals

**An instance with no name**, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean#L60).

> A positive functional scaled by a nonnegative real.

```lean
instance : SMul ℝ≥0 (E →ₚ[ℝ] ℝ)
```

**`PositiveLinearMap.nnsmul_apply`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean#L64).

```lean
lemma nnsmul_apply (c : ℝ≥0) (φ : E →ₚ[ℝ] ℝ) (f : E) : (c • φ) f = c * φ f
```

## B. The order on positive functionals

**`PositiveLinearMap.dominator`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean#L74).

> An element above both `f` and `0`.

```lean
noncomputable def dominator (f : E) : E
```

**`PositiveLinearMap.le_dominator`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean#L77).

```lean
lemma le_dominator (f : E) : f ≤ dominator f
```

**`PositiveLinearMap.dominator_nonneg`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean#L80).

```lean
lemma dominator_nonneg (f : E) : 0 ≤ dominator f
```

**`PositiveLinearMap.instPartialOrder`**, an instance, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean#L83).

> Positive functionals are ordered by comparing them on the positive cone.

```lean
instance instPartialOrder : PartialOrder (E →ₚ[ℝ] ℝ)
```

**`PositiveLinearMap.le_def`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean#L95).

```lean
lemma le_def {φ ψ : E →ₚ[ℝ] ℝ} : φ ≤ ψ ↔ ∀ f, 0 ≤ f → φ f ≤ ψ f
```

**`PositiveLinearMap.zero_le`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean#L97).

```lean
lemma zero_le (φ : E →ₚ[ℝ] ℝ) : 0 ≤ φ
```

**`PositiveLinearMap.le_add_right`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean#L99).

```lean
lemma le_add_right (φ ψ : E →ₚ[ℝ] ℝ) : φ ≤ φ + ψ
```

**`PositiveLinearMap.le_sum`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean#L102).

```lean
lemma le_sum {ι : Type*} {t : Finset ι} (ψ : ι → E →ₚ[ℝ] ℝ) {i : ι} (hi : i ∈ t) :
    ψ i ≤ ∑ j ∈ t, ψ j
```

**`PositiveLinearMap.subOfLE`**, a def, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean#L108).

> The difference of two positive functionals, one below the other.

```lean
def subOfLE (φ ψ : E →ₚ[ℝ] ℝ) (h : ψ ≤ φ) : E →ₚ[ℝ] ℝ
```

**`PositiveLinearMap.subOfLE_apply`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean#L111).

```lean
lemma subOfLE_apply (φ ψ : E →ₚ[ℝ] ℝ) (h : ψ ≤ φ) (f : E) :
    subOfLE φ ψ h f = φ f - ψ f
```

**`PositiveLinearMap.add_subOfLE`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean#L114).

```lean
lemma add_subOfLE (φ ψ : E →ₚ[ℝ] ℝ) (h : ψ ≤ φ) : ψ + subOfLE φ ψ h = φ
```

**`PositiveLinearMap.eq_zero_of_add_eq_zero`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean#L117).

```lean
lemma eq_zero_of_add_eq_zero {φ ψ : E →ₚ[ℝ] ℝ} (h : φ + ψ = 0) : φ = 0
```

**`PositiveLinearMap.eq_subOfLE_add_subOfLE`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean#L120).

```lean
lemma eq_subOfLE_add_subOfLE {φ σ θ₁ θ₂ α β : E →ₚ[ℝ] ℝ} (h : φ + σ = α + β)
    (e : φ = θ₁ + θ₂) (h₁ : θ₁ ≤ α) (h₂ : θ₂ ≤ β) : σ = subOfLE α θ₁ h₁ + subOfLE β θ₂ h₂
```

**`PositiveLinearMap.eq_zero_of_map_eq_zero`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean#L131).

> A positive functional vanishing at an order unit vanishes.

```lean
lemma eq_zero_of_map_eq_zero {u : E} (hu : IsOrderUnit u) {ψ : E →ₚ[ℝ] ℝ} (h : ψ u = 0) :
    ψ = 0
```

## C. Extending from the cone

**`PositiveLinearMap.coneExt`**, a def, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean#L150).

> The extension of `F` from the cone: `F b - F (b - f)` for any `b` above `f` and `0`.

```lean
noncomputable def coneExt (f : E) : ℝ
```

**`PositiveLinearMap.map_zero_of_cone_add`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean#L155).

```lean
lemma map_zero_of_cone_add : F 0 = 0
```

**`PositiveLinearMap.coneExt_eq`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean#L162).

> The extension does not depend on the element `b` above `f` and `0`.

```lean
lemma coneExt_eq {f b : E} (hb : 0 ≤ b) (hbf : f ≤ b) : coneExt F f = F b - F (b - f)
```

**`PositiveLinearMap.coneExt_of_nonneg`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean#L170).

```lean
lemma coneExt_of_nonneg {f : E} (hf : 0 ≤ f) : coneExt F f = F f
```

**`PositiveLinearMap.coneExt_add`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean#L174).

```lean
lemma coneExt_add (f g : E) : coneExt F (f + g) = coneExt F f + coneExt F g
```

**`PositiveLinearMap.coneExt_neg`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean#L185).

```lean
lemma coneExt_neg (f : E) : coneExt F (-f) = -coneExt F f
```

**`PositiveLinearMap.coneExt_smul_of_pos`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean#L194).

```lean
lemma coneExt_smul_of_pos {c : ℝ} (hc : 0 < c) (f : E) : coneExt F (c • f) = c * coneExt F f
```

**`PositiveLinearMap.coneExt_smul`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean#L201).

```lean
lemma coneExt_smul (c : ℝ) (f : E) : coneExt F (c • f) = c * coneExt F f
```

**`PositiveLinearMap.ofCone`**, a def, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean#L213).

> A nonnegative, additive and positively homogeneous function on the positive cone extends to a
> positive functional.

```lean
noncomputable def ofCone : E →ₚ[ℝ] ℝ
```

**`PositiveLinearMap.ofCone_apply`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean#L220).

```lean
lemma ofCone_apply {f : E} (hf : 0 ≤ f) : ofCone F h0 hadd hsmul f = F f
```

## Depends on

- [Strong units](strongunit.md)

## Sources

- [PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Basic.lean)
