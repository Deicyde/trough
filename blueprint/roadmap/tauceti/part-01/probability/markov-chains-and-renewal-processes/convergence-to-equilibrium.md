---
declaration: theorem
origin: cited
lean: ProbabilityTheory.Kernel.Invariant.tendsto_tvDist_pow_comp
statement: formalized
proof: formalized
---

# Convergence to equilibrium

For an irreducible aperiodic kernel,
an invariant probability attracts every initial probability in total variation.

```lean
ProbabilityTheory.Kernel.Invariant.tendsto_tvDist_pow_comp.{u_1} {α : Type u_1} [MeasurableSpace α]
  [MeasurableSingletonClass α] {κ : ProbabilityTheory.Kernel α α}
  [ProbabilityTheory.IsMarkovKernel κ]
  [ProbabilityTheory.Kernel.IsIrreducible MeasureTheory.Measure.count κ]
  {π : MeasureTheory.Measure α} [MeasureTheory.IsProbabilityMeasure π] (hπ : κ.Invariant π)
  (hκ : κ.IsAperiodic) (ν : MeasureTheory.Measure α) [MeasureTheory.IsProbabilityMeasure ν] :
  Filter.Tendsto (fun n => MeasureTheory.tvDist (ν.bind ⇑(κ ^ n)) π) Filter.atTop (nhds 0)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Chapman–Kolmogorov lower bound](../other-results/chapman-kolmogorov-lower-bound.md)

## Lean

Formalized in Tau Ceti as [`ProbabilityTheory.Kernel.Invariant.tendsto_tvDist_pow_comp`](https://taucetiproject.org/docs/TauCeti/Probability/MarkovChain/Equilibrium.html#ProbabilityTheory.Kernel.Invariant.tendsto_tvDist_pow_comp).

## Sources

- [Tau Ceti documentation: `ProbabilityTheory.Kernel.Invariant.tendsto_tvDist_pow_comp`](https://taucetiproject.org/docs/TauCeti/Probability/MarkovChain/Equilibrium.html#ProbabilityTheory.Kernel.Invariant.tendsto_tvDist_pow_comp)
- [Source of `ProbabilityTheory.Kernel.Invariant.tendsto_tvDist_pow_comp` in TauCeti/Probability/MarkovChain/Equilibrium.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/MarkovChain/Equilibrium.lean#L47)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)
