---
declaration: module
origin: cited
lean: ProbabilisticTheory.IsJordanOrderUnit, ProbabilisticTheory.IsJordanOrderUnit.sq_nonneg
statement: formalized
proof: formalized
---

# Jordan order-unit spaces

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.Basic`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Basic.lean): 2 declarations, 2 with a docstring.

> Jordan order-unit spaces: order-unit spaces that are Jordan algebras with nonnegative squares.

## i. Overview

> Quantum observables carry, besides their order and unit, the Jordan product `a ∘ b`, a commutative
> product satisfying the Jordan identity. A Jordan order-unit space is an order-unit space that is a
> real Jordan algebra, using Mathlib's `IsCommJordan`, whose squares are nonnegative: `0 ≤ a ∘ a`. In
> the operator picture `⟪ψ, a² ψ⟫ = ‖a ψ‖² ≥ 0`.

## ii. Key results

> - `IsJordanOrderUnit` : a Jordan order-unit space.
> - `IsJordanOrderUnit.sq_nonneg` : squares are nonnegative.

## iv. References

> * None.

## A. The compatibility class

**`ProbabilisticTheory.IsJordanOrderUnit`**, a class, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Basic.lean#L49).

> A coherent unital Jordan algebra with an order unit and positive squares. Bundling the
> data-bearing algebra and order-unit parents together prevents incompatible additions, scalar
> actions, orders, or units from being selected downstream.

```lean
class IsJordanOrderUnit (E : Type*) extends NonAssocCommRing E, OrderUnitSpace E,
    SMulCommClass ℝ E E, IsScalarTower ℝ E E, IsCommJordan E where
  /-- Every Jordan square is a possible measurement outcome. -/
  mul_self_nonneg : ∀ a : E, 0 ≤ a * a
  /-- The algebra product and the distinguished order unit satisfy the complement-square
  expansion. This records the compatibility between the two data-bearing parent structures. -/
  one_sub_mul_one_sub : ∀ a : E, (1 - a) * (1 - a) = 1 - a - a + a * a
  /-- Multiplication by an order-unit complement has the expected algebraic expansion. -/
  mul_one_sub : ∀ a : E, a * (1 - a) = a - a * a
```

## B. Consequences

**`ProbabilisticTheory.IsJordanOrderUnit.sq_nonneg`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Basic.lean#L66).

> Squares are nonnegative.

```lean
lemma sq_nonneg (a : E) : 0 ≤ a * a
```

## Depends on

- [Ordered vector spaces and order units](../../../../physlib/probabilistictheory/orderunit/basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Basic.lean)
