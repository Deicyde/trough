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
- [Source of `TauCeti.Probability.samplePopulation_dirac` in TauCeti/Probability/PopulationSampling/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/PopulationSampling/Basic.lean#L103)
- [Tau Ceti roadmap status: Sampling with and without replacement, exact discrepancy for finite populations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FiniteSamplingDiscrepancy/STATUS.md)
