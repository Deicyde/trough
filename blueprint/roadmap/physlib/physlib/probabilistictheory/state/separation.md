---
declaration: module
origin: cited
lean: UnitalPositiveLinearMap.apply_eq_zero_of_apply_one_eq_zero, UnitalPositiveLinearMap.exists_apply_neg_of_not_nonneg, UnitalPositiveLinearMap.nonneg_iff_forall_state_nonneg, UnitalPositiveLinearMap.instNonemptyState, UnitalPositiveLinearMap.orderUnitNorm_le_iff_forall_abs_apply_le, UnitalPositiveLinearMap.sSup_abs_apply_eq_orderUnitNorm, UnitalPositiveLinearMap.orderUnitNorm_one, UnitalPositiveLinearMap.ext_of_forall_apply_eq
statement: formalized
proof: formalized
---

# Separation by states

The module `Physlib.ProbabilisticTheory.State.Separation`, [Physlib/ProbabilisticTheory/State/Separation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Separation.lean): 8 declarations, 8 with a docstring.

> States determine positivity, the order-unit norm, and equality of observables.

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

## iv. References

## A. Separating points from the cone

**`UnitalPositiveLinearMap.apply_eq_zero_of_apply_one_eq_zero`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Separation.lean#L63).

> A positive functional vanishing at the order unit vanishes everywhere.

```lean
lemma apply_eq_zero_of_apply_one_eq_zero [OrderUnitSpace E] {p : E →ₚ[ℝ] ℝ}
    (h1 : p (1 : E) = 0) (A : E) : p A = 0
```

**`UnitalPositiveLinearMap.exists_apply_neg_of_not_nonneg`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Separation.lean#L72).

> Every element outside the positive cone is strictly separated from it by a state.

```lean
lemma exists_apply_neg_of_not_nonneg {A : E} (hA : ¬ 0 ≤ A) : ∃ ω : 𝓢[ℝ, E], ω A < 0
```

## B. The positive cone

**`UnitalPositiveLinearMap.nonneg_iff_forall_state_nonneg`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Separation.lean#L88).

> An element is positive iff every state assigns it a nonnegative value.

```lean
lemma nonneg_iff_forall_state_nonneg (A : E) : 0 ≤ A ↔ ∀ ω : 𝓢[ℝ, E], 0 ≤ ω A
```

## C. The order-unit norm

**`UnitalPositiveLinearMap.instNonemptyState`**, an instance, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Separation.lean#L101).

> Every nontrivial Archimedean order-unit space has a state.

```lean
instance instNonemptyState [Nontrivial E] : Nonempty (𝓢[ℝ, E])
```

**`UnitalPositiveLinearMap.orderUnitNorm_le_iff_forall_abs_apply_le`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Separation.lean#L109).

> The order-unit norm is at most `r` iff every state predicts an absolute value at most `r`.

```lean
lemma orderUnitNorm_le_iff_forall_abs_apply_le [Nontrivial E] (A : E) (r : ℝ) :
    orderUnitNorm A ≤ r ↔ ∀ ω : 𝓢[ℝ, E], |ω A| ≤ r
```

**`UnitalPositiveLinearMap.sSup_abs_apply_eq_orderUnitNorm`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Separation.lean#L119).

> The order-unit norm is the supremum of `|ω A|` over all states `ω`.

```lean
lemma sSup_abs_apply_eq_orderUnitNorm [Nontrivial E] (A : E) :
    sSup (Set.range fun ω : 𝓢[ℝ, E] => |ω A|) = orderUnitNorm A
```

**`UnitalPositiveLinearMap.orderUnitNorm_one`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Separation.lean#L127).

> The order unit has norm exactly `1`.

```lean
lemma orderUnitNorm_one [Nontrivial E] : orderUnitNorm (1 : E) = 1
```

## D. Separation of points

**`UnitalPositiveLinearMap.ext_of_forall_apply_eq`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Separation.lean#L137).

> States separate points: if `ω A = ω B` for every state `ω`, then `A = B`.

```lean
lemma ext_of_forall_apply_eq {A B : E} (h : ∀ ω : 𝓢[ℝ, E], ω A = ω B) : A = B
```

## Depends on

- [Positive unital maps](../channel/basic.md)
- [Archimedean order-unit spaces](../orderunit/archimedean.md)

## Proof depends on

- [The metric space of states](metric.md)

## Sources

- [Physlib/ProbabilisticTheory/State/Separation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Separation.lean)
