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

- [Bornology](../../overview/analysis/topological-vector-spaces/bornology.md)
- [Exponential](../../overview/analysis/special-functions/exponential.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Completeness](../../overview/topology/uniform-notions/completeness.md)
- [Field $\Q$ of rational numbers](../../undergraduate/ring-theory/field-theory/field-q-of-rational-numbers.md)
- [Normed vector space over a normed field](../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Ordered ring](../../overview/general-algebra/rings/ordered-ring.md)
- [The Binomial Theorem](../../hundred-theorems/part-02/the-binomial-theorem.md)
- [The Triangle Inequality](../../hundred-theorems/part-04/the-triangle-inequality.md)
- [Topological module](../../overview/topology/topological-algebra/topological-module.md)
- [Topological ring](../../overview/topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.tendsto_choose_mul_pow_of_tendsto_mul_atTop`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Distributions/Poisson/PoissonLimitThm.html#ProbabilityTheory.tendsto_choose_mul_pow_of_tendsto_mul_atTop)
- [Source of `ProbabilityTheory.tendsto_choose_mul_pow_of_tendsto_mul_atTop` in Mathlib/Probability/Distributions/Poisson/PoissonLimitThm.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Probability/Distributions/Poisson/PoissonLimitThm.lean#L66)
- [1000+ theorems list: Q7208500](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L3671)
- [1000+ theorems project: Q7208500](https://1000-plus.github.io/all.html?length=-1#Q7208500)
- [Wikipedia: Poisson limit theorem](https://en.wikipedia.org/wiki/Poisson_limit_theorem)
- [Wikidata: Q7208500](https://www.wikidata.org/wiki/Q7208500)
