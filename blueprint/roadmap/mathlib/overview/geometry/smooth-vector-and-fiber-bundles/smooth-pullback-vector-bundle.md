---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ContMDiffVectorBundle.pullback
mathlib_file: Mathlib/Geometry/Manifold/VectorBundle/Pullback.lean
---

# (smooth) pullback vector bundle

For a `C^n` vector bundle `E` over a manifold `B` and a `C^n` map `f : B' → B`, the pullback
vector bundle `f *ᵖ E` is a `C^n` vector bundle.

```lean
ContMDiffVectorBundle.pullback.{u_1, u_2, u_3, u_4, u_5, u_6, u_7, u_8, u_9} {𝕜 : Type u_1}
  {B : Type u_2} {B' : Type u_3} (F : Type u_4) (E : B → Type u_5) {n : WithTop ℕ∞}
  [NontriviallyNormedField 𝕜] [(x : B) → AddCommMonoid (E x)] [(x : B) → _root_.Module 𝕜 (E x)]
  [NormedAddCommGroup F] [NormedSpace 𝕜 F] [TopologicalSpace (Bundle.TotalSpace F E)]
  [(x : B) → TopologicalSpace (E x)] {EB : Type u_6} [NormedAddCommGroup EB] [NormedSpace 𝕜 EB]
  {HB : Type u_7} [TopologicalSpace HB] {IB : ModelWithCorners 𝕜 EB HB} [TopologicalSpace B]
  [ChartedSpace HB B] {EB' : Type u_8} [NormedAddCommGroup EB'] [NormedSpace 𝕜 EB'] {HB' : Type u_9}
  [TopologicalSpace HB'] (IB' : ModelWithCorners 𝕜 EB' HB') [TopologicalSpace B']
  [ChartedSpace HB' B'] [FiberBundle F E] [VectorBundle 𝕜 F E] [ContMDiffVectorBundle n F E IB]
  (f : ContMDiffMap IB' IB B' B n) : ContMDiffVectorBundle n F (⇑f *ᵖ E) IB'
```

## Depends on

- [(smooth) vector bundle](smooth-vector-bundle.md)
- [Smooth map between manifolds](../differentiable-manifolds/part-01/smooth-map-between-manifolds.md)

## Proof depends on

- [$C^k$ function](../../analysis/differentiability/c-k-function.md)
- [Absolutely convergent series in Banach spaces](../../analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Cantor’s Theorem](../../../hundred-theorems/part-04/cantors-theorem.md)
- [Cardinal](../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Characteristic p](../../general-algebra/field-theory/characteristic-p.md)
- [Closed map](../../topology/general-topology/part-01/closed-map.md)
- [Completion of an abelian topological group](../../topology/topological-algebra/completion-of-an-abelian-topological-group.md)
- [Euclidean affine space](../affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Existence of bases](../../../undergraduate/linear-algebra/fundamentals/existence-of-bases.md)
- [Finite product of metric spaces](../../../undergraduate/topology/topology-and-metric-spaces/finite-product-of-metric-spaces.md)
- [Holomorphic functions](../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Kernel of a linear map](../../../undergraduate/linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Limit point](../../../undergraduate/single-variable-real-analysis/sequences-of-real-numbers/limit-point.md)
- [Open map](../../topology/general-topology/part-01/open-map.md)
- [Pointwise convergence](../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)
- [Product of vector spaces](../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Schroeder-Bernstein Theorem](../../../hundred-theorems/part-02/schroeder-bernstein-theorem.md)
- [Sequential space](../../topology/general-topology/part-01/sequential-space.md)
- [Squeeze theorem](../../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [Sum of a Geometric Series](../../../hundred-theorems/part-04/sum-of-a-geometric-series.md)
- [Sum of subspaces](../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)
- [The Number of Subsets of a Set](../../../hundred-theorems/part-03/the-number-of-subsets-of-a-set.md)
- [Topological module](../../topology/topological-algebra/topological-module.md)
- [Topology of a metric space](../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../../analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Uniformly continuous function](../../topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `ContMDiffVectorBundle.pullback`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/VectorBundle/Pullback.html#ContMDiffVectorBundle.pullback)
- [Source of `ContMDiffVectorBundle.pullback` in Mathlib/Geometry/Manifold/VectorBundle/Pullback.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/VectorBundle/Pullback.lean#L37)
- [Mathlib overview: Geometry › Smooth vector and fiber bundles](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L471)
