---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: HasFDerivAt.comp
mathlib_file: Mathlib/Analysis/Calculus/FDeriv/Comp.lean
---

# Derivative of a composition of functions

The chain rule.

```lean
HasFDerivAt.comp.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜] {E : Type u_2}
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] {F : Type u_3} [NormedAddCommGroup F] [NormedSpace 𝕜 F]
  {G : Type u_4} [AddCommGroup G] [TopologicalSpace G] [_root_.Module 𝕜 G] [ContinuousAdd G]
  [ContinuousSMul 𝕜 G] {f : E → F} {f' : E →L[𝕜] F} (x : E) {g : F → G} {g' : F →L[𝕜] G}
  (hg : HasFDerivAt g g' (f x)) (hf : HasFDerivAt f f' x) : HasFDerivAt (g ∘ f) (g' ∘SL f') x
```

## Depends on

- [Differentiable function between normed vector spaces](differentiable-function-between-normed-vector-sp.md)
- [Normed vector space over a normed field](../normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Topological module](../../topology/topological-algebra/topological-module.md)

## Proof depends on

- [Closure](../../topology/general-topology/part-01/closure.md)
- [Cluster point](../../topology/general-topology/part-01/cluster-point.md)
- [Homeomorphisms](../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Lipschitz continuity](../../topology/metric-spaces/lipschitz-continuity.md)
- [Metric structure](../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Open map](../../topology/general-topology/part-01/open-map.md)
- [Product of vector spaces](../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Squeeze theorem](../../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [The Triangle Inequality](../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological ring](../../topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Uniformly continuous function](../../topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `HasFDerivAt.comp`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/FDeriv/Comp.html#HasFDerivAt.comp)
- [Source of `HasFDerivAt.comp` in Mathlib/Analysis/Calculus/FDeriv/Comp.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/FDeriv/Comp.lean#L101)
- [Mathlib overview: Analysis › Differentiability](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L308)
