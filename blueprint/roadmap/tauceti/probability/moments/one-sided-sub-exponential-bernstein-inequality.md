---
declaration: theorem
origin: cited
lean: ProbabilityTheory.iIndepFun.measureReal_sum_ge_le_of_hasSubexponentialMGF
statement: formalized
proof: formalized
---

# One-sided sub-exponential Bernstein inequality

For independent centered variables with
common parameter `K`, this bounds the upper tail of a finite sum.

```lean
ProbabilityTheory.iIndepFun.measureReal_sum_ge_le_of_hasSubexponentialMGF.{u_1, u_2} {Ω : Type u_1}
  [MeasurableSpace Ω] {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsProbabilityMeasure μ]
  {ι : Type u_2} {X : ι → Ω → ℝ} (h_indep : ProbabilityTheory.iIndepFun X μ) {s : Finset ι}
  {K t : ℝ} (hK : 0 < K) (hX : ∀ i ∈ s, TauCeti.Probability.HasSubexponentialMGF (X i) K μ)
  (hmean : ∀ i ∈ s, ∫ (x : Ω), X i x ∂μ = 0) (ht : 0 < t) :
  μ.real {ω | t ≤ ∑ i ∈ s, X i ω} ≤ Real.exp (-t ^ 2 / (4 * (↑s.card * K ^ 2 + K * t)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ProbabilityTheory.iIndepFun.measureReal_sum_ge_le_of_hasSubexponentialMGF`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/SubExponential.html#ProbabilityTheory.iIndepFun.measureReal_sum_ge_le_of_hasSubexponentialMGF).

## Sources

- [Tau Ceti documentation: `ProbabilityTheory.iIndepFun.measureReal_sum_ge_le_of_hasSubexponentialMGF`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/SubExponential.html#ProbabilityTheory.iIndepFun.measureReal_sum_ge_le_of_hasSubexponentialMGF)
- [Source of `ProbabilityTheory.iIndepFun.measureReal_sum_ge_le_of_hasSubexponentialMGF` in TauCeti/Probability/Moments/SubExponential.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Moments/SubExponential.lean#L139)
