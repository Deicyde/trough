---
declaration: theorem
origin: cited
lean: ProbabilityTheory.HasLaw.tendstoInDistribution_sum_sub_div_sqrt_of_abs_sub_le
statement: formalized
proof: formalized
---

# Central limit theorem for bounded summands with diverging variance

Let the rows of the
triangular array `X n i`, `i : ι n`, be independent, the `n`th row on its own probability space
`(Ω n, P n)`, and suppose every centred summand is bounded: `|X n i - E[X n i]| ≤ C` almost
surely, for one constant `C`. If the row variance `∑ i, Var[X n i]` tends to infinity, then the
centred row sum divided by its standard deviation converges in distribution to a standard Gaussian
random variable `Y`.

For sums of independent indicators of events `A n i` with probabilities `p n i`, the centred
summands are bounded by `1`, so the conclusion holds as soon as `∑ i, p n i (1 - p n i) → ∞`.

```lean
ProbabilityTheory.HasLaw.tendstoInDistribution_sum_sub_div_sqrt_of_abs_sub_le.{u_1, u_2, u_3}
  {Ω : ℕ → Type u_1} {mΩ : (n : ℕ) → MeasurableSpace (Ω n)}
  {P : (n : ℕ) → MeasureTheory.Measure (Ω n)} [∀ (n : ℕ), MeasureTheory.IsProbabilityMeasure (P n)]
  {Ω' : Type u_2} {mΩ' : MeasurableSpace Ω'} {P' : MeasureTheory.Measure Ω'}
  [MeasureTheory.IsProbabilityMeasure P'] {Y : Ω' → ℝ} {ι : ℕ → Type u_3} [(n : ℕ) → Fintype (ι n)]
  {X : (n : ℕ) → ι n → Ω n → ℝ}
  (hY : ProbabilityTheory.HasLaw Y (ProbabilityTheory.gaussianReal 0 1) P')
  (hindep : ∀ (n : ℕ), ProbabilityTheory.iIndepFun (X n) (P n))
  (hm : ∀ (n : ℕ) (i : ι n), AEMeasurable (X n i) (P n)) {C : ℝ}
  (hC : ∀ (n : ℕ) (i : ι n), ∀ᵐ (ω : Ω n) ∂P n, |X n i ω - ∫ (x : Ω n), X n i x ∂P n| ≤ C)
  (hvar :
    Filter.Tendsto (fun n => ∑ i, ProbabilityTheory.variance (X n i) (P n)) Filter.atTop
      Filter.atTop) :
  MeasureTheory.TendstoInDistribution
    (fun n ω =>
      (∑ i, (X n i ω - ∫ (x : Ω n), X n i x ∂P n)) /
        √(∑ i, ProbabilityTheory.variance (X n i) (P n)))
    Filter.atTop Y P P'
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Lindeberg–Feller central limit theorem (sufficiency direction)](lindeberg-feller-central-limit-theorem-sufficien.md)

## Lean

Formalized in Tau Ceti as [`ProbabilityTheory.HasLaw.tendstoInDistribution_sum_sub_div_sqrt_of_abs_sub_le`](https://taucetiproject.org/docs/TauCeti/Probability/CentralLimitTheorem/Lindeberg.html#ProbabilityTheory.HasLaw.tendstoInDistribution_sum_sub_div_sqrt_of_abs_sub_le).

## Sources

- [Tau Ceti documentation: `ProbabilityTheory.HasLaw.tendstoInDistribution_sum_sub_div_sqrt_of_abs_sub_le`](https://taucetiproject.org/docs/TauCeti/Probability/CentralLimitTheorem/Lindeberg.html#ProbabilityTheory.HasLaw.tendstoInDistribution_sum_sub_div_sqrt_of_abs_sub_le)
- [Source of `ProbabilityTheory.HasLaw.tendstoInDistribution_sum_sub_div_sqrt_of_abs_sub_le` in TauCeti/Probability/CentralLimitTheorem/Lindeberg.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/CentralLimitTheorem/Lindeberg.lean#L308)
