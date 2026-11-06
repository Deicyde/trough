---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: taylor_mean_remainder_lagrange
mathlib_file: Mathlib/Analysis/Calculus/Taylor.lean
---

# Taylor's theorem with Lagrange form for remainder

**Taylor's theorem** with the Lagrange form of the remainder.

We assume that `f` is `n`-times continuously differentiable in the closed set `uIcc x₀ x` and
`n+1`-times differentiable on the open set `uIoo x₀ x`. Then there exists an `x' ∈ uIoo x₀ x` such
that
$$f(x) - (P_n f)(x₀, x) = \frac{f^{(n+1)}(x') (x - x₀)^{n+1}}{(n+1)!},$$
where $P_n f$ denotes the Taylor polynomial of degree $n$ and $f^{(n+1)}$ is the $n+1$-th iterated
derivative.

```lean
taylor_mean_remainder_lagrange {f : ℝ → ℝ} {x x₀ : ℝ} {n : ℕ} (hx : x₀ ≠ x)
  (hf : ContDiffOn ℝ (↑n) f (Set.uIcc x₀ x))
  (hf' : DifferentiableOn ℝ (iteratedDerivWithin n f (Set.uIcc x₀ x)) (Set.uIoo x₀ x)) :
  ∃ x' ∈ Set.uIoo x₀ x,
    f x - taylorWithinEval f n (Set.uIcc x₀ x) x₀ x =
      iteratedDerivWithin (n + 1) f (Set.uIcc x₀ x) x' * (x - x₀) ^ (n + 1) / ↑(n + 1).factorial
```

Freek Wiedijk's list (no. 35) also cites `taylor_mean_remainder_cauchy`, `map_add_eq_sum_add_integral_iteratedFDeriv`.

The 1000+ list (Q1137206) also cites `taylor_mean_remainder_cauchy`.

## Depends on

- [Holomorphic functions](../../single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Infinite sum](../../../overview/topology/topological-algebra/infinite-sum.md)
- [Inner product space, over $R$ or $C$](../../../overview/analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Norm of a continuous linear map](../../../overview/analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Polynomial in one indeterminate](../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-one-indeterminate.md)
- [Radius of convergence](../../single-variable-complex-analysis/complex-valued-series/radius-of-convergence.md)

## Proof depends on

- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Closure](../../../overview/topology/general-topology/part-01/closure.md)
- [Cluster point](../../../overview/topology/general-topology/part-01/cluster-point.md)
- [Derivative at a point](../differentiability/derivative-at-a-point.md)
- [Field $\R$ of real numbers](../../ring-theory/field-theory/field-r-of-real-numbers.md)
- [Generating sets](../../linear-algebra/fundamentals/generating-sets.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)
- [Polynomial functions](../elementary-functions-trigonometric-rational-exp/polynomial-functions.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)
- [Topology on a normed vector space](../../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)

## Sources

- [Mathlib documentation: `taylor_mean_remainder_lagrange`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Taylor.html#taylor_mean_remainder_lagrange)
- [Source of `taylor_mean_remainder_lagrange` in Mathlib/Analysis/Calculus/Taylor.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/Taylor.lean#L322)
- [Mathlib undergraduate list: Single Variable Real Analysis › Taylor-like theorems](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L327)
- [Freek Wiedijk's 100 theorems, no. 35](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L183)
- [1000+ theorems list: Q1137206](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1399)
- [1000+ theorems project: Q1137206](https://1000-plus.github.io/all.html?length=-1#Q1137206)
- [Wikipedia: Taylor's theorem](https://en.wikipedia.org/wiki/Taylor's_theorem)
- [Wikidata: Q1137206](https://www.wikidata.org/wiki/Q1137206)
