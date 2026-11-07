---
declaration: theorem
origin: cited
lean: TauCeti.Probability.ExchangeableAt.etvDist_prefixLaw_sampleWithReplacement_le
statement: formalized
proof: formalized
---

# Finite de Finetti theorem, total-variation form

If the first `n` coordinates of a
process are exchangeable and `m ≤ n`, then the total variation distance between the `m`-prefix
law and the with-replacement sample of the `n`-prefix law (for `n > 0`, the empirical-product
mixture) is at most `2 * choose m 2 / n`.

The normalization is Mathlib's: `etvDist P Q` is the signed-measure norm `‖P - Q‖`, twice the
distance `sup_A |P A - Q A|`, so in terms of that distance the bound is `choose m 2 / n`
(`etvDist_le_two_mul_iff`).

```lean
TauCeti.Probability.ExchangeableAt.etvDist_prefixLaw_sampleWithReplacement_le.{u_1, u_2}
  {α : Type u_1} [MeasurableSpace α] {Ω : Type u_2} [MeasurableSpace Ω]
  {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsProbabilityMeasure μ] {X : ℕ → Ω → α} {m n : ℕ}
  (h : TauCeti.Probability.ExchangeableAt μ X n) (hmn : m ≤ n)
  (hX : ∀ (i : Fin n), AEMeasurable (X ↑i) μ) :
  MeasureTheory.etvDist (TauCeti.Probability.prefixLaw μ X m)
      (TauCeti.Probability.sampleWithReplacement (TauCeti.Probability.prefixLaw μ X n)) ≤
    2 * (↑(m.choose 2) / ↑n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.ExchangeableAt.etvDist_prefixLaw_sampleWithReplacement_le`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/FiniteDeFinetti.html#TauCeti.Probability.ExchangeableAt.etvDist_prefixLaw_sampleWithReplacement_le).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.ExchangeableAt.etvDist_prefixLaw_sampleWithReplacement_le`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/FiniteDeFinetti.html#TauCeti.Probability.ExchangeableAt.etvDist_prefixLaw_sampleWithReplacement_le)
- [Source of `TauCeti.Probability.ExchangeableAt.etvDist_prefixLaw_sampleWithReplacement_le` in TauCeti/Probability/Exchangeability/FiniteDeFinetti.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Exchangeability/FiniteDeFinetti.lean#L185)
- [Tau Ceti roadmap status: Exchangeability and de Finetti](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/Exchangeability/STATUS.md)
