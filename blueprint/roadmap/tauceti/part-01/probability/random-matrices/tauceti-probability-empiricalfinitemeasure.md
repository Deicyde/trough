---
declaration: def
origin: cited
lean: TauCeti.Probability.empiricalFiniteMeasure
statement: formalized
---

# TauCeti.Probability.empiricalFiniteMeasure

The empirical finite measure `(card κ)⁻¹ ∑ᵢ δ_{x i}` of a finite family `x : κ → α`.

Values are counted with multiplicity. For a nonempty index type this is a probability measure, the
one underlying `empiricalMeasureOfFintype`; for an empty family it is the zero measure.

```lean
TauCeti.Probability.empiricalFiniteMeasure.{u_1, u_4} {α : Type u_1} [MeasurableSpace α]
  {κ : Type u_4} [Fintype κ] (x : κ → α) : MeasureTheory.FiniteMeasure α
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.empiricalFiniteMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/Process/EmpiricalMeasure.html#TauCeti.Probability.empiricalFiniteMeasure).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.empiricalFiniteMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/Process/EmpiricalMeasure.html#TauCeti.Probability.empiricalFiniteMeasure)
- [Source of `TauCeti.Probability.empiricalFiniteMeasure` in TauCeti/Probability/Process/EmpiricalMeasure.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Process/EmpiricalMeasure.lean#L54)
- [Tau Ceti roadmap status: Random matrices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RandomMatrices/STATUS.md)
