---
declaration: def
origin: cited
lean: ProbabilityTheory.Kernel.markovChainKernel
statement: formalized
---

# The path-law kernel of a homogeneous Markov chain

the kernel sending a state `x` to the law
`markovChainLaw (Measure.dirac x) κ` of the chain started at `x` (`markovChainKernel_apply`). Being
a kernel, it records that this law depends measurably on the starting state, and every path law of
the chain is its mixture over the initial law (`markovChainLaw_eq_comp`).

```lean
ProbabilityTheory.Kernel.markovChainKernel.{u_1} {α : Type u_1} [MeasurableSpace α]
  (κ : ProbabilityTheory.Kernel α α) [ProbabilityTheory.IsMarkovKernel κ] :
  ProbabilityTheory.Kernel α (ℕ → α)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ProbabilityTheory.Kernel.markovChainKernel`](https://taucetiproject.org/docs/TauCeti/Probability/Process/MarkovChain.html#ProbabilityTheory.Kernel.markovChainKernel).

## Sources

- [Tau Ceti documentation: `ProbabilityTheory.Kernel.markovChainKernel`](https://taucetiproject.org/docs/TauCeti/Probability/Process/MarkovChain.html#ProbabilityTheory.Kernel.markovChainKernel)
- [Source of `ProbabilityTheory.Kernel.markovChainKernel` in TauCeti/Probability/Process/MarkovChain.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Process/MarkovChain.lean#L178)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)
