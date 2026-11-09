# Topology of a metric space

Mathlib states this as `Metric.isOpen_iff`.

```lean
Metric.isOpen_iff.{u} {α : Type u} [PseudoMetricSpace α] {s : Set α} :
  IsOpen s ↔ ∀ x ∈ s, ∃ ε > 0, Metric.ball x ε ⊆ s
```

## Depends on

- [Ball](../../../overview/topology/metric-spaces/ball.md)

## Proof depends on

- [Field $\R$ of real numbers](../../ring-theory/field-theory/field-r-of-real-numbers.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `Metric.isOpen_iff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/MetricSpace/Pseudo/Defs.html#Metric.isOpen_iff)
- [Source of `Metric.isOpen_iff` in Mathlib/Topology/MetricSpace/Pseudo/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/MetricSpace/Pseudo/Defs.lean#L836)
- [Mathlib undergraduate list: Topology › Topology and Metric Spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L405)
