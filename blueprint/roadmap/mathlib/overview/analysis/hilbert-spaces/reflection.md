# Reflection

Reflection in a complete subspace of an inner product space.  The word "reflection" is
sometimes understood to mean specifically reflection in a codimension-one subspace, and sometimes
more generally to cover operations such as reflection in a point.  The definition here, of
reflection in a subspace, is a more general sense of the word that includes both those common
cases.

```lean
Submodule.reflection.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜] [NormedAddCommGroup E]
  [InnerProductSpace 𝕜 E] (K : Submodule 𝕜 E) [K.HasOrthogonalProjection] : E ≃ₗᵢ[𝕜] E
```

## Depends on

- [Orthogonal projection](orthogonal-projection.md)

## Sources

- [Mathlib documentation: `Submodule.reflection`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/Projection/Reflection.html#Submodule.reflection)
- [Source of `Submodule.reflection` in Mathlib/Analysis/InnerProductSpace/Projection/Reflection.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/InnerProductSpace/Projection/Reflection.lean#L47)
- [Mathlib overview: Analysis › Hilbert spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L299)
