---
declaration: theorem
origin: cited
lean: TauCeti.Probability.ExchangeableAt.prefixLaw_le_sampleWithReplacement_add, TauCeti.Probability.ExchangeableAt.sampleWithReplacement_le_prefixLaw_add
statement: formalized
proof: formalized
---

# Quantitative finite de Finetti bound, exchangeable law to empirical mixture

If the first
`n` coordinates of a process are exchangeable and `m ≤ n`, then every measurable event under the
`m`-prefix law has mass at most its mass under sampling `m` entries with replacement from the first
`n` coordinates, plus `choose m 2 / n`. For `n > 0` that sample is the mixture of `m`-fold products
of the empirical distribution of the first `n` coordinates.

```lean
TauCeti.Probability.ExchangeableAt.prefixLaw_le_sampleWithReplacement_add.{u_1, u_2} {α : Type u_1}
  [MeasurableSpace α] {Ω : Type u_2} [MeasurableSpace Ω] {μ : MeasureTheory.Measure Ω}
  [MeasureTheory.IsProbabilityMeasure μ] {X : ℕ → Ω → α} {m n : ℕ}
  (h : TauCeti.Probability.ExchangeableAt μ X n) (hmn : m ≤ n)
  (hX : ∀ (i : Fin n), AEMeasurable (X ↑i) μ) {A : Set (Fin m → α)} (hA : MeasurableSet A) :
  (TauCeti.Probability.prefixLaw μ X m) A ≤
    (TauCeti.Probability.sampleWithReplacement (TauCeti.Probability.prefixLaw μ X n)) A +
      ↑(m.choose 2) / ↑n
```

## Depends on

Its statement uses no other declaration mapped here.

## Informally uses

- [Finite de Finetti theorem, total-variation form](finite-de-finetti-theorem-total-variation-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.ExchangeableAt.prefixLaw_le_sampleWithReplacement_add`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/FiniteDeFinetti.html#TauCeti.Probability.ExchangeableAt.prefixLaw_le_sampleWithReplacement_add).

## Other forms

**Quantitative finite de Finetti bound, empirical mixture to exchangeable law.** Formalized in Tau Ceti as [`TauCeti.Probability.ExchangeableAt.sampleWithReplacement_le_prefixLaw_add`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/FiniteDeFinetti.html#TauCeti.Probability.ExchangeableAt.sampleWithReplacement_le_prefixLaw_add).

```lean
TauCeti.Probability.ExchangeableAt.sampleWithReplacement_le_prefixLaw_add.{u_1, u_2} {α : Type u_1}
  [MeasurableSpace α] {Ω : Type u_2} [MeasurableSpace Ω] {μ : MeasureTheory.Measure Ω}
  [MeasureTheory.IsProbabilityMeasure μ] {X : ℕ → Ω → α} {m n : ℕ}
  (h : TauCeti.Probability.ExchangeableAt μ X n) (hmn : m ≤ n)
  (hX : ∀ (i : Fin n), AEMeasurable (X ↑i) μ) {A : Set (Fin m → α)} (hA : MeasurableSet A) :
  (TauCeti.Probability.sampleWithReplacement (TauCeti.Probability.prefixLaw μ X n)) A ≤
    (TauCeti.Probability.prefixLaw μ X m) A + ↑(m.choose 2) / ↑n
```

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.ExchangeableAt.prefixLaw_le_sampleWithReplacement_add`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/FiniteDeFinetti.html#TauCeti.Probability.ExchangeableAt.prefixLaw_le_sampleWithReplacement_add)
- [Source of `TauCeti.Probability.ExchangeableAt.prefixLaw_le_sampleWithReplacement_add` in TauCeti/Probability/Exchangeability/FiniteDeFinetti.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Exchangeability/FiniteDeFinetti.lean#L158)
