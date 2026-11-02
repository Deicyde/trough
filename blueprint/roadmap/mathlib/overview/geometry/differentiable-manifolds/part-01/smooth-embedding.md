---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: Manifold.IsSmoothEmbedding
mathlib_file: Mathlib/Geometry/Manifold/SmoothEmbedding.lean
---

# Smooth embedding

A `C^n` map `f : M → M'` is a smooth `C^n` embedding if it is a topological embedding
and a `C^n` immersion.

```lean
Manifold.IsSmoothEmbedding.{u_1, u_2, u_4, u_6, u_8, u_10, u_12} {𝕜 : Type u_1}
  [NontriviallyNormedField 𝕜] {E₁ : Type u_2} {E₃ : Type u_4} [NormedAddCommGroup E₁]
  [NormedSpace 𝕜 E₁] [NormedAddCommGroup E₃] [NormedSpace 𝕜 E₃] {H : Type u_6} {G : Type u_8}
  [TopologicalSpace H] [TopologicalSpace G] (I : ModelWithCorners 𝕜 E₁ H)
  (J : ModelWithCorners 𝕜 E₃ G) {M : Type u_10} {N : Type u_12} [TopologicalSpace M]
  [ChartedSpace H M] [TopologicalSpace N] [ChartedSpace G N] (n : WithTop ℕ∞) (f : M → N) : Prop
```

## Depends on

- [Smooth immersion](smooth-immersion.md)

## Sources

- [Mathlib documentation: `Manifold.IsSmoothEmbedding`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/SmoothEmbedding.html#Manifold.IsSmoothEmbedding)
- [Source of `Manifold.IsSmoothEmbedding` in Mathlib/Geometry/Manifold/SmoothEmbedding.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/SmoothEmbedding.lean#L67)
- [Mathlib overview: Geometry › Differentiable manifolds](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L443)
