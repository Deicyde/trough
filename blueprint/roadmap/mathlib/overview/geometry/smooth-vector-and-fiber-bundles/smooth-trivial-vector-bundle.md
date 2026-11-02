---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Bundle.Trivial.contMDiffVectorBundle
mathlib_file: Mathlib/Geometry/Manifold/VectorBundle/Basic.lean
---

# (smooth) trivial vector bundle

A trivial vector bundle over a manifold is a `C^n` vector bundle.

```lean
Bundle.Trivial.contMDiffVectorBundle.{u_1, u_2, u_3, u_6, u_7} {n : WithTop ℕ∞} {𝕜 : Type u_1}
  {B : Type u_2} (F : Type u_3) [NontriviallyNormedField 𝕜] {EB : Type u_6} [NormedAddCommGroup EB]
  [NormedSpace 𝕜 EB] {HB : Type u_7} [TopologicalSpace HB] {IB : ModelWithCorners 𝕜 EB HB}
  [TopologicalSpace B] [ChartedSpace HB B] [NormedAddCommGroup F] [NormedSpace 𝕜 F] :
  ContMDiffVectorBundle n F (Bundle.Trivial B F) IB
```

## Depends on

- [(smooth) vector bundle](smooth-vector-bundle.md)

## Proof depends on

- [$C^k$ function](../../analysis/differentiability/c-k-function.md)
- [Absolutely convergent series in Banach spaces](../../analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Closed map](../../topology/general-topology/part-01/closed-map.md)
- [Completion of an abelian topological group](../../topology/topological-algebra/completion-of-an-abelian-topological-group.md)
- [Euclidean affine space](../affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Existence of bases](../../../undergraduate/linear-algebra/fundamentals/existence-of-bases.md)
- [Holomorphic functions](../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Kernel of a linear map](../../../undergraduate/linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Limit point](../../../undergraduate/single-variable-real-analysis/sequences-of-real-numbers/limit-point.md)
- [Open map](../../topology/general-topology/part-01/open-map.md)
- [Product of vector spaces](../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Sequential space](../../topology/general-topology/part-01/sequential-space.md)
- [Smooth map between manifolds](../differentiable-manifolds/part-01/smooth-map-between-manifolds.md)
- [Squeeze theorem](../../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [Sum of a Geometric Series](../../../hundred-theorems/part-04/sum-of-a-geometric-series.md)
- [Sum of subspaces](../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)
- [The Number of Subsets of a Set](../../../hundred-theorems/part-03/the-number-of-subsets-of-a-set.md)
- [Topological module](../../topology/topological-algebra/topological-module.md)
- [Topology of a metric space](../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../../analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Uniformly continuous function](../../topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `Bundle.Trivial.contMDiffVectorBundle`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/VectorBundle/Basic.html#Bundle.Trivial.contMDiffVectorBundle)
- [Source of `Bundle.Trivial.contMDiffVectorBundle` in Mathlib/Geometry/Manifold/VectorBundle/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/VectorBundle/Basic.lean#L609)
- [Mathlib overview: Geometry › Smooth vector and fiber bundles](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L469)
