---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Vitali.exists_disjoint_covering_ae
mathlib_file: Mathlib/MeasureTheory/Covering/Vitali.lean
---

# Vitali covering theorem

The measurable **Vitali covering theorem**.

Assume one is given a family `t` of closed sets with nonempty interior, such that each `a ∈ t` is
included in a ball `B (x, r)` and covers a definite proportion of the ball `B (x, 3 r)` for a given
measure `μ` \(think of the situation where `μ` is a doubling measure and `t` is a family of balls\).
Consider a \(possibly non-measurable\) set `s` at which the family is fine, i.e., every point of `s`
belongs to arbitrarily small elements of `t`. Then one can extract from `t` a disjoint subfamily
that covers almost all `s`.

For more flexibility, we give a statement with a parameterized family of sets.

```lean
Vitali.exists_disjoint_covering_ae.{u_1, u_2} {α : Type u_1} {ι : Type u_2} [PseudoMetricSpace α]
  [MeasurableSpace α] [OpensMeasurableSpace α] [SecondCountableTopology α]
  (μ : MeasureTheory.Measure α) [MeasureTheory.IsLocallyFiniteMeasure μ] (s : Set α) (t : Set ι)
  (C : NNReal) (r : ι → ℝ) (c : ι → α) (B : ι → Set α)
  (hB : ∀ a ∈ t, B a ⊆ Metric.closedBall (c a) (r a))
  (μB : ∀ a ∈ t, μ (Metric.closedBall (c a) (3 * r a)) ≤ ↑C * μ (B a))
  (ht : ∀ a ∈ t, (interior (B a)).Nonempty) (h't : ∀ a ∈ t, IsClosed (B a))
  (hf : ∀ x ∈ s, ∀ ε > 0, ∃ a ∈ t, r a ≤ ε ∧ c a = x) :
  ∃ u ⊆ t, u.Countable ∧ u.PairwiseDisjoint B ∧ μ (s \ ⋃ a ∈ u, B a) = 0
```

## Depends on

- [Bornology](../../../../overview/analysis/topological-vector-spaces/bornology.md)
- [Positive measure](../../../../overview/analysis/measures-and-integral-calculus/part-01/positive-measure.md)
- [Uniform space](../../../../overview/topology/uniform-notions/uniform-space.md)

## Proof depends on

- [Ball](../../../../overview/topology/metric-spaces/ball.md)
- [Characteristic zero](../../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Closure](../../../../overview/topology/general-topology/part-01/closure.md)
- [Field $\R$ of real numbers](../../../../undergraduate/ring-theory/field-theory/part-01/field-r-of-real-numbers.md)
- [Order topology](../../../../overview/topology/topological-algebra/order-topology.md)
- [Topological ring](../../../../overview/topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `Vitali.exists_disjoint_covering_ae`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Covering/Vitali.html#Vitali.exists_disjoint_covering_ae)
- [Source of `Vitali.exists_disjoint_covering_ae` in Mathlib/MeasureTheory/Covering/Vitali.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Covering/Vitali.lean#L229)
- [1000+ theorems list: Q3229352](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2367)
- [1000+ theorems project: Q3229352](https://1000-plus.github.io/?length=-1#Q3229352)
- [Wikipedia: Vitali covering theorem](https://en.wikipedia.org/wiki/Vitali_covering_theorem)
- [Wikidata: Q3229352](https://www.wikidata.org/wiki/Q3229352)
