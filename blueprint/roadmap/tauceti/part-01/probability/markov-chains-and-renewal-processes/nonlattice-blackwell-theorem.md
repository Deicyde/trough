---
declaration: theorem
origin: cited
lean: MeasureTheory.Measure.tendsto_renewalFunction_add_sub, MeasureTheory.Measure.tendsto_renewalMeasure_Ioc_sub, MeasureTheory.Measure.tendsto_renewalMeasure_real_Ioc
statement: formalized
proof: formalized
---

# Nonlattice Blackwell theorem

The increase in the expected renewal count
from `t` to `t + u` tends to `u` times the real value of the reciprocal extended mean.
The artificial arrival at zero is excluded, while genuine zero-time arrivals cancel
in the difference. No finite-mean assumption is required.

```lean
MeasureTheory.Measure.tendsto_renewalFunction_add_sub (F : MeasureTheory.Measure NNReal)
  [MeasureTheory.IsProbabilityMeasure F] (hNL : ¬F.IsLattice) (u : NNReal) :
  Filter.Tendsto (fun t => (F.renewalFunction (t + u)).toReal - (F.renewalFunction t).toReal)
    Filter.atTop (nhds ((∫⁻ (x : NNReal), ↑x ∂F)⁻¹.toReal * ↑u))
```

## Depends on

- [MeasureTheory.Measure.renewalMeasure](measuretheory-measure-renewalmeasure.md)

## Proof depends on

- [Prokhorov's theorem for finite measures](../../measure-theory/measure/prokhorovs-theorem-for-finite-measures.md)
- [Rigidity of harmonic measures](rigidity-of-harmonic-measures.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.tendsto_renewalFunction_add_sub`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/Blackwell.html#MeasureTheory.Measure.tendsto_renewalFunction_add_sub).

## Other forms

**Nonlattice Blackwell theorem, backward windows.** Formalized in Tau Ceti as [`MeasureTheory.Measure.tendsto_renewalMeasure_Ioc_sub`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/Blackwell.html#MeasureTheory.Measure.tendsto_renewalMeasure_Ioc_sub).

```lean
MeasureTheory.Measure.tendsto_renewalMeasure_Ioc_sub (F : MeasureTheory.Measure NNReal)
  [MeasureTheory.IsProbabilityMeasure F] (hNL : ¬F.IsLattice) (u : NNReal) :
  Filter.Tendsto (fun t => F.renewalMeasure (Set.Ioc (t - u) t)) Filter.atTop
    (nhds ((∫⁻ (x : NNReal), ↑x ∂F)⁻¹ * ↑u))
```

**Nonlattice Blackwell theorem, forward windows.** Formalized in Tau Ceti as [`MeasureTheory.Measure.tendsto_renewalMeasure_real_Ioc`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/Blackwell.html#MeasureTheory.Measure.tendsto_renewalMeasure_real_Ioc).

```lean
MeasureTheory.Measure.tendsto_renewalMeasure_real_Ioc (F : MeasureTheory.Measure NNReal)
  [MeasureTheory.IsProbabilityMeasure F] (hNL : ¬F.IsLattice) (u : NNReal) :
  Filter.Tendsto (fun t => F.renewalMeasure.real (Set.Ioc t (t + u))) Filter.atTop
    (nhds ((∫⁻ (x : NNReal), ↑x ∂F)⁻¹.toReal * ↑u))
```

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.tendsto_renewalFunction_add_sub`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/Blackwell.html#MeasureTheory.Measure.tendsto_renewalFunction_add_sub)
- [Source of `MeasureTheory.Measure.tendsto_renewalFunction_add_sub` in TauCeti/Probability/Renewal/Blackwell.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Renewal/Blackwell.lean#L97)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)
