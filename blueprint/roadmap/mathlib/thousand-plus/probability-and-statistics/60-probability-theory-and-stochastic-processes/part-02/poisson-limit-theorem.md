---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.tendsto_choose_mul_pow_of_tendsto_mul_atTop
mathlib_file: Mathlib/Probability/Distributions/Poisson/PoissonLimitThm.lean
---

# Poisson limit theorem

**Poisson limit Theorem**: If `n * p n → r` as `n → ∞`. Then
`(n.choose k) * (p n)^k * (1 - p n)^(n - k) → exp (-r) * r^k / k!`.

```lean
ProbabilityTheory.tendsto_choose_mul_pow_of_tendsto_mul_atTop {p : ℕ → ℝ} {r : ℝ} (k : ℕ)
  (hr : Filter.Tendsto (fun n => ↑n * p n) Filter.atTop (nhds r)) :
  Filter.Tendsto (fun n => ↑(n.choose k) * p n ^ k * (1 - p n) ^ (n - k)) Filter.atTop
    (nhds (Real.exp (-r) * r ^ k / ↑k.factorial))
```

## Depends on

- [Bornology](../../../../overview/analysis/topological-vector-spaces/bornology.md)
- [Exponential](../../../../overview/analysis/special-functions/exponential.md)
- [Uniform space](../../../../overview/topology/uniform-notions/uniform-space.md)

## Proof depends on

- [$C^k$ function](../../../../overview/analysis/differentiability/c-k-function.md)
- [Absolutely convergent series in Banach spaces](../../../../overview/analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Affine function](../../../../overview/geometry/affine-and-euclidean-geometry/affine-function.md)
- [Completion of an abelian topological group](../../../../overview/topology/topological-algebra/completion-of-an-abelian-topological-group.md)
- [Derivative at a point](../../../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Derivative of the inverse of a function (Single Variable Real Analysis)](../../../../undergraduate/single-variable-real-analysis/differentiability/derivative-of-the-inverse-of-a-function.md)
- [Differentials (linear tangent functions)](../../../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Euclidean affine space](../../../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Fundamental Theorem of Integral Calculus](../../../../hundred-theorems/part-01/fundamental-theorem-of-integral-calculus.md)
- [Holomorphic functions](../../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Matrix exponential](../../../../undergraduate/linear-algebra/exponential/matrix-exponential.md)
- [Sequential space](../../../../overview/topology/general-topology/part-01/sequential-space.md)
- [Sum of a Geometric Series](../../../../hundred-theorems/part-04/sum-of-a-geometric-series.md)
- [The Number of Subsets of a Set](../../../../hundred-theorems/part-03/the-number-of-subsets-of-a-set.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.tendsto_choose_mul_pow_of_tendsto_mul_atTop`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Distributions/Poisson/PoissonLimitThm.html#ProbabilityTheory.tendsto_choose_mul_pow_of_tendsto_mul_atTop)
- [Source of `ProbabilityTheory.tendsto_choose_mul_pow_of_tendsto_mul_atTop` in Mathlib/Probability/Distributions/Poisson/PoissonLimitThm.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Probability/Distributions/Poisson/PoissonLimitThm.lean#L66)
- [1000+ theorems list: Q7208500](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L3671)
- [1000+ theorems project: Q7208500](https://1000-plus.github.io/?length=-1#Q7208500)
- [Wikipedia: Poisson limit theorem](https://en.wikipedia.org/wiki/Poisson_limit_theorem)
- [Wikidata: Q7208500](https://www.wikidata.org/wiki/Q7208500)
