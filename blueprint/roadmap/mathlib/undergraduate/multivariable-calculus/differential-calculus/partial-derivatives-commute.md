# Partial derivatives commute

If a function is differentiable, and has two derivatives at `x`, then the second
derivative is symmetric.

```lean
second_derivative_symmetric.{u_1, u_2, u_3} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜]
  {E : Type u_2} {F : Type u_3} [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] {f : E → F} [IsRCLikeNormedField 𝕜] {f' : E → E →L[𝕜] F}
  {f'' : E →L[𝕜] E →L[𝕜] F} {x : E} (hf : ∀ (y : E), HasFDerivAt f (f' y) y)
  (hx : HasFDerivAt f' f'' x) (v w : E) : (f'' v) w = (f'' w) v
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Completeness](../../../overview/topology/uniform-notions/completeness.md)
- [Differentiable function between normed vector spaces](../../../overview/analysis/differentiability/differentiable-function-between-normed-vector-sp.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Proof depends on

- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Convex subsets](../../affine-and-euclidean-geometry/convexity/convex-subsets.md)
- [Derivative at a point](../../single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Order topology](../../../overview/topology/topological-algebra/order-topology.md)
- [The Triangle Inequality](../../../hundred-theorems/part-04/the-triangle-inequality.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)

## Sources

- [Mathlib documentation: `second_derivative_symmetric`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/FDeriv/Symmetric.html#second_derivative_symmetric)
- [Source of `second_derivative_symmetric` in Mathlib/Analysis/Calculus/FDeriv/Symmetric.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Calculus/FDeriv/Symmetric.lean#L484)
- [Mathlib undergraduate list: Multivariable calculus › Differential calculus](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L467)
