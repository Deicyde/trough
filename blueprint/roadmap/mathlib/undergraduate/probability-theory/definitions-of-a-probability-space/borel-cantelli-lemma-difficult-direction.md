---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.measure_limsup_eq_one
mathlib_file: Mathlib/Probability/BorelCantelli.lean
---

# Borel-Cantelli lemma (difficult direction)

**The second Borel-Cantelli lemma**: Given a sequence of independent sets `(sₙ)` such that
`∑ n, μ sₙ = ∞`, `limsup sₙ` has measure 1.

```lean
ProbabilityTheory.measure_limsup_eq_one.{u_1} {Ω : Type u_1} {m0 : MeasurableSpace Ω}
  {μ : MeasureTheory.Measure Ω} {s : ℕ → Set Ω} (hsm : ∀ (n : ℕ), MeasurableSet (s n))
  (hs : ProbabilityTheory.iIndepSet s μ) (hs' : ∑' (n : ℕ), μ (s n) = ⊤) :
  μ (Filter.limsup s Filter.atTop) = 1
```

## Depends on

- [Independent events](../../../overview/probability-theory/definitions-in-probability-theory/independent-events.md)

## Proof depends on

- [Approximation by step functions](../../measures-and-integral-calculus/measure-theory/approximation-by-step-functions.md)
- [Bochner integral](../../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Conditional expectation](../../../overview/probability-theory/definitions-in-probability-theory/conditional-expectation.md)
- [Independence of random variables](../../../overview/probability-theory/random-variables-and-their-laws/independence-of-random-variables.md)
- [Independent sigma-algebras](../../../overview/probability-theory/definitions-in-probability-theory/independent-sigma-algebras.md)
- [Metric structure](../../single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Pointwise convergence](../../single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)
- [Probability measure](../../../overview/probability-theory/definitions-in-probability-theory/probability-measure.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.measure_limsup_eq_one`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/BorelCantelli.html#ProbabilityTheory.measure_limsup_eq_one)
- [Source of `ProbabilityTheory.measure_limsup_eq_one` in Mathlib/Probability/BorelCantelli.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Probability/BorelCantelli.lean#L68)
- [Mathlib undergraduate list: Probability Theory › Definitions of a probability space](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L553)
