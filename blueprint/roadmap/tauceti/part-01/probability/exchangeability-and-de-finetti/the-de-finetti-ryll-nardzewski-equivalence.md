---
declaration: theorem
origin: cited
lean: TauCeti.Probability.deFinetti_RyllNardzewski_equivalence, TauCeti.Probability.contractable_iff_exchangeable_and_mixedIID
statement: formalized
proof: formalized
---

# The de Finetti–Ryll-Nardzewski equivalence

A process with a.e. measurable coordinates,
valued in a standard Borel space, is contractable iff it is both exchangeable and
conditionally i.i.d. Derived from the two-way `contractable_iff_conditionallyIID`, with the
exchangeability conjunct supplied by `ConditionallyIID.exchangeable` (the conjunct is redundant
given conditional i.i.d.-ness).

```lean
TauCeti.Probability.deFinetti_RyllNardzewski_equivalence.{u_1, u_2} {Ω : Type u_1} {α : Type u_2}
  {mΩ : MeasurableSpace Ω} [MeasurableSpace α] [StandardBorelSpace α] {μ : MeasureTheory.Measure Ω}
  [MeasureTheory.IsFiniteMeasure μ] {X : ℕ → Ω → α} (hX_meas : ∀ (n : ℕ), AEMeasurable (X n) μ) :
  TauCeti.Probability.Contractable μ X ↔
    TauCeti.Probability.Exchangeable μ X ∧ TauCeti.Probability.ConditionallyIID μ X
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [De Finetti–Ryll-Nardzewski, two-way conditional form](de-finetti-ryll-nardzewski-two-way-conditional-f.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.deFinetti_RyllNardzewski_equivalence`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/Theorem.html#TauCeti.Probability.deFinetti_RyllNardzewski_equivalence).

## Other forms

**The de Finetti–Ryll-Nardzewski equivalence, mixture form (Kallenberg, Theorem 1.1), in conjunction form.** Formalized in Tau Ceti as [`TauCeti.Probability.contractable_iff_exchangeable_and_mixedIID`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/Theorem.html#TauCeti.Probability.contractable_iff_exchangeable_and_mixedIID).

```lean
TauCeti.Probability.contractable_iff_exchangeable_and_mixedIID.{u_1, u_2} {Ω : Type u_1}
  {α : Type u_2} {mΩ : MeasurableSpace Ω} [MeasurableSpace α] [StandardBorelSpace α]
  {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsFiniteMeasure μ] {X : ℕ → Ω → α}
  (hX_meas : ∀ (n : ℕ), AEMeasurable (X n) μ) :
  TauCeti.Probability.Contractable μ X ↔
    TauCeti.Probability.Exchangeable μ X ∧ TauCeti.Probability.MixedIID μ X
```

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.deFinetti_RyllNardzewski_equivalence`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/Theorem.html#TauCeti.Probability.deFinetti_RyllNardzewski_equivalence)
- [Source of `TauCeti.Probability.deFinetti_RyllNardzewski_equivalence` in TauCeti/Probability/DeFinetti/Theorem.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/DeFinetti/Theorem.lean#L184)
- [Tau Ceti roadmap status: Exchangeability and de Finetti](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/Exchangeability/STATUS.md)
