# Isometric inclusion in double dual

The inclusion of a normed space in its double strong dual is an isometry onto its image.

```lean
NormedSpace.inclusionInDoubleDualLi.{u, v} (𝕜 : Type v) [RCLike 𝕜] {E : Type u}
  [SeminormedAddCommGroup E] [NormedSpace 𝕜 E] : E →ₗᵢ[𝕜] StrongDual 𝕜 (StrongDual 𝕜 E)
```

## Depends on

- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Completeness](../../topology/uniform-notions/completeness.md)
- [Dual of a normed space](dual-of-a-normed-space.md)
- [Finite set](../../data-structures/sets/finite-set.md)
- [Normed vector space over a normed field](normed-vector-space-over-a-normed-field.md)
- [Topological module](../../topology/topological-algebra/topological-module.md)
- [Topological ring](../../topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `NormedSpace.inclusionInDoubleDualLi`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Module/DoubleDual.html#NormedSpace.inclusionInDoubleDualLi)
- [Source of `NormedSpace.inclusionInDoubleDualLi` in Mathlib/Analysis/Normed/Module/DoubleDual.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Normed/Module/DoubleDual.lean#L86)
- [Mathlib overview: Analysis › Normed vector spaces/Banach spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L290)
