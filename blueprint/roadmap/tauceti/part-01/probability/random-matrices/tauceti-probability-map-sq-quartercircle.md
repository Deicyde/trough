---
declaration: theorem
origin: cited
lean: TauCeti.Probability.map_sq_quarterCircle
statement: formalized
proof: formalized
---

# TauCeti.Probability.map_sq_quarterCircle

The square of a quarter-circle variable has the Marchenko–Pastur law of ratio one.

```lean
TauCeti.Probability.map_sq_quarterCircle :
  MeasureTheory.Measure.map (fun x => x ^ 2) TauCeti.Probability.quarterCircle =
    TauCeti.Probability.marchenkoPastur 1
```

## Depends on

- [TauCeti.Probability.marchenkoPastur](tauceti-probability-marchenkopastur.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.map_sq_quarterCircle`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/QuarterCircle.html#TauCeti.Probability.map_sq_quarterCircle).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.map_sq_quarterCircle`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/QuarterCircle.html#TauCeti.Probability.map_sq_quarterCircle)
- [Source of `TauCeti.Probability.map_sq_quarterCircle` in TauCeti/Probability/Distributions/QuarterCircle.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Distributions/QuarterCircle.lean#L157)
- [Tau Ceti roadmap status: Random matrices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RandomMatrices/STATUS.md)
