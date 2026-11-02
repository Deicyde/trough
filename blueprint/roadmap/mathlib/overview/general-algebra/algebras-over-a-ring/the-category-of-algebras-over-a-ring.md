---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: AlgCat
mathlib_file: Mathlib/Algebra/Category/AlgCat/Basic.lean
---

# The category of algebras over a ring

The category of R-algebras and their morphisms.

```lean
AlgCat.{v, u} (R : Type u) [CommRing R] : Type (max u (v + 1))
```

## Depends on

- [Associative algebra over a commutative ring](associative-algebra-over-a-commutative-ring.md)
- [Ring](../rings/ring.md)

## Sources

- [Mathlib documentation: `AlgCat`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/AlgCat/Basic.html#AlgCat)
- [Source of `AlgCat` in Mathlib/Algebra/Category/AlgCat/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Category/AlgCat/Basic.lean#L28)
- [Mathlib overview: General algebra › Algebras over a ring](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L111)
