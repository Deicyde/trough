# Central limit theorem

**Central Limit Theorem:** Given a sequence of random variables `X : ℕ → Ω → ℝ` that are
independent, identically distributed with mean `μ` and variance `v`, and a random variable
`Y : Ω' → ℝ` following `gaussianReal 0 v`, the sequence
`n ↦ (√n)⁻¹ * (∑ k ∈ Finset.range n, X k ω - n * μ)` converges to `Y` in distribution.

```lean
ProbabilityTheory.tendstoInDistribution_inv_sqrt_mul_sum_sub.{u_1, u_2} {Ω : Type u_1}
  {Ω' : Type u_2} {mΩ : MeasurableSpace Ω} {mΩ' : MeasurableSpace Ω'} {P : MeasureTheory.Measure Ω}
  {P' : MeasureTheory.Measure Ω'} {X : ℕ → Ω → ℝ} {Y : Ω' → ℝ}
  [MeasureTheory.IsProbabilityMeasure P] [MeasureTheory.IsProbabilityMeasure P']
  (hY :
    ProbabilityTheory.HasLaw Y
      (ProbabilityTheory.gaussianReal 0 (ProbabilityTheory.variance (X 0) P).toNNReal) P')
  (hX : MeasureTheory.MemLp (X 0) 2 P) (hindep : ProbabilityTheory.iIndepFun X P)
  (hident : ∀ (i : ℕ), ProbabilityTheory.IdentDistrib (X i) (X 0) P P) :
  MeasureTheory.TendstoInDistribution
    (fun n ω => (√↑n)⁻¹ * (∑ k ∈ Finset.range n, X k ω - ↑n * ∫ (x : Ω), X 0 x ∂P)) Filter.atTop Y
    (fun x => P) P'
```

## Depends on

- [Gaussian law](../random-variables-and-their-laws/gaussian-law.md)
- [Independence of random variables](../random-variables-and-their-laws/independence-of-random-variables.md)
- [Probability measure](../definitions-in-probability-theory/probability-measure.md)
- [Variance of a real-valued random variable](../random-variables-and-their-laws/variance-of-a-real-valued-random-variable.md)

## Proof depends on

- [Characteristic p](../../general-algebra/field-theory/characteristic-p.md)
- [Continuous mapping theorem](../../../thousand-plus/probability-and-statistics/continuous-mapping-theorem.md)
- [Lévy continuity theorem](../../../thousand-plus/probability-and-statistics/levy-continuity-theorem.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.tendstoInDistribution_inv_sqrt_mul_sum_sub`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/CentralLimitTheorem.html#ProbabilityTheory.tendstoInDistribution_inv_sqrt_mul_sum_sub)
- [Source of `ProbabilityTheory.tendstoInDistribution_inv_sqrt_mul_sum_sub` in Mathlib/Probability/CentralLimitTheorem.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Probability/CentralLimitTheorem.lean#L117)
- [Mathlib overview: Probability Theory › Convergence of a sequence of random variables](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L421)
- [Mathlib undergraduate list: Probability Theory › Convergence of a sequence of random variables](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L585)
- [Freek Wiedijk's 100 theorems, no. 47](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/100.yaml#L247)
- [1000+ theorems list: Q190391](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L141)
- [1000+ theorems project: Q190391](https://1000-plus.github.io/all.html?length=-1#Q190391)
- [Wikipedia: Central limit theorem](https://en.wikipedia.org/wiki/Central_limit_theorem)
- [Wikidata: Q190391](https://www.wikidata.org/wiki/Q190391)
