---
declaration: theorem
origin: cited
lean: ProbabilityTheory.Kernel.tendsto_tvDist_pow_comp_of_parallelComp_isRecurrent
statement: formalized
proof: formalized
---

# ProbabilityTheory.Kernel.tendsto_tvDist_pow_comp_of_parallelComp_isRecurrent

If the independent square chain is irreducible and recurrent, any two initial
probability laws become asymptotically indistinguishable in total variation.

```lean
ProbabilityTheory.Kernel.tendsto_tvDist_pow_comp_of_parallelComp_isRecurrent.{u_1} {α : Type u_1}
  [MeasurableSpace α] [MeasurableEq α] (κ : ProbabilityTheory.Kernel α α)
  [ProbabilityTheory.IsMarkovKernel κ]
  [ProbabilityTheory.Kernel.IsIrreducible MeasureTheory.Measure.count (κ.parallelComp κ)]
  {z : α × α} (hz : (κ.parallelComp κ).IsRecurrent z) (ν ν' : MeasureTheory.Measure α)
  [MeasureTheory.IsProbabilityMeasure ν] [MeasureTheory.IsProbabilityMeasure ν'] :
  Filter.Tendsto (fun n => MeasureTheory.tvDist (ν.bind ⇑(κ ^ n)) (ν'.bind ⇑(κ ^ n))) Filter.atTop
    (nhds 0)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Chapman–Kolmogorov lower bound](../other-results/chapman-kolmogorov-lower-bound.md)
- [The recurrence criterion](the-recurrence-criterion.md)

## Lean

Formalized in Tau Ceti as [`ProbabilityTheory.Kernel.tendsto_tvDist_pow_comp_of_parallelComp_isRecurrent`](https://taucetiproject.org/docs/TauCeti/Probability/MarkovChain/Coupling/Convergence.html#ProbabilityTheory.Kernel.tendsto_tvDist_pow_comp_of_parallelComp_isRecurrent).

## Sources

- [Tau Ceti documentation: `ProbabilityTheory.Kernel.tendsto_tvDist_pow_comp_of_parallelComp_isRecurrent`](https://taucetiproject.org/docs/TauCeti/Probability/MarkovChain/Coupling/Convergence.html#ProbabilityTheory.Kernel.tendsto_tvDist_pow_comp_of_parallelComp_isRecurrent)
- [Source of `ProbabilityTheory.Kernel.tendsto_tvDist_pow_comp_of_parallelComp_isRecurrent` in TauCeti/Probability/MarkovChain/Coupling/Convergence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/MarkovChain/Coupling/Convergence.lean#L90)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)
