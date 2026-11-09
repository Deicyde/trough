# Limits of sequences

Mathlib states this as `Metric.tendsto_atTop`.

```lean
Metric.tendsto_atTop.{u, v} {α : Type u} {β : Type v} [PseudoMetricSpace α] [Nonempty β]
  [SemilatticeSup β] {u : β → α} {a : α} :
  Filter.Tendsto u Filter.atTop (nhds a) ↔ ∀ ε > 0, ∃ N, ∀ n ≥ N, dist (u n) a < ε
```

## Depends on

- [Bornology](../../../overview/analysis/topological-vector-spaces/bornology.md)
- [Order](../../single-variable-real-analysis/real-numbers/order.md)

## Proof depends on

- [Ball](../../../overview/topology/metric-spaces/ball.md)
- [Field $\R$ of real numbers](../../ring-theory/field-theory/field-r-of-real-numbers.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `Metric.tendsto_atTop`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/MetricSpace/Pseudo/Defs.html#Metric.tendsto_atTop)
- [Source of `Metric.tendsto_atTop` in Mathlib/Topology/MetricSpace/Pseudo/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/MetricSpace/Pseudo/Defs.lean#L911)
- [Mathlib undergraduate list: Topology › Topology and Metric Spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L408)
