---
declaration: module
origin: cited
lean: ProbabilisticTheory.Effect.instMetricSpace, ProbabilisticTheory.Effect.dist_eq_orderUnitNorm, ProbabilisticTheory.Effect.orderUnitNorm_two_smul_sub_one_le_one, ProbabilisticTheory.Effect.mem_effect_two_inv_smul_one_add, ProbabilisticTheory.Effect.two_inv_smul_one_add_two_smul_sub_one, ProbabilisticTheory.Effect.two_smul_two_inv_smul_one_add_sub_one, ProbabilisticTheory.Effect.effectEquiv
statement: formalized
proof: formalized
---

# The metric space of effects (Physlib)

The module `Physlib.ProbabilisticTheory.Effect.Metric`, [Physlib/ProbabilisticTheory/Effect/Metric.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Effect/Metric.lean): 7 declarations, 6 with a docstring.

> The order-unit metric on effects and their identification with the order-unit-norm ball.

## i. Overview

> Effects sit inside `P.Observables`. Pulling back the order-unit norm along this inclusion
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

**`ProbabilisticTheory.Effect.instMetricSpace`**, an instance, [line 52](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Effect/Metric.lean#L52).

> Effects, metrized by the order-unit norm on the observables.

```lean
noncomputable scoped instance instMetricSpace : MetricSpace P.Effect
```

**`ProbabilisticTheory.Effect.dist_eq_orderUnitNorm`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Effect/Metric.lean#L57).

```lean
lemma dist_eq_orderUnitNorm (e f : P.Effect) : dist e f = orderUnitNorm (e.1 - f.1)
```

## B. Effects as points of the order-unit-norm ball

**`ProbabilisticTheory.Effect.orderUnitNorm_two_smul_sub_one_le_one`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Effect/Metric.lean#L67).

> Doubling and re-centering an effect at the order unit lands in the order-unit-norm ball.

```lean
lemma orderUnitNorm_two_smul_sub_one_le_one (e : P.Effect) :
    orderUnitNorm (2 • (e : P.Observables) - 1) ≤ 1
```

**`ProbabilisticTheory.Effect.mem_effect_two_inv_smul_one_add`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Effect/Metric.lean#L81).

> Undoing the re-centering on a point of the order-unit-norm ball gives back an effect.

```lean
lemma mem_effect_two_inv_smul_one_add {A : P.Observables} (hA : orderUnitNorm A ≤ 1) :
    (2 : ℝ)⁻¹ • (1 + A) ∈ P.Effect
```

**`ProbabilisticTheory.Effect.two_inv_smul_one_add_two_smul_sub_one`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Effect/Metric.lean#L93).

> Re-centering, then undoing it, returns the original effect.

```lean
lemma two_inv_smul_one_add_two_smul_sub_one (e : P.Effect) :
    (2 : ℝ)⁻¹ • (1 + (2 • (e : P.Observables) - 1)) = (e : P.Observables)
```

**`ProbabilisticTheory.Effect.two_smul_two_inv_smul_one_add_sub_one`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Effect/Metric.lean#L99).

> Undoing the re-centering, then redoing it, returns the original ball point.

```lean
lemma two_smul_two_inv_smul_one_add_sub_one (A : P.Observables) :
    2 • ((2 : ℝ)⁻¹ • (1 + A)) - 1 = A
```

**`ProbabilisticTheory.Effect.effectEquiv`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Effect/Metric.lean#L106).

> Effects correspond to points of the order-unit-norm ball by doubling and re-centering at the
> order unit: `e ↦ 2 • e - 1`, with inverse `A ↦ (1 + A) / 2`.

```lean
noncomputable def effectEquiv : P.Effect ≃ {A : P.Observables // orderUnitNorm A ≤ 1}
```

## Depends on

- [Effects (Physlib)](basic.md)

## Sources

- [Physlib/ProbabilisticTheory/Effect/Metric.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Effect/Metric.lean)
