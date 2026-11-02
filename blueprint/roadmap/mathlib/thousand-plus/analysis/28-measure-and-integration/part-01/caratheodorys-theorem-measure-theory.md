---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.OuterMeasure.caratheodory
mathlib_file: Mathlib/MeasureTheory/OuterMeasure/Caratheodory.lean
---

# Carathéodory's theorem (measure theory)

Given an outer measure `μ`, the Carathéodory-measurable space is
defined such that `s` is measurable if `∀ t, μ t = μ (t ∩ s) + μ (t \ s)`.

```lean
MeasureTheory.OuterMeasure.caratheodory.{u} {α : Type u} (m : MeasureTheory.OuterMeasure α) :
  MeasurableSpace α
```

Hard to say what exactly is meant.

## Depends on

- [Infinite sum](../../../../overview/topology/topological-algebra/infinite-sum.md)
- [Ordered ring](../../../../overview/general-algebra/rings/ordered-ring.md)
- [Real number](../../../../overview/general-algebra/numbers/real-number.md)
- [Sigma-algebra](../../../../overview/analysis/measures-and-integral-calculus/part-01/sigma-algebra.md)

## Sources

- [Mathlib documentation: `MeasureTheory.OuterMeasure.caratheodory`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/OuterMeasure/Caratheodory.html#MeasureTheory.OuterMeasure.caratheodory)
- [Source of `MeasureTheory.OuterMeasure.caratheodory` in Mathlib/MeasureTheory/OuterMeasure/Caratheodory.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/OuterMeasure/Caratheodory.lean#L181)
- [1000+ theorems list: Q258374](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L297)
- [1000+ theorems project: Q258374](https://1000-plus.github.io/all.html?length=-1#Q258374)
- [Wikipedia: Carathéodory's theorem (measure theory)](https://en.wikipedia.org/wiki/Carath%C3%A9odory's_theorem_%28measure_theory%29)
- [Wikidata: Q258374](https://www.wikidata.org/wiki/Q258374)
