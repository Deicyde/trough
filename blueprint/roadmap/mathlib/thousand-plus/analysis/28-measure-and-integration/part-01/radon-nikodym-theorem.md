---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Measure.absolutelyContinuous_iff_withDensity_rnDeriv_eq
mathlib_file: Mathlib/MeasureTheory/Measure/Decomposition/RadonNikodym.lean
---

# Radon–Nikodym theorem

**The Radon-Nikodym theorem**: Given two measures `μ` and `ν`, if
`HaveLebesgueDecomposition μ ν`, then `μ` is absolutely continuous to `ν` if and only if
`ν.withDensity (rnDeriv μ ν) = μ`.

```lean
MeasureTheory.Measure.absolutelyContinuous_iff_withDensity_rnDeriv_eq.{u_1} {α : Type u_1}
  {m : MeasurableSpace α} {μ ν : MeasureTheory.Measure α} [μ.HaveLebesgueDecomposition ν] :
  μ.AbsolutelyContinuous ν ↔ ν.withDensity (μ.rnDeriv ν) = μ
```

## Depends on

- [Associative algebra over a commutative ring](../../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Carathéodory's theorem (measure theory)](caratheodorys-theorem-measure-theory.md)
- [Integral of positive measurable functions](../../../../overview/analysis/measures-and-integral-calculus/part-01/integral-of-positive-measurable-functions.md)
- [Linear map](../../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Measurable function](../../../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)

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

- [Mathlib documentation: `MeasureTheory.Measure.absolutelyContinuous_iff_withDensity_rnDeriv_eq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/Decomposition/RadonNikodym.html#MeasureTheory.Measure.absolutelyContinuous_iff_withDensity_rnDeriv_eq)
- [Source of `MeasureTheory.Measure.absolutelyContinuous_iff_withDensity_rnDeriv_eq` in Mathlib/MeasureTheory/Measure/Decomposition/RadonNikodym.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Measure/Decomposition/RadonNikodym.lean#L66)
- [1000+ theorems list: Q1191319](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1506)
- [1000+ theorems project: Q1191319](https://1000-plus.github.io/?length=-1#Q1191319)
- [Wikipedia: Radon–Nikodym theorem](https://en.wikipedia.org/wiki/Radon%E2%80%93Nikodym_theorem)
- [Wikidata: Q1191319](https://www.wikidata.org/wiki/Q1191319)
