---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Metric.isOpen_iff
mathlib_file: Mathlib/Topology/MetricSpace/Pseudo/Defs.lean
---

# Topology of a metric space

Mathlib states this as `Metric.isOpen_iff`.

```lean
Metric.isOpen_iff.{u} {α : Type u} [PseudoMetricSpace α] {s : Set α} :
  IsOpen s ↔ ∀ x ∈ s, ∃ ε > 0, Metric.ball x ε ⊆ s
```

## Depends on

- [Ball](../../../overview/topology/metric-spaces/ball.md)

## Proof depends on

- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Field $\R$ of real numbers](../../ring-theory/field-theory/part-01/field-of-real-numbers.md)
- [Group](../../../overview/general-algebra/group-theory/part-01/group.md)
- [Group morphism](../../../overview/general-algebra/group-theory/part-01/group-morphism.md)
- [Invertible elements](../../ring-theory/divisibility-in-integral-domains/invertible-elements.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)
- [Permutation group of a type](../../../overview/general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Product of rings](../../ring-theory/fundamentals/product-of-rings.md)
- [Ring structure $\Z$](../../ring-theory/fundamentals/ring-structure.md)

## Sources

- [Mathlib documentation: `Metric.isOpen_iff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/MetricSpace/Pseudo/Defs.html#Metric.isOpen_iff)
- [Source of `Metric.isOpen_iff` in Mathlib/Topology/MetricSpace/Pseudo/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/MetricSpace/Pseudo/Defs.lean#L836)
- [Mathlib undergraduate list: Topology › Topology and Metric Spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L405)
