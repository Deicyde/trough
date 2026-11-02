---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.measure_zero_or_one_of_measurableSet_limsup_atTop
mathlib_file: Mathlib/Probability/Independence/ZeroOne.lean
---

# Kolmogorov's $0$-$1$ law

**Kolmogorov's 0-1 law** : any event in the tail σ-algebra of an independent sequence of
sub-σ-algebras has probability 0 or 1.
The tail σ-algebra `limsup s atTop` is the same as `⋂ n, ⋃ i ≥ n, s i`.

```lean
ProbabilityTheory.measure_zero_or_one_of_measurableSet_limsup_atTop.{u_2, u_3} {Ω : Type u_2}
  {ι : Type u_3} {s : ι → MeasurableSpace Ω} {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω}
  [SemilatticeSup ι] [NoMaxOrder ι] [Nonempty ι] (h_le : ∀ (n : ι), s n ≤ m0)
  (h_indep : ProbabilityTheory.iIndep s μ) {t : Set Ω} (ht_tail : MeasurableSet t) :
  μ t = 0 ∨ μ t = 1
```

## Depends on

- [Independent sigma-algebras](../definitions-in-probability-theory/independent-sigma-algebras.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Borel sigma-algebra](../../analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Cantor’s Theorem](../../../hundred-theorems/part-04/cantors-theorem.md)
- [Cardinal](../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Closure](../../topology/general-topology/part-01/closure.md)
- [Cluster point](../../topology/general-topology/part-01/cluster-point.md)
- [Completeness of R](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Continuity of monotone functions](../../../undergraduate/single-variable-real-analysis/real-valued-functions-defined-on-a-subset-of/continuity-of-monotone-functions.md)
- [Hausdorff space](../../topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Metric space](../../topology/metric-spaces/metric-space.md)
- [Module](../../linear-algebra/fundamentals/module.md)
- [Open map](../../topology/general-topology/part-01/open-map.md)
- [Probability measure](../definitions-in-probability-theory/probability-measure.md)
- [Schroeder-Bernstein Theorem](../../../hundred-theorems/part-02/schroeder-bernstein-theorem.md)
- [Topological module](../../topology/topological-algebra/topological-module.md)
- [Topological ring](../../topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Uniformly continuous function](../../topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.measure_zero_or_one_of_measurableSet_limsup_atTop`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Independence/ZeroOne.html#ProbabilityTheory.measure_zero_or_one_of_measurableSet_limsup_atTop)
- [Source of `ProbabilityTheory.measure_zero_or_one_of_measurableSet_limsup_atTop` in Mathlib/Probability/Independence/ZeroOne.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Probability/Independence/ZeroOne.lean#L287)
- [Mathlib overview: Probability Theory › Random variables and their laws](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L403)
- [Mathlib undergraduate list: Probability Theory › Definitions of a probability space](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L551)
