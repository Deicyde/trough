---
declaration: theorem
origin: cited
lean: TauCeti.Probability.IsFilteredPoissonProcess.martingale_compensated_sq_sub
statement: formalized
proof: formalized
---

# TauCeti.Probability.IsFilteredPoissonProcess.martingale_compensated_sq_sub

The compensated square `(N t - α * t)² - α * t` is a martingale.

```lean
TauCeti.Probability.IsFilteredPoissonProcess.martingale_compensated_sq_sub.{u_1} {Ω : Type u_1}
  {mΩ : MeasurableSpace Ω} {P : MeasureTheory.Measure Ω} {ℱ : MeasureTheory.Filtration NNReal mΩ}
  {α : NNReal} {N : NNReal → Ω → ℝ} (hN : TauCeti.Probability.IsFilteredPoissonProcess ℱ α N P) :
  MeasureTheory.Martingale (fun t ω => (N t ω - ↑α * ↑t) ^ 2 - ↑α * ↑t) ℱ P
```

## Depends on

- [TauCeti.Probability.IsFilteredPoissonProcess](tauceti-probability-isfilteredpoissonprocess.md)

## Proof depends on

- [TauCeti.Probability.IsFilteredPoissonProcess.martingale_compensated](tauceti-probability-isfilteredpoissonprocess-mar.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.IsFilteredPoissonProcess.martingale_compensated_sq_sub`](https://taucetiproject.org/docs/TauCeti/Probability/Process/Poisson/Martingale.html#TauCeti.Probability.IsFilteredPoissonProcess.martingale_compensated_sq_sub).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.IsFilteredPoissonProcess.martingale_compensated_sq_sub`](https://taucetiproject.org/docs/TauCeti/Probability/Process/Poisson/Martingale.html#TauCeti.Probability.IsFilteredPoissonProcess.martingale_compensated_sq_sub)
- [Source of `TauCeti.Probability.IsFilteredPoissonProcess.martingale_compensated_sq_sub` in TauCeti/Probability/Process/Poisson/Martingale.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Process/Poisson/Martingale.lean#L147)
- [Tau Ceti roadmap status: Stochastic calculus, Brownian motion and diffusions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/StochasticCalculus/STATUS.md)
