---
declaration: theorem
origin: cited
lean: TauCeti.Probability.measureReal_sum_range_ge_le_of_bounded_martingale_differences, TauCeti.Probability.measureReal_sum_range_ge_le_of_mem_Icc_martingale_differences
statement: formalized
proof: formalized
---

# Azuma-Hoeffding inequality

Let `Y i` be a strongly adapted sequence of martingale
differences with `|Y i| ≤ b i` almost surely, mean zero at time zero, and conditional mean zero at
each later step. Then the upper tail of the sum of its first `n` terms is bounded by
`exp (-ε ^ 2 / (2 * ∑ i < n, b i ^ 2))`.

```lean
TauCeti.Probability.measureReal_sum_range_ge_le_of_bounded_martingale_differences.{u_1}
  {Ω : Type u_1} [mΩ : MeasurableSpace Ω] {μ : MeasureTheory.Measure Ω}
  [MeasureTheory.IsProbabilityMeasure μ] {ℱ : MeasureTheory.Filtration ℕ mΩ} {Y : ℕ → Ω → ℝ}
  {b : ℕ → NNReal} (h_adapted : MeasureTheory.StronglyAdapted ℱ Y) (n : ℕ)
  (hbound : ∀ i < n, ∀ᵐ (ω : Ω) ∂μ, |Y i ω| ≤ ↑(b i)) (hmean0 : ∫ (ω : Ω), Y 0 ω ∂μ = 0)
  (hmean : ∀ i < n - 1, μ[Y (i + 1) | ↑ℱ i] =ᵐ[μ] 0) {ε : ℝ} (hε : 0 ≤ ε) :
  μ.real {ω | ε ≤ ∑ i ∈ Finset.range n, Y i ω} ≤
    Real.exp (-ε ^ 2 / (2 * ∑ i ∈ Finset.range n, ↑(b i) ^ 2))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.measureReal_sum_range_ge_le_of_bounded_martingale_differences`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/Azuma.html#TauCeti.Probability.measureReal_sum_range_ge_le_of_bounded_martingale_differences).

## Other forms

**Azuma-Hoeffding inequality for interval-bounded martingale differences.** Formalized in Tau Ceti as [`TauCeti.Probability.measureReal_sum_range_ge_le_of_mem_Icc_martingale_differences`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/Azuma.html#TauCeti.Probability.measureReal_sum_range_ge_le_of_mem_Icc_martingale_differences).

```lean
TauCeti.Probability.measureReal_sum_range_ge_le_of_mem_Icc_martingale_differences.{u_1}
  {Ω : Type u_1} [mΩ : MeasurableSpace Ω] {μ : MeasureTheory.Measure Ω}
  [MeasureTheory.IsProbabilityMeasure μ] {ℱ : MeasureTheory.Filtration ℕ mΩ} {Y : ℕ → Ω → ℝ}
  {a b : ℕ → ℝ} (h_adapted : MeasureTheory.StronglyAdapted ℱ Y) (n : ℕ)
  (hbound : ∀ i < n, ∀ᵐ (ω : Ω) ∂μ, Y i ω ∈ Set.Icc (a i) (b i)) (hmean0 : ∫ (ω : Ω), Y 0 ω ∂μ = 0)
  (hmean : ∀ i < n - 1, μ[Y (i + 1) | ↑ℱ i] =ᵐ[μ] 0) {ε : ℝ} (hε : 0 ≤ ε) :
  μ.real {ω | ε ≤ ∑ i ∈ Finset.range n, Y i ω} ≤
    Real.exp (-ε ^ 2 / (2 * ∑ i ∈ Finset.range n, (↑‖b i - a i‖₊ / 2) ^ 2))
```

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.measureReal_sum_range_ge_le_of_bounded_martingale_differences`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/Azuma.html#TauCeti.Probability.measureReal_sum_range_ge_le_of_bounded_martingale_differences)
- [Source of `TauCeti.Probability.measureReal_sum_range_ge_le_of_bounded_martingale_differences` in TauCeti/Probability/Moments/Azuma.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Moments/Azuma.lean#L280)
