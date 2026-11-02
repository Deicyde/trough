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
- [Cauchy sequence](../../../overview/topology/uniform-notions/cauchy-sequence.md)
- [Completeness](../../../overview/topology/uniform-notions/completeness.md)
- [Order](../../single-variable-real-analysis/real-numbers/order.md)

## Proof depends on

- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Continuous function](../../../overview/topology/general-topology/part-01/continuous-function.md)
- [Field $\R$ of real numbers](../../ring-theory/field-theory/part-01/field-of-real-numbers.md)
- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Group](../../../overview/general-algebra/group-theory/part-01/group.md)
- [Induced topology](../../../overview/topology/general-topology/part-01/induced-topology.md)
- [Invertible elements](../../ring-theory/divisibility-in-integral-domains/invertible-elements.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)
- [Permutation group of a type](../../../overview/general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Product of rings](../../ring-theory/fundamentals/product-of-rings.md)
- [Ring morphism](../../../overview/general-algebra/rings/ring-morphism.md)
- [Ring structure $\Z$](../../ring-theory/fundamentals/ring-structure.md)

## Sources

- [Mathlib documentation: `Metric.complete_of_cauchySeq_tendsto`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/MetricSpace/Cauchy.html#Metric.complete_of_cauchySeq_tendsto)
- [Source of `Metric.complete_of_cauchySeq_tendsto` in Mathlib/Topology/MetricSpace/Cauchy.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/MetricSpace/Cauchy.lean#L48)
- [Mathlib undergraduate list: Topology › Topology and Metric Spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L420)
