---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.tendstoInDistribution_inv_sqrt_mul_sum_sub
mathlib_file: Mathlib/Probability/CentralLimitTheorem.lean
---

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
- [Lipschitz continuity](../../topology/metric-spaces/lipschitz-continuity.md)
- [Probability measure](../definitions-in-probability-theory/probability-measure.md)
- [Variance of a real-valued random variable](../random-variables-and-their-laws/variance-of-a-real-valued-random-variable.md)

## Proof depends on

- [Change of variables to polar co-ordinates](../../../undergraduate/measures-and-integral-calculus/integration/change-of-variables-to-polar-co-ordinates.md)
- [Connected components](../../../undergraduate/topology/topology-and-metric-spaces/connected-components.md)
- [Connectedness](../../topology/general-topology/part-01/connectedness.md)
- [Continuity of the sum of a series of functions](../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/continuity-of-the-sum-of-a-series-of-functions.md)
- [Continuous mapping theorem](../../../thousand-plus/probability-and-statistics/60-probability-theory-and-stochastic-processes/part-01/continuous-mapping-theorem.md)
- [Determinant of vectors](../../../undergraduate/linear-algebra/multilinearity/determinant-of-vectors.md)
- [Divergence theorem](../../analysis/measures-and-integral-calculus/part-02/divergence-theorem.md)
- [Higher-order derivatives of functions](../../../undergraduate/single-variable-real-analysis/differentiability/higher-order-derivatives-of-functions.md)
- [Independent sigma-algebras](../definitions-in-probability-theory/independent-sigma-algebras.md)
- [Lévy continuity theorem](../../../thousand-plus/probability-and-statistics/60-probability-theory-and-stochastic-processes/part-02/levy-continuity-theorem.md)
- [Orientation of a $\R$-vector space](../../../undergraduate/linear-algebra/multilinearity/orientation-of-a-vector-space.md)
- [Path connectedness](../../../undergraduate/topology/topology-and-metric-spaces/path-connectedness.md)
- [Unitary group](../../../undergraduate/group-theory/classical-automorphism-groups/unitary-group.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.tendstoInDistribution_inv_sqrt_mul_sum_sub`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/CentralLimitTheorem.html#ProbabilityTheory.tendstoInDistribution_inv_sqrt_mul_sum_sub)
- [Source of `ProbabilityTheory.tendstoInDistribution_inv_sqrt_mul_sum_sub` in Mathlib/Probability/CentralLimitTheorem.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Probability/CentralLimitTheorem.lean#L117)
- [Mathlib overview: Probability Theory › Convergence of a sequence of random variables](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L421)
- [Mathlib undergraduate list: Probability Theory › Convergence of a sequence of random variables](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L585)
- [Freek Wiedijk's 100 theorems, no. 47](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L247)
- [1000+ theorems list: Q190391](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L141)
- [1000+ theorems project: Q190391](https://1000-plus.github.io/?length=-1#Q190391)
- [Wikipedia: Central limit theorem](https://en.wikipedia.org/wiki/Central_limit_theorem)
- [Wikidata: Q190391](https://www.wikidata.org/wiki/Q190391)
