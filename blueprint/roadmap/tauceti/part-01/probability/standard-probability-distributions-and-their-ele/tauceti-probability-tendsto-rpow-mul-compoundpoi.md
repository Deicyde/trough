---
declaration: theorem
origin: cited
lean: TauCeti.Probability.tendsto_rpow_mul_compoundPoissonMeasure_real_Ioi
statement: formalized
proof: formalized
---

# TauCeti.Probability.tendsto_rpow_mul_compoundPoissonMeasure_real_Ioi

A power-law right-tail constant of the jump distribution is multiplied by the rate
under compound Poisson summation, including rate zero and zero tail constants.

```lean
TauCeti.Probability.tendsto_rpow_mul_compoundPoissonMeasure_real_Ioi {μ : MeasureTheory.Measure ℝ}
  [MeasureTheory.IsProbabilityMeasure μ] (r : NNReal) {α C : ℝ}
  (hμ : Filter.Tendsto (fun x => x ^ α * μ.real (Set.Ioi x)) Filter.atTop (nhds C)) :
  Filter.Tendsto
    (fun x => x ^ α * (TauCeti.Probability.compoundPoissonMeasure r μ).real (Set.Ioi x))
    Filter.atTop (nhds (↑r * C))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.tendsto_rpow_mul_compoundPoissonMeasure_real_Ioi`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/CompoundPoisson/Tail.html#TauCeti.Probability.tendsto_rpow_mul_compoundPoissonMeasure_real_Ioi).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.tendsto_rpow_mul_compoundPoissonMeasure_real_Ioi`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/CompoundPoisson/Tail.html#TauCeti.Probability.tendsto_rpow_mul_compoundPoissonMeasure_real_Ioi)
- [Source of `TauCeti.Probability.tendsto_rpow_mul_compoundPoissonMeasure_real_Ioi` in TauCeti/Probability/Distributions/CompoundPoisson/Tail.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Distributions/CompoundPoisson/Tail.lean#L39)
- [Tau Ceti roadmap status: Standard probability distributions and their elementary theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/StandardDistributions/STATUS.md)
