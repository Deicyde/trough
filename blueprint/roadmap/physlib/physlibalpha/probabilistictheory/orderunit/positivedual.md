---
declaration: module
origin: cited
lean: ProbabilisticTheory.OrderUnitSpace.isOrderUnit_one, PositiveLinearMap.eq_zero_of_map_one_eq_zero
statement: formalized
proof: formalized
---

# The unit of an order-unit space as an order unit

The module `PhyslibAlpha.ProbabilisticTheory.OrderUnit.PositiveDual`, [PhyslibAlpha/ProbabilisticTheory/OrderUnit/PositiveDual.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/PositiveDual.lean): 3 declarations (1 instance with no name), 3 with a docstring.

> The unit of an order-unit space is an order unit, so weight-zero positive functionals vanish.

## i. Overview

> The unit of an order-unit space is an order unit of the underlying ordered vector space, so the
> general order theory of positive functionals applies to observables. In particular a positive
> functional that vanishes on the unit vanishes everywhere.

## ii. Key results

> - `OrderUnitSpace.isOrderUnit_one` : the unit is an order unit.
> - `PositiveLinearMap.eq_zero_of_map_one_eq_zero` : a positive functional of total weight zero
>   vanishes.

## iv. References

> * None.

## A. The unit as an order unit

**`ProbabilisticTheory.OrderUnitSpace.isOrderUnit_one`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/PositiveDual.lean#L51).

> The unit is an order unit: nonnegative, and every observable lies below a multiple of it.

```lean
lemma isOrderUnit_one : IsOrderUnit (1 : E)
```

**An instance with no name**, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/PositiveDual.lean#L54).

> Any two observables lie below a common one.

```lean
instance : IsDirectedOrder E
```

## B. Positive functionals

**`PositiveLinearMap.eq_zero_of_map_one_eq_zero`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/PositiveDual.lean#L61).

> A positive functional with total weight zero vanishes.

```lean
lemma _root_.PositiveLinearMap.eq_zero_of_map_one_eq_zero {E : Type*} [OrderUnitSpace E]
    {ψ : E →ₚ[ℝ] ℝ} (h : ψ 1 = 0) : ψ = 0
```

## Depends on

- [Ordered vector spaces and order units](../../../physlib/probabilistictheory/orderunit/basic.md)
- [Strong units](../../mathematics/part-02/order/strongunit.md)

## Proof depends on

- [Positive functionals](../../mathematics/part-02/order/positivedual-basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/OrderUnit/PositiveDual.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/PositiveDual.lean)
