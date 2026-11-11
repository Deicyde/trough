---
declaration: theorem
origin: cited
lean: TauCeti.Probability.JointlyExchangeable.conditionallyIID_arrayRow_arrayBlockPair, TauCeti.Probability.SeparatelyExchangeable.conditionallyIID_arrayCol, TauCeti.Probability.JointlyExchangeable.conditionallyIID_arrayRow_arrayBlock, TauCeti.Probability.SeparatelyExchangeable.conditionallyIID_arrayRow
statement: formalized
proof: formalized
---

# De Finetti's theorem for the rows of a block of pairs

The conclusion simultaneously
describes both orientations of the selected rectangular cross-block.

```lean
TauCeti.Probability.JointlyExchangeable.conditionallyIID_arrayRow_arrayBlockPair.{u_1, u_2}
  {α : Type u_1} {Ω : Type u_2} [MeasurableSpace α] [MeasurableSpace Ω]
  {μ : MeasureTheory.Measure Ω} {X : ℕ × ℕ → Ω → α} {e f : ℕ → ℕ} [StandardBorelSpace α]
  [MeasureTheory.IsFiniteMeasure μ] (h : TauCeti.Probability.JointlyExchangeable μ X)
  (hX : ∀ (p : ℕ × ℕ), AEMeasurable (X p) μ) (he : Function.Injective e) (hf : Function.Injective f)
  (hd : Disjoint (Set.range e) (Set.range f)) :
  TauCeti.Probability.ConditionallyIID μ
    (TauCeti.Probability.arrayRow (TauCeti.Probability.arrayBlockPair X e f))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [De Finetti's theorem](../exchangeability-and-de-finetti/de-finettis-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.JointlyExchangeable.conditionallyIID_arrayRow_arrayBlockPair`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/Arrays/DeFinetti.html#TauCeti.Probability.JointlyExchangeable.conditionallyIID_arrayRow_arrayBlockPair).

## Other forms

**De Finetti's theorem for the columns of a separately exchangeable array.** Formalized in Tau Ceti as [`TauCeti.Probability.SeparatelyExchangeable.conditionallyIID_arrayCol`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/Arrays/DeFinetti.html#TauCeti.Probability.SeparatelyExchangeable.conditionallyIID_arrayCol).

```lean
TauCeti.Probability.SeparatelyExchangeable.conditionallyIID_arrayCol.{u_1, u_2} {α : Type u_1}
  {Ω : Type u_2} [MeasurableSpace α] [MeasurableSpace Ω] [StandardBorelSpace α]
  {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsFiniteMeasure μ] {X : ℕ × ℕ → Ω → α}
  (h : TauCeti.Probability.SeparatelyExchangeable μ X) (hX : ∀ (p : ℕ × ℕ), AEMeasurable (X p) μ) :
  TauCeti.Probability.ConditionallyIID μ (TauCeti.Probability.arrayCol X)
```

**De Finetti's theorem for the rows of a block of a jointly exchangeable array.** Formalized in Tau Ceti as [`TauCeti.Probability.JointlyExchangeable.conditionallyIID_arrayRow_arrayBlock`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/Arrays/DeFinetti.html#TauCeti.Probability.JointlyExchangeable.conditionallyIID_arrayRow_arrayBlock).

```lean
TauCeti.Probability.JointlyExchangeable.conditionallyIID_arrayRow_arrayBlock.{u_1, u_2}
  {α : Type u_1} {Ω : Type u_2} [MeasurableSpace α] [MeasurableSpace Ω]
  {μ : MeasureTheory.Measure Ω} {X : ℕ × ℕ → Ω → α} {e f : ℕ → ℕ} [StandardBorelSpace α]
  [MeasureTheory.IsFiniteMeasure μ] (h : TauCeti.Probability.JointlyExchangeable μ X)
  (hX : ∀ (p : ℕ × ℕ), AEMeasurable (X p) μ) (he : Function.Injective e) (hf : Function.Injective f)
  (hd : Disjoint (Set.range e) (Set.range f)) :
  TauCeti.Probability.ConditionallyIID μ
    (TauCeti.Probability.arrayRow (TauCeti.Probability.arrayBlock X e f))
```

**De Finetti's theorem for the rows of a separately exchangeable array.** Formalized in Tau Ceti as [`TauCeti.Probability.SeparatelyExchangeable.conditionallyIID_arrayRow`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/Arrays/DeFinetti.html#TauCeti.Probability.SeparatelyExchangeable.conditionallyIID_arrayRow).

```lean
TauCeti.Probability.SeparatelyExchangeable.conditionallyIID_arrayRow.{u_1, u_2} {α : Type u_1}
  {Ω : Type u_2} [MeasurableSpace α] [MeasurableSpace Ω] [StandardBorelSpace α]
  {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsFiniteMeasure μ] {X : ℕ × ℕ → Ω → α}
  (h : TauCeti.Probability.SeparatelyExchangeable μ X) (hX : ∀ (p : ℕ × ℕ), AEMeasurable (X p) μ) :
  TauCeti.Probability.ConditionallyIID μ (TauCeti.Probability.arrayRow X)
```

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.JointlyExchangeable.conditionallyIID_arrayRow_arrayBlockPair`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/Arrays/DeFinetti.html#TauCeti.Probability.JointlyExchangeable.conditionallyIID_arrayRow_arrayBlockPair)
- [Source of `TauCeti.Probability.JointlyExchangeable.conditionallyIID_arrayRow_arrayBlockPair` in TauCeti/Probability/Exchangeability/Arrays/DeFinetti.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Exchangeability/Arrays/DeFinetti.lean#L90)
