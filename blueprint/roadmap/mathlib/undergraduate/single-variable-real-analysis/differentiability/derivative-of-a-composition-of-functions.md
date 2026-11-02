---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: deriv_comp
mathlib_file: Mathlib/Analysis/Calculus/Deriv/Comp.lean
---

# Derivative of a composition of functions (Single Variable Real Analysis)

Mathlib states this as `deriv_comp`.

```lean
deriv_comp.{u, u_1} {𝕜 : Type u} [NontriviallyNormedField 𝕜] (x : 𝕜) {𝕜' : Type u_1}
  [NontriviallyNormedField 𝕜'] [NormedAlgebra 𝕜 𝕜'] {h : 𝕜 → 𝕜'} {h₂ : 𝕜' → 𝕜'}
  (hh₂ : DifferentiableAt 𝕜' h₂ (h x)) (hh : DifferentiableAt 𝕜 h x) :
  deriv (h₂ ∘ h) x = deriv h₂ (h x) * deriv h x
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
- [Open map](../../../overview/topology/general-topology/part-01/open-map.md)
- [Product of vector spaces](../../linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Squeeze theorem](../../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [The Triangle Inequality](../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Uniformly continuous function](../../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `deriv_comp`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Deriv/Comp.html#deriv_comp)
- [Source of `deriv_comp` in Mathlib/Analysis/Calculus/Deriv/Comp.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/Deriv/Comp.lean#L299)
- [Mathlib undergraduate list: Single Variable Real Analysis › Differentiability](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L316)
