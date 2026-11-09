---
declaration: theorem
origin: cited
lean: TauCeti.Probability.conditionallyIID_of_exchangeableFamily_of_equiv_nat
statement: formalized
proof: formalized
---

# De Finetti's theorem transported along an explicit enumeration

Under a finite measure,
an exchangeable family with measurable coordinates whose index type is equivalent to `ℕ` is
conditionally i.i.d.

```lean
TauCeti.Probability.conditionallyIID_of_exchangeableFamily_of_equiv_nat.{u_1, u_2, u_3}
  {Ω : Type u_1} {α : Type u_2} {ι : Type u_3} [MeasurableSpace Ω] [MeasurableSpace α]
  [StandardBorelSpace α] [Nonempty α] {μ : MeasureTheory.Measure Ω}
  [MeasureTheory.IsFiniteMeasure μ] {X : ι → Ω → α}
  (hX : TauCeti.Probability.ExchangeableFamily μ X) (e : ι ≃ ℕ)
  (hX_meas : ∀ (i : ι), Measurable (X i)) : TauCeti.Probability.ConditionallyIID μ X
```

## Depends on

Its statement uses no other declaration mapped here.

## Informally uses

- [De Finetti's theorem](../exchangeability-and-de-finetti/de-finettis-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.conditionallyIID_of_exchangeableFamily_of_equiv_nat`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/CountableIndex.html#TauCeti.Probability.conditionallyIID_of_exchangeableFamily_of_equiv_nat).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.conditionallyIID_of_exchangeableFamily_of_equiv_nat`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/CountableIndex.html#TauCeti.Probability.conditionallyIID_of_exchangeableFamily_of_equiv_nat)
- [Source of `TauCeti.Probability.conditionallyIID_of_exchangeableFamily_of_equiv_nat` in TauCeti/Probability/DeFinetti/CountableIndex.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/DeFinetti/CountableIndex.lean#L38)
