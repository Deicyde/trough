---
declaration: abbrev
origin: cited
mathlib: true
mathlib_declaration: GroupLieAlgebra
mathlib_file: Mathlib/Geometry/Manifold/GroupLieAlgebra.lean
---

# Lie algebra of a Lie group

The Lie algebra of a Lie group, i.e., its tangent space at the identity. We use the word
`GroupLieAlgebra` instead of `LieAlgebra` as the latter is taken as a generic class.

```lean
GroupLieAlgebra.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜] {H : Type u_2}
  [TopologicalSpace H] {E : Type u_3} [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  (I : ModelWithCorners 𝕜 E H) (G : Type u_4) [TopologicalSpace G] [ChartedSpace H G] [Group G] :
  Type u_3
```

## Depends on

- [Associative algebra over a commutative ring](../../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Completeness](../../../topology/uniform-notions/completeness.md)
- [Continuous function](../../../topology/general-topology/part-01/continuous-function.md)
- [Convex subsets](../../../../undergraduate/affine-and-euclidean-geometry/convexity/convex-subsets.md)
- [Group](../../../general-algebra/group-theory/part-01/group.md)
- [Normed vector space over a normed field](../../../analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Permutation group of a type](../../../general-algebra/group-theory/part-02/permutation-group-of-a-type.md)

## Sources

- [Mathlib documentation: `GroupLieAlgebra`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/GroupLieAlgebra.html#GroupLieAlgebra)
- [Source of `GroupLieAlgebra` in Mathlib/Geometry/Manifold/GroupLieAlgebra.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/GroupLieAlgebra.lean#L52)
- [Mathlib overview: Geometry › Differentiable manifolds](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L459)
