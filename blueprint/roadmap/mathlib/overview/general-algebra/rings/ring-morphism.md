---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: RingHom
mathlib_file: Mathlib/Algebra/Ring/Hom/Defs.lean
---

# Ring morphism

Bundled semiring homomorphisms; use this for bundled ring homomorphisms too.

This extends from both `MonoidHom` and `MonoidWithZeroHom` in order to put the fields in a
sensible order, even though `MonoidWithZeroHom` already extends `MonoidHom`.

```lean
RingHom.{u_5, u_6} (α : Type u_5) (β : Type u_6) [NonAssocSemiring α] [NonAssocSemiring β] :
  Type (max u_5 u_6)
```

## Depends on

- [Array](../../data-structures/list-like-structures/array.md)
- [Group morphism](../group-theory/part-01/group-morphism.md)

## Sources

- [Mathlib documentation: `RingHom`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Hom/Defs.html#RingHom)
- [Source of `RingHom` in Mathlib/Algebra/Ring/Hom/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Ring/Hom/Defs.lean#L303)
- [Mathlib overview: General algebra › Rings](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L66)
- [Mathlib undergraduate list: Ring Theory › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L128)
