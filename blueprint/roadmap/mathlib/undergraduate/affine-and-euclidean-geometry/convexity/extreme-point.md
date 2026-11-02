---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Set.extremePoints
mathlib_file: Mathlib/Analysis/Convex/Extreme.lean
---

# Extreme point

A point `x` is an extreme point of a set `A` if `x` belongs to no open segment with ends in
`A`, except for the obvious `openSegment x x`.

```lean
Set.extremePoints.{u_1, u_2} (𝕜 : Type u_1) {E : Type u_2} [Semiring 𝕜] [PartialOrder 𝕜]
  [AddCommMonoid E] [SMul 𝕜 E] (A : Set E) : Set E
```

## Depends on

- [Natural number](../../../overview/general-algebra/numbers/natural-number.md)
- [Set](../../../overview/data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `Set.extremePoints`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Convex/Extreme.html#Set.extremePoints)
- [Source of `Set.extremePoints` in Mathlib/Analysis/Convex/Extreme.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Convex/Extreme.lean#L68)
- [Mathlib undergraduate list: Affine and Euclidean Geometry › Convexity](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L257)
