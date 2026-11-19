---
declaration: theorem
origin: cited
lean: ProbabilityTheory.IsGaussian.integral_prod_sub_dual_eq_sum_perfectMatching
statement: formalized
proof: formalized
---

# Wick--Isserlis formula

A centered mixed moment of finitely many linear observables of
a Gaussian measure is the sum of covariance products over perfect matchings of the positions.
The statement includes empty and odd position types.

```lean
ProbabilityTheory.IsGaussian.integral_prod_sub_dual_eq_sum_perfectMatching.{u_1, u_2} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [MeasurableSpace E] [BorelSpace E]
  (μ : MeasureTheory.Measure E) [ProbabilityTheory.IsGaussian μ] {ι : Type u_2} [Fintype ι]
  [DecidableEq ι] (L : ι → StrongDual ℝ E) :
  ∫ (x : E), ∏ i, ((L i) x - ∫ (x : E), (L i) x ∂μ) ∂μ =
    ∑ D,
      ∏ e ∈ D.edgeFinset,
        Sym2.lift ⟨fun i j => ProbabilityTheory.covariance (⇑(L i)) (⇑(L j)) μ, ⋯⟩ e
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ProbabilityTheory.IsGaussian.integral_prod_sub_dual_eq_sum_perfectMatching`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gaussian/Wick.html#ProbabilityTheory.IsGaussian.integral_prod_sub_dual_eq_sum_perfectMatching).

## Sources

- [Tau Ceti documentation: `ProbabilityTheory.IsGaussian.integral_prod_sub_dual_eq_sum_perfectMatching`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gaussian/Wick.html#ProbabilityTheory.IsGaussian.integral_prod_sub_dual_eq_sum_perfectMatching)
- [Source of `ProbabilityTheory.IsGaussian.integral_prod_sub_dual_eq_sum_perfectMatching` in TauCeti/Probability/Distributions/Gaussian/Wick.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Distributions/Gaussian/Wick.lean#L49)
