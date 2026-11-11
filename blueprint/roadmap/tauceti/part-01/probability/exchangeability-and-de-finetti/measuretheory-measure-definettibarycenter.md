---
declaration: def
origin: cited
lean: MeasureTheory.Measure.deFinettiBarycenter
statement: formalized
---

# MeasureTheory.Measure.deFinettiBarycenter

The **de Finetti barycenter** of a mixing law `π` on `ProbabilityMeasure α`: the measure
`∫ P^{⊗ℕ} dπ(P)` on `ℕ → α` mixing the countable powers against `π`. For `π` a probability
measure this is the law of a sequence drawn i.i.d. from a `π`-random probability measure.

```lean
MeasureTheory.Measure.deFinettiBarycenter.{u_1} {α : Type u_1} [MeasurableSpace α]
  (π : MeasureTheory.Measure (MeasureTheory.ProbabilityMeasure α)) : MeasureTheory.Measure (ℕ → α)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.deFinettiBarycenter`](https://taucetiproject.org/docs/TauCeti/Probability/Process/PathLaw/Mixture.html#MeasureTheory.Measure.deFinettiBarycenter).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.deFinettiBarycenter`](https://taucetiproject.org/docs/TauCeti/Probability/Process/PathLaw/Mixture.html#MeasureTheory.Measure.deFinettiBarycenter)
- [Source of `MeasureTheory.Measure.deFinettiBarycenter` in TauCeti/Probability/Process/PathLaw/Mixture.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Process/PathLaw/Mixture.lean#L44)
- [Tau Ceti roadmap status: Exchangeability and de Finetti](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/Exchangeability/STATUS.md)
