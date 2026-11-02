---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: ContMDiffVectorBundle
mathlib_file: Mathlib/Geometry/Manifold/VectorBundle/Basic.lean
---

# (smooth) vector bundle

When `B` is a manifold with respect to a model `IB` and `E` is a
topological vector bundle over `B` with fibers isomorphic to `F`,
then `ContMDiffVectorBundle n F E IB` registers that the bundle is `C^n`, in the sense of having
`C^n` transition functions. This is a mixin, not carrying any new data.

```lean
ContMDiffVectorBundle.{u_1, u_2, u_3, u_5, u_6, u_7} (n : WithTop ℕ∞) {𝕜 : Type u_1} {B : Type u_2}
  (F : Type u_3) (E : B → Type u_5) [NontriviallyNormedField 𝕜] {EB : Type u_6}
  [NormedAddCommGroup EB] [NormedSpace 𝕜 EB] {HB : Type u_7} [TopologicalSpace HB]
  (IB : ModelWithCorners 𝕜 EB HB) [TopologicalSpace B] [ChartedSpace HB B]
  [(x : B) → AddCommMonoid (E x)] [(x : B) → _root_.Module 𝕜 (E x)] [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] [TopologicalSpace (Bundle.TotalSpace F E)] [(x : B) → TopologicalSpace (E x)]
  [FiberBundle F E] [VectorBundle 𝕜 F E] : Prop
```

## Depends on

- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Completeness](../../topology/uniform-notions/completeness.md)
- [Convex subsets](../../../undergraduate/affine-and-euclidean-geometry/convexity/convex-subsets.md)
- [Field $\R$ of real numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-of-real-numbers.md)
- [Homeomorphisms](../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Infinite sum](../../topology/topological-algebra/infinite-sum.md)
- [Metric structure](../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Norm of a continuous linear map](../../analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Ordered ring](../../general-algebra/rings/ordered-ring.md)
- [Permutation group of a type](../../general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Radius of convergence](../../../undergraduate/single-variable-complex-analysis/complex-valued-series/radius-of-convergence.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure.md)
- [Topological vector bundle](../../topology/general-topology/part-01/topological-vector-bundle.md)

## Sources

- [Mathlib documentation: `ContMDiffVectorBundle`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/VectorBundle/Basic.html#ContMDiffVectorBundle)
- [Source of `ContMDiffVectorBundle` in Mathlib/Geometry/Manifold/VectorBundle/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/VectorBundle/Basic.lean#L301)
- [Mathlib overview: Geometry › Smooth vector and fiber bundles](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L468)
