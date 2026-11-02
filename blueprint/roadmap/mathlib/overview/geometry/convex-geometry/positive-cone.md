---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: ConvexCone.positive
mathlib_file: Mathlib/Geometry/Convex/Cone/Basic.lean
---

# Positive cone

The positive cone is the convex cone formed by the set of nonnegative elements in an ordered
module.

```lean
ConvexCone.positive.{u_2, u_4} (R : Type u_2) (M : Type u_4) [Semiring R] [PartialOrder R]
  [AddCommMonoid M] [PartialOrder M] [IsOrderedAddMonoid M] [_root_.Module R M] [PosSMulMono R M] :
  ConvexCone R M
```

## Depends on

- [Convex cone](convex-cone.md)
- [Module](../../linear-algebra/fundamentals/module.md)

## Sources

- [Mathlib documentation: `ConvexCone.positive`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Convex/Cone/Basic.html#ConvexCone.positive)
- [Source of `ConvexCone.positive` in Mathlib/Geometry/Convex/Cone/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Convex/Cone/Basic.lean#L557)
- [Mathlib overview: Geometry › Convex geometry](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L490)
