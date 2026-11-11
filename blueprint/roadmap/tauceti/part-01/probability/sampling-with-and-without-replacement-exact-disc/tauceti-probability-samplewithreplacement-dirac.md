---
declaration: theorem
origin: cited
lean: TauCeti.Probability.sampleWithReplacement_dirac
statement: formalized
proof: formalized
---

# TauCeti.Probability.sampleWithReplacement_dirac

Sampling a deterministic population with replacement is the pushforward of uniform
selections, without an injectivity constraint.

```lean
TauCeti.Probability.sampleWithReplacement_dirac.{u_1, u_2, u_3} {α : Type u_1} [MeasurableSpace α]
  {ι : Type u_2} {κ : Type u_3} [MeasurableSpace κ] [MeasurableSingletonClass κ] [Fintype ι]
  [Finite κ] (x : κ → α) :
  TauCeti.Probability.sampleWithReplacement (MeasureTheory.Measure.dirac x) =
    MeasureTheory.Measure.map (fun k i => x (k i)) (ProbabilityTheory.uniformOn Set.univ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.Probability.samplePopulation_dirac](tauceti-probability-samplepopulation-dirac.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.sampleWithReplacement_dirac`](https://taucetiproject.org/docs/TauCeti/Probability/PopulationSampling/Finite.html#TauCeti.Probability.sampleWithReplacement_dirac).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.sampleWithReplacement_dirac`](https://taucetiproject.org/docs/TauCeti/Probability/PopulationSampling/Finite.html#TauCeti.Probability.sampleWithReplacement_dirac)
- [Source of `TauCeti.Probability.sampleWithReplacement_dirac` in TauCeti/Probability/PopulationSampling/Finite.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/PopulationSampling/Finite.lean#L169)
- [Tau Ceti roadmap status: Sampling with and without replacement, exact discrepancy for finite populations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FiniteSamplingDiscrepancy/STATUS.md)
