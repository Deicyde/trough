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
- [Inner product space, over $R$ or $C$](../../../analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Linear independence](../../../../undergraduate/linear-algebra/fundamentals/linear-independence.md)
- [Norms $\lVert\cdot\rVert_p$ on $\R^n$ and $\C^n$](../../../../undergraduate/topology/normed-vector-spaces-on-r-and-c/norms-lvert-cdot-rvert-p-on-r-n-and-c-n.md)
- [Smooth or analytic manifold (with boundary and corners)](smooth-or-analytic-manifold-with-boundary-and-co.md)

## Proof depends on

- [$C^k$ function](../../../analysis/differentiability/c-k-function.md)
- [Characteristic zero](../../../general-algebra/field-theory/characteristic-zero.md)
- [Compactness in terms of filters](../../../topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Existence of orthonormal basis](../../../linear-algebra/finite-dimensional-inner-product-spaces-see-also/existence-of-orthonormal-basis.md)
- [Finite-dimensionality](../../../linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Ordered ring](../../../general-algebra/rings/ordered-ring.md)
- [Orthogonal projection](../../../analysis/hilbert-spaces/orthogonal-projection.md)
- [Topological ring](../../../topology/topological-algebra/topological-ring.md)
- [Topology on a normed vector space](../../../analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)

## Sources

- [Mathlib documentation: `EuclideanSpace.instIsManifoldSphere`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/Instances/Sphere.html#EuclideanSpace.instIsManifoldSphere)
- [Source of `EuclideanSpace.instIsManifoldSphere` in Mathlib/Geometry/Manifold/Instances/Sphere.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/Instances/Sphere.lean#L384)
- [Mathlib overview: Geometry › Differentiable manifolds](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L460)
