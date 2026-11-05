---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: AlgebraicGeometry.LocallyRingedSpace
mathlib_file: Mathlib/Geometry/RingedSpace/LocallyRingedSpace.lean
---

# Locally ringed space

A `LocallyRingedSpace` is a topological space equipped with a sheaf of commutative rings
such that all the stalks are local rings.

A morphism of locally ringed spaces is a morphism of ringed spaces
such that the morphisms induced on stalks are local ring homomorphisms.

```lean
AlgebraicGeometry.LocallyRingedSpace.{u} : Type (u + 1)
```

## Depends on

- [Local ring](../../general-algebra/rings/local-ring.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)
- [Ring morphism](../../general-algebra/rings/ring-morphism.md)
- [Sheafed space](../../general-algebra/category-theory/sheafed-space.md)

## Sources

- [Mathlib documentation: `AlgebraicGeometry.LocallyRingedSpace`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/RingedSpace/LocallyRingedSpace.html#AlgebraicGeometry.LocallyRingedSpace)
- [Source of `AlgebraicGeometry.LocallyRingedSpace` in Mathlib/Geometry/RingedSpace/LocallyRingedSpace.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/RingedSpace/LocallyRingedSpace.lean#L40)
- [Mathlib overview: Geometry › Algebraic geometry](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L483)
