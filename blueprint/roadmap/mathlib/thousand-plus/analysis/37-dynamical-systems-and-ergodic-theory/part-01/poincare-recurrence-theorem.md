---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Conservative.ae_mem_imp_frequently_image_mem
mathlib_file: Mathlib/Dynamics/Ergodic/Conservative.lean
---

# Poincaré recurrence theorem

Poincaré recurrence theorem: given a conservative map `f` and a measurable set `s`,
almost every point `x ∈ s` returns back to `s` infinitely many times.

```lean
MeasureTheory.Conservative.ae_mem_imp_frequently_image_mem.{u_1} {α : Type u_1} [MeasurableSpace α]
  {f : α → α} {s : Set α} {μ : MeasureTheory.Measure α} (hf : MeasureTheory.Conservative f μ)
  (hs : MeasureTheory.NullMeasurableSet s μ) :
  ∀ᵐ (x : α) ∂μ, x ∈ s → ∃ᶠ (n : ℕ) in Filter.atTop, f^[n] x ∈ s
```

## Depends on

- [Almost sure convergence](../../../../overview/probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Associative algebra over a commutative ring](../../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Carathéodory's theorem (measure theory)](../../28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)
- [Linear map](../../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Measurable function](../../../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)
- [Positive measure](../../../../overview/analysis/measures-and-integral-calculus/part-01/positive-measure.md)

## Proof depends on

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

- [Mathlib documentation: `MeasureTheory.Conservative.ae_mem_imp_frequently_image_mem`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Dynamics/Ergodic/Conservative.html#MeasureTheory.Conservative.ae_mem_imp_frequently_image_mem)
- [Source of `MeasureTheory.Conservative.ae_mem_imp_frequently_image_mem` in Mathlib/Dynamics/Ergodic/Conservative.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Dynamics/Ergodic/Conservative.lean#L156)
- [1000+ theorems list: Q226014](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L247)
- [1000+ theorems project: Q226014](https://1000-plus.github.io/?length=-1#Q226014)
- [Wikipedia: Poincaré recurrence theorem](https://en.wikipedia.org/wiki/Poincar%C3%A9_recurrence_theorem)
- [Wikidata: Q226014](https://www.wikidata.org/wiki/Q226014)
