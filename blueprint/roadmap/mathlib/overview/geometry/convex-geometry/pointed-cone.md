# Pointed cone

A pointed cone is a submodule of a module with scalars restricted to being nonnegative.

```lean
PointedCone.{u_5, u_6} (R : Type u_5) (E : Type u_6) [Semiring R] [PartialOrder R] [IsOrderedRing R]
  [AddCommMonoid E] [_root_.Module R E] : Type u_6
```

## Depends on

- [Module](../../linear-algebra/fundamentals/module.md)
- [Ordered ring](../../general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `PointedCone`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Convex/Cone/Pointed.html#PointedCone)
- [Source of `PointedCone` in Mathlib/Geometry/Convex/Cone/Pointed.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Convex/Cone/Pointed.lean#L32)
- [Mathlib overview: Geometry › Convex geometry](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L491)
