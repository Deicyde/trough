# Hausdorff measure

Hausdorff measure on an (e)metric space.

```lean
MeasureTheory.Measure.hausdorffMeasure.{u_2} {X : Type u_2} [EMetricSpace X] [MeasurableSpace X]
  [BorelSpace X] (d : ℝ) : MeasureTheory.Measure X
```

## Depends on

- [Borel sigma-algebra](borel-sigma-algebra.md)
- [Carathéodory's theorem (measure theory)](../../../../thousand-plus/analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Positive measure](positive-measure.md)

## Sources

- [Mathlib documentation: `MeasureTheory.Measure.hausdorffMeasure`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/Hausdorff.html#MeasureTheory.Measure.hausdorffMeasure)
- [Source of `MeasureTheory.Measure.hausdorffMeasure` in Mathlib/MeasureTheory/Measure/Hausdorff.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Measure/Hausdorff.lean#L534)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L344)
