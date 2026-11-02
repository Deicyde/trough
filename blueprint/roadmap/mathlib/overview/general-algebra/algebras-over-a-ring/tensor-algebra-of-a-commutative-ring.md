---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: TensorAlgebra
mathlib_file: Mathlib/LinearAlgebra/TensorAlgebra/Basic.lean
---

# Tensor algebra of a commutative ring

The tensor algebra of the module `M` over the commutative semiring `R`.

```lean
TensorAlgebra.{u_1, u_2} (R : Type u_1) [CommSemiring R] (M : Type u_2) [AddCommMonoid M]
  [_root_.Module R M] : Type (max u_1 u_2)
```

## Depends on

- [Associative algebra over a commutative ring](associative-algebra-over-a-commutative-ring.md)
- [Free algebra of a commutative ring](free-algebra-of-a-commutative-ring.md)
- [Module](../../linear-algebra/fundamentals/module.md)

## Sources

- [Mathlib documentation: `TensorAlgebra`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorAlgebra/Basic.html#TensorAlgebra)
- [Source of `TensorAlgebra` in Mathlib/LinearAlgebra/TensorAlgebra/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/TensorAlgebra/Basic.lean#L63)
- [Mathlib overview: General algebra › Algebras over a ring](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L114)
