---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.TendstoInMeasure
mathlib_file: Mathlib/MeasureTheory/Function/ConvergenceInMeasure.lean
---

# Convergence in probability

A sequence of functions `f` is said to converge in measure to some function `g` if for all
`ε > 0`, the measure of the set `{x | ε ≤ dist (f i x) (g x)}` tends to 0 as `i` converges along
some given filter `l`.

```lean
MeasureTheory.TendstoInMeasure.{u_1, u_2, u_4} {α : Type u_1} {ι : Type u_2} {E : Type u_4}
  [EDist E] {x✝ : MeasurableSpace α} (μ : MeasureTheory.Measure α) (f : ι → α → E) (l : Filter ι)
  (g : α → E) : Prop
```

## Depends on

- [Positive measure](../../analysis/measures-and-integral-calculus/part-01/positive-measure.md)

## Sources

- [Mathlib documentation: `MeasureTheory.TendstoInMeasure`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Function/ConvergenceInMeasure.html#MeasureTheory.TendstoInMeasure)
- [Source of `MeasureTheory.TendstoInMeasure` in Mathlib/MeasureTheory/Function/ConvergenceInMeasure.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Function/ConvergenceInMeasure.lean#L54)
- [Mathlib overview: Probability Theory › Convergence of a sequence of random variables](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L414)
- [Mathlib undergraduate list: Probability Theory › Convergence of a sequence of random variables](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L577)
