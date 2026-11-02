---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: InnerProductSpace.toDual
mathlib_file: Mathlib/Analysis/InnerProductSpace/Dual.lean
---

# Fréchet-Riesz representation of the dual of a Hilbert space

**Fréchet-Riesz representation**: any `ℓ` in the dual of a Hilbert space `E` is of the form
`fun u => ⟪y, u⟫` for some `y : E`, i.e. `toDualMap` is surjective.

```lean
InnerProductSpace.toDual.{u_1, u_2} (𝕜 : Type u_1) (E : Type u_2) [RCLike 𝕜] [NormedAddCommGroup E]
  [InnerProductSpace 𝕜 E] [CompleteSpace E] : E ≃ₗᵢ⋆[𝕜] StrongDual 𝕜 E
```

## Depends on

- [Dual of a normed space](../normed-vector-spaces-banach-spaces/dual-of-a-normed-space.md)
- [Inner product space, over $R$ or $C$](inner-product-space-over-r-or-c.md)
- [Range of a linear map](../../../undergraduate/linear-algebra/fundamentals/range-of-a-linear-map.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)
- [Topological ring](../../topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `InnerProductSpace.toDual`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/Dual.html#InnerProductSpace.toDual)
- [Source of `InnerProductSpace.toDual` in Mathlib/Analysis/InnerProductSpace/Dual.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/InnerProductSpace/Dual.lean#L133)
- [Mathlib overview: Analysis › Hilbert spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L303)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Euclidean and Hermitian spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L217)
- [Mathlib undergraduate list: Topology › Hilbert spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L441)
- [1000+ theorems list: Q1357684](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1634)
- [1000+ theorems project: Q1357684](https://1000-plus.github.io/all.html?length=-1#Q1357684)
- [Wikipedia: Riesz representation theorem](https://en.wikipedia.org/wiki/Riesz_representation_theorem)
- [Wikidata: Q1357684](https://www.wikidata.org/wiki/Q1357684)
