---
declaration: theorem
origin: cited
lean: TauCeti.Probability.contractable_iff_conditionallyIID, TauCeti.Probability.contractable_iff_mixedIID
statement: formalized
proof: formalized
---

# De Finetti–Ryll-Nardzewski, two-way conditional form

A process with a.e. measurable
coordinates, valued in a standard Borel space, under a finite measure, is contractable iff
it is conditionally i.i.d. This is the sharp conditional equivalence, matching
`contractable_iff_mixedIID` on the mixture side; the converse is `ConditionallyIID.contractable`,
which needs no side hypotheses.

```lean
TauCeti.Probability.contractable_iff_conditionallyIID.{u_1, u_2} {Ω : Type u_1} {α : Type u_2}
  {mΩ : MeasurableSpace Ω} [MeasurableSpace α] [StandardBorelSpace α] {μ : MeasureTheory.Measure Ω}
  [MeasureTheory.IsFiniteMeasure μ] {X : ℕ → Ω → α} (hX_meas : ∀ (n : ℕ), AEMeasurable (X n) μ) :
  TauCeti.Probability.Contractable μ X ↔ TauCeti.Probability.ConditionallyIID μ X
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [De Finetti's theorem](de-finettis-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.contractable_iff_conditionallyIID`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/Theorem.html#TauCeti.Probability.contractable_iff_conditionallyIID).

## Other forms

**De Finetti–Ryll-Nardzewski, two-way mixture form.** Formalized in Tau Ceti as [`TauCeti.Probability.contractable_iff_mixedIID`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/Theorem.html#TauCeti.Probability.contractable_iff_mixedIID).

```lean
TauCeti.Probability.contractable_iff_mixedIID.{u_1, u_2} {Ω : Type u_1} {α : Type u_2}
  {mΩ : MeasurableSpace Ω} [MeasurableSpace α] [StandardBorelSpace α] {μ : MeasureTheory.Measure Ω}
  [MeasureTheory.IsFiniteMeasure μ] {X : ℕ → Ω → α} (hX_meas : ∀ (n : ℕ), AEMeasurable (X n) μ) :
  TauCeti.Probability.Contractable μ X ↔ TauCeti.Probability.MixedIID μ X
```

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.contractable_iff_conditionallyIID`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/Theorem.html#TauCeti.Probability.contractable_iff_conditionallyIID)
- [Source of `TauCeti.Probability.contractable_iff_conditionallyIID` in TauCeti/Probability/DeFinetti/Theorem.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/DeFinetti/Theorem.lean#L174)
- [Tau Ceti roadmap status: Exchangeability and de Finetti](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/Exchangeability/STATUS.md)
