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
- [Source of `TauCeti.Probability.empiricalFiniteMeasure` in TauCeti/Probability/Process/EmpiricalMeasure.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Process/EmpiricalMeasure.lean#L54)
- [Tau Ceti roadmap status: Random matrices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RandomMatrices/STATUS.md)
