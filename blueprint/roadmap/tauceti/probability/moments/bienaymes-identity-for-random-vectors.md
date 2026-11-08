---
declaration: theorem
origin: cited
lean: TauCeti.integral_norm_sum_sq_of_pairwise_indepFun
statement: formalized
proof: formalized
---

# Bienaymé's identity for random vectors

If the random vectors `X i`, `i ∈ s`, in a real
Hilbert space are square-integrable, centered and pairwise independent, then the expected squared
norm of their sum is the sum of their expected squared norms.

```lean
TauCeti.integral_norm_sum_sq_of_pairwise_indepFun.{u_1, u_2, u_3} {Ω : Type u_1} {ι : Type u_2}
  {E : Type u_3} {mΩ : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [CompleteSpace E] [MeasurableSpace E] [BorelSpace E]
  [MeasureTheory.IsFiniteMeasure μ] {X : ι → Ω → E} {s : Finset ι}
  (hX : ∀ i ∈ s, MeasureTheory.MemLp (X i) 2 μ) (hmean : ∀ i ∈ s, ∫ (x : Ω), X i x ∂μ = 0)
  (hindep : (↑s).Pairwise fun i j => ProbabilityTheory.IndepFun (X i) (X j) μ) :
  ∫ (ω : Ω), ‖∑ i ∈ s, X i ω‖ ^ 2 ∂μ = ∑ i ∈ s, ∫ (ω : Ω), ‖X i ω‖ ^ 2 ∂μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.integral_norm_sum_sq_of_pairwise_indepFun`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/SampleMean.html#TauCeti.integral_norm_sum_sq_of_pairwise_indepFun).

## Sources

- [Tau Ceti documentation: `TauCeti.integral_norm_sum_sq_of_pairwise_indepFun`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/SampleMean.html#TauCeti.integral_norm_sum_sq_of_pairwise_indepFun)
- [Source of `TauCeti.integral_norm_sum_sq_of_pairwise_indepFun` in TauCeti/Probability/Moments/SampleMean.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Moments/SampleMean.lean#L59)
