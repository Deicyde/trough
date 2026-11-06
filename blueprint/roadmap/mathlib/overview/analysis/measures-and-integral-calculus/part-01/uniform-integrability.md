---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.UniformIntegrable
mathlib_file: Mathlib/MeasureTheory/Function/UniformIntegrable.lean
---

# Uniform integrability

In probability theory, a family of measurable functions is uniformly integrable if it is
uniformly integrable in the measure theory sense and is uniformly bounded.

```lean
MeasureTheory.UniformIntegrable.{u_1, u_2, u_3} {α : Type u_1} {β : Type u_2} {ι : Type u_3}
  [NormedAddCommGroup β] {x✝ : MeasurableSpace α} (f : ι → α → β) (p : ENNReal)
  (μ : MeasureTheory.Measure α) : Prop
```

## Depends on

- [Almost sure convergence](../../../probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Associative algebra over a commutative ring](../../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Carathéodory's theorem (measure theory)](../../../../thousand-plus/analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Continuous function](../../../topology/general-topology/part-01/continuous-function.md)
- [Integral of positive measurable functions](integral-of-positive-measurable-functions.md)
- [Linear map](../../../linear-algebra/fundamentals/linear-map.md)
- [Metric space](../../../topology/metric-spaces/metric-space.md)

## Sources

- [Mathlib documentation: `MeasureTheory.UniformIntegrable`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Function/UniformIntegrable.html#MeasureTheory.UniformIntegrable)
- [Source of `MeasureTheory.UniformIntegrable` in Mathlib/MeasureTheory/Function/UniformIntegrable.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Function/UniformIntegrable.lean#L70)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L351)
