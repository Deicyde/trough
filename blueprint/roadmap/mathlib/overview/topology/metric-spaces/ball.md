# Ball

`ball x ε` is the set of all points `y` with `dist y x < ε`

```lean
Metric.ball.{u} {α : Type u} [PseudoMetricSpace α] (x : α) (ε : ℝ) : Set α
```

## Depends on

- [Bornology](../../analysis/topological-vector-spaces/bornology.md)
- [Order](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)

## Sources

- [Mathlib documentation: `Metric.ball`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/MetricSpace/Pseudo/Defs.html#Metric.ball)
- [Source of `Metric.ball` in Mathlib/Topology/MetricSpace/Pseudo/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Topology/MetricSpace/Pseudo/Defs.lean#L367)
- [Mathlib overview: Topology › Metric spaces](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L261)
