# Smooth map between manifolds

`ContMDiff I I' n f` indicates that the function `f : M → M'` between manifolds
is `n` times continuously differentiable.

`f` is `n` times continuously differentiable if it is continuous and, for any pair of points,
it is `n` times continuously differentiable in the charts around these points.
The parameter `n` belongs to `ℕ∞ω` (accessible in the `ContDiff` scope), i.e. it can be a natural
number, `∞`, or `ω`, where `C^ω` corresponds to analytic functions.

```lean
ContMDiff.{u_1, u_2, u_3, u_4, u_5, u_6, u_7} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜]
  {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {H : Type u_3} [TopologicalSpace H]
  (I : ModelWithCorners 𝕜 E H) {M : Type u_4} [TopologicalSpace M] [ChartedSpace H M]
  {E' : Type u_5} [NormedAddCommGroup E'] [NormedSpace 𝕜 E'] {H' : Type u_6} [TopologicalSpace H']
  (I' : ModelWithCorners 𝕜 E' H') {M' : Type u_7} [TopologicalSpace M'] [ChartedSpace H' M']
  (n : WithTop ℕ∞) (f : M → M') : Prop
```

## Depends on

- [Associative algebra over a commutative ring](../../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Completeness](../../../topology/uniform-notions/completeness.md)
- [Convex subsets](../../../../undergraduate/affine-and-euclidean-geometry/convexity/convex-subsets.md)
- [Infinite sum](../../../topology/topological-algebra/infinite-sum.md)
- [Norm of a continuous linear map](../../../analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Radius of convergence](../../../../undergraduate/single-variable-complex-analysis/complex-valued-series/radius-of-convergence.md)

## Sources

- [Mathlib documentation: `ContMDiff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/ContMDiff/Defs.html#ContMDiff)
- [Source of `ContMDiff` in Mathlib/Geometry/Manifold/ContMDiff/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/ContMDiff/Defs.lean#L204)
- [Mathlib overview: Geometry › Differentiable manifolds](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L441)
