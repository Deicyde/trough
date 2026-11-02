---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: PointedCone.dual
mathlib_file: Mathlib/Geometry/Convex/Cone/Dual.lean
---

# Dual cone

The dual cone of a set `s` with respect to a bilinear pairing `p` is the cone consisting of all
points `y` such that for all points `x ∈ s` we have `0 ≤ p x y`.

```lean
PointedCone.dual.{u_1, u_2, u_3} {R : Type u_1} [CommSemiring R] [PartialOrder R] [IsOrderedRing R]
  {M : Type u_2} [AddCommMonoid M] [_root_.Module R M] {N : Type u_3} [AddCommMonoid N]
  [_root_.Module R N] (p : M →ₗ[R] N →ₗ[R] R) (s : Set M) : PointedCone R N
```

## Depends on

- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Linear map](../../linear-algebra/fundamentals/linear-map.md)
- [Pointed cone](pointed-cone.md)

## Sources

- [Mathlib documentation: `PointedCone.dual`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Convex/Cone/Dual.html#PointedCone.dual)
- [Source of `PointedCone.dual` in Mathlib/Geometry/Convex/Cone/Dual.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Convex/Cone/Dual.lean#L48)
- [Mathlib overview: Geometry › Convex geometry](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L492)
