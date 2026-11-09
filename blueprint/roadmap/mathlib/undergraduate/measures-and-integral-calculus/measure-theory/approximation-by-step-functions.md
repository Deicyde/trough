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
- [Measurable function](../../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)
- [Order topology](../../../overview/topology/topological-algebra/order-topology.md)
- [Real number](../../../overview/general-algebra/numbers/real-number.md)

## Proof depends on

- [Continuous function](../../../overview/topology/general-topology/part-01/continuous-function.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `MeasureTheory.SimpleFunc.tendsto_approxOn`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Function/SimpleFuncDense.html#MeasureTheory.SimpleFunc.tendsto_approxOn)
- [Source of `MeasureTheory.SimpleFunc.tendsto_approxOn` in Mathlib/MeasureTheory/Function/SimpleFuncDense.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/MeasureTheory/Function/SimpleFuncDense.lean#L154)
- [Mathlib undergraduate list: Measures and integral calculus › Measure theory](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L511)
