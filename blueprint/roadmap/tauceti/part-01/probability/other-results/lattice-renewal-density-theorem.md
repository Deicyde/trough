---
declaration: theorem
origin: cited
lean: MeasureTheory.Measure.IsLatticeSpan.tendsto_renewalMeasure_real_mul
statement: formalized
proof: formalized
---

# Lattice renewal density theorem

At greatest span, the real mass of the renewal
measure at `n * a` tends to `a` times the reciprocal extended interarrival mean.
Zero gaps and infinite means are included.

```lean
MeasureTheory.Measure.IsLatticeSpan.tendsto_renewalMeasure_real_mul
  {F : MeasureTheory.Measure NNReal} [MeasureTheory.IsProbabilityMeasure F] {a : NNReal}
  (ha : F.IsLatticeSpan a) (hmax : IsGreatest {b | F.IsLatticeSpan b} a) :
  Filter.Tendsto (fun n => F.renewalMeasure.real {↑n * a}) Filter.atTop
    (nhds (↑a * (∫⁻ (t : NNReal), ↑t ∂F)⁻¹.toReal))
```

## Depends on

- [MeasureTheory.Measure.renewalMeasure](../markov-chains-and-renewal-processes/measuretheory-measure-renewalmeasure.md)

## Proof depends on

- [Almost-sure renewal law of large numbers](../markov-chains-and-renewal-processes/almost-sure-renewal-law-of-large-numbers.md)
- [Chapman–Kolmogorov lower bound](chapman-kolmogorov-lower-bound.md)
- [MeasureTheory.Measure.countdownKernel](../markov-chains-and-renewal-processes/measuretheory-measure-countdownkernel.md)
- [ProbabilityTheory.Kernel.tendsto_tvDist_pow_comp_of_parallelComp_isRecurrent](../markov-chains-and-renewal-processes/probabilitytheory-kernel-tendsto-tvdist-pow-comp.md)
- [Uniqueness for the renewal equation](../markov-chains-and-renewal-processes/uniqueness-for-the-renewal-equation.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.IsLatticeSpan.tendsto_renewalMeasure_real_mul`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/Lattice/Blackwell.html#MeasureTheory.Measure.IsLatticeSpan.tendsto_renewalMeasure_real_mul).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.IsLatticeSpan.tendsto_renewalMeasure_real_mul`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/Lattice/Blackwell.html#MeasureTheory.Measure.IsLatticeSpan.tendsto_renewalMeasure_real_mul)
- [Source of `MeasureTheory.Measure.IsLatticeSpan.tendsto_renewalMeasure_real_mul` in TauCeti/Probability/Renewal/Lattice/Blackwell.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Renewal/Lattice/Blackwell.lean#L42)
