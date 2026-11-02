---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: IsManifold.disjointUnion
mathlib_file: Mathlib/Geometry/Manifold/IsManifold/Basic.lean
---

# Disjoint union of manifolds

The disjoint union of two `C^n` manifolds modelled on `(E, H)`
is a `C^n` manifold modelled on `(E, H)`.

```lean
IsManifold.disjointUnion.{u_1, u_2, u_3, u_4, u_5} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜]
  {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {H : Type u_3} [TopologicalSpace H]
  {I : ModelWithCorners 𝕜 E H} {n : WithTop ℕ∞} {M : Type u_4} [TopologicalSpace M]
  [ChartedSpace H M] {M' : Type u_5} [TopologicalSpace M'] [ChartedSpace H M']
  [hM : IsManifold I n M] [hM' : IsManifold I n M'] : IsManifold I n (M ⊕ M')
```

## Depends on

- [Smooth or analytic manifold (with boundary and corners)](smooth-or-analytic-manifold-with-boundary-and-co.md)

## Proof depends on

- [$C^k$ function](../../../analysis/differentiability/c-k-function.md)
- [Absolutely convergent series in Banach spaces](../../../analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Cantor’s Theorem](../../../../hundred-theorems/part-04/cantors-theorem.md)
- [Cardinal](../../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Characteristic p](../../../general-algebra/field-theory/characteristic-p.md)
- [Closed map](../../../topology/general-topology/part-01/closed-map.md)
- [Completion of an abelian topological group](../../../topology/topological-algebra/completion-of-an-abelian-topological-group.md)
- [Existence of bases](../../../../undergraduate/linear-algebra/fundamentals/existence-of-bases.md)
- [Finite product of metric spaces](../../../../undergraduate/topology/topology-and-metric-spaces/finite-product-of-metric-spaces.md)
- [Holomorphic functions](../../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Kernel of a linear map](../../../../undergraduate/linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Limit point](../../../../undergraduate/single-variable-real-analysis/sequences-of-real-numbers/limit-point.md)
- [Open map](../../../topology/general-topology/part-01/open-map.md)
- [Pointwise convergence](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)
- [Product of vector spaces](../../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Schroeder-Bernstein Theorem](../../../../hundred-theorems/part-02/schroeder-bernstein-theorem.md)
- [Sequential space](../../../topology/general-topology/part-01/sequential-space.md)
- [Squeeze theorem](../../../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [Sum of a Geometric Series](../../../../hundred-theorems/part-04/sum-of-a-geometric-series.md)
- [Sum of subspaces](../../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)
- [The Number of Subsets of a Set](../../../../hundred-theorems/part-03/the-number-of-subsets-of-a-set.md)
- [Topological module](../../../topology/topological-algebra/topological-module.md)
- [Topology of a metric space](../../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../../../analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Uniformly continuous function](../../../topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `IsManifold.disjointUnion`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/IsManifold/Basic.html#IsManifold.disjointUnion)
- [Source of `IsManifold.disjointUnion` in Mathlib/Geometry/Manifold/IsManifold/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/IsManifold/Basic.lean#L959)
- [Mathlib overview: Geometry › Differentiable manifolds](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L445)
