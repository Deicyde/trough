---
declaration: module
origin: cited
lean: PhyslibAlpha.ProbabilisticTheory.OrderedVectorSpace, PhyslibAlpha.ProbabilisticTheory.OrderUnitSpace, PhyslibAlpha.ProbabilisticTheory.OrderUnitSpace.exists_two_sided_bound, PhyslibAlpha.ProbabilisticTheory.OrderUnitSpace.exists_eq_sub_nonneg, PhyslibAlpha.ProbabilisticTheory.OrderUnitSpace.exists_real_shift_nonneg, PhyslibAlpha.ProbabilisticTheory.OrderedVectorSpace.nonneg_add_eq_zero
statement: formalized
proof: formalized
---

# Ordered vector spaces and order units (PhyslibAlpha)

The module `PhyslibAlpha.ProbabilisticTheory.OrderUnit.Basic`, [PhyslibAlpha/ProbabilisticTheory/OrderUnit/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Basic.lean): 6 declarations, 6 with a docstring.

## i. Overview

> Order-unit spaces capture the basic structure needed for a probabilistic theory: observables,
> positivity, effects, states and probabilities. They do this without assuming that the theory is
> classical or quantum, or that observables have any particular algebraic structure.
>
> In quantum mechanics, the standard example is the real vector space of self-adjoint matrices,
> ordered by positive semidefiniteness, with the identity matrix as 1. Keeping only the vector
> space, its order, and this distinguished unit gives the abstract order-unit setting.

## ii. Key results

> - `OrderUnitSpace.exists_two_sided_bound` : every observable sits between `-(n • 1)` and `n • 1`,
>   for some `n`.
> - `OrderUnitSpace.exists_eq_sub_nonneg` : every observable is a difference of two positive
>   observables.
> - `OrderUnitSpace.exists_real_shift_nonneg` : enough copies of the order unit shift any element
>   into the positive cone.
> - `OrderedVectorSpace.nonneg_add_eq_zero` : the positive cone meets its negation only at `0`.

## iv. References

## A. Ordered vector spaces and order-unit elements

**`PhyslibAlpha.ProbabilisticTheory.OrderedVectorSpace`**, a class, [line 56](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Basic.lean#L56).

> An ordered real vector space.

```lean
class OrderedVectorSpace (E : Type*) extends AddCommGroup E, PartialOrder E, Module ℝ E,
    IsOrderedAddMonoid E, PosSMulMono ℝ E
```

**`PhyslibAlpha.ProbabilisticTheory.OrderUnitSpace`**, a class, [line 62](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Basic.lean#L62).

> An ordered real vector space whose distinguished element `1` is an order unit: it is
> nonnegative, and every element is bounded above by a natural multiple of it. No multiplication is
> assumed.

```lean
class OrderUnitSpace (E : Type*) extends OrderedVectorSpace E, One E where
  /-- The distinguished unit is nonnegative. -/
  one_nonneg : 0 ≤ (1 : E)
  /-- Every element is bounded above by a natural multiple of the order unit. -/
  exists_nsmul_one_le : ∀ B : E, ∃ n : ℕ, B ≤ n • (1 : E)
```

## B. Consequences of being an order unit

**`PhyslibAlpha.ProbabilisticTheory.OrderUnitSpace.exists_two_sided_bound`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Basic.lean#L79).

> Every element is bounded on both sides by a natural multiple of the order unit.

```lean
lemma exists_two_sided_bound (A : E) : ∃ n : ℕ, -(n • (1 : E)) ≤ A ∧ A ≤ n • (1 : E)
```

**`PhyslibAlpha.ProbabilisticTheory.OrderUnitSpace.exists_eq_sub_nonneg`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Basic.lean#L86).

> Every element is a difference of two positive elements.

```lean
lemma exists_eq_sub_nonneg (A : E) : ∃ Ap An : E, 0 ≤ Ap ∧ 0 ≤ An ∧ A = Ap - An
```

**`PhyslibAlpha.ProbabilisticTheory.OrderUnitSpace.exists_real_shift_nonneg`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Basic.lean#L94).

> Every element becomes nonnegative after adding enough copies of the order unit: the positive
> cone reaches everywhere, once you're allowed to shift by the unit.

```lean
lemma exists_real_shift_nonneg (A : E) : ∃ r : ℝ, 0 ≤ r • (1 : E) + A
```

**`PhyslibAlpha.ProbabilisticTheory.OrderedVectorSpace.nonneg_add_eq_zero`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Basic.lean#L108).

> A nonnegative vector that adds with another nonnegative vector to `0` is itself `0`: the
> positive cone meets its negation only at `0`.

```lean
lemma nonneg_add_eq_zero {A B : E} (hA : 0 ≤ A) (hB : 0 ≤ B) (hAB : A + B = 0) : A = 0
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ProbabilisticTheory/OrderUnit/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Basic.lean)
