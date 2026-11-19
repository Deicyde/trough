---
declaration: theorem
origin: cited
lean: ProbabilityTheory.Kernel.Invariant.apply_singleton_eq_inv_meanReturnTime
statement: formalized
proof: formalized
---

# Kac's formula

For any invariant probability measure `π` of a counting-measure-irreducible
Markov chain and any state `x`, `π {x} = (κ.meanReturnTime x)⁻¹`. No aperiodicity hypothesis is
needed.

```lean
ProbabilityTheory.Kernel.Invariant.apply_singleton_eq_inv_meanReturnTime.{u_1} {α : Type u_1}
  [MeasurableSpace α] [MeasurableSingletonClass α] {κ : ProbabilityTheory.Kernel α α}
  [ProbabilityTheory.IsMarkovKernel κ]
  [ProbabilityTheory.Kernel.IsIrreducible MeasureTheory.Measure.count κ]
  {π : MeasureTheory.Measure α} [MeasureTheory.IsProbabilityMeasure π] (hπ : κ.Invariant π)
  (x : α) : π {x} = (κ.meanReturnTime x)⁻¹
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Expected occupation measure in one return cycle started at `x`](expected-occupation-measure-in-one-return-cycle.md)

## Lean

Formalized in Tau Ceti as [`ProbabilityTheory.Kernel.Invariant.apply_singleton_eq_inv_meanReturnTime`](https://taucetiproject.org/docs/TauCeti/Probability/MarkovChain/Invariant.html#ProbabilityTheory.Kernel.Invariant.apply_singleton_eq_inv_meanReturnTime).

## Sources

- [Tau Ceti documentation: `ProbabilityTheory.Kernel.Invariant.apply_singleton_eq_inv_meanReturnTime`](https://taucetiproject.org/docs/TauCeti/Probability/MarkovChain/Invariant.html#ProbabilityTheory.Kernel.Invariant.apply_singleton_eq_inv_meanReturnTime)
- [Source of `ProbabilityTheory.Kernel.Invariant.apply_singleton_eq_inv_meanReturnTime` in TauCeti/Probability/MarkovChain/Invariant.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/MarkovChain/Invariant.lean#L603)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)
