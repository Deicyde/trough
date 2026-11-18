---
declaration: module
origin: cited
lean: ProbabilisticTheory.OrderedVectorSpace, ProbabilisticTheory.OrderUnitSpace, ProbabilisticTheory.instOrderUnitSpace, ProbabilisticTheory.OrderUnitSpace.exists_two_sided_bound, ProbabilisticTheory.OrderUnitSpace.exists_eq_sub_nonneg, ProbabilisticTheory.OrderUnitSpace.exists_real_shift_nonneg, ProbabilisticTheory.OrderedVectorSpace.nonneg_add_eq_zero
statement: formalized
proof: formalized
---

# Ordered vector spaces and order units

The module `Physlib.ProbabilisticTheory.OrderUnit.Basic`, [Physlib/ProbabilisticTheory/OrderUnit/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Basic.lean): 7 declarations, 7 with a docstring.

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

**`ProbabilisticTheory.OrderedVectorSpace`**, a class, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Basic.lean#L54).

> An ordered real vector space.

```lean
class OrderedVectorSpace (E : Type*) extends AddCommGroup E, PartialOrder E, Module ℝ E,
    IsOrderedAddMonoid E, PosSMulMono ℝ E
```

**`ProbabilisticTheory.OrderUnitSpace`**, a class, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Basic.lean#L60).

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

**`ProbabilisticTheory.instOrderUnitSpace`**, an instance, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Basic.lean#L67).

> The observables stored in a probabilistic theory form an order-unit space.

```lean
instance instOrderUnitSpace (P : ProbabilisticTheory) : OrderUnitSpace P.Observables
```

## B. Consequences of being an order unit

**`ProbabilisticTheory.OrderUnitSpace.exists_two_sided_bound`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Basic.lean#L82).

> Every element is bounded on both sides by a natural multiple of the order unit.

```lean
lemma exists_two_sided_bound (A : E) : ∃ n : ℕ, -(n • (1 : E)) ≤ A ∧ A ≤ n • (1 : E)
```

**`ProbabilisticTheory.OrderUnitSpace.exists_eq_sub_nonneg`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Basic.lean#L89).

> Every element is a difference of two positive elements.

```lean
lemma exists_eq_sub_nonneg (A : E) : ∃ Ap An : E, 0 ≤ Ap ∧ 0 ≤ An ∧ A = Ap - An
```

**`ProbabilisticTheory.OrderUnitSpace.exists_real_shift_nonneg`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Basic.lean#L97).

> Every element becomes nonnegative after adding enough copies of the order unit: the positive
> cone reaches everywhere, once you're allowed to shift by the unit.

```lean
lemma exists_real_shift_nonneg (A : E) : ∃ r : ℝ, 0 ≤ r • (1 : E) + A
```

**`ProbabilisticTheory.OrderedVectorSpace.nonneg_add_eq_zero`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Basic.lean#L111).

> A nonnegative vector that adds with another nonnegative vector to `0` is itself `0`: the
> positive cone meets its negation only at `0`.

```lean
lemma nonneg_add_eq_zero {A B : E} (hA : 0 ≤ A) (hB : 0 ≤ B) (hAB : A + B = 0) : A = 0
```

## Depends on

- [Probabilistic theories](../basic.md)

## Sources

- [Physlib/ProbabilisticTheory/OrderUnit/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Basic.lean)
