---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: EuclideanSpace.instIsManifoldSphere
mathlib_file: Mathlib/Geometry/Manifold/Instances/Sphere.lean
---

# Sphere

The unit sphere in an `n + 1`-dimensional inner product space `E` is an analytic manifold,
modelled on the Euclidean space of dimension `n`.

```lean
EuclideanSpace.instIsManifoldSphere.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] {n : ℕ} [Fact (Module.finrank ℝ E = n + 1)] :
  IsManifold (modelWithCornersSelf ℝ (EuclideanSpace ℝ (Fin n))) ⊤ ↑(Metric.sphere 0 1)
```

## Depends on

- [Cardinal](../../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Completeness of R](../../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Existence of orthonormal basis](../../../linear-algebra/finite-dimensional-inner-product-spaces-see-also/existence-of-orthonormal-basis.md)
- [Finite-dimensionality](../../../linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Linear independence](../../../../undergraduate/linear-algebra/fundamentals/linear-independence.md)
- [Norms $\lVert\cdot\rVert_p$ on $\R^n$ and $\C^n$](../../../../undergraduate/topology/normed-vector-spaces-on-and/norms-p-on-n-and-n.md)
- [Orthogonal projection](../../../analysis/hilbert-spaces/orthogonal-projection.md)
- [Smooth or analytic manifold (with boundary and corners)](smooth-or-analytic-manifold-with-boundary-and-co.md)
- [Topological ring](../../../topology/topological-algebra/topological-ring.md)

## Proof depends on

- [$C^k$ function](../../../analysis/differentiability/c-k-function.md)
- [Absolutely convergent series in Banach spaces](../../../analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Algebra of endomorphisms of a vector space](../../../../undergraduate/linear-algebra/fundamentals/algebra-of-endomorphisms-of-a-vector-space.md)
- [Arithmetic Mean/Geometric Mean](../../../../hundred-theorems/part-02/arithmetic-mean-geometric-mean.md)
- [Cauchy-Schwarz inequality](../../../analysis/hilbert-spaces/cauchy-schwarz-inequality.md)
- [Characteristic p](../../../general-algebra/field-theory/characteristic-p.md)
- [Closed map](../../../topology/general-topology/part-01/closed-map.md)
- [Complementary subspaces](../../../../undergraduate/linear-algebra/fundamentals/complementary-subspaces.md)
- [Completion of an abelian topological group](../../../topology/topological-algebra/completion-of-an-abelian-topological-group.md)
- [Dual of a normed space](../../../analysis/normed-vector-spaces-banach-spaces/dual-of-a-normed-space.md)
- [Euclidean affine space](../../affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Heine-Borel theorem (finite-dimensional normed spaces are proper)](../../../analysis/normed-vector-spaces-banach-spaces/heine-borel-theorem-finite-dimensional-normed-sp.md)
- [Hilbert projection theorem](../../../../undergraduate/topology/hilbert-spaces/hilbert-projection-theorem.md)
- [Holomorphic functions](../../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Limit point](../../../../undergraduate/single-variable-real-analysis/sequences-of-real-numbers/limit-point.md)
- [Pointwise convergence](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)
- [Quotient space](../../../linear-algebra/fundamentals/quotient-space.md)
- [Self-adjoint operator](../../../analysis/hilbert-spaces/self-adjoint-operator.md)
- [Sequential space](../../../topology/general-topology/part-01/sequential-space.md)
- [Sum of a Geometric Series](../../../../hundred-theorems/part-04/sum-of-a-geometric-series.md)
- [The Number of Subsets of a Set](../../../../hundred-theorems/part-03/the-number-of-subsets-of-a-set.md)

## Sources

- [Mathlib documentation: `EuclideanSpace.instIsManifoldSphere`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/Instances/Sphere.html#EuclideanSpace.instIsManifoldSphere)
- [Source of `EuclideanSpace.instIsManifoldSphere` in Mathlib/Geometry/Manifold/Instances/Sphere.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/Instances/Sphere.lean#L384)
- [Mathlib overview: Geometry › Differentiable manifolds](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L460)
