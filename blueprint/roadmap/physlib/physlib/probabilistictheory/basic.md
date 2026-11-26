---
declaration: module
origin: cited
lean: ProbabilisticTheory, ProbabilisticTheory.real
statement: formalized
proof: formalized
---

# Probabilistic theories

The module `Physlib.ProbabilisticTheory.Basic`, [Physlib/ProbabilisticTheory/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Basic.lean): 2 declarations, 2 with a docstring.

> A probabilistic theory is described by its ordered real observables and a certain outcome.

## i. Overview

> The observables of a physical system form an ordered real vector space. Positive observables are
> those whose measured values are never negative. The certain outcome `1` bounds every observable
> up to a multiple and sets the scale for measurement outcomes. The order is Archimedean, so no
> observable is infinitesimally positive and the certain outcome defines a genuine norm.

## ii. Key results

> - `ProbabilisticTheory` : ordered real observables with a certain outcome and an Archimedean
>   order.
> - `ProbabilisticTheory.real` : real-valued outcomes with unit 1.

## iv. References

## A. Observable space and certain outcome

**`ProbabilisticTheory`**, a structure, [line 43](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Basic.lean#L43).

> An ordered real observable space with a certain outcome and no infinitesimal observables.

```lean
structure ProbabilisticTheory where
  /-- The real observables. -/
  Observables : Type*
  /-- Observables can be added and subtracted. -/
  [addCommGroup : AddCommGroup Observables]
  /-- The order saying which observables are positive. -/
  [partialOrder : PartialOrder Observables]
  /-- Observables can be scaled by real numbers. -/
  [module : Module ℝ Observables]
  /-- Adding an observable preserves the order. -/
  [isOrderedAddMonoid : IsOrderedAddMonoid Observables]
  /-- Scaling by a nonnegative real preserves the order. -/
  [posSMulMono : PosSMulMono ℝ Observables]
  /-- The certain outcome. -/
  [one : One Observables]
  /-- The certain outcome is nonnegative. -/
  one_nonneg' : 0 ≤ (1 : Observables)
  /-- Every observable is bounded above by a natural multiple of the certain outcome. -/
  exists_nsmul_one_le' : ∀ B : Observables, ∃ n : ℕ, B ≤ n • (1 : Observables)
  /-- An observable below every positive multiple of the certain outcome is nonpositive. -/
  le_zero_of_forall_pos_smul_one_le' : ∀ A : Observables,
    (∀ ε : ℝ, 0 < ε → A ≤ ε • (1 : Observables)) → A ≤ 0
```

## B. The real numbers

**`ProbabilisticTheory.real`**, an abbrev, [line 73](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Basic.lean#L73).

> The real numbers with their usual order and unit 1.

```lean
abbrev ProbabilisticTheory.real : ProbabilisticTheory
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/ProbabilisticTheory/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Basic.lean)
