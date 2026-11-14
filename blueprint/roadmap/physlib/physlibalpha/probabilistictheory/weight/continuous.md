---
declaration: module
origin: cited
lean: PositiveLinearMap.abs_apply_le_apply_one_mul_orderUnitNorm, PositiveLinearMap.toOrderUnitContinuousLinearMap, PositiveLinearMap.toOrderUnitContinuousLinearMap_apply, ProbabilisticTheory.Weight.IsFinite.toOrderUnitContinuousLinearMap, ProbabilisticTheory.Weight.IsFinite.toOrderUnitContinuousLinearMap_apply_of_nonneg
statement: formalized
proof: formalized
---

# Finite weights are continuous

The module `PhyslibAlpha.ProbabilisticTheory.Weight.Continuous`, [PhyslibAlpha/ProbabilisticTheory/Weight/Continuous.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Continuous.lean): 5 declarations, 3 with a docstring.

> Positive functionals are order-unit-norm bounded, so finite weights are continuous functionals.

## i. Overview

> A positive functional is bounded for the order-unit norm, `|ψ a| ≤ ψ 1 ‖a‖`. So every finite weight
> is a continuous linear functional on the observables with the order-unit norm.

## ii. Key results

> - `PositiveLinearMap.abs_apply_le_apply_one_mul_orderUnitNorm` : `|ψ a| ≤ ψ 1 ‖a‖`.
> - `Weight.IsFinite.toOrderUnitContinuousLinearMap` : a finite weight as a continuous functional.

## iv. References

> * None.

## A. Positive functionals are bounded

**`PositiveLinearMap.abs_apply_le_apply_one_mul_orderUnitNorm`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Continuous.lean#L56).

> A positive functional is order-unit-norm bounded, with bound given by its value at the order
> unit.  For a normalized positive functional this specializes to the contractive state bound.

```lean
lemma abs_apply_le_apply_one_mul_orderUnitNorm (f : E →ₚ[ℝ] ℝ) (x : E) :
    |f x| ≤ f 1 * orderUnitNorm x
```

**`PositiveLinearMap.toOrderUnitContinuousLinearMap`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Continuous.lean#L73).

> A positive functional as a continuous functional on the canonical order-unit-norm copy.

```lean
noncomputable def toOrderUnitContinuousLinearMap (f : E →ₚ[ℝ] ℝ) :
    WithOrderUnitNorm E →L[ℝ] ℝ
```

**`PositiveLinearMap.toOrderUnitContinuousLinearMap_apply`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Continuous.lean#L81).

```lean
lemma toOrderUnitContinuousLinearMap_apply (f : E →ₚ[ℝ] ℝ) (x : E) :
    f.toOrderUnitContinuousLinearMap x = f x
```

## B. Finite weights as continuous functionals

**`ProbabilisticTheory.Weight.IsFinite.toOrderUnitContinuousLinearMap`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Continuous.lean#L101).

> The canonical continuous linear extension of a finite weight to the order-unit-norm copy.

```lean
noncomputable def toOrderUnitContinuousLinearMap {w : Weight E} (hw : w.IsFinite) :
    WithOrderUnitNorm E →L[ℝ] ℝ
```

**`ProbabilisticTheory.Weight.IsFinite.toOrderUnitContinuousLinearMap_apply_of_nonneg`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Continuous.lean#L105).

```lean
lemma toOrderUnitContinuousLinearMap_apply_of_nonneg {w : Weight E} (hw : w.IsFinite)
    (x : PosCone E) :
    hw.toOrderUnitContinuousLinearMap (x : E) = (w x).toReal
```

## Depends on

- [The canonical normed copy of an order-unit space](../orderunit/normed.md)
- [Extending finite weights (PhyslibAlpha)](extension.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Weight/Continuous.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Continuous.lean)
