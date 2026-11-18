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
- [Source of `ConvexCone.Salient` in Mathlib/Geometry/Convex/Cone/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Geometry/Convex/Cone/Basic.lean#L297)
- [Mathlib overview: Geometry › Convex geometry](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L489)
