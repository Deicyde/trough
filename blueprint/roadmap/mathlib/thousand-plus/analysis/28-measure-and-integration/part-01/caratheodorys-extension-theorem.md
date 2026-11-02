---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.AddContent.measure, MeasureTheory.AddContent.measure_eq
mathlib_file: Mathlib/MeasureTheory/OuterMeasure/OfAddContent.lean
---

# Carathéodory's extension theorem

Mathlib records this with 2 declarations.

`MeasureTheory.AddContent.measure`: Construct a measure from a sigma-subadditive content on a semiring, assuming the semiring
generates a given measurable structure. The measure is defined on this measurable structure.

```lean
MeasureTheory.AddContent.measure.{u_1} {α : Type u_1} {C : Set (Set α)} [mα : MeasurableSpace α]
  (m : MeasureTheory.AddContent ENNReal C) (hC : MeasureTheory.IsSetSemiring C)
  (hC_gen : mα ≤ MeasurableSpace.generateFrom C) (m_sigma_subadd : m.IsSigmaSubadditive) :
  MeasureTheory.Measure α
```

`MeasureTheory.AddContent.measure_eq`: The measure defined through a sigma-subadditive
content on a semiring coincides with the content on the semiring.

```lean
MeasureTheory.AddContent.measure_eq.{u_1} {α : Type u_1} {C : Set (Set α)} {s : Set α}
  [mα : MeasurableSpace α] (m : MeasureTheory.AddContent ENNReal C)
  (hC : MeasureTheory.IsSetSemiring C) (hC_gen : mα = MeasurableSpace.generateFrom C)
  (m_sigma_subadd : m.IsSigmaSubadditive) (hs : s ∈ C) : (m.measure hC ⋯ m_sigma_subadd) s = m s
```

## Depends on

- [Carathéodory's theorem (measure theory)](caratheodorys-theorem-measure-theory.md)
- [Positive measure](../../../../overview/analysis/measures-and-integral-calculus/part-01/positive-measure.md)

## Proof depends on

- [Almost sure convergence](../../../../overview/probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Associative algebra over a commutative ring](../../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Cantor’s Theorem](../../../../hundred-theorems/part-04/cantors-theorem.md)
- [Cardinal](../../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Closure](../../../../overview/topology/general-topology/part-01/closure.md)
- [Cluster point](../../../../overview/topology/general-topology/part-01/cluster-point.md)
- [Completeness of R](../../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Continuity of monotone functions](../../../../undergraduate/single-variable-real-analysis/real-valued-functions-defined-on-a-subset-of/continuity-of-monotone-functions.md)
- [Hausdorff space](../../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Module](../../../../overview/linear-algebra/fundamentals/module.md)
- [Open map](../../../../overview/topology/general-topology/part-01/open-map.md)
- [Schroeder-Bernstein Theorem](../../../../hundred-theorems/part-02/schroeder-bernstein-theorem.md)
- [Topological module](../../../../overview/topology/topological-algebra/topological-module.md)
- [Topological ring](../../../../overview/topology/topological-algebra/topological-ring.md)
- [Uniformly continuous function](../../../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `MeasureTheory.AddContent.measure`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/OuterMeasure/OfAddContent.html#MeasureTheory.AddContent.measure)
- [Source of `MeasureTheory.AddContent.measure` in Mathlib/MeasureTheory/OuterMeasure/OfAddContent.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/OuterMeasure/OfAddContent.lean#L160)
- [Mathlib documentation: `MeasureTheory.AddContent.measure_eq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/OuterMeasure/OfAddContent.html#MeasureTheory.AddContent.measure_eq)
- [Source of `MeasureTheory.AddContent.measure_eq` in Mathlib/MeasureTheory/OuterMeasure/OfAddContent.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/OuterMeasure/OfAddContent.lean#L169)
- [1000+ theorems list: Q2631152](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2274)
- [1000+ theorems project: Q2631152](https://1000-plus.github.io/?length=-1#Q2631152)
- [Wikipedia: Carathéodory's extension theorem](https://en.wikipedia.org/wiki/Carath%C3%A9odory's_extension_theorem)
- [Wikidata: Q2631152](https://www.wikidata.org/wiki/Q2631152)
