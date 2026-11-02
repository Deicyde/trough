---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: intervalIntegral.continuous_of_dominated_interval
mathlib_file: Mathlib/MeasureTheory/Integral/DominatedConvergence.lean
---

# Continuity of integrals with respect to parameters

Continuity of interval integral with respect to a parameter.
Given `F : X → ℝ → E`, assume each `F x` is ae-measurable on `[a, b]`,
and assume it is bounded by a function integrable on `[a, b]` independent of `x`.
If `(fun x ↦ F x t)` is continuous for almost every `t` in `[a, b]`
then the same holds for `(fun x ↦ ∫ t in a..b, F x t ∂μ) s x₀`.

```lean
intervalIntegral.continuous_of_dominated_interval.{u_2, u_3} {E : Type u_2} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {μ : MeasureTheory.Measure ℝ} {X : Type u_3} [TopologicalSpace X]
  [FirstCountableTopology X] {F : X → ℝ → E} {bound : ℝ → ℝ} {a b : ℝ}
  (hF_meas : ∀ (x : X), MeasureTheory.AEStronglyMeasurable (F x) (μ.restrict (Set.uIoc a b)))
  (h_bound : ∀ (x : X), ∀ᵐ (t : ℝ) ∂μ, t ∈ Set.uIoc a b → ‖F x t‖ ≤ bound t)
  (bound_integrable : IntervalIntegrable bound μ a b)
  (h_cont : ∀ᵐ (t : ℝ) ∂μ, t ∈ Set.uIoc a b → Continuous fun x => F x t) :
  Continuous fun x => ∫ (t : ℝ) in a..b, F x t ∂μ
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Bochner integral](../../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Carathéodory's theorem (measure theory)](../../../thousand-plus/analysis/28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)

## Proof depends on

- [Borel sigma-algebra](../../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Metric structure](../../single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Topological module](../../../overview/topology/topological-algebra/topological-module.md)

## Sources

- [Mathlib documentation: `intervalIntegral.continuous_of_dominated_interval`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/DominatedConvergence.html#intervalIntegral.continuous_of_dominated_interval)
- [Source of `intervalIntegral.continuous_of_dominated_interval` in Mathlib/MeasureTheory/Integral/DominatedConvergence.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Integral/DominatedConvergence.lean#L289)
- [Mathlib undergraduate list: Measures and integral calculus › Integration](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L519)
