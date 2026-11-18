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
TauCeti.Probability.sampleWithReplacement_dirac.{u_1, u_3, u_4} {α : Type u_1} [MeasurableSpace α]
  {ι : Type u_3} {κ : Type u_4} [MeasurableSpace κ] [MeasurableSingletonClass κ] [Fintype ι]
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
- [Source of `TauCeti.Probability.sampleWithReplacement_dirac` in TauCeti/Probability/PopulationSampling/Finite.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/PopulationSampling/Finite.lean#L194)
- [Tau Ceti roadmap status: Sampling with and without replacement, exact discrepancy for finite populations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FiniteSamplingDiscrepancy/STATUS.md)
