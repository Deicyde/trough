---
declaration: def
origin: cited
lean: ProbabilityTheory.Kernel.cycleOccupation
statement: formalized
---

# Expected occupation measure in one return cycle started at `x`

for a measurable set `s`,
`κ.cycleOccupation x s` is the expected number of times `n < T_x⁺` before the first positive return
to `x` at which the chain started at `x` visits `s`.

```lean
ProbabilityTheory.Kernel.cycleOccupation.{u_1} {α : Type u_1} [MeasurableSpace α]
  (κ : ProbabilityTheory.Kernel α α) [ProbabilityTheory.IsMarkovKernel κ] (x : α) :
  MeasureTheory.Measure α
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ProbabilityTheory.Kernel.cycleOccupation`](https://taucetiproject.org/docs/TauCeti/Probability/MarkovChain/Invariant.html#ProbabilityTheory.Kernel.cycleOccupation).

## Sources

- [Tau Ceti documentation: `ProbabilityTheory.Kernel.cycleOccupation`](https://taucetiproject.org/docs/TauCeti/Probability/MarkovChain/Invariant.html#ProbabilityTheory.Kernel.cycleOccupation)
- [Source of `ProbabilityTheory.Kernel.cycleOccupation` in TauCeti/Probability/MarkovChain/Invariant.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/MarkovChain/Invariant.lean#L155)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)
