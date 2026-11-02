---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: polynomialFunctions_closure_eq_top
mathlib_file: Mathlib/Topology/ContinuousMap/Weierstrass.lean
---

# Weierstrass polynomial approximation theorem

The **Weierstrass Approximation Theorem**:
polynomials functions on `[a, b] ⊆ ℝ` are dense in `C([a,b],ℝ)`

\(While we could deduce this as an application of the Stone-Weierstrass theorem,
our proof of that relies on the fact that `abs` is in the closure of polynomials on `[-M, M]`,
so we may as well get this done first.\)

```lean
polynomialFunctions_closure_eq_top (a b : ℝ) :
  (polynomialFunctions (Set.Icc a b)).topologicalClosure = ⊤
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Bornology](../../../overview/analysis/topological-vector-spaces/bornology.md)
- [Closure](../../../overview/topology/general-topology/part-01/closure.md)
- [Compact open topology](../../../overview/topology/general-topology/part-01/compact-open-topology.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Order (Real numbers)](../real-numbers/order.md)
- [Order topology](../../../overview/topology/topological-algebra/order-topology.md)
- [Polynomial functions](../elementary-functions-trigonometric-rational-exp/polynomial-functions.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)
- [Uniform space](../../../overview/topology/uniform-notions/uniform-space.md)

## Proof depends on

- [Completeness of R](../topology-of-r/completeness-of-r.md)
- [Convex function](../../../overview/analysis/convexity/convex-function.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Heine-Cantor theorem](../../../overview/topology/uniform-notions/heine-cantor-theorem.md)
- [Homeomorphisms](../../topology/topology-and-metric-spaces/homeomorphisms.md)
- [Limit point](../sequences-of-real-numbers/limit-point.md)
- [Lipschitz continuity](../../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Local convexity](../../../overview/analysis/topological-vector-spaces/local-convexity.md)
- [Metric structure](../topology-of-r/metric-structure.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Open map](../../../overview/topology/general-topology/part-01/open-map.md)
- [Polynomial in several indeterminates](../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-several-indeterminates.md)
- [Product of vector spaces](../../linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Squeeze theorem](../../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [The Binomial Theorem](../../../hundred-theorems/part-03/the-binomial-theorem.md)
- [The Triangle Inequality](../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological module](../../../overview/topology/topological-algebra/topological-module.md)
- [Topology of a metric space](../../topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Uniform convergence](../../../overview/topology/uniform-notions/uniform-convergence.md)
- [Uniformly continuous function](../../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `polynomialFunctions_closure_eq_top`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/ContinuousMap/Weierstrass.html#polynomialFunctions_closure_eq_top)
- [Source of `polynomialFunctions_closure_eq_top` in Mathlib/Topology/ContinuousMap/Weierstrass.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/ContinuousMap/Weierstrass.lean#L48)
- [Mathlib undergraduate list: Single Variable Real Analysis › Sequences and series of functions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L356)
