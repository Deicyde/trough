---
declaration: theorem
origin: cited
lean: TauCeti.Probability.ExchangeableAt.prefixLaw_le_sampleWithReplacement_add_exact_collision, TauCeti.Probability.ExchangeableAt.sampleWithReplacement_le_prefixLaw_add_exact_collision
statement: formalized
proof: formalized
---

# Exact finite de Finetti bound, exchangeable law to empirical mixture

Under finite
exchangeability and `m ≤ n`, the prefix law exceeds its with-replacement sample on a measurable
event by at most the exact index-collision error.

```lean
TauCeti.Probability.ExchangeableAt.prefixLaw_le_sampleWithReplacement_add_exact_collision.{u_1, u_2}
  {α : Type u_1} [MeasurableSpace α] {Ω : Type u_2} [MeasurableSpace Ω]
  {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsProbabilityMeasure μ] {X : ℕ → Ω → α} {m n : ℕ}
  (h : TauCeti.Probability.ExchangeableAt μ X n) (hmn : m ≤ n)
  (hX : ∀ (i : Fin n), AEMeasurable (X ↑i) μ) {A : Set (Fin m → α)} (hA : MeasurableSet A) :
  (TauCeti.Probability.prefixLaw μ X m) A ≤
    (TauCeti.Probability.sampleWithReplacement (TauCeti.Probability.prefixLaw μ X n)) A +
      (1 - ↑(n.descFactorial m) / ↑n ^ m)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.ExchangeableAt.prefixLaw_le_sampleWithReplacement_add_exact_collision`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/FiniteDeFinetti.html#TauCeti.Probability.ExchangeableAt.prefixLaw_le_sampleWithReplacement_add_exact_collision).

## Other forms

**Exact finite de Finetti bound, empirical mixture to exchangeable law.** Formalized in Tau Ceti as [`TauCeti.Probability.ExchangeableAt.sampleWithReplacement_le_prefixLaw_add_exact_collision`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/FiniteDeFinetti.html#TauCeti.Probability.ExchangeableAt.sampleWithReplacement_le_prefixLaw_add_exact_collision).

```lean
TauCeti.Probability.ExchangeableAt.sampleWithReplacement_le_prefixLaw_add_exact_collision.{u_1, u_2}
  {α : Type u_1} [MeasurableSpace α] {Ω : Type u_2} [MeasurableSpace Ω]
  {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsProbabilityMeasure μ] {X : ℕ → Ω → α} {m n : ℕ}
  (h : TauCeti.Probability.ExchangeableAt μ X n) (hmn : m ≤ n)
  (hX : ∀ (i : Fin n), AEMeasurable (X ↑i) μ) {A : Set (Fin m → α)} (hA : MeasurableSet A) :
  (TauCeti.Probability.sampleWithReplacement (TauCeti.Probability.prefixLaw μ X n)) A ≤
    (TauCeti.Probability.prefixLaw μ X m) A + (1 - ↑(n.descFactorial m) / ↑n ^ m)
```

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.ExchangeableAt.prefixLaw_le_sampleWithReplacement_add_exact_collision`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/FiniteDeFinetti.html#TauCeti.Probability.ExchangeableAt.prefixLaw_le_sampleWithReplacement_add_exact_collision)
- [Source of `TauCeti.Probability.ExchangeableAt.prefixLaw_le_sampleWithReplacement_add_exact_collision` in TauCeti/Probability/Exchangeability/FiniteDeFinetti.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Exchangeability/FiniteDeFinetti.lean#L134)
