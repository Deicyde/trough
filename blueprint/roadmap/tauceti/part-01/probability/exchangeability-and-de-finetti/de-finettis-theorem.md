---
declaration: theorem
origin: cited
lean: TauCeti.Probability.deFinetti, TauCeti.Probability.deFinetti_equivalence, TauCeti.Probability.conditionallyIID_of_exchangeableFamily, TauCeti.Probability.deFinetti_tendsto_empiricalMeasure_apply, TauCeti.Probability.deFinetti_empiricalMeasure, TauCeti.Probability.deFinetti_viaL2, TauCeti.Probability.deFinetti_viaKoopman, TauCeti.Probability.conditionallyIID_of_exchangeable, TauCeti.Probability.mixedIIDWith_of_contractable, TauCeti.Probability.exchangeable_iff_mixedIID, TauCeti.Probability.mixedIID_of_contractable, TauCeti.Probability.mixedIID_of_exchangeable, TauCeti.Probability.deFinetti_mixture
statement: formalized
proof: formalized
---

# De Finetti's theorem

An exchangeable process valued in a standard Borel space is
conditionally i.i.d. This is the conventional theorem-name handle for
`conditionallyIID_of_exchangeable`.

```lean
TauCeti.Probability.deFinetti.{u_1, u_2} {Ω : Type u_1} {α : Type u_2} {mΩ : MeasurableSpace Ω}
  [MeasurableSpace α] [StandardBorelSpace α] {μ : MeasureTheory.Measure Ω}
  [MeasureTheory.IsFiniteMeasure μ] {X : ℕ → Ω → α} (hX_meas : ∀ (n : ℕ), AEMeasurable (X n) μ)
  (hX : TauCeti.Probability.Exchangeable μ X) : TauCeti.Probability.ConditionallyIID μ X
```

## Depends on

- [TauCeti.Probability.empiricalFiniteMeasure](../random-matrices/tauceti-probability-empiricalfinitemeasure.md)

## Proof depends on

- [The contractable form of de Finetti's theorem via `L²` averaging](../other-results/the-contractable-form-of-de-finettis-theorem-via.md)
- [De Finetti's theorem transported along an explicit enumeration](../other-results/de-finettis-theorem-transported-along-an-explici.md)
- [The mean ergodic theorem for conditional expectations](../other-results/the-mean-ergodic-theorem-for-conditional-expecta.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.deFinetti`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/Theorem.html#TauCeti.Probability.deFinetti).

## Other forms

**De Finetti's theorem as an equivalence.** Formalized in Tau Ceti as [`TauCeti.Probability.deFinetti_equivalence`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/Theorem.html#TauCeti.Probability.deFinetti_equivalence).

```lean
TauCeti.Probability.deFinetti_equivalence.{u_1, u_2} {Ω : Type u_1} {α : Type u_2}
  {mΩ : MeasurableSpace Ω} [MeasurableSpace α] [StandardBorelSpace α] {μ : MeasureTheory.Measure Ω}
  [MeasureTheory.IsFiniteMeasure μ] {X : ℕ → Ω → α} (hX_meas : ∀ (n : ℕ), AEMeasurable (X n) μ) :
  TauCeti.Probability.Exchangeable μ X ↔ TauCeti.Probability.ConditionallyIID μ X
```

**De Finetti's theorem for countably infinite index types.** Formalized in Tau Ceti as [`TauCeti.Probability.conditionallyIID_of_exchangeableFamily`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/CountableIndex.html#TauCeti.Probability.conditionallyIID_of_exchangeableFamily).

```lean
TauCeti.Probability.conditionallyIID_of_exchangeableFamily.{u_1, u_2, u_3} {Ω : Type u_1}
  {α : Type u_2} {ι : Type u_3} [MeasurableSpace Ω] [MeasurableSpace α] [Countable ι] [Infinite ι]
  [StandardBorelSpace α] {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsFiniteMeasure μ]
  {X : ι → Ω → α} (hX : TauCeti.Probability.ExchangeableFamily μ X)
  (hX_meas : ∀ (i : ι), Measurable (X i)) : TauCeti.Probability.ConditionallyIID μ X
```

**De Finetti's theorem in empirical-frequency form.** Formalized in Tau Ceti as [`TauCeti.Probability.deFinetti_tendsto_empiricalMeasure_apply`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/EmpiricalMeasure.html#TauCeti.Probability.deFinetti_tendsto_empiricalMeasure_apply).

```lean
TauCeti.Probability.deFinetti_tendsto_empiricalMeasure_apply.{u_1, u_2} {Ω : Type u_1}
  {α : Type u_2} [MeasurableSpace Ω] [MeasurableSpace α] {μ : MeasureTheory.Measure Ω}
  {X : ℕ → Ω → α} [StandardBorelSpace α] [MeasureTheory.IsFiniteMeasure μ]
  (hX : TauCeti.Probability.Exchangeable μ X) (hX_meas : ∀ (n : ℕ), AEMeasurable (X n) μ) :
  ∃ ν,
    TauCeti.Probability.ConditionallyIIDWith μ X ν ∧
      ∀ (B : Set α),
        MeasurableSet B →
          ∀ᵐ (ω : Ω) ∂μ,
            Filter.Tendsto
              (fun n => (↑(TauCeti.Probability.empiricalMeasure (fun i => X i ω) n) B).toReal)
              Filter.atTop (nhds (↑(ν ω) B).toReal)
```

**De Finetti's theorem in empirical-measure form.** Formalized in Tau Ceti as [`TauCeti.Probability.deFinetti_empiricalMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/EmpiricalMeasure.html#TauCeti.Probability.deFinetti_empiricalMeasure).

```lean
TauCeti.Probability.deFinetti_empiricalMeasure.{u_1, u_2} {Ω : Type u_1} {α : Type u_2}
  [MeasurableSpace Ω] [MeasurableSpace α] {μ : MeasureTheory.Measure Ω} {X : ℕ → Ω → α}
  [TopologicalSpace α] [PolishSpace α] [BorelSpace α] [MeasureTheory.IsFiniteMeasure μ]
  (hX : TauCeti.Probability.Exchangeable μ X) (hX_meas : ∀ (n : ℕ), AEMeasurable (X n) μ) :
  ∃ ν,
    TauCeti.Probability.ConditionallyIIDWith μ X ν ∧
      ∀ᵐ (ω : Ω) ∂μ,
        Filter.Tendsto (fun n => TauCeti.Probability.empiricalMeasure (fun i => X i ω) n)
          Filter.atTop (nhds (ν ω))
```

**De Finetti's theorem via `L²` averaging.** Formalized in Tau Ceti as [`TauCeti.Probability.deFinetti_viaL2`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/ViaL2/Theorem.html#TauCeti.Probability.deFinetti_viaL2).

```lean
TauCeti.Probability.deFinetti_viaL2.{u_1, u_2} {Ω : Type u_1} {α : Type u_2} [MeasurableSpace Ω]
  [MeasurableSpace α] [StandardBorelSpace α] [Nonempty α] {μ : MeasureTheory.Measure Ω}
  [MeasureTheory.IsFiniteMeasure μ] {X : ℕ → Ω → α} (hX_meas : ∀ (n : ℕ), Measurable (X n))
  (hX : TauCeti.Probability.Exchangeable μ X) : TauCeti.Probability.ConditionallyIID μ X
```

**de Finetti's theorem via Koopman operators.** Formalized in Tau Ceti as [`TauCeti.Probability.deFinetti_viaKoopman`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/ViaKoopman/Theorem.html#TauCeti.Probability.deFinetti_viaKoopman).

```lean
TauCeti.Probability.deFinetti_viaKoopman.{u_1, u_2} {Ω : Type u_1} {α : Type u_2}
  [MeasurableSpace Ω] [MeasurableSpace α] [StandardBorelSpace α] [Nonempty α]
  {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsFiniteMeasure μ] {X : ℕ → Ω → α}
  (hX_meas : ∀ (n : ℕ), Measurable (X n)) (hX : TauCeti.Probability.Exchangeable μ X) :
  TauCeti.Probability.ConditionallyIID μ X
```

**De Finetti's theorem, conditional form.** Formalized in Tau Ceti as [`TauCeti.Probability.conditionallyIID_of_exchangeable`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/Theorem.html#TauCeti.Probability.conditionallyIID_of_exchangeable).

```lean
TauCeti.Probability.conditionallyIID_of_exchangeable.{u_1, u_2} {Ω : Type u_1} {α : Type u_2}
  {mΩ : MeasurableSpace Ω} [MeasurableSpace α] [StandardBorelSpace α] {μ : MeasureTheory.Measure Ω}
  [MeasureTheory.IsFiniteMeasure μ] {X : ℕ → Ω → α} (hX : TauCeti.Probability.Exchangeable μ X)
  (hX_meas : ∀ (n : ℕ), AEMeasurable (X n) μ) : TauCeti.Probability.ConditionallyIID μ X
```

**de Finetti's theorem, directed form.** Formalized in Tau Ceti as [`TauCeti.Probability.mixedIIDWith_of_contractable`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/BlockFactorization.html#TauCeti.Probability.mixedIIDWith_of_contractable).

```lean
TauCeti.Probability.mixedIIDWith_of_contractable.{u_1, u_2} {Ω : Type u_1} {α : Type u_2}
  {mΩ : MeasurableSpace Ω} [MeasurableSpace α] [StandardBorelSpace Ω] [StandardBorelSpace α]
  [Nonempty α] {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsFiniteMeasure μ] {X : ℕ → Ω → α}
  (hX : TauCeti.Probability.Contractable μ X) (hX_meas : ∀ (n : ℕ), Measurable (X n)) :
  TauCeti.Probability.MixedIIDWith μ X (TauCeti.Probability.tailConditionalProbabilityMeasure μ X)
```

**De Finetti's theorem, mixture equivalence form (Kallenberg, Theorem 1.1).** Formalized in Tau Ceti as [`TauCeti.Probability.exchangeable_iff_mixedIID`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/Theorem.html#TauCeti.Probability.exchangeable_iff_mixedIID).

```lean
TauCeti.Probability.exchangeable_iff_mixedIID.{u_1, u_2} {Ω : Type u_1} {α : Type u_2}
  {mΩ : MeasurableSpace Ω} [MeasurableSpace α] [StandardBorelSpace α] {μ : MeasureTheory.Measure Ω}
  [MeasureTheory.IsFiniteMeasure μ] {X : ℕ → Ω → α} (hX_meas : ∀ (n : ℕ), AEMeasurable (X n) μ) :
  TauCeti.Probability.Exchangeable μ X ↔ TauCeti.Probability.MixedIID μ X
```

**de Finetti's theorem, mixture form: contractable ⇒ mixed i.i.d.** Formalized in Tau Ceti as [`TauCeti.Probability.mixedIID_of_contractable`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/BlockFactorization.html#TauCeti.Probability.mixedIID_of_contractable).

```lean
TauCeti.Probability.mixedIID_of_contractable.{u_3, u_4} {Ω : Type u_3} {α : Type u_4}
  [MeasurableSpace Ω] [MeasurableSpace α] [StandardBorelSpace α] [Nonempty α]
  {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsFiniteMeasure μ] {X : ℕ → Ω → α}
  (hX : TauCeti.Probability.Contractable μ X) (hX_meas : ∀ (n : ℕ), Measurable (X n)) :
  TauCeti.Probability.MixedIID μ X
```

**de Finetti's theorem, mixture form: exchangeable ⇒ mixed i.i.d.** Formalized in Tau Ceti as [`TauCeti.Probability.mixedIID_of_exchangeable`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/BlockFactorization.html#TauCeti.Probability.mixedIID_of_exchangeable).

```lean
TauCeti.Probability.mixedIID_of_exchangeable.{u_3, u_4} {Ω : Type u_3} {α : Type u_4}
  [MeasurableSpace Ω] [MeasurableSpace α] [StandardBorelSpace α] [Nonempty α]
  {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsFiniteMeasure μ] {X : ℕ → Ω → α}
  (hX : TauCeti.Probability.Exchangeable μ X) (hX_meas : ∀ (n : ℕ), Measurable (X n)) :
  TauCeti.Probability.MixedIID μ X
```

**De Finetti's theorem, unique mixture form.** Formalized in Tau Ceti as [`TauCeti.Probability.deFinetti_mixture`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/Representation.html#TauCeti.Probability.deFinetti_mixture).

```lean
TauCeti.Probability.deFinetti_mixture.{u_1, u_2} {Ω : Type u_1} {α : Type u_2} [MeasurableSpace Ω]
  [MeasurableSpace α] [StandardBorelSpace α] {μ : MeasureTheory.Measure Ω}
  [MeasureTheory.IsProbabilityMeasure μ] {X : ℕ → Ω → α} (hX : TauCeti.Probability.Exchangeable μ X)
  (hX_meas : ∀ (n : ℕ), AEMeasurable (X n) μ) :
  ∃! π,
    TauCeti.Probability.pathLaw μ X =
      (↑π).bind fun P => MeasureTheory.Measure.infinitePi fun x => ↑P
```

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.deFinetti`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/Theorem.html#TauCeti.Probability.deFinetti)
- [Source of `TauCeti.Probability.deFinetti` in TauCeti/Probability/DeFinetti/Theorem.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/DeFinetti/Theorem.lean#L160)
