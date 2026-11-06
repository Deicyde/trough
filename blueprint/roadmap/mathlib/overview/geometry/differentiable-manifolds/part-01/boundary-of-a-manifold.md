# Boundary of a manifold

The **boundary** of a manifold `M` is the set of its boundary points.

```lean
ModelWithCorners.boundary.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜]
  {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {H : Type u_3} [TopologicalSpace H]
  {I : ModelWithCorners 𝕜 E H} (M : Type u_4) [TopologicalSpace M] [ChartedSpace H M] : Set M
```

## Depends on

- [Associative algebra over a commutative ring](../../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Closure](../../../topology/general-topology/part-01/closure.md)
- [Completeness](../../../topology/uniform-notions/completeness.md)
- [Continuous function](../../../topology/general-topology/part-01/continuous-function.md)
- [Convex subsets](../../../../undergraduate/affine-and-euclidean-geometry/convexity/convex-subsets.md)
- [Normed vector space over a normed field](../../../analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Sources

- [Mathlib documentation: `ModelWithCorners.boundary`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/IsManifold/InteriorBoundary.html#ModelWithCorners.boundary)
- [Source of `ModelWithCorners.boundary` in Mathlib/Geometry/Manifold/IsManifold/InteriorBoundary.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/IsManifold/InteriorBoundary.lean#L111)
- [Mathlib overview: Geometry › Differentiable manifolds](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L447)
