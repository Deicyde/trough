---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: VectorField.mlieBracket
mathlib_file: Mathlib/Geometry/Manifold/VectorField/LieBracket.lean
---

# Lie bracket of vector field

The Lie bracket of two vector fields in a manifold.

```lean
VectorField.mlieBracket.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜]
  {H : Type u_2} [TopologicalSpace H] {E : Type u_3} [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  (I : ModelWithCorners 𝕜 E H) {M : Type u_4} [TopologicalSpace M] [ChartedSpace H M]
  (V W : (x : M) → TangentSpace I x) (x₀ : M) : TangentSpace I x₀
```

## Depends on

- [Homeomorphisms](../../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Pullback of vector fields](pullback-of-vector-fields.md)

## Sources

- [Mathlib documentation: `VectorField.mlieBracket`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/VectorField/LieBracket.html#VectorField.mlieBracket)
- [Source of `VectorField.mlieBracket` in Mathlib/Geometry/Manifold/VectorField/LieBracket.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/VectorField/LieBracket.lean#L69)
- [Mathlib overview: Geometry › Differentiable manifolds](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L451)
