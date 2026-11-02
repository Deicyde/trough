---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: LieAlgebra
mathlib_file: Mathlib/Algebra/Lie/Basic.lean
---

# Lie algebra

A Lie algebra is a module with compatible product, known as the bracket, satisfying the Jacobi
identity. Forgetting the scalar multiplication, every Lie algebra is a Lie ring.

```lean
LieAlgebra.{u, v} (R : Type u) (L : Type v) [CommRing R] [LieRing L] : Type (max u v)
```

## Depends on

- [Module](../../linear-algebra/fundamentals/module.md)
- [Ring](../rings/ring.md)

## Sources

- [Mathlib documentation: `LieAlgebra`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/Basic.html#LieAlgebra)
- [Source of `LieAlgebra` in Mathlib/Algebra/Lie/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Lie/Basic.lean#L71)
- [Mathlib overview: General algebra › Algebras over a ring](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L115)
