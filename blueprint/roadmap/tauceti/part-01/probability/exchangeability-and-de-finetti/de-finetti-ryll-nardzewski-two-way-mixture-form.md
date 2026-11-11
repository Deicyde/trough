---
declaration: theorem
origin: cited
lean: TauCeti.Probability.contractable_iff_mixedIID, TauCeti.Probability.contractable_iff_conditionallyIID
statement: formalized
proof: formalized
---

# De Finetti–Ryll-Nardzewski, two-way mixture form

A process with a.e. measurable
coordinates, valued in a standard Borel space, under a finite measure, is contractable iff
it is mixed i.i.d. Forward: the conditional summit (`conditionallyIID_of_contractable`) followed
by `mixedIID_of_conditionallyIID`; converse: `MixedIID.contractable`, which needs no side
hypotheses.

```lean
TauCeti.Probability.contractable_iff_mixedIID.{u_1, u_2} {Ω : Type u_1} {α : Type u_2}
  {mΩ : MeasurableSpace Ω} [MeasurableSpace α] [StandardBorelSpace α] {μ : MeasureTheory.Measure Ω}
  [MeasureTheory.IsFiniteMeasure μ] {X : ℕ → Ω → α} (hX_meas : ∀ (n : ℕ), AEMeasurable (X n) μ) :
  TauCeti.Probability.Contractable μ X ↔ TauCeti.Probability.MixedIID μ X
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [De Finetti's theorem](de-finettis-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.contractable_iff_mixedIID`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/Theorem.html#TauCeti.Probability.contractable_iff_mixedIID).

## Other forms

**De Finetti–Ryll-Nardzewski, two-way conditional form.** Formalized in Tau Ceti as [`TauCeti.Probability.contractable_iff_conditionallyIID`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/Theorem.html#TauCeti.Probability.contractable_iff_conditionallyIID).

```lean
TauCeti.Probability.contractable_iff_conditionallyIID.{u_1, u_2} {Ω : Type u_1} {α : Type u_2}
  {mΩ : MeasurableSpace Ω} [MeasurableSpace α] [StandardBorelSpace α] {μ : MeasureTheory.Measure Ω}
  [MeasureTheory.IsFiniteMeasure μ] {X : ℕ → Ω → α} (hX_meas : ∀ (n : ℕ), AEMeasurable (X n) μ) :
  TauCeti.Probability.Contractable μ X ↔ TauCeti.Probability.ConditionallyIID μ X
```

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.contractable_iff_mixedIID`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/Theorem.html#TauCeti.Probability.contractable_iff_mixedIID)
- [Source of `TauCeti.Probability.contractable_iff_mixedIID` in TauCeti/Probability/DeFinetti/Theorem.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/DeFinetti/Theorem.lean#L210)
