---
declaration: theorem
origin: cited
lean: TauCeti.Probability.deFinetti_RyllNardzewski_equivalence, TauCeti.Probability.contractable_iff_exchangeable_and_mixedIID, TauCeti.Probability.contractable_iff_conditionallyIID, TauCeti.Probability.contractable_iff_mixedIID
statement: formalized
proof: formalized
---

# The de Finetti–Ryll-Nardzewski equivalence

A process with a.e. measurable coordinates,
valued in a nonempty standard Borel space, is contractable iff it is both exchangeable and
conditionally i.i.d. Derived from the two-way `contractable_iff_conditionallyIID`, with the
exchangeability conjunct supplied by `ConditionallyIID.exchangeable` (the conjunct is redundant
given conditional i.i.d.-ness).

```lean
TauCeti.Probability.deFinetti_RyllNardzewski_equivalence.{u_1, u_2} {Ω : Type u_1} {α : Type u_2}
  {mΩ : MeasurableSpace Ω} [MeasurableSpace α] [StandardBorelSpace α] [Nonempty α]
  {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsFiniteMeasure μ] {X : ℕ → Ω → α}
  (hX_meas : ∀ (n : ℕ), AEMeasurable (X n) μ) :
  TauCeti.Probability.Contractable μ X ↔
    TauCeti.Probability.Exchangeable μ X ∧ TauCeti.Probability.ConditionallyIID μ X
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [De Finetti's theorem](de-finettis-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.deFinetti_RyllNardzewski_equivalence`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/Theorem.html#TauCeti.Probability.deFinetti_RyllNardzewski_equivalence).

## Other forms

**The de Finetti–Ryll-Nardzewski equivalence, mixture form (Kallenberg, Theorem 1.1), in conjunction form.** Formalized in Tau Ceti as [`TauCeti.Probability.contractable_iff_exchangeable_and_mixedIID`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/Theorem.html#TauCeti.Probability.contractable_iff_exchangeable_and_mixedIID).

```lean
TauCeti.Probability.contractable_iff_exchangeable_and_mixedIID.{u_1, u_2} {Ω : Type u_1}
  {α : Type u_2} {mΩ : MeasurableSpace Ω} [MeasurableSpace α] [StandardBorelSpace α] [Nonempty α]
  {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsFiniteMeasure μ] {X : ℕ → Ω → α}
  (hX_meas : ∀ (n : ℕ), AEMeasurable (X n) μ) :
  TauCeti.Probability.Contractable μ X ↔
    TauCeti.Probability.Exchangeable μ X ∧ TauCeti.Probability.MixedIID μ X
```

**De Finetti–Ryll-Nardzewski, two-way conditional form.** Formalized in Tau Ceti as [`TauCeti.Probability.contractable_iff_conditionallyIID`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/Theorem.html#TauCeti.Probability.contractable_iff_conditionallyIID).

```lean
TauCeti.Probability.contractable_iff_conditionallyIID.{u_1, u_2} {Ω : Type u_1} {α : Type u_2}
  {mΩ : MeasurableSpace Ω} [MeasurableSpace α] [StandardBorelSpace α] [Nonempty α]
  {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsFiniteMeasure μ] {X : ℕ → Ω → α}
  (hX_meas : ∀ (n : ℕ), AEMeasurable (X n) μ) :
  TauCeti.Probability.Contractable μ X ↔ TauCeti.Probability.ConditionallyIID μ X
```

**De Finetti–Ryll-Nardzewski, two-way mixture form.** Formalized in Tau Ceti as [`TauCeti.Probability.contractable_iff_mixedIID`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/Theorem.html#TauCeti.Probability.contractable_iff_mixedIID).

```lean
TauCeti.Probability.contractable_iff_mixedIID.{u_1, u_2} {Ω : Type u_1} {α : Type u_2}
  {mΩ : MeasurableSpace Ω} [MeasurableSpace α] [StandardBorelSpace α] [Nonempty α]
  {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsFiniteMeasure μ] {X : ℕ → Ω → α}
  (hX_meas : ∀ (n : ℕ), AEMeasurable (X n) μ) :
  TauCeti.Probability.Contractable μ X ↔ TauCeti.Probability.MixedIID μ X
```

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.deFinetti_RyllNardzewski_equivalence`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/Theorem.html#TauCeti.Probability.deFinetti_RyllNardzewski_equivalence)
- [Source of `TauCeti.Probability.deFinetti_RyllNardzewski_equivalence` in TauCeti/Probability/DeFinetti/Theorem.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/DeFinetti/Theorem.lean#L181)
- [Tau Ceti roadmap status: Exchangeability and de Finetti](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/Exchangeability/STATUS.md)
