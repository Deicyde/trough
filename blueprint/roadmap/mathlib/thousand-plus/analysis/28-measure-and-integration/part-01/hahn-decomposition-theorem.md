---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.SignedMeasure.exists_isCompl_positive_negative
mathlib_file: Mathlib/MeasureTheory/VectorMeasure/Decomposition/Hahn.lean
---

# Hahn decomposition theorem

**The Hahn decomposition theorem**: Given a signed measure `s`, there exist
complement measurable sets `i` and `j` such that `i` is positive, `j` is negative.

```lean
MeasureTheory.SignedMeasure.exists_isCompl_positive_negative.{u_1} {α : Type u_1}
  [MeasurableSpace α] (s : MeasureTheory.SignedMeasure α) :
  ∃ i j,
    MeasurableSet i ∧
      MeasureTheory.VectorMeasure.restrict 0 i ≤ MeasureTheory.VectorMeasure.restrict s i ∧
        MeasurableSet j ∧
          MeasureTheory.VectorMeasure.restrict s j ≤ MeasureTheory.VectorMeasure.restrict 0 j ∧
            IsCompl i j
```

## Depends on

- [Bornology](../../../../overview/analysis/topological-vector-spaces/bornology.md)
- [Events](../../../../undergraduate/probability-theory/definitions-of-a-probability-space/events.md)
- [Infinite sum](../../../../overview/topology/topological-algebra/infinite-sum.md)
- [Order (Real numbers)](../../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)
- [Uniform space](../../../../overview/topology/uniform-notions/uniform-space.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Closure](../../../../overview/topology/general-topology/part-01/closure.md)
- [Cluster point](../../../../overview/topology/general-topology/part-01/cluster-point.md)
- [Completeness of R](../../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Hausdorff space](../../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Metric structure](../../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Module](../../../../overview/linear-algebra/fundamentals/module.md)
- [Order topology](../../../../overview/topology/topological-algebra/order-topology.md)
- [Uniformly continuous function](../../../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `MeasureTheory.SignedMeasure.exists_isCompl_positive_negative`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/VectorMeasure/Decomposition/Hahn.html#MeasureTheory.SignedMeasure.exists_isCompl_positive_negative)
- [Source of `MeasureTheory.SignedMeasure.exists_isCompl_positive_negative` in Mathlib/MeasureTheory/VectorMeasure/Decomposition/Hahn.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/VectorMeasure/Decomposition/Hahn.lean#L407)
- [1000+ theorems list: Q1568811](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1778)
- [1000+ theorems project: Q1568811](https://1000-plus.github.io/?length=-1#Q1568811)
- [Wikipedia: Hahn decomposition theorem](https://en.wikipedia.org/wiki/Hahn_decomposition_theorem)
- [Wikidata: Q1568811](https://www.wikidata.org/wiki/Q1568811)
