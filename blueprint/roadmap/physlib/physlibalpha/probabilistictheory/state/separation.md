---
declaration: module
origin: cited
lean: ProbabilisticTheory.UnitalPositiveLinearMap.apply_eq_zero_of_apply_one_eq_zero, ProbabilisticTheory.UnitalPositiveLinearMap.exists_apply_neg_of_not_nonneg, ProbabilisticTheory.UnitalPositiveLinearMap.nonneg_iff_forall_state_nonneg, ProbabilisticTheory.UnitalPositiveLinearMap.instNonemptyState, ProbabilisticTheory.UnitalPositiveLinearMap.exists_state_apply_gt_of_not_le, ProbabilisticTheory.UnitalPositiveLinearMap.exists_state_abs_apply_gt_of_lt_orderUnitNorm, ProbabilisticTheory.UnitalPositiveLinearMap.sSup_abs_apply_eq_orderUnitNorm, ProbabilisticTheory.UnitalPositiveLinearMap.orderUnitNorm_one
statement: formalized
proof: formalized
---

# Separation by states

The module `PhyslibAlpha.ProbabilisticTheory.State.Separation`, [PhyslibAlpha/ProbabilisticTheory/State/Separation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Separation.lean): 13 declarations, 12 with a docstring.

> Via Hahn–Banach, states separate points and determine the positive cone and order-unit norm.

## i. Overview

> In an Archimedean order-unit space, states determine the entire ordered normed structure. An
> element is positive exactly when every state assigns it a nonnegative value, and its order-unit
> norm is `‖A‖₁ = sup { |ω A| : ω a state }`. Consequently, states separate points: two elements are
> equal whenever every state assigns them the same value.
>
> The main ingredient is Hahn–Banach separation of a point from the positive cone. Applied to an
> element `A ≱ 0`, it produces a state `ω` with `ω A < 0`. Everything else follows from this one
> separation fact.

## ii. Key results

> - `UnitalPositiveLinearMap.exists_apply_neg_of_not_nonneg` : every element outside the positive
>   cone is separated from it by a state.
> - `UnitalPositiveLinearMap.nonneg_iff_forall_state_nonneg` : states determine the positive cone.
> - `UnitalPositiveLinearMap.sSup_abs_apply_eq_orderUnitNorm` : states determine the order-unit norm.
> - `UnitalPositiveLinearMap.ext_of_forall_apply_eq` : states separate points.
> - `UnitalPositiveLinearMap.toOrderUnitContinuousLinearMap` : a state as a continuous functional.

## iv. References

> * None.

## A. Separating points from the cone

**`ProbabilisticTheory.UnitalPositiveLinearMap.apply_eq_zero_of_apply_one_eq_zero`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Separation.lean#L69).

> A positive functional vanishing at the order unit vanishes everywhere.

```lean
lemma apply_eq_zero_of_apply_one_eq_zero {p : E →ₚ[ℝ] ℝ}
    (h1 : p (1 : E) = 0) (A : E) :
    p A = 0
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.exists_apply_neg_of_not_nonneg`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Separation.lean#L77).

> Every element outside the positive cone is strictly separated from it by a state.

```lean
lemma exists_apply_neg_of_not_nonneg {A : E} (hA : ¬ 0 ≤ A) : ∃ ω : 𝓢[ℝ, E], ω A < 0
```

## B. The positive cone

**`ProbabilisticTheory.UnitalPositiveLinearMap.nonneg_iff_forall_state_nonneg`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Separation.lean#L101).

> An element is positive iff every state assigns it a nonnegative value.

```lean
lemma nonneg_iff_forall_state_nonneg (A : E) : 0 ≤ A ↔ ∀ ω : 𝓢[ℝ, E], 0 ≤ ω A
```

## C. The order-unit norm

**`ProbabilisticTheory.UnitalPositiveLinearMap.instNonemptyState`**, an instance, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Separation.lean#L114).

> Every nontrivial Archimedean order-unit space has a state.

```lean
instance instNonemptyState [Nontrivial E] : Nonempty (𝓢[ℝ, E])
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.exists_state_apply_gt_of_not_le`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Separation.lean#L124).

> If `A ≤ r • 1` fails, some state predicts more than `r` for `A`.

```lean
lemma exists_state_apply_gt_of_not_le {A : E} {r : ℝ} (h : ¬ A ≤ r • (1 : E)) :
    ∃ ω : 𝓢[ℝ, E], r < ω A
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.exists_state_abs_apply_gt_of_lt_orderUnitNorm`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Separation.lean#L130).

> Any scalar below the order-unit norm of `A` is exceeded by `|ω A|` for some state `ω`.

```lean
lemma exists_state_abs_apply_gt_of_lt_orderUnitNorm [Nontrivial E] (A : E) {r : ℝ}
    (hr : r < orderUnitNorm A) : ∃ ω : 𝓢[ℝ, E], r < |ω A|
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.sSup_abs_apply_eq_orderUnitNorm`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Separation.lean#L143).

> The order-unit norm is the supremum of `|ω A|` over all states `ω`.

```lean
lemma sSup_abs_apply_eq_orderUnitNorm [Nontrivial E] (A : E) :
    sSup (Set.range fun ω : 𝓢[ℝ, E] => |ω A|) = orderUnitNorm A
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.orderUnitNorm_one`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Separation.lean#L152).

> The order unit has norm exactly `1`.

```lean
lemma orderUnitNorm_one [Nontrivial E] : orderUnitNorm (1 : E) = 1
```

## D. Separation of points

**`ProbabilisticTheory.UnitalPositiveLinearMap.ext_of_forall_apply_eq`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Separation.lean#L163).

> States separate points: if `ω A = ω B` for every state `ω`, then `A = B`.

```lean
lemma ext_of_forall_apply_eq {A B : E} (h : ∀ ω : 𝓢[ℝ, E], ω A = ω B) : A = B
```

## E. Continuous-dual realization

**`ProbabilisticTheory.UnitalPositiveLinearMap.toOrderUnitContinuousLinearMap`**, a def, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Separation.lean#L174).

> A state as a continuous functional on the canonical order-unit-norm copy.

```lean
noncomputable def toOrderUnitContinuousLinearMap (ω : 𝓢[ℝ, E]) :
    WithOrderUnitNorm E →L[ℝ] ℝ
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.toOrderUnitContinuousLinearMap_apply`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Separation.lean#L179).

```lean
lemma toOrderUnitContinuousLinearMap_apply (ω : 𝓢[ℝ, E]) (A : E) :
    ω.toOrderUnitContinuousLinearMap A = ω A
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.toOrderUnitContinuousLinearMap_injective`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Separation.lean#L183).

> The continuous-dual realization of states is injective.

```lean
lemma toOrderUnitContinuousLinearMap_injective :
    Function.Injective
      (toOrderUnitContinuousLinearMap : 𝓢[ℝ, E] → WithOrderUnitNorm E →L[ℝ] ℝ)
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.norm_toOrderUnitContinuousLinearMap`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Separation.lean#L193).

> Every state has continuous-dual norm one for the order-unit norm.

```lean
lemma norm_toOrderUnitContinuousLinearMap [Nontrivial E] (ω : 𝓢[ℝ, E]) :
    ‖ω.toOrderUnitContinuousLinearMap‖ = 1
```

## Depends on

- [Finite weights are continuous](../weight/continuous.md)

## Proof depends on

- [The metric space of states](metric.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/State/Separation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Separation.lean)
