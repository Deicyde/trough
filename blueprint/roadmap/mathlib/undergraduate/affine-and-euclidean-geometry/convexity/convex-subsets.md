---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Convex
mathlib_file: Mathlib/Analysis/Convex/Basic.lean
---

# Convex subsets

Convexity of sets.

```lean
Convex.{u_1, u_2} (𝕜 : Type u_1) {E : Type u_2} [Semiring 𝕜] [PartialOrder 𝕜] [AddCommMonoid E]
  [SMul 𝕜 E] (s : Set E) : Prop
```

## Depends on

- [Array](../../../overview/data-structures/list-like-structures/array.md)
- [Natural number](../../../overview/general-algebra/numbers/natural-number.md)
- [Set](../../../overview/data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `Convex`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Convex/Basic.html#Convex)
- [Source of `Convex` in Mathlib/Analysis/Convex/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Convex/Basic.lean#L52)
- [Mathlib undergraduate list: Affine and Euclidean Geometry › Convexity](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L255)
