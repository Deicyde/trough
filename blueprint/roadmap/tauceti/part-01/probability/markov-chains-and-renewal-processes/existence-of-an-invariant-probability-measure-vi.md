---
declaration: theorem
origin: cited
lean: ProbabilityTheory.Kernel.exists_invariant_probability_iff_forall_isPositiveRecurrent
statement: formalized
proof: formalized
---

# Existence of an invariant probability measure via positive recurrence of all states

For a
nonempty counting-measure-irreducible chain, an invariant probability measure exists if and only if
every state is positive recurrent.

```lean
ProbabilityTheory.Kernel.exists_invariant_probability_iff_forall_isPositiveRecurrent.{u_1}
  {α : Type u_1} [MeasurableSpace α] [MeasurableSingletonClass α] (κ : ProbabilityTheory.Kernel α α)
  [ProbabilityTheory.IsMarkovKernel κ] [Nonempty α]
  [ProbabilityTheory.Kernel.IsIrreducible MeasureTheory.Measure.count κ] :
  (∃ π, MeasureTheory.IsProbabilityMeasure π ∧ κ.Invariant π) ↔ ∀ (x : α), κ.IsPositiveRecurrent x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Expected occupation measure in one return cycle started at `x`](expected-occupation-measure-in-one-return-cycle.md)

## Lean

Formalized in Tau Ceti as [`ProbabilityTheory.Kernel.exists_invariant_probability_iff_forall_isPositiveRecurrent`](https://taucetiproject.org/docs/TauCeti/Probability/MarkovChain/Invariant.html#ProbabilityTheory.Kernel.exists_invariant_probability_iff_forall_isPositiveRecurrent).

## Sources

- [Tau Ceti documentation: `ProbabilityTheory.Kernel.exists_invariant_probability_iff_forall_isPositiveRecurrent`](https://taucetiproject.org/docs/TauCeti/Probability/MarkovChain/Invariant.html#ProbabilityTheory.Kernel.exists_invariant_probability_iff_forall_isPositiveRecurrent)
- [Source of `ProbabilityTheory.Kernel.exists_invariant_probability_iff_forall_isPositiveRecurrent` in TauCeti/Probability/MarkovChain/Invariant.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/MarkovChain/Invariant.lean#L651)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)
