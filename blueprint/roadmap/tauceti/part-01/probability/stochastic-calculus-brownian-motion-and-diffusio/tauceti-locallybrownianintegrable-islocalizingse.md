---
declaration: theorem
origin: cited
lean: TauCeti.LocallyBrownianIntegrable.isLocalizingSequence_energyLocalizer
statement: formalized
proof: formalized
---

# TauCeti.LocallyBrownianIntegrable.isLocalizingSequence_energyLocalizer

Positive integer closed energy levels yield a native localizing sequence on the raw
filtration. The stopping times are increasing everywhere and tend to infinity almost surely.

```lean
TauCeti.LocallyBrownianIntegrable.isLocalizingSequence_energyLocalizer.{u_1} {Ω : Type u_1}
  {mΩ : MeasurableSpace Ω} {ℱ : MeasureTheory.Filtration NNReal mΩ} {P : MeasureTheory.Measure Ω}
  {H : NNReal → Ω → ℝ} (hH : TauCeti.LocallyBrownianIntegrable ℱ P H) :
  ProbabilityTheory.IsLocalizingSequence ℱ (fun n => TauCeti.nnvolume.energyLocalizer H (↑n + 1)) P
```

## Depends on

- [MeasureTheory.Measure.energyLocalizer](measuretheory-measure-energylocalizer.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LocallyBrownianIntegrable.isLocalizingSequence_energyLocalizer`](https://taucetiproject.org/docs/TauCeti/Probability/BrownianMotion/Integral/Energy/Localization.html#TauCeti.LocallyBrownianIntegrable.isLocalizingSequence_energyLocalizer).

## Sources

- [Tau Ceti documentation: `TauCeti.LocallyBrownianIntegrable.isLocalizingSequence_energyLocalizer`](https://taucetiproject.org/docs/TauCeti/Probability/BrownianMotion/Integral/Energy/Localization.html#TauCeti.LocallyBrownianIntegrable.isLocalizingSequence_energyLocalizer)
- [Source of `TauCeti.LocallyBrownianIntegrable.isLocalizingSequence_energyLocalizer` in TauCeti/Probability/BrownianMotion/Integral/Energy/Localization.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/BrownianMotion/Integral/Energy/Localization.lean#L76)
- [Tau Ceti roadmap status: Stochastic calculus, Brownian motion and diffusions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/StochasticCalculus/STATUS.md)
