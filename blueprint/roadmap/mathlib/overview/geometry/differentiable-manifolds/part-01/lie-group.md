---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: LieGroup
mathlib_file: Mathlib/Geometry/Manifold/Algebra/LieGroup.lean
---

# Lie group

A (multiplicative) Lie group is a group and a `C^n` manifold at the same time in which
the multiplication and inverse operations are `C^n`.

```lean
LieGroup.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜] {H : Type u_2}
  [TopologicalSpace H] {E : Type u_3} [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  (I : ModelWithCorners 𝕜 E H) (n : WithTop ℕ∞) (G : Type u_4) [Group G] [TopologicalSpace G]
  [ChartedSpace H G] : Prop
```

## Depends on

- [Group](../../../general-algebra/group-theory/part-01/group.md)
- [Product of vector spaces](../../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Smooth map between manifolds](smooth-map-between-manifolds.md)
- [Smooth or analytic manifold (with boundary and corners)](smooth-or-analytic-manifold-with-boundary-and-co.md)

## Sources

- [Mathlib documentation: `LieGroup`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/Algebra/LieGroup.html#LieGroup)
- [Source of `LieGroup` in Mathlib/Geometry/Manifold/Algebra/LieGroup.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/Algebra/LieGroup.lean#L69)
- [Mathlib overview: Geometry › Differentiable manifolds](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L458)
