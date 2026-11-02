---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: ConvexCone.Salient
mathlib_file: Mathlib/Geometry/Convex/Cone/Basic.lean
---

# Salient cone

A convex cone is salient if it doesn't include `x` and `-x` for any nonzero `x`.

```lean
ConvexCone.Salient.{u_2, u_3} {R : Type u_2} {G : Type u_3} [Semiring R] [PartialOrder R]
  [AddCommGroup G] [SMul R G] (C : ConvexCone R G) : Prop
```

## Depends on

- [Convex cone](convex-cone.md)
- [Integer](../../general-algebra/numbers/integer.md)

## Sources

- [Mathlib documentation: `ConvexCone.Salient`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Convex/Cone/Basic.html#ConvexCone.Salient)
- [Source of `ConvexCone.Salient` in Mathlib/Geometry/Convex/Cone/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Convex/Cone/Basic.lean#L297)
- [Mathlib overview: Geometry › Convex geometry](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L489)
