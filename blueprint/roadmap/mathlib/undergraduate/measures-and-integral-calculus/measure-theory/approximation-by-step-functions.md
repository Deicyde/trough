---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.SimpleFunc.tendsto_approxOn
mathlib_file: Mathlib/MeasureTheory/Function/SimpleFuncDense.lean
---

# Approximation by step functions

Mathlib states this as `MeasureTheory.SimpleFunc.tendsto_approxOn`.

```lean
MeasureTheory.SimpleFunc.tendsto_approxOn.{u_1, u_2} {α : Type u_1} {β : Type u_2}
  [MeasurableSpace α] [PseudoEMetricSpace α] [OpensMeasurableSpace α] [MeasurableSpace β]
  {f : β → α} (hf : Measurable f) {s : Set α} {y₀ : α} (h₀ : y₀ ∈ s)
  [TopologicalSpace.SeparableSpace ↑s] {x : β} (hx : f x ∈ closure s) :
  Filter.Tendsto (fun n => (MeasureTheory.SimpleFunc.approxOn f hf s y₀ h₀ n) x) Filter.atTop
    (nhds (f x))
```

## Depends on

- [Borel sigma-algebra](../../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Closure](../../../overview/topology/general-topology/part-01/closure.md)
- [Induced topology](../../../overview/topology/general-topology/part-01/induced-topology.md)
- [Measurable function](../../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)
- [Order (Real numbers)](../../single-variable-real-analysis/real-numbers/order.md)
- [Order topology](../../../overview/topology/topological-algebra/order-topology.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)
- [Uniform space](../../../overview/topology/uniform-notions/uniform-space.md)

## Proof depends on

- [Ball](../../../overview/topology/metric-spaces/ball.md)
- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Compactness in terms of filters](../../../overview/topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Continuity of inverse functions](../../single-variable-real-analysis/real-valued-functions-defined-on-a-subset-of-r/continuity-of-inverse-functions.md)
- [Field $\R$ of real numbers](../../ring-theory/field-theory/part-01/field-r-of-real-numbers.md)
- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Group](../../../overview/general-algebra/group-theory/part-01/group.md)
- [Invertible elements](../../ring-theory/divisibility-in-integral-domains/invertible-elements.md)
- [Limit point](../../single-variable-real-analysis/sequences-of-real-numbers/limit-point.md)
- [Permutation group of a type](../../../overview/general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Product of rings](../../ring-theory/fundamentals/product-of-rings.md)
- [Ring morphism](../../../overview/general-algebra/rings/ring-morphism.md)
- [Ring structure $\Z$](../../ring-theory/fundamentals/ring-structure-z.md)

## Sources

- [Mathlib documentation: `MeasureTheory.SimpleFunc.tendsto_approxOn`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Function/SimpleFuncDense.html#MeasureTheory.SimpleFunc.tendsto_approxOn)
- [Source of `MeasureTheory.SimpleFunc.tendsto_approxOn` in Mathlib/MeasureTheory/Function/SimpleFuncDense.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Function/SimpleFuncDense.lean#L154)
- [Mathlib undergraduate list: Measures and integral calculus › Measure theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L511)
