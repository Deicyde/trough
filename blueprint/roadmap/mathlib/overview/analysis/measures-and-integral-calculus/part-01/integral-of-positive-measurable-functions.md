# Integral of positive measurable functions

The **lower Lebesgue integral** of a function `f` with respect to a measure `μ`.

```lean
MeasureTheory.lintegral.{u_1} {α : Type u_1} {m : MeasurableSpace α} (μ : MeasureTheory.Measure α)
  (f : α → ENNReal) : ENNReal
```

## Depends on

- [Positive measure](positive-measure.md)

## Sources

- [Mathlib documentation: `MeasureTheory.lintegral`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/Lebesgue/Basic.html#MeasureTheory.lintegral)
- [Source of `MeasureTheory.lintegral` in Mathlib/MeasureTheory/Integral/Lebesgue/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/MeasureTheory/Integral/Lebesgue/Basic.lean#L47)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L347)
- [Mathlib undergraduate list: Measures and integral calculus › Integration](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L513)
- [Freek Wiedijk's 100 theorems, no. 86](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/100.yaml#L440)
