---
declaration: theorem
origin: cited
lean: ProbabilityTheory.Kernel.tendsto_pow_comp_real_singleton_of_isAperiodic
statement: formalized
proof: formalized
---

# The singleton convergence theorem

For an irreducible aperiodic chain, the mass of a
state converges to the reciprocal of its extended mean positive return time, from every
initial probability. Infinite return-time mean gives limit zero.

```lean
ProbabilityTheory.Kernel.tendsto_pow_comp_real_singleton_of_isAperiodic.{u_1} {α : Type u_1}
  [MeasurableSpace α] [MeasurableSingletonClass α] (κ : ProbabilityTheory.Kernel α α)
  [ProbabilityTheory.IsMarkovKernel κ]
  [ProbabilityTheory.Kernel.IsIrreducible MeasureTheory.Measure.count κ] (hκ : κ.IsAperiodic)
  (ν : MeasureTheory.Measure α) [MeasureTheory.IsProbabilityMeasure ν] (y : α) :
  Filter.Tendsto (fun n => (ν.bind ⇑(κ ^ n)).real {y}) Filter.atTop
    (nhds (κ.meanReturnTime y)⁻¹.toReal)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Convergence to equilibrium](../markov-chains-and-renewal-processes/convergence-to-equilibrium.md)
- [Expected occupation measure in one return cycle started at `x`](../markov-chains-and-renewal-processes/expected-occupation-measure-in-one-return-cycle.md)
- [Kac's formula](../markov-chains-and-renewal-processes/kacs-formula.md)
- [Pointwise decay at an infinite-mean state](../markov-chains-and-renewal-processes/pointwise-decay-at-an-infinite-mean-state.md)

## Lean

Formalized in Tau Ceti as [`ProbabilityTheory.Kernel.tendsto_pow_comp_real_singleton_of_isAperiodic`](https://taucetiproject.org/docs/TauCeti/Probability/MarkovChain/Convergence.html#ProbabilityTheory.Kernel.tendsto_pow_comp_real_singleton_of_isAperiodic).

## Sources

- [Tau Ceti documentation: `ProbabilityTheory.Kernel.tendsto_pow_comp_real_singleton_of_isAperiodic`](https://taucetiproject.org/docs/TauCeti/Probability/MarkovChain/Convergence.html#ProbabilityTheory.Kernel.tendsto_pow_comp_real_singleton_of_isAperiodic)
- [Source of `ProbabilityTheory.Kernel.tendsto_pow_comp_real_singleton_of_isAperiodic` in TauCeti/Probability/MarkovChain/Convergence.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/MarkovChain/Convergence.lean#L57)
