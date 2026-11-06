# Orthogonal complement

The subspace of vectors orthogonal to a given subspace, denoted `Kᗮ`.

```lean
Submodule.orthogonal.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜] [NormedAddCommGroup E]
  [InnerProductSpace 𝕜 E] (K : Submodule 𝕜 E) : Submodule 𝕜 E
```

## Depends on

- [Inner product space, over $R$ or $C$](inner-product-space-over-r-or-c.md)

## Sources

- [Mathlib documentation: `Submodule.orthogonal`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/Orthogonal.html#Submodule.orthogonal)
- [Source of `Submodule.orthogonal` in Mathlib/Analysis/InnerProductSpace/Orthogonal.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/InnerProductSpace/Orthogonal.lean#L41)
- [Mathlib overview: Analysis › Hilbert spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L300)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Euclidean and Hermitian spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L218)
