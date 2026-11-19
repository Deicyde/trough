---
declaration: theorem
origin: cited
lean: ProbabilityTheory.HasLaw.tendstoInDistribution_sum_of_lindeberg
statement: formalized
proof: formalized
---

# Lindeberg–Feller central limit theorem (sufficiency direction)

Let `X n i`, `i : ι n`,
be a triangular array of real random variables, the `n`th row on its own probability space
`(Ω n, P n)`. Suppose the rows are independent, centred and square integrable, with row variances
summing to `1` for all large `n`. If the Lindeberg condition
`∑ i, E[X n i ^ 2; ε ≤ |X n i|] → 0` holds for every `ε > 0`, then the row sums converge in
distribution to a standard Gaussian random variable `Y`.

```lean
ProbabilityTheory.HasLaw.tendstoInDistribution_sum_of_lindeberg.{u_1, u_2, u_3} {Ω : ℕ → Type u_1}
  {mΩ : (n : ℕ) → MeasurableSpace (Ω n)} {P : (n : ℕ) → MeasureTheory.Measure (Ω n)}
  [∀ (n : ℕ), MeasureTheory.IsProbabilityMeasure (P n)] {Ω' : Type u_2} {mΩ' : MeasurableSpace Ω'}
  {P' : MeasureTheory.Measure Ω'} [MeasureTheory.IsProbabilityMeasure P'] {Y : Ω' → ℝ}
  {ι : ℕ → Type u_3} [(n : ℕ) → Fintype (ι n)] {X : (n : ℕ) → ι n → Ω n → ℝ}
  (hY : ProbabilityTheory.HasLaw Y (ProbabilityTheory.gaussianReal 0 1) P')
  (hindep : ∀ (n : ℕ), ProbabilityTheory.iIndepFun (X n) (P n))
  (hL2 : ∀ (n : ℕ) (i : ι n), MeasureTheory.MemLp (X n i) 2 (P n))
  (h0 : ∀ (n : ℕ) (i : ι n), ∫ (x : Ω n), X n i x ∂P n = 0)
  (hvar : ∀ᶠ (n : ℕ) in Filter.atTop, ∑ i, ProbabilityTheory.variance (X n i) (P n) = 1)
  (hlind :
    ∀ ε > 0,
      Filter.Tendsto
        (fun n => ∑ i, ∫ (x : Ω n), {ω | ε ≤ |X n i ω|}.indicator (fun ω => X n i ω ^ 2) x ∂P n)
        Filter.atTop (nhds 0)) :
  MeasureTheory.TendstoInDistribution (fun n ω => ∑ i, X n i ω) Filter.atTop Y P P'
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Taylor bound for `exp (x * I)`](../../analysis/part-04/special-functions/taylor-bound-for-exp-x-i.md)

## Lean

Formalized in Tau Ceti as [`ProbabilityTheory.HasLaw.tendstoInDistribution_sum_of_lindeberg`](https://taucetiproject.org/docs/TauCeti/Probability/CentralLimitTheorem/Lindeberg.html#ProbabilityTheory.HasLaw.tendstoInDistribution_sum_of_lindeberg).

## Sources

- [Tau Ceti documentation: `ProbabilityTheory.HasLaw.tendstoInDistribution_sum_of_lindeberg`](https://taucetiproject.org/docs/TauCeti/Probability/CentralLimitTheorem/Lindeberg.html#ProbabilityTheory.HasLaw.tendstoInDistribution_sum_of_lindeberg)
- [Source of `ProbabilityTheory.HasLaw.tendstoInDistribution_sum_of_lindeberg` in TauCeti/Probability/CentralLimitTheorem/Lindeberg.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/CentralLimitTheorem/Lindeberg.lean#L242)
