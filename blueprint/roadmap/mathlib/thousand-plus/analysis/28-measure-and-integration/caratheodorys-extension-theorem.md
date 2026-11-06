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
- [Positive measure](../../../overview/analysis/measures-and-integral-calculus/part-01/positive-measure.md)

## Proof depends on

- [Continuous function](../../../overview/topology/general-topology/part-01/continuous-function.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Order topology](../../../overview/topology/topological-algebra/order-topology.md)

## Sources

- [Mathlib documentation: `MeasureTheory.AddContent.measure`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/OuterMeasure/OfAddContent.html#MeasureTheory.AddContent.measure)
- [Source of `MeasureTheory.AddContent.measure` in Mathlib/MeasureTheory/OuterMeasure/OfAddContent.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/OuterMeasure/OfAddContent.lean#L160)
- [Mathlib documentation: `MeasureTheory.AddContent.measure_eq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/OuterMeasure/OfAddContent.html#MeasureTheory.AddContent.measure_eq)
- [Source of `MeasureTheory.AddContent.measure_eq` in Mathlib/MeasureTheory/OuterMeasure/OfAddContent.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/OuterMeasure/OfAddContent.lean#L169)
- [1000+ theorems list: Q2631152](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2274)
- [1000+ theorems project: Q2631152](https://1000-plus.github.io/all.html?length=-1#Q2631152)
- [Wikipedia: Carathéodory's extension theorem](https://en.wikipedia.org/wiki/Carath%C3%A9odory's_extension_theorem)
- [Wikidata: Q2631152](https://www.wikidata.org/wiki/Q2631152)
