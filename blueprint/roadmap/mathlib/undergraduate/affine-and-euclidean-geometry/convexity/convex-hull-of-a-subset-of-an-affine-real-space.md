---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: convexHull
mathlib_file: Mathlib/Analysis/Convex/Hull.lean
---

# Convex hull of a subset of an affine real space

The convex hull of a set `s` is the minimal convex set that includes `s`.

```lean
convexHull.{u_1, u_2} (𝕜 : Type u_1) {E : Type u_2} [Semiring 𝕜] [PartialOrder 𝕜] [AddCommMonoid E]
  [_root_.Module 𝕜 E] : ClosureOperator (Set E)
```

## Depends on

- [Convex subsets](convex-subsets.md)
- [Module](../../../overview/linear-algebra/fundamentals/module.md)

## Sources

- [Mathlib documentation: `convexHull`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Convex/Hull.html#convexHull)
- [Source of `convexHull` in Mathlib/Analysis/Convex/Hull.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Convex/Hull.lean#L46)
- [Mathlib undergraduate list: Affine and Euclidean Geometry › Convexity](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L256)
