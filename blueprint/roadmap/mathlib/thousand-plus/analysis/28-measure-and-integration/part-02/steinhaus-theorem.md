---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Measure.div_mem_nhds_one_of_haar_pos
mathlib_file: Mathlib/MeasureTheory/Measure/Haar/Basic.lean
---

# Steinhaus theorem

**Steinhaus Theorem**.

In any locally compact group `G` with an inner regular Haar measure `μ`,
for any measurable set `E` of positive measure, the set `E / E` is a neighbourhood of `1`.

```lean
MeasureTheory.Measure.div_mem_nhds_one_of_haar_pos.{u_1} {G : Type u_1} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [MeasurableSpace G] [BorelSpace G]
  (μ : MeasureTheory.Measure G) [μ.IsHaarMeasure] [LocallyCompactSpace G] [μ.InnerRegular]
  (E : Set G) (hE : MeasurableSet E) (hEpos : 0 < μ E) : E / E ∈ nhds 1
```

## Depends on

- [Almost sure convergence](../../../../overview/probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Associative algebra over a commutative ring](../../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Borel sigma-algebra](../../../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Carathéodory's theorem (measure theory)](../part-01/caratheodorys-theorem-measure-theory.md)
- [Compactness in terms of filters](../../../../overview/topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Linear map](../../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Measurable function](../../../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)
- [Positive measure](../../../../overview/analysis/measures-and-integral-calculus/part-01/positive-measure.md)
- [Topological group](../../../../overview/topology/topological-algebra/topological-group.md)

## Proof depends on

- [Closure](../../../../overview/topology/general-topology/part-01/closure.md)

## Sources

- [Mathlib documentation: `MeasureTheory.Measure.div_mem_nhds_one_of_haar_pos`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/Haar/Basic.html#MeasureTheory.Measure.div_mem_nhds_one_of_haar_pos)
- [Source of `MeasureTheory.Measure.div_mem_nhds_one_of_haar_pos` in Mathlib/MeasureTheory/Measure/Haar/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Measure/Haar/Basic.lean#L629)
- [1000+ theorems list: Q3527166](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2515)
- [1000+ theorems project: Q3527166](https://1000-plus.github.io/all.html?length=-1#Q3527166)
- [Wikipedia: Steinhaus theorem](https://en.wikipedia.org/wiki/Steinhaus_theorem)
- [Wikidata: Q3527166](https://www.wikidata.org/wiki/Q3527166)
