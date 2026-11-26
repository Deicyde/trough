---
declaration: module
origin: cited
lean: ProbabilisticTheory.one_nonneg, ProbabilisticTheory.exists_nsmul_one_le, ProbabilisticTheory.exists_two_sided_bound, ProbabilisticTheory.exists_real_shift_nonneg, ProbabilisticTheory.nonneg_add_eq_zero
statement: formalized
proof: formalized
---

# Ordered vector spaces and order units (Physlib)

The module `Physlib.ProbabilisticTheory.OrderUnit.Basic`, [Physlib/ProbabilisticTheory/OrderUnit/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Basic.lean): 5 declarations, 5 with a docstring.

## i. Overview

> Order-unit spaces capture the basic structure needed for a probabilistic theory: observables,
> positivity, effects, states and probabilities. They do this without assuming that the system is
> classical or quantum, or that observables have any particular algebraic structure.
>
> In quantum mechanics, the standard example is the real vector space of self-adjoint matrices,
> ordered by positive semidefiniteness, with the identity matrix as 1. Keeping only the vector
> space, its order, and this distinguished unit gives the abstract order-unit setting.

## ii. Key results

> - `ProbabilisticTheory.exists_two_sided_bound` : every observable sits between `-(n • 1)` and
>   `n • 1`, for some `n`.
> - `ProbabilisticTheory.exists_real_shift_nonneg` : enough copies of the order unit shift any element
>   into the positive cone.
> - `ProbabilisticTheory.nonneg_add_eq_zero` : the positive cone meets its negation only at `0`.

## iv. References

## A. Ordered vector spaces and order-unit elements

**`ProbabilisticTheory.one_nonneg`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Basic.lean#L54).

> The certain outcome is nonnegative.

```lean
lemma one_nonneg : 0 ≤ (1 : P.Observables)
```

**`ProbabilisticTheory.exists_nsmul_one_le`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Basic.lean#L57).

> Every observable is bounded above by a natural multiple of the certain outcome.

```lean
lemma exists_nsmul_one_le (B : P.Observables) : ∃ n : ℕ, B ≤ n • (1 : P.Observables)
```

## B. Consequences of being an order unit

**`ProbabilisticTheory.exists_two_sided_bound`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Basic.lean#L67).

> Every element is bounded on both sides by a natural multiple of the order unit.

```lean
lemma exists_two_sided_bound (A : P.Observables) :
    ∃ n : ℕ, -(n • (1 : P.Observables)) ≤ A ∧ A ≤ n • (1 : P.Observables)
```

**`ProbabilisticTheory.exists_real_shift_nonneg`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Basic.lean#L76).

> Every element becomes nonnegative after adding enough copies of the order unit: the positive
> cone reaches everywhere, once you're allowed to shift by the unit.

```lean
lemma exists_real_shift_nonneg (A : P.Observables) : ∃ r : ℝ, 0 ≤ r • (1 : P.Observables) + A
```

**`ProbabilisticTheory.nonneg_add_eq_zero`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Basic.lean#L84).

> A nonnegative vector that adds with another nonnegative vector to `0` is itself `0`: the
> positive cone meets its negation only at `0`.

```lean
lemma nonneg_add_eq_zero {A B : P.Observables} (hA : 0 ≤ A) (hB : 0 ≤ B) (hAB : A + B = 0) :
    A = 0
```

## Depends on

- [Probabilistic theories](../basic.md)

## Sources

- [Physlib/ProbabilisticTheory/OrderUnit/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Basic.lean)
