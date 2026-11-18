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

- [MeasureTheory.Measure.renewalMeasure](measuretheory-measure-renewalmeasure.md)

## Proof depends on

- [Chapman–Kolmogorov lower bound](../other-results/chapman-kolmogorov-lower-bound.md)
- [Convergence to equilibrium](convergence-to-equilibrium.md)
- [Pointwise decay at an infinite-mean state](pointwise-decay-at-an-infinite-mean-state.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.IsLatticeSpan.tendsto_renewalMeasure_real_mul`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/Lattice/Blackwell.html#MeasureTheory.Measure.IsLatticeSpan.tendsto_renewalMeasure_real_mul).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.IsLatticeSpan.tendsto_renewalMeasure_real_mul`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/Lattice/Blackwell.html#MeasureTheory.Measure.IsLatticeSpan.tendsto_renewalMeasure_real_mul)
- [Source of `MeasureTheory.Measure.IsLatticeSpan.tendsto_renewalMeasure_real_mul` in TauCeti/Probability/Renewal/Lattice/Blackwell.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Renewal/Lattice/Blackwell.lean#L42)
