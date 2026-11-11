---
declaration: theorem
origin: cited
lean: MeasureTheory.Measure.IsLatticeSpan.tendsto_renewalFunction_succ_mul_sub
statement: formalized
proof: formalized
---

# Lattice Blackwell theorem

At greatest span `a`, the increase in expected renewal
count from `n * a` to `(n + 1) * a` tends to `a` times the real value of the reciprocal
(in `ℝ≥0∞`) of the mean `∫⁻ t, (t : ℝ≥0∞) ∂F`.
The initial artificial arrival is excluded from the renewal function, while genuine
zero-time arrivals are retained. Infinite mean gives limit zero.

```lean
MeasureTheory.Measure.IsLatticeSpan.tendsto_renewalFunction_succ_mul_sub
  {F : MeasureTheory.Measure NNReal} [MeasureTheory.IsProbabilityMeasure F] {a : NNReal}
  (ha : F.IsLatticeSpan a) (hmax : IsGreatest {b | F.IsLatticeSpan b} a) :
  Filter.Tendsto
    (fun n => (F.renewalFunction (↑(n + 1) * a)).toReal - (F.renewalFunction (↑n * a)).toReal)
    Filter.atTop (nhds (↑a * (∫⁻ (t : NNReal), ↑t ∂F)⁻¹.toReal))
```

## Depends on

- [MeasureTheory.Measure.renewalMeasure](../markov-chains-and-renewal-processes/measuretheory-measure-renewalmeasure.md)

## Proof depends on

- [Lattice renewal density theorem](lattice-renewal-density-theorem.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.IsLatticeSpan.tendsto_renewalFunction_succ_mul_sub`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/Lattice/Blackwell.html#MeasureTheory.Measure.IsLatticeSpan.tendsto_renewalFunction_succ_mul_sub).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.IsLatticeSpan.tendsto_renewalFunction_succ_mul_sub`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/Lattice/Blackwell.html#MeasureTheory.Measure.IsLatticeSpan.tendsto_renewalFunction_succ_mul_sub)
- [Source of `MeasureTheory.Measure.IsLatticeSpan.tendsto_renewalFunction_succ_mul_sub` in TauCeti/Probability/Renewal/Lattice/Blackwell.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Renewal/Lattice/Blackwell.lean#L87)
