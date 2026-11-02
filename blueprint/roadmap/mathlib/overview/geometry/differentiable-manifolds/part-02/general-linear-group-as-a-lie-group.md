---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Units.instLieGroupModelWithCornersSelf
mathlib_file: Mathlib/Geometry/Manifold/Instances/UnitsOfNormedAlgebra.lean
---

# General linear group as a Lie group

The units of a complete normed ring form a Lie group.

```lean
Units.instLieGroupModelWithCornersSelf.{u_1, u_2} {R : Type u_1} [NormedRing R] [CompleteSpace R]
  {n : WithTop ℕ∞} {𝕜 : Type u_2} [NontriviallyNormedField 𝕜] [NormedAlgebra 𝕜 R] :
  LieGroup (modelWithCornersSelf 𝕜 R) n Rˣ
```

## Depends on

- [Lie group](../part-01/lie-group.md)
- [Open map](../../../topology/general-topology/part-01/open-map.md)

## Proof depends on

- [$C^k$ function](../../../analysis/differentiability/c-k-function.md)
- [Absolutely convergent series in Banach spaces](../../../analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Algebra of endomorphisms of a vector space](../../../../undergraduate/linear-algebra/fundamentals/algebra-of-endomorphisms-of-a-vector-space.md)
- [Cantor’s Theorem](../../../../hundred-theorems/part-04/cantors-theorem.md)
- [Cardinal](../../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Characteristic p](../../../general-algebra/field-theory/characteristic-p.md)
- [Closed map](../../../topology/general-topology/part-01/closed-map.md)
- [Completion of an abelian topological group](../../../topology/topological-algebra/completion-of-an-abelian-topological-group.md)
- [Euclidean affine space](../../affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Existence of bases](../../../../undergraduate/linear-algebra/fundamentals/existence-of-bases.md)
- [Finite product of metric spaces](../../../../undergraduate/topology/topology-and-metric-spaces/finite-product-of-metric-spaces.md)
- [Holomorphic functions](../../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Kernel of a linear map](../../../../undergraduate/linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Limit point](../../../../undergraduate/single-variable-real-analysis/sequences-of-real-numbers/limit-point.md)
- [Pointwise convergence](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)
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

- [Mathlib documentation: `Units.instLieGroupModelWithCornersSelf`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/Instances/UnitsOfNormedAlgebra.html#Units.instLieGroupModelWithCornersSelf)
- [Source of `Units.instLieGroupModelWithCornersSelf` in Mathlib/Geometry/Manifold/Instances/UnitsOfNormedAlgebra.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/Instances/UnitsOfNormedAlgebra.lean#L63)
- [Mathlib overview: Geometry › Differentiable manifolds](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L462)
