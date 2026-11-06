# Probability measure

A measure `μ` is called a probability measure if `μ univ = 1`.

```lean
MeasureTheory.IsProbabilityMeasure.{u_1} {α : Type u_1} {m0 : MeasurableSpace α}
  (μ : MeasureTheory.Measure α) : Prop
```

## Depends on

- [Positive measure](../../analysis/measures-and-integral-calculus/part-01/positive-measure.md)

## Sources

- [Mathlib documentation: `MeasureTheory.IsProbabilityMeasure`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/Typeclasses/Probability.html#MeasureTheory.IsProbabilityMeasure)
- [Source of `MeasureTheory.IsProbabilityMeasure` in Mathlib/MeasureTheory/Measure/Typeclasses/Probability.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Measure/Typeclasses/Probability.lean#L63)
- [Mathlib overview: Probability Theory › Definitions in probability theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L392)
- [Mathlib undergraduate list: Probability Theory › Definitions of a probability space](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L546)
