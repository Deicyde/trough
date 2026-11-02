---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.mul_meas_ge_le_lintegral
mathlib_file: Mathlib/MeasureTheory/Integral/Lebesgue/Markov.lean
---

# Markov inequality

**Markov's inequality** also known as **Chebyshev's first inequality**. For a version assuming
`AEMeasurable`, see `mul_meas_ge_le_lintegral₀`.

```lean
MeasureTheory.mul_meas_ge_le_lintegral.{u_1} {α : Type u_1} {mα : MeasurableSpace α}
  {μ : MeasureTheory.Measure α} {f : α → ENNReal} (hf : Measurable f) (ε : ENNReal) :
  ε * μ {x | ε ≤ f x} ≤ ∫⁻ (a : α), f a ∂μ
```

## Depends on

- [Integral of positive measurable functions](../../analysis/measures-and-integral-calculus/part-01/integral-of-positive-measurable-functions.md)
- [Measurable function](../../analysis/measures-and-integral-calculus/part-01/measurable-function.md)

## Proof depends on

- [Almost sure convergence](almost-sure-convergence.md)
- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Borel sigma-algebra](../../analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Carathéodory's theorem (measure theory)](../../../thousand-plus/analysis/28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)
- [Continuous function](../../topology/general-topology/part-01/continuous-function.md)
- [Induced topology](../../topology/general-topology/part-01/induced-topology.md)
- [Linear map](../../linear-algebra/fundamentals/linear-map.md)
- [Order topology](../../topology/topological-algebra/order-topology.md)

## Sources

- [Mathlib documentation: `MeasureTheory.mul_meas_ge_le_lintegral`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/Lebesgue/Markov.html#MeasureTheory.mul_meas_ge_le_lintegral)
- [Source of `MeasureTheory.mul_meas_ge_le_lintegral` in Mathlib/MeasureTheory/Integral/Lebesgue/Markov.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Integral/Lebesgue/Markov.lean#L57)
- [Mathlib overview: Probability Theory › Convergence of a sequence of random variables](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L418)
- [Mathlib undergraduate list: Probability Theory › Convergence of a sequence of random variables](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L580)
