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

- [Euclidean affine space](../../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Extended real number](../../../overview/general-algebra/numbers/extended-real-number.md)
- [Extreme value theorem](../../../overview/topology/topological-algebra/extreme-value-theorem.md)
- [Hitting time](../../../overview/probability-theory/stochastic-processes/hitting-time.md)
- [Independence of random variables](../../../overview/probability-theory/random-variables-and-their-laws/independence-of-random-variables.md)
- [Independent sigma-algebras](../../../overview/probability-theory/definitions-in-probability-theory/independent-sigma-algebras.md)
- [Local convexity](../../../overview/analysis/topological-vector-spaces/local-convexity.md)
- [Martingale](../../../overview/probability-theory/stochastic-processes/martingale.md)
- [Maximal ideal](../../../overview/general-algebra/ideals-and-quotients/maximal-ideal.md)
- [Optional stopping theorem](../../../overview/probability-theory/stochastic-processes/optional-stopping-theorem.md)
- [Probability measure](../../../overview/probability-theory/definitions-in-probability-theory/probability-measure.md)
- [Quotient space](../../../overview/linear-algebra/fundamentals/quotient-space.md)
- [Sequential space](../../../overview/topology/general-topology/part-01/sequential-space.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.measure_limsup_eq_one`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/BorelCantelli.html#ProbabilityTheory.measure_limsup_eq_one)
- [Source of `ProbabilityTheory.measure_limsup_eq_one` in Mathlib/Probability/BorelCantelli.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Probability/BorelCantelli.lean#L68)
- [Mathlib undergraduate list: Probability Theory › Definitions of a probability space](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L553)
