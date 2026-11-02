---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Besicovitch.exists_disjoint_closedBall_covering_ae
mathlib_file: Mathlib/MeasureTheory/Covering/Besicovitch.lean
---

# Besicovitch covering theorem

The measurable **Besicovitch covering theorem**.

Assume that, for any `x` in a set `s`, one is given a set of admissible closed balls centered at
`x`, with arbitrarily small radii. Then there exists a disjoint covering of almost all `s` by
admissible closed balls centered at some points of `s`. We can even require that the radius at `x`
is bounded by a given function `R x`. (Take `R = 1` if you don't need this additional feature).

This version requires the underlying measure to be sigma-finite, and the space to have the
Besicovitch covering property (which is satisfied for instance by normed real vector spaces).

```lean
Besicovitch.exists_disjoint_closedBall_covering_ae.{u_1} {α : Type u_1} [MetricSpace α]
  [SecondCountableTopology α] [MeasurableSpace α] [OpensMeasurableSpace α]
  [HasBesicovitchCovering α] (μ : MeasureTheory.Measure α) [MeasureTheory.SFinite μ] (f : α → Set ℝ)
  (s : Set α) (hf : ∀ x ∈ s, ∀ δ > 0, (f x ∩ Set.Ioo 0 δ).Nonempty) (R : α → ℝ)
  (hR : ∀ x ∈ s, 0 < R x) :
  ∃ t r,
    t.Countable ∧
      t ⊆ s ∧
        (∀ x ∈ t, r x ∈ f x ∩ Set.Ioo 0 (R x)) ∧
          μ (s \ ⋃ x ∈ t, Metric.closedBall x (r x)) = 0 ∧
            t.PairwiseDisjoint fun x => Metric.closedBall x (r x)
```

## Depends on

- [Carathéodory's theorem (measure theory)](../../28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)
- [Metric space](../../../../overview/topology/metric-spaces/metric-space.md)
- [Positive measure](../../../../overview/analysis/measures-and-integral-calculus/part-01/positive-measure.md)

## Proof depends on

- [Almost sure convergence](../../../../overview/probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Associative algebra over a commutative ring](../../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Cantor’s Theorem](../../../../hundred-theorems/part-04/cantors-theorem.md)
- [Cardinal](../../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Closure](../../../../overview/topology/general-topology/part-01/closure.md)
- [Cluster point](../../../../overview/topology/general-topology/part-01/cluster-point.md)
- [Completeness of R](../../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Continuity of monotone functions](../../../../undergraduate/single-variable-real-analysis/real-valued-functions-defined-on-a-subset-of-r/continuity-of-monotone-functions.md)
- [Hausdorff space](../../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Module](../../../../overview/linear-algebra/fundamentals/module.md)
- [Open map](../../../../overview/topology/general-topology/part-01/open-map.md)
- [Ordinal](../../../../overview/logic-and-computation/set-theory/ordinals/ordinal.md)
- [Schroeder-Bernstein Theorem](../../../../hundred-theorems/part-02/schroeder-bernstein-theorem.md)
- [Topological module](../../../../overview/topology/topological-algebra/topological-module.md)
- [Topological ring](../../../../overview/topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Uniformly continuous function](../../../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `Besicovitch.exists_disjoint_closedBall_covering_ae`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Covering/Besicovitch.html#Besicovitch.exists_disjoint_closedBall_covering_ae)
- [Source of `Besicovitch.exists_disjoint_closedBall_covering_ae` in Mathlib/MeasureTheory/Covering/Besicovitch.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Covering/Besicovitch.lean#L823)
- [1000+ theorems list: Q137164](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L56)
- [1000+ theorems project: Q137164](https://1000-plus.github.io/?length=-1#Q137164)
- [Wikipedia: Besicovitch covering theorem](https://en.wikipedia.org/wiki/Besicovitch_covering_theorem)
- [Wikidata: Q137164](https://www.wikidata.org/wiki/Q137164)
