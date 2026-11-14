---
declaration: module
origin: cited
lean: ProbabilisticTheory.Effect.instMetricSpace, ProbabilisticTheory.Effect.dist_eq_orderUnitNorm, ProbabilisticTheory.Effect.orderUnitNorm_two_smul_sub_one_le_one, ProbabilisticTheory.Effect.mem_effect_two_inv_smul_one_add, ProbabilisticTheory.Effect.two_inv_smul_one_add_two_smul_sub_one, ProbabilisticTheory.Effect.two_smul_two_inv_smul_one_add_sub_one, ProbabilisticTheory.Effect.effectEquiv
statement: formalized
proof: formalized
---

# The metric space of effects

The module `Physlib.ProbabilisticTheory.Effect.Metric`, [Physlib/ProbabilisticTheory/Effect/Metric.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Metric.lean): 7 declarations, 6 with a docstring.

> The order-unit metric on effects and their identification with the order-unit-norm ball.

## i. Overview

> Effects sit inside `E`, so pulling back the order-unit norm along the inclusion `Effect E ↪ E`
> gives them a metric space structure for free.
>
> Effects also correspond to points of the order-unit-norm ball, by the affine rescaling
> `e ↦ 2 • e - 1` that turns `[0, 1]` into the symmetric `[-1, 1]` the norm itself ranges over.

## ii. Key results

> - `Effect.dist_eq_orderUnitNorm` : the effect metric is the order-unit norm of the difference.
> - `Effect.effectEquiv` : effects correspond to points of the order-unit-norm ball.

## iv. References

> * None.

## A. The effect metric

**`ProbabilisticTheory.Effect.instMetricSpace`**, an instance, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Metric.lean#L56).

> Effects, metrized by the order-unit norm on `E`.

```lean
noncomputable scoped instance instMetricSpace : MetricSpace (Effect E)
```

**`ProbabilisticTheory.Effect.dist_eq_orderUnitNorm`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Metric.lean#L61).

```lean
lemma dist_eq_orderUnitNorm (e f : Effect E) : dist e f = orderUnitNorm ((e : E) - (f : E))
```

## B. Effects as points of the order-unit-norm ball

**`ProbabilisticTheory.Effect.orderUnitNorm_two_smul_sub_one_le_one`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Metric.lean#L71).

> Doubling and re-centering an effect at the order unit lands in the order-unit-norm ball.

```lean
lemma orderUnitNorm_two_smul_sub_one_le_one (e : Effect E) :
    orderUnitNorm (2 • (e : E) - 1) ≤ 1
```

**`ProbabilisticTheory.Effect.mem_effect_two_inv_smul_one_add`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Metric.lean#L85).

> Undoing the re-centering on a point of the order-unit-norm ball gives back an effect.

```lean
lemma mem_effect_two_inv_smul_one_add {A : E} (hA : orderUnitNorm A ≤ 1) :
    (2 : ℝ)⁻¹ • (1 + A) ∈ Effect E
```

**`ProbabilisticTheory.Effect.two_inv_smul_one_add_two_smul_sub_one`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Metric.lean#L96).

> Re-centering, then undoing it, returns the original effect.

```lean
lemma two_inv_smul_one_add_two_smul_sub_one (e : Effect E) :
    (2 : ℝ)⁻¹ • (1 + (2 • (e : E) - 1)) = (e : E)
```

**`ProbabilisticTheory.Effect.two_smul_two_inv_smul_one_add_sub_one`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Metric.lean#L102).

> Undoing the re-centering, then redoing it, returns the original ball point.

```lean
lemma two_smul_two_inv_smul_one_add_sub_one (A : E) :
    2 • ((2 : ℝ)⁻¹ • (1 + A)) - 1 = A
```

**`ProbabilisticTheory.Effect.effectEquiv`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Metric.lean#L109).

> Effects correspond to points of the order-unit-norm ball by doubling and re-centering at the
> order unit: `e ↦ 2 • e - 1`, with inverse `A ↦ (1 + A) / 2`.

```lean
noncomputable def effectEquiv : Effect E ≃ {A : E // orderUnitNorm A ≤ 1}
```

## Depends on

- [Effects](basic.md)

## Sources

- [Physlib/ProbabilisticTheory/Effect/Metric.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Metric.lean)
