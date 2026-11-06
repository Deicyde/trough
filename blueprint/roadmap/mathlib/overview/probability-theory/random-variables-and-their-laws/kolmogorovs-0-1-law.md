# Kolmogorov's $0$-$1$ law

**Kolmogorov's 0-1 law** : any event in the tail σ-algebra of an independent sequence of
sub-σ-algebras has probability 0 or 1.
The tail σ-algebra `limsup s atTop` is the same as `⋂ n, ⋃ i ≥ n, s i`.

```lean
ProbabilityTheory.measure_zero_or_one_of_measurableSet_limsup_atTop.{u_2, u_3} {Ω : Type u_2}
  {ι : Type u_3} {s : ι → MeasurableSpace Ω} {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω}
  [SemilatticeSup ι] [NoMaxOrder ι] [Nonempty ι] (h_le : ∀ (n : ι), s n ≤ m0)
  (h_indep : ProbabilityTheory.iIndep s μ) {t : Set Ω} (ht_tail : MeasurableSet t) :
  μ t = 0 ∨ μ t = 1
```

## Depends on

- [Independent sigma-algebras](../definitions-in-probability-theory/independent-sigma-algebras.md)

## Proof depends on

- [Borel sigma-algebra](../../analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Completeness](../../topology/uniform-notions/completeness.md)
- [Metric space](../../topology/metric-spaces/metric-space.md)
- [Probability measure](../definitions-in-probability-theory/probability-measure.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.measure_zero_or_one_of_measurableSet_limsup_atTop`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Independence/ZeroOne.html#ProbabilityTheory.measure_zero_or_one_of_measurableSet_limsup_atTop)
- [Source of `ProbabilityTheory.measure_zero_or_one_of_measurableSet_limsup_atTop` in Mathlib/Probability/Independence/ZeroOne.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Probability/Independence/ZeroOne.lean#L287)
- [Mathlib overview: Probability Theory › Random variables and their laws](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L403)
- [Mathlib undergraduate list: Probability Theory › Definitions of a probability space](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L551)
