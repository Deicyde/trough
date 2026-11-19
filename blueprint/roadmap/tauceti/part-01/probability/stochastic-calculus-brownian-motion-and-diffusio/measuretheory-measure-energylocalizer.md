---
declaration: def
origin: cited
lean: MeasureTheory.Measure.energyLocalizer
statement: formalized
---

# MeasureTheory.Measure.energyLocalizer

First closed-level hit of the accumulated energy of the finite-energy cutoff.
A positive level gives a strictly positive time for an atomless time measure.

```lean
MeasureTheory.Measure.energyLocalizer.{u_1, u_2} {Ω : Type u_1} {E : Type u_2}
  [NormedAddCommGroup E] (μ : MeasureTheory.Measure NNReal) (H : NNReal → Ω → E) (C : NNReal) :
  Ω → WithTop NNReal
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.energyLocalizer`](https://taucetiproject.org/docs/TauCeti/Probability/Process/EnergyLocalizer.html#MeasureTheory.Measure.energyLocalizer).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.energyLocalizer`](https://taucetiproject.org/docs/TauCeti/Probability/Process/EnergyLocalizer.html#MeasureTheory.Measure.energyLocalizer)
- [Source of `MeasureTheory.Measure.energyLocalizer` in TauCeti/Probability/Process/EnergyLocalizer.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Process/EnergyLocalizer.lean#L42)
- [Tau Ceti roadmap status: Stochastic calculus, Brownian motion and diffusions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/StochasticCalculus/STATUS.md)
