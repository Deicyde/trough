---
declaration: abbrev
origin: cited
mathlib: true
mathlib_declaration: ExteriorAlgebra
mathlib_file: Mathlib/LinearAlgebra/ExteriorAlgebra/Basic.lean
---

# Exterior algebra

The exterior algebra of an `R`-module `M`.

```lean
ExteriorAlgebra.{u1, u2} (R : Type u1) [CommRing R] (M : Type u2) [AddCommGroup M]
  [_root_.Module R M] : Type (max u1 u2)
```

## Depends on

- [Clifford algebra](clifford-algebra.md)

## Sources

- [Mathlib documentation: `ExteriorAlgebra`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/ExteriorAlgebra/Basic.html#ExteriorAlgebra)
- [Source of `ExteriorAlgebra` in Mathlib/LinearAlgebra/ExteriorAlgebra/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/ExteriorAlgebra/Basic.lean#L58)
- [Mathlib overview: General algebra › Algebras over a ring](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L116)
