---
declaration: theorem
origin: cited
lean: TauCeti.Probability.sampleWithoutReplacement_dirac
statement: formalized
proof: formalized
---

# TauCeti.Probability.sampleWithoutReplacement_dirac

Sampling a deterministic population without replacement is the pushforward of uniform
injective selections.

```lean
TauCeti.Probability.sampleWithoutReplacement_dirac.{u_1, u_2, u_3} {α : Type u_1}
  [MeasurableSpace α] {ι : Type u_2} {κ : Type u_3} [Finite κ] [MeasurableSpace κ]
  [MeasurableSingletonClass κ] (x : κ → α) :
  TauCeti.Probability.sampleWithoutReplacement (MeasureTheory.Measure.dirac x) =
    MeasureTheory.Measure.map (fun k i => x (k i))
      (ProbabilityTheory.uniformOn {k | Function.Injective k})
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.Probability.samplePopulation_dirac](tauceti-probability-samplepopulation-dirac.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.sampleWithoutReplacement_dirac`](https://taucetiproject.org/docs/TauCeti/Probability/PopulationSampling/Finite.html#TauCeti.Probability.sampleWithoutReplacement_dirac).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.sampleWithoutReplacement_dirac`](https://taucetiproject.org/docs/TauCeti/Probability/PopulationSampling/Finite.html#TauCeti.Probability.sampleWithoutReplacement_dirac)
- [Source of `TauCeti.Probability.sampleWithoutReplacement_dirac` in TauCeti/Probability/PopulationSampling/Finite.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/PopulationSampling/Finite.lean#L86)
- [Tau Ceti roadmap status: Sampling with and without replacement, exact discrepancy for finite populations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FiniteSamplingDiscrepancy/STATUS.md)
