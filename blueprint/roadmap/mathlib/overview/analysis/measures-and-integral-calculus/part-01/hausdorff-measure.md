---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Measure.hausdorffMeasure
mathlib_file: Mathlib/MeasureTheory/Measure/Hausdorff.lean
---

# Hausdorff measure

Hausdorff measure on an (e)metric space.

```lean
MeasureTheory.Measure.hausdorffMeasure.{u_2} {X : Type u_2} [EMetricSpace X] [MeasurableSpace X]
  [BorelSpace X] (d : ℝ) : MeasureTheory.Measure X
```

## Depends on

- [Borel sigma-algebra](borel-sigma-algebra.md)
- [Carathéodory's theorem (measure theory)](../../../../thousand-plus/analysis/28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)
- [Induced topology](../../../topology/general-topology/part-01/induced-topology.md)
- [Positive measure](positive-measure.md)
- [Power functions](../../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-etc/power-functions.md)
- [Uniform space](../../../topology/uniform-notions/uniform-space.md)

## Sources

- [Mathlib documentation: `MeasureTheory.Measure.hausdorffMeasure`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/Hausdorff.html#MeasureTheory.Measure.hausdorffMeasure)
- [Source of `MeasureTheory.Measure.hausdorffMeasure` in Mathlib/MeasureTheory/Measure/Hausdorff.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Measure/Hausdorff.lean#L534)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L344)
