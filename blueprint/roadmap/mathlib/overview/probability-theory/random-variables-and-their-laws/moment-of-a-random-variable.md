---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.moment
mathlib_file: Mathlib/Probability/Moments/Basic.lean
---

# Moment of a random variable

Moment of a real random variable, `μ[X ^ p]`.

```lean
ProbabilityTheory.moment.{u_1} {Ω : Type u_1} {m : MeasurableSpace Ω} (X : Ω → ℝ) (p : ℕ)
  (μ : MeasureTheory.Measure Ω) : ℝ
```

## Depends on

- [Bochner integral](../../analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Completeness of R](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Inner product space, over $R$ or $C$](../../analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.moment`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Moments/Basic.html#ProbabilityTheory.moment)
- [Source of `ProbabilityTheory.moment` in Mathlib/Probability/Moments/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Probability/Moments/Basic.lean#L55)
- [Mathlib overview: Probability Theory › Random variables and their laws](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L405)
- [Mathlib undergraduate list: Probability Theory › Random variables and their laws](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L565)
