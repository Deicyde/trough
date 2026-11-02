---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: CliffordAlgebra
mathlib_file: Mathlib/LinearAlgebra/CliffordAlgebra/Basic.lean
---

# Clifford algebra

The Clifford algebra of an `R`-module `M` equipped with a `QuadraticForm` `Q`.

```lean
CliffordAlgebra.{u_1, u_2} {R : Type u_1} [CommRing R] {M : Type u_2} [AddCommGroup M]
  [_root_.Module R M] (Q : QuadraticForm R M) : Type (max u_1 u_2)
```

## Depends on

- [Quadratic form](../../linear-algebra/bilinear-and-quadratic-forms/quadratic-form.md)
- [Ring](../rings/ring.md)
- [Tensor algebra of a commutative ring](tensor-algebra-of-a-commutative-ring.md)

## Sources

- [Mathlib documentation: `CliffordAlgebra`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/CliffordAlgebra/Basic.html#CliffordAlgebra)
- [Source of `CliffordAlgebra` in Mathlib/LinearAlgebra/CliffordAlgebra/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/CliffordAlgebra/Basic.lean#L68)
- [Mathlib overview: General algebra › Algebras over a ring](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L117)
