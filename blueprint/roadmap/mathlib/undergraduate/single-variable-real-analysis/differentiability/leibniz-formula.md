---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: deriv_mul
mathlib_file: Mathlib/Analysis/Calculus/Deriv/Mul.lean
---

# Leibniz formula

Mathlib states this as `deriv_mul`.

```lean
deriv_mul.{u, u_3} {𝕜 : Type u} [NontriviallyNormedField 𝕜] {x : 𝕜} {𝔸 : Type u_3} [NormedRing 𝔸]
  [NormedAlgebra 𝕜 𝔸] {c d : 𝕜 → 𝔸} (hc : DifferentiableAt 𝕜 c x) (hd : DifferentiableAt 𝕜 d x) :
  deriv (c * d) x = deriv c x * d x + c x * deriv d x
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Differentiable function between normed vector spaces](../../../overview/analysis/differentiability/differentiable-function-between-normed-vector-sp.md)
- [Differentials (linear tangent functions)](../../multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Proof depends on

- [Closure](../../../overview/topology/general-topology/part-01/closure.md)
- [Cluster point](../../../overview/topology/general-topology/part-01/cluster-point.md)
- [Derivative at a point](derivative-at-a-point.md)
- [Generating sets](../../linear-algebra/fundamentals/generating-sets.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../topology/topology-and-metric-spaces/homeomorphisms.md)
- [Lipschitz continuity](../../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Metric structure](../topology-of-r/metric-structure.md)
- [Norm of a continuous linear map](../../../overview/analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Open map](../../../overview/topology/general-topology/part-01/open-map.md)
- [Product of vector spaces](../../linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Squeeze theorem](../../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [The Triangle Inequality](../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Uniformly continuous function](../../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `deriv_mul`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Deriv/Mul.html#deriv_mul)
- [Source of `deriv_mul` in Mathlib/Analysis/Calculus/Deriv/Mul.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/Deriv/Mul.lean#L281)
- [Mathlib undergraduate list: Single Variable Real Analysis › Differentiability](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L323)
