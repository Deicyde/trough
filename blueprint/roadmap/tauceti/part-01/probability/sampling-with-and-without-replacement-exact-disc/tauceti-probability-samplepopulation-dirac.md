---
declaration: theorem
origin: cited
lean: TauCeti.Probability.samplePopulation_dirac
statement: formalized
proof: formalized
---

# TauCeti.Probability.samplePopulation_dirac

Sampling a deterministic population is the pushforward of the selection law by reading
that population at the selected indices.

```lean
TauCeti.Probability.samplePopulation_dirac.{u_1, u_2, u_3} {α : Type u_1} [MeasurableSpace α]
  {ι : Type u_2} {κ : Type u_3} [MeasurableSpace κ] [Countable κ] [MeasurableSingletonClass κ]
  (σ : MeasureTheory.Measure (ι → κ)) [MeasureTheory.SFinite σ] (x : κ → α) :
  TauCeti.Probability.samplePopulation σ (MeasureTheory.Measure.dirac x) =
    MeasureTheory.Measure.map (fun k i => x (k i)) σ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.samplePopulation_dirac`](https://taucetiproject.org/docs/TauCeti/Probability/PopulationSampling/Basic.html#TauCeti.Probability.samplePopulation_dirac).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.samplePopulation_dirac`](https://taucetiproject.org/docs/TauCeti/Probability/PopulationSampling/Basic.html#TauCeti.Probability.samplePopulation_dirac)
- [Source of `TauCeti.Probability.samplePopulation_dirac` in TauCeti/Probability/PopulationSampling/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/PopulationSampling/Basic.lean#L126)
- [Tau Ceti roadmap status: Sampling with and without replacement, exact discrepancy for finite populations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FiniteSamplingDiscrepancy/STATUS.md)
