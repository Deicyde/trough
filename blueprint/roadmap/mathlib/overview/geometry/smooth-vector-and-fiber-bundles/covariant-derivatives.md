---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: CovariantDerivative
mathlib_file: Mathlib/Geometry/Manifold/VectorBundle/CovariantDerivative/Basic.lean
---

# Covariant derivatives

Bundled global covariant derivative on a vector bundle.
Caution, the argument order is nonstandard: `cov σ x (X x)` corresponds to `∇_X σ x` on paper.

```lean
CovariantDerivative.{u_1, u_2, u_3, u_4, u_5, u_6} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜]
  {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {H : Type u_3} [TopologicalSpace H]
  (I : ModelWithCorners 𝕜 E H) {M : Type u_4} [TopologicalSpace M] [ChartedSpace H M] (F : Type u_5)
  [NormedAddCommGroup F] [NormedSpace 𝕜 F] (V : M → Type u_6)
  [TopologicalSpace (Bundle.TotalSpace F V)] [(x : M) → AddCommGroup (V x)]
  [(x : M) → _root_.Module 𝕜 (V x)] [(x : M) → TopologicalSpace (V x)]
  [∀ (x : M), IsTopologicalAddGroup (V x)] [∀ (x : M), ContinuousSMul 𝕜 (V x)] [FiberBundle F V] :
  Type (max (max u_2 u_4) u_6)
```

## Depends on

- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Completeness](../../topology/uniform-notions/completeness.md)
- [Continuous linear map](../../topology/topological-algebra/continuous-linear-map.md)
- [Convex subsets](../../../undergraduate/affine-and-euclidean-geometry/convexity/convex-subsets.md)
- [Normed vector space over a normed field](../../analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Permutation group of a type](../../general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Topological fiber bundle](../../topology/general-topology/part-01/topological-fiber-bundle.md)
- [Topological module](../../topology/topological-algebra/topological-module.md)

## Sources

- [Mathlib documentation: `CovariantDerivative`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/VectorBundle/CovariantDerivative/Basic.html#CovariantDerivative)
- [Source of `CovariantDerivative` in Mathlib/Geometry/Manifold/VectorBundle/CovariantDerivative/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/VectorBundle/CovariantDerivative/Basic.lean#L361)
- [Mathlib overview: Geometry › Smooth vector and fiber bundles](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L473)
