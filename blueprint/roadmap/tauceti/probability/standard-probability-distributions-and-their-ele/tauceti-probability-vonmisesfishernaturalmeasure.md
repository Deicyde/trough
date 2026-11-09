---
declaration: def
origin: cited
lean: TauCeti.Probability.vonMisesFisherNaturalMeasure
statement: formalized
---

# TauCeti.Probability.vonMisesFisherNaturalMeasure

The von Mises–Fisher law with natural parameter `η`, relative to uniform sphere probability.
In dimension zero the sphere and this measure are empty.

```lean
TauCeti.Probability.vonMisesFisherNaturalMeasure.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] (η : E) :
  MeasureTheory.Measure ↑(Metric.sphere 0 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.vonMisesFisherNaturalMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/VonMisesFisher/Basic.html#TauCeti.Probability.vonMisesFisherNaturalMeasure).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.vonMisesFisherNaturalMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/VonMisesFisher/Basic.html#TauCeti.Probability.vonMisesFisherNaturalMeasure)
- [Source of `TauCeti.Probability.vonMisesFisherNaturalMeasure` in TauCeti/Probability/Distributions/VonMisesFisher/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Distributions/VonMisesFisher/Basic.lean#L46)
- [Tau Ceti roadmap status: Standard probability distributions and their elementary theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/StandardDistributions/STATUS.md)
