# Uniformly continuous function

Mathlib states this as `Metric.uniformContinuous_iff`.

```lean
Metric.uniformContinuous_iff.{u, v} {α : Type u} {β : Type v} [PseudoMetricSpace α]
  [PseudoMetricSpace β] {f : α → β} :
  UniformContinuous f ↔ ∀ ε > 0, ∃ δ > 0, ∀ ⦃a b : α⦄, dist a b < δ → dist (f a) (f b) < ε
```

## Depends on

- [Bornology](../../analysis/topological-vector-spaces/bornology.md)
- [Order](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)

## Proof depends on

- [Field $\R$ of real numbers](../../../undergraduate/ring-theory/field-theory/field-r-of-real-numbers.md)
- [Ordered ring](../../general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `Metric.uniformContinuous_iff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/MetricSpace/Pseudo/Defs.html#Metric.uniformContinuous_iff)
- [Source of `Metric.uniformContinuous_iff` in Mathlib/Topology/MetricSpace/Pseudo/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/MetricSpace/Pseudo/Defs.lean#L758)
- [Mathlib overview: Topology › Uniform notions](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L239)
- [Mathlib undergraduate list: Topology › Topology and Metric Spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L418)
