---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: second_derivative_symmetric
mathlib_file: Mathlib/Analysis/Calculus/FDeriv/Symmetric.lean
---

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
- [Field $\R$ of real numbers](../../ring-theory/field-theory/part-01/field-r-of-real-numbers.md)
- [Induced topology](../../../overview/topology/general-topology/part-01/induced-topology.md)
- [Metric structure](../../single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Permutation group of a type](../../../overview/general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Ring structure $\Z$](../../ring-theory/fundamentals/ring-structure-z.md)

## Proof depends on

- [Affine function](../../../overview/geometry/affine-and-euclidean-geometry/affine-function.md)
- [Completeness of R](../../single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Convex function](../../../overview/analysis/convexity/convex-function.md)
- [Derivative at a point](../../single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Derivative of a composition of functions (Analysis)](../../../overview/analysis/differentiability/derivative-of-a-composition-of-functions.md)
- [Euclidean affine space](../../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Norm of a continuous linear map](../../../overview/analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Topology on a normed vector space](../../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)

## Sources

- [Mathlib documentation: `second_derivative_symmetric`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/FDeriv/Symmetric.html#second_derivative_symmetric)
- [Source of `second_derivative_symmetric` in Mathlib/Analysis/Calculus/FDeriv/Symmetric.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/FDeriv/Symmetric.lean#L484)
- [Mathlib undergraduate list: Multivariable calculus › Differential calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L467)
