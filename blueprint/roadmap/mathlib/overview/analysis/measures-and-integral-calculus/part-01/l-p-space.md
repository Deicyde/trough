# $L^p$ space

Lp space

```lean
MeasureTheory.Lp.{u_6, u_7} {α : Type u_7} (E : Type u_6) {m : MeasurableSpace α}
  [NormedAddCommGroup E] (p : ENNReal) (μ : MeasureTheory.Measure α := by volume_tac) :
  AddSubgroup (α →ₘ[μ] E)
```

## Depends on

- [Almost sure convergence](../../../probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Continuous function](../../../topology/general-topology/part-01/continuous-function.md)
- [Integral of positive measurable functions](integral-of-positive-measurable-functions.md)
- [Metric space](../../../topology/metric-spaces/metric-space.md)

## Sources

- [Mathlib documentation: `MeasureTheory.Lp`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Function/LpSpace/Basic.html#MeasureTheory.Lp)
- [Source of `MeasureTheory.Lp` in Mathlib/MeasureTheory/Function/LpSpace/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/MeasureTheory/Function/LpSpace/Basic.lean#L88)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L352)
- [Mathlib overview: Probability Theory › Convergence of a sequence of random variables](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L415)
- [Mathlib undergraduate list: Measures and integral calculus › Integration](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L521)
- [Mathlib undergraduate list: Probability Theory › Convergence of a sequence of random variables](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L578)
