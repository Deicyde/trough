---
declaration: def
origin: cited
lean: TauCeti.IsPredictableTime
statement: formalized
---

# TauCeti.IsPredictableTime

A time is pointwise predictable if it admits an everywhere finite announcing sequence.
Such a time is automatically a stopping time, even for a raw filtration.

```lean
TauCeti.IsPredictableTime.{u_1} {Ω : Type u_1} {m : MeasurableSpace Ω}
  (ℱ : MeasureTheory.Filtration NNReal m) (τ : Ω → WithTop NNReal) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsPredictableTime`](https://taucetiproject.org/docs/TauCeti/Probability/Process/Predictable/StoppingTime.html#TauCeti.IsPredictableTime).

## Sources

- [Tau Ceti documentation: `TauCeti.IsPredictableTime`](https://taucetiproject.org/docs/TauCeti/Probability/Process/Predictable/StoppingTime.html#TauCeti.IsPredictableTime)
- [Source of `TauCeti.IsPredictableTime` in TauCeti/Probability/Process/Predictable/StoppingTime.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Process/Predictable/StoppingTime.lean#L57)
- [Tau Ceti roadmap status: Stochastic calculus, Brownian motion and diffusions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/StochasticCalculus/STATUS.md)
