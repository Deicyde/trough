---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: ArithmeticFunction
mathlib_file: Mathlib/NumberTheory/ArithmeticFunction/Defs.lean
---

# Arithmetic functions

An arithmetic function is a function from `ℕ` that maps 0 to 0. In the literature, they are
often instead defined as functions from `ℕ+`. Multiplication on `ArithmeticFunctions` is by
Dirichlet convolution.

```lean
ArithmeticFunction.{u_1} (R : Type u_1) [Zero R] : Type u_1
```

## Depends on

- [Array](../../data-structures/list-like-structures/array.md)
- [Natural number](../numbers/natural-number.md)

## Sources

- [Mathlib documentation: `ArithmeticFunction`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/ArithmeticFunction/Defs.html#ArithmeticFunction)
- [Source of `ArithmeticFunction` in Mathlib/NumberTheory/ArithmeticFunction/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/ArithmeticFunction/Defs.lean#L48)
- [Mathlib overview: General algebra › Number theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L147)
