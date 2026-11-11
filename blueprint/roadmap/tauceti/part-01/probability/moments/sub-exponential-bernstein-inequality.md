---
declaration: theorem
origin: cited
lean: ProbabilityTheory.iIndepFun.measureReal_abs_sum_ge_le_of_hasSubexponentialMGF
statement: formalized
proof: formalized
---

# Sub-exponential Bernstein inequality

If the `Xᵢ`, `i ∈ s`, are independent, centered
and sub-exponential with common parameter `K`, then for `t > 0`

`P(|∑ i ∈ s, Xᵢ| ≥ t) ≤ 2 * exp (-t^2 / (4 * (|s| * K^2 + K * t)))`.

The constants follow directly from the centered MGF bound `E exp (λ Xᵢ) ≤ exp (K ^ 2 * λ ^ 2)`
for `|λ| ≤ 1 / K`.

```lean
ProbabilityTheory.iIndepFun.measureReal_abs_sum_ge_le_of_hasSubexponentialMGF.{u_1, u_2}
  {Ω : Type u_1} [MeasurableSpace Ω] {μ : MeasureTheory.Measure Ω}
  [MeasureTheory.IsProbabilityMeasure μ] {ι : Type u_2} {X : ι → Ω → ℝ}
  (h_indep : ProbabilityTheory.iIndepFun X μ) {s : Finset ι} {K t : ℝ} (hK : 0 < K)
  (hX : ∀ i ∈ s, TauCeti.Probability.HasSubexponentialMGF (X i) K μ)
  (hmean : ∀ i ∈ s, ∫ (x : Ω), X i x ∂μ = 0) (ht : 0 < t) :
  μ.real {ω | t ≤ |∑ i ∈ s, X i ω|} ≤ 2 * Real.exp (-t ^ 2 / (4 * (↑s.card * K ^ 2 + K * t)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [One-sided sub-exponential Bernstein inequality](one-sided-sub-exponential-bernstein-inequality.md)

## Lean

Formalized in Tau Ceti as [`ProbabilityTheory.iIndepFun.measureReal_abs_sum_ge_le_of_hasSubexponentialMGF`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/SubExponential.html#ProbabilityTheory.iIndepFun.measureReal_abs_sum_ge_le_of_hasSubexponentialMGF).

## Sources

- [Tau Ceti documentation: `ProbabilityTheory.iIndepFun.measureReal_abs_sum_ge_le_of_hasSubexponentialMGF`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/SubExponential.html#ProbabilityTheory.iIndepFun.measureReal_abs_sum_ge_le_of_hasSubexponentialMGF)
- [Source of `ProbabilityTheory.iIndepFun.measureReal_abs_sum_ge_le_of_hasSubexponentialMGF` in TauCeti/Probability/Moments/SubExponential.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Moments/SubExponential.lean#L195)
