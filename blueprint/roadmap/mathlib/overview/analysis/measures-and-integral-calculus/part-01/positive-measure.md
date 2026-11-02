---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Measure
mathlib_file: Mathlib/MeasureTheory/Measure/MeasureSpaceDef.lean
---

# Positive measure

A measure is defined to be an outer measure that is countably additive on
measurable sets, with the additional assumption that the outer measure is the canonical
extension of the restricted measure.

The measure of a set `s`, denoted `μ s`, is an extended nonnegative real. The real-valued version
is written `μ.real s`.

```lean
MeasureTheory.Measure.{u_5} (α : Type u_5) [MeasurableSpace α] : Type u_5
```

## Depends on

- [Events](../../../../undergraduate/probability-theory/definitions-of-a-probability-space/events.md)
- [Infinite sum](../../../topology/topological-algebra/infinite-sum.md)
- [Real number](../../../general-algebra/numbers/real-number.md)

## Sources

- [Mathlib documentation: `MeasureTheory.Measure`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/MeasureSpaceDef.html#MeasureTheory.Measure)
- [Source of `MeasureTheory.Measure` in Mathlib/MeasureTheory/Measure/MeasureSpaceDef.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Measure/MeasureSpaceDef.lean#L70)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L341)
- [Mathlib undergraduate list: Measures and integral calculus › Measure theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L506)
