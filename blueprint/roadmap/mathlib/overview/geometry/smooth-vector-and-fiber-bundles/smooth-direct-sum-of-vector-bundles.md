---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Bundle.Prod.contMDiffVectorBundle
mathlib_file: Mathlib/Geometry/Manifold/VectorBundle/Basic.lean
---

# (smooth) direct sum of vector bundles

The direct sum of two `C^n` vector bundles over the same base is a `C^n` vector bundle.

```lean
Bundle.Prod.contMDiffVectorBundle.{u_1, u_2, u_6, u_7, u_10, u_11, u_12, u_13} {n : WithTop ℕ∞}
  {𝕜 : Type u_1} {B : Type u_2} [NontriviallyNormedField 𝕜] {EB : Type u_6} [NormedAddCommGroup EB]
  [NormedSpace 𝕜 EB] {HB : Type u_7} [TopologicalSpace HB] {IB : ModelWithCorners 𝕜 EB HB}
  [TopologicalSpace B] [ChartedSpace HB B] (F₁ : Type u_10) [NormedAddCommGroup F₁]
  [NormedSpace 𝕜 F₁] (E₁ : B → Type u_11) [TopologicalSpace (Bundle.TotalSpace F₁ E₁)]
  [(x : B) → AddCommMonoid (E₁ x)] [(x : B) → _root_.Module 𝕜 (E₁ x)] (F₂ : Type u_12)
  [NormedAddCommGroup F₂] [NormedSpace 𝕜 F₂] (E₂ : B → Type u_13)
  [TopologicalSpace (Bundle.TotalSpace F₂ E₂)] [(x : B) → AddCommMonoid (E₂ x)]
  [(x : B) → _root_.Module 𝕜 (E₂ x)] [(x : B) → TopologicalSpace (E₁ x)]
  [(x : B) → TopologicalSpace (E₂ x)] [FiberBundle F₁ E₁] [FiberBundle F₂ E₂] [VectorBundle 𝕜 F₁ E₁]
  [VectorBundle 𝕜 F₂ E₂] [ContMDiffVectorBundle n F₁ E₁ IB] [ContMDiffVectorBundle n F₂ E₂ IB] :
  ContMDiffVectorBundle n (F₁ × F₂) (fun x => E₁ x × E₂ x) IB
```

## Depends on

- [(smooth) vector bundle](smooth-vector-bundle.md)
- [Product of vector spaces](../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)

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

- [Mathlib documentation: `Bundle.Prod.contMDiffVectorBundle`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/VectorBundle/Basic.html#Bundle.Prod.contMDiffVectorBundle)
- [Source of `Bundle.Prod.contMDiffVectorBundle` in Mathlib/Geometry/Manifold/VectorBundle/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/VectorBundle/Basic.lean#L636)
- [Mathlib overview: Geometry › Smooth vector and fiber bundles](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L470)
