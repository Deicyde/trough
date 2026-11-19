---
declaration: theorem
origin: cited
lean: ProbabilityTheory.Kernel.tendsto_pow_comp_real_singleton_of_isAperiodic_of_lintegral_return_eq_top
statement: formalized
proof: formalized
---

# Pointwise decay at an infinite-mean state

For an irreducible
aperiodic Markov kernel, if the expected first positive return time to `y` is infinite,
then the time-`n` mass of `{y}` tends to zero from every initial probability law `ν`.
The mean assigns infinity to nonreturn, so no recurrence assumption is needed.

```lean
ProbabilityTheory.Kernel.tendsto_pow_comp_real_singleton_of_isAperiodic_of_lintegral_return_eq_top.{u_1}
  {α : Type u_1} [MeasurableSpace α] [MeasurableSingletonClass α] (κ : ProbabilityTheory.Kernel α α)
  [ProbabilityTheory.IsMarkovKernel κ]
  [ProbabilityTheory.Kernel.IsIrreducible MeasureTheory.Measure.count κ] (hκ : κ.IsAperiodic)
  {y : α}
  (hy :
    ∫⁻ (x : ℕ → α),
        WithTop.recTopCoe ⊤ (fun n => ↑n)
          (MeasureTheory.hittingAfter (fun n x => x n) {y} 1
            x) ∂TauCeti.Probability.markovChainLaw (MeasureTheory.Measure.dirac y) κ =
      ⊤)
  (ν : MeasureTheory.Measure α) [MeasureTheory.IsProbabilityMeasure ν] :
  Filter.Tendsto (fun n => (ν.bind ⇑(κ ^ n)).real {y}) Filter.atTop (nhds 0)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Chapman–Kolmogorov lower bound](../other-results/chapman-kolmogorov-lower-bound.md)

## Lean

Formalized in Tau Ceti as [`ProbabilityTheory.Kernel.tendsto_pow_comp_real_singleton_of_isAperiodic_of_lintegral_return_eq_top`](https://taucetiproject.org/docs/TauCeti/Probability/MarkovChain/Pointwise.html#ProbabilityTheory.Kernel.tendsto_pow_comp_real_singleton_of_isAperiodic_of_lintegral_return_eq_top).

## Sources

- [Tau Ceti documentation: `ProbabilityTheory.Kernel.tendsto_pow_comp_real_singleton_of_isAperiodic_of_lintegral_return_eq_top`](https://taucetiproject.org/docs/TauCeti/Probability/MarkovChain/Pointwise.html#ProbabilityTheory.Kernel.tendsto_pow_comp_real_singleton_of_isAperiodic_of_lintegral_return_eq_top)
- [Source of `ProbabilityTheory.Kernel.tendsto_pow_comp_real_singleton_of_isAperiodic_of_lintegral_return_eq_top` in TauCeti/Probability/MarkovChain/Pointwise.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/MarkovChain/Pointwise.lean#L75)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)
