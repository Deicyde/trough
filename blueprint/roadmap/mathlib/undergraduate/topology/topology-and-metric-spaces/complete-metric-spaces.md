---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Metric.complete_of_cauchySeq_tendsto
mathlib_file: Mathlib/Topology/MetricSpace/Cauchy.lean
---

# Complete metric spaces

A pseudo-metric space is complete iff every Cauchy sequence converges.

```lean
Metric.complete_of_cauchySeq_tendsto.{u} {α : Type u} [PseudoMetricSpace α] :
  (∀ (u : ℕ → α), CauchySeq u → ∃ a, Filter.Tendsto u Filter.atTop (nhds a)) → CompleteSpace α
```

## Depends on

- [Bornology](../../../overview/analysis/topological-vector-spaces/bornology.md)
- [Completeness](../../../overview/topology/uniform-notions/completeness.md)
- [Order](../../single-variable-real-analysis/real-numbers/order.md)

## Sources

- [Mathlib documentation: `Metric.complete_of_cauchySeq_tendsto`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/MetricSpace/Cauchy.html#Metric.complete_of_cauchySeq_tendsto)
- [Source of `Metric.complete_of_cauchySeq_tendsto` in Mathlib/Topology/MetricSpace/Cauchy.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/MetricSpace/Cauchy.lean#L48)
- [Mathlib undergraduate list: Topology › Topology and Metric Spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L420)
