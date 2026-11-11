---
declaration: theorem
origin: cited
lean: ProbabilityTheory.Kernel.tsum_pow_apply_singleton_self_eq_top_iff
statement: formalized
proof: formalized
---

# The recurrence criterion

The chain started at `y` returns to `y` almost surely exactly when
the mean number of visits `∑ n, (κ ^ n) y {y}` is infinite.

```lean
ProbabilityTheory.Kernel.tsum_pow_apply_singleton_self_eq_top_iff.{u_1} {α : Type u_1}
  [MeasurableSpace α] [MeasurableSingletonClass α] (κ : ProbabilityTheory.Kernel α α)
  [ProbabilityTheory.IsMarkovKernel κ] (y : α) :
  ∑' (n : ℕ), ((κ ^ n) y) {y} = ⊤ ↔
    (TauCeti.Probability.markovChainLaw (MeasureTheory.Measure.dirac y) κ)
        {x | MeasureTheory.hittingAfter (fun n x => x n) {y} 1 x ≠ ⊤} =
      1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ProbabilityTheory.Kernel.tsum_pow_apply_singleton_self_eq_top_iff`](https://taucetiproject.org/docs/TauCeti/Probability/MarkovChain/Visits.html#ProbabilityTheory.Kernel.tsum_pow_apply_singleton_self_eq_top_iff).

## Sources

- [Tau Ceti documentation: `ProbabilityTheory.Kernel.tsum_pow_apply_singleton_self_eq_top_iff`](https://taucetiproject.org/docs/TauCeti/Probability/MarkovChain/Visits.html#ProbabilityTheory.Kernel.tsum_pow_apply_singleton_self_eq_top_iff)
- [Source of `ProbabilityTheory.Kernel.tsum_pow_apply_singleton_self_eq_top_iff` in TauCeti/Probability/MarkovChain/Visits.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/MarkovChain/Visits.lean#L295)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)
