---
declaration: module
origin: cited
lean: ProbabilisticTheory.State.apply_eq_zero_of_apply_one_eq_zero, ProbabilisticTheory.State.exists_apply_neg_of_not_nonneg, ProbabilisticTheory.State.nonneg_iff_forall_state_nonneg, ProbabilisticTheory.State.instNonemptyState, ProbabilisticTheory.State.orderUnitNorm_le_iff_forall_abs_apply_le, ProbabilisticTheory.State.sSup_abs_apply_eq_orderUnitNorm, ProbabilisticTheory.State.orderUnitNorm_one, ProbabilisticTheory.State.ext_of_forall_apply_eq
statement: formalized
proof: formalized
---

# Separation by states (Physlib)

The module `Physlib.ProbabilisticTheory.State.Separation`, [Physlib/ProbabilisticTheory/State/Separation.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Separation.lean): 8 declarations, 8 with a docstring.

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

> - `ProbabilisticTheory.State.exists_apply_neg_of_not_nonneg` : every element outside the positive
>   cone is separated from it by a state.
> - `ProbabilisticTheory.State.nonneg_iff_forall_state_nonneg` : states determine the positive cone.
> - `ProbabilisticTheory.State.sSup_abs_apply_eq_orderUnitNorm` : states determine the order-unit
>   norm.
> - `ProbabilisticTheory.State.ext_of_forall_apply_eq` : states separate points.

## iv. References

## A. Separating points from the cone

**`ProbabilisticTheory.State.apply_eq_zero_of_apply_one_eq_zero`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Separation.lean#L62).

> A positive functional vanishing at the order unit vanishes everywhere.

```lean
lemma apply_eq_zero_of_apply_one_eq_zero {p : P.Observables →ₚ[ℝ] ℝ}
    (h1 : p (1 : P.Observables) = 0) (A : P.Observables) : p A = 0
```

**`ProbabilisticTheory.State.exists_apply_neg_of_not_nonneg`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Separation.lean#L69).

> Every element outside the positive cone is strictly separated from it by a state.

```lean
lemma exists_apply_neg_of_not_nonneg {A : P.Observables} (hA : ¬ 0 ≤ A) :
    ∃ ω : P.State, ω A < 0
```

## B. The positive cone

**`ProbabilisticTheory.State.nonneg_iff_forall_state_nonneg`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Separation.lean#L86).

> An element is positive iff every state assigns it a nonnegative value.

```lean
lemma nonneg_iff_forall_state_nonneg (A : P.Observables) : 0 ≤ A ↔ ∀ ω : P.State, 0 ≤ ω A
```

## C. The order-unit norm

**`ProbabilisticTheory.State.instNonemptyState`**, an instance, [line 99](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Separation.lean#L99).

> Every nontrivial Archimedean order-unit space has a state.

```lean
instance instNonemptyState [Nontrivial P.Observables] : Nonempty P.State
```

**`ProbabilisticTheory.State.orderUnitNorm_le_iff_forall_abs_apply_le`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Separation.lean#L107).

> The order-unit norm is at most `r` iff every state predicts an absolute value at most `r`.

```lean
lemma orderUnitNorm_le_iff_forall_abs_apply_le [Nontrivial P.Observables] (A : P.Observables)
    (r : ℝ) :
    orderUnitNorm A ≤ r ↔ ∀ ω : P.State, |ω A| ≤ r
```

**`ProbabilisticTheory.State.sSup_abs_apply_eq_orderUnitNorm`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Separation.lean#L118).

> The order-unit norm is the supremum of `|ω A|` over all states `ω`.

```lean
lemma sSup_abs_apply_eq_orderUnitNorm [Nontrivial P.Observables] (A : P.Observables) :
    sSup (Set.range fun ω : P.State => |ω A|) = orderUnitNorm A
```

**`ProbabilisticTheory.State.orderUnitNorm_one`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Separation.lean#L126).

> The order unit has norm exactly `1`.

```lean
lemma orderUnitNorm_one [Nontrivial P.Observables] : orderUnitNorm (1 : P.Observables) = 1
```

## D. Separation of points

**`ProbabilisticTheory.State.ext_of_forall_apply_eq`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Separation.lean#L136).

> States separate points: if `ω A = ω B` for every state `ω`, then `A = B`.

```lean
lemma ext_of_forall_apply_eq {A B : P.Observables} (h : ∀ ω : P.State, ω A = ω B) : A = B
```

## Depends on

- [Archimedean order-unit spaces (Physlib)](../orderunit/archimedean.md)
- [States](basic.md)

## Proof depends on

- [The metric space of states (Physlib)](metric.md)

## Sources

- [Physlib/ProbabilisticTheory/State/Separation.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Separation.lean)
