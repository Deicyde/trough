---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.cond_eq_inv_mul_cond_mul
mathlib_file: Mathlib/Probability/ConditionalProbability.lean
---

# Bayes' theorem

**Bayes' Theorem**

```lean
ProbabilityTheory.cond_eq_inv_mul_cond_mul.{u_1} {Ω : Type u_1} {m : MeasurableSpace Ω}
  {s t : Set Ω} (hms : MeasurableSet s) (hmt : MeasurableSet t) (μ : MeasureTheory.Measure Ω)
  [MeasureTheory.IsFiniteMeasure μ] : μ[t | s] = (μ s)⁻¹ * μ[s | t] * μ t
```

## Depends on

- [Conditional probability](../../../../overview/probability-theory/definitions-in-probability-theory/conditional-probability.md)

## Proof depends on

- [Almost sure convergence](../../../../overview/probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Cantor’s Theorem](../../../../hundred-theorems/part-04/cantors-theorem.md)
- [Cardinal](../../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Closure](../../../../overview/topology/general-topology/part-01/closure.md)
- [Cluster point](../../../../overview/topology/general-topology/part-01/cluster-point.md)
- [Completeness of R](../../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Continuity of monotone functions](../../../../undergraduate/single-variable-real-analysis/real-valued-functions-defined-on-a-subset-of/continuity-of-monotone-functions.md)
- [Hausdorff space](../../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Open map](../../../../overview/topology/general-topology/part-01/open-map.md)
- [Schroeder-Bernstein Theorem](../../../../hundred-theorems/part-02/schroeder-bernstein-theorem.md)
- [Topological module](../../../../overview/topology/topological-algebra/topological-module.md)
- [Topological ring](../../../../overview/topology/topological-algebra/topological-ring.md)
- [Uniformly continuous function](../../../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.cond_eq_inv_mul_cond_mul`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/ConditionalProbability.html#ProbabilityTheory.cond_eq_inv_mul_cond_mul)
- [Source of `ProbabilityTheory.cond_eq_inv_mul_cond_mul` in Mathlib/Probability/ConditionalProbability.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Probability/ConditionalProbability.lean#L272)
- [1000+ theorems list: Q182505](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L108)
- [1000+ theorems project: Q182505](https://1000-plus.github.io/?length=-1#Q182505)
- [Wikipedia: Bayes' theorem](https://en.wikipedia.org/wiki/Bayes'_theorem)
- [Wikidata: Q182505](https://www.wikidata.org/wiki/Q182505)
