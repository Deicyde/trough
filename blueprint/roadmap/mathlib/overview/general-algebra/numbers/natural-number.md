---
declaration: inductive
origin: cited
mathlib: true
mathlib_declaration: Nat
mathlib_file: Init/Prelude.lean
---

# Natural number

The natural numbers, starting at zero.

This type is special-cased by both the kernel and the compiler, and overridden with an efficient
implementation. Both use a fast arbitrary-precision arithmetic library (usually
[GMP](https://gmplib.org/)); at runtime, `Nat` values that are sufficiently small are unboxed.

```lean
Nat : Type
```

Automatically generated when defining the natural numbers.

## Depends on

Its statement uses no other concept on these lists.

## Sources

- [Mathlib documentation: `Nat`](https://leanprover-community.github.io/mathlib4_docs/Init/Prelude.html#Nat)
- [Mathlib overview: General algebra › Numbers](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L21)
- [Mathlib undergraduate list: Single Variable Real Analysis › Sequences of real numbers](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L286)
- [Freek Wiedijk's 100 theorems, no. 74](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L374)
