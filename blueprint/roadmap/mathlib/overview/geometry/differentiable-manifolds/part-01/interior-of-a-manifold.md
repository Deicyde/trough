---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: ModelWithCorners.interior
mathlib_file: Mathlib/Geometry/Manifold/IsManifold/InteriorBoundary.lean
---

# Interior of a manifold

The **interior** of a manifold `M` is the set of its interior points.

```lean
ModelWithCorners.interior.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜]
  {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {H : Type u_3} [TopologicalSpace H]
  {I : ModelWithCorners 𝕜 E H} (M : Type u_4) [TopologicalSpace M] [ChartedSpace H M] : Set M
```

## Depends on

- [Associative algebra over a commutative ring](../../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Completeness](../../../topology/uniform-notions/completeness.md)
- [Continuous function](../../../topology/general-topology/part-01/continuous-function.md)
- [Convex subsets](../../../../undergraduate/affine-and-euclidean-geometry/convexity/convex-subsets.md)
- [Field $\R$ of real numbers](../../../../undergraduate/ring-theory/field-theory/part-01/field-r-of-real-numbers.md)
- [Metric structure](../../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Normed vector space over a normed field](../../../analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Ordered ring](../../../general-algebra/rings/ordered-ring.md)
- [Permutation group of a type](../../../general-algebra/group-theory/part-02/permutation-group-of-a-type.md)

## Sources

- [Mathlib documentation: `ModelWithCorners.interior`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/IsManifold/InteriorBoundary.html#ModelWithCorners.interior)
- [Source of `ModelWithCorners.interior` in Mathlib/Geometry/Manifold/IsManifold/InteriorBoundary.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/IsManifold/InteriorBoundary.lean#L102)
- [Mathlib overview: Geometry › Differentiable manifolds](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L446)
