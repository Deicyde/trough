---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Manifold.IsImmersion
mathlib_file: Mathlib/Geometry/Manifold/Immersion.lean
---

# Smooth immersion

`f : M → N` is a `C^n` immersion if around each point `x ∈ M`,
there are charts `φ` and `ψ` of `M` and `N` around `x` and `f x`, respectively
such that in these charts, `f` looks like `u ↦ (u, 0)`.

Implicit in this definition is an abstract choice `F` of a complement of `E` in `E'`:
being an immersion includes a choice of linear isomorphism between `E × F` and `E'`, which is where
the choice of `F` enters. If you need stronger control over the complement `F`,
use `IsImmersionOfComplement` instead.

Note that our global choice of complement is a bit stronger than asking `f` to be an immersion at
each `x ∈ M` w.r.t. potentially varying complements: see `isImmersionAt` for details.

```lean
Manifold.IsImmersion.{u, u_1, u_2, u_7, u_9, u_11, u_13} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜]
  {E : Type u_2} {E'' : Type u} [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedAddCommGroup E'']
  [NormedSpace 𝕜 E''] {H : Type u_7} [TopologicalSpace H] {G : Type u_9} [TopologicalSpace G]
  (I : ModelWithCorners 𝕜 E H) (J : ModelWithCorners 𝕜 E'' G) {M : Type u_11} [TopologicalSpace M]
  [ChartedSpace H M] {N : Type u_13} [TopologicalSpace N] [ChartedSpace G N] (n : WithTop ℕ∞)
  (f : M → N) : Prop
```

## Depends on

- [Associative algebra over a commutative ring](../../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Completeness](../../../topology/uniform-notions/completeness.md)
- [Convex subsets](../../../../undergraduate/affine-and-euclidean-geometry/convexity/convex-subsets.md)
- [Field $\R$ of real numbers](../../../../undergraduate/ring-theory/field-theory/part-01/field-r-of-real-numbers.md)
- [Homeomorphisms](../../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Infinite sum](../../../topology/topological-algebra/infinite-sum.md)
- [Metric structure](../../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Norm of a continuous linear map](../../../analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Ordered ring](../../../general-algebra/rings/ordered-ring.md)
- [Permutation group of a type](../../../general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Product of vector spaces](../../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Radius of convergence](../../../../undergraduate/single-variable-complex-analysis/complex-valued-series/radius-of-convergence.md)
- [Ring structure $\Z$](../../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)

## Sources

- [Mathlib documentation: `Manifold.IsImmersion`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/Immersion.html#Manifold.IsImmersion)
- [Source of `Manifold.IsImmersion` in Mathlib/Geometry/Manifold/Immersion.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/Immersion.lean#L790)
- [Mathlib overview: Geometry › Differentiable manifolds](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L442)
