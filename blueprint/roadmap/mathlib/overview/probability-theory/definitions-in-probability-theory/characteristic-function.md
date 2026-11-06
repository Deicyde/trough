# Characteristic function

The characteristic function of a measure in an inner product space.

```lean
MeasureTheory.charFun.{u_2} {E : Type u_2} {mE : MeasurableSpace E} [Inner ℝ E]
  (μ : MeasureTheory.Measure E) (t : E) : ℂ
```

## Depends on

- [Bochner integral](../../analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Complex exponential](../../../undergraduate/single-variable-complex-analysis/complex-valued-series/complex-exponential.md)
- [Inner product space, over $R$ or $C$](../../analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)

## Sources

- [Mathlib documentation: `MeasureTheory.charFun`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/CharacteristicFunction/Basic.html#MeasureTheory.charFun)
- [Source of `MeasureTheory.charFun` in Mathlib/MeasureTheory/Measure/CharacteristicFunction/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Measure/CharacteristicFunction/Basic.lean#L129)
- [Mathlib overview: Probability Theory › Definitions in probability theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L397)
- [Mathlib undergraduate list: Probability Theory › Random variables and their laws](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L573)
