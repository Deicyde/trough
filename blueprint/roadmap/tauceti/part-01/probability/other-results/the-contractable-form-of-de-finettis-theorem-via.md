---
declaration: theorem
origin: cited
lean: TauCeti.Probability.conditionallyIID_of_contractable_viaL2
statement: formalized
proof: formalized
---

# The contractable form of de Finetti's theorem via `L²` averaging

A contractable process
valued in a nonempty standard Borel space is conditionally i.i.d.

The directing measure witnessing the conclusion is
`tailConditionalProbabilityMeasure μ X`; its stronger witness-level statement is
`Contractable.conditionallyIIDWith_directingProbabilityMeasure`.

```lean
TauCeti.Probability.conditionallyIID_of_contractable_viaL2.{u_1, u_2} {Ω : Type u_1} {α : Type u_2}
  [MeasurableSpace Ω] [MeasurableSpace α] [StandardBorelSpace α] [Nonempty α]
  {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsFiniteMeasure μ] {X : ℕ → Ω → α}
  (hX : TauCeti.Probability.Contractable μ X) (hX_meas : ∀ (n : ℕ), Measurable (X n)) :
  TauCeti.Probability.ConditionallyIID μ X
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.conditionallyIID_of_contractable_viaL2`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/ViaL2/Theorem.html#TauCeti.Probability.conditionallyIID_of_contractable_viaL2).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.conditionallyIID_of_contractable_viaL2`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/ViaL2/Theorem.html#TauCeti.Probability.conditionallyIID_of_contractable_viaL2)
- [Source of `TauCeti.Probability.conditionallyIID_of_contractable_viaL2` in TauCeti/Probability/DeFinetti/ViaL2/Theorem.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/DeFinetti/ViaL2/Theorem.lean#L58)
