---
declaration: inductive
origin: cited
mathlib: true
mathlib_declaration: Int
---

# Integer

The integers.

This type is special-cased by the compiler and overridden with an efficient implementation. The
runtime has a special representation for `Int` that stores “small” signed numbers directly, while
larger numbers use a fast arbitrary-precision arithmetic library (usually
[GMP](https://gmplib.org/)). A “small number” is an integer that can be encoded with one fewer bits
than the platform's pointer size (i.e. 63 bits on 64-bit architectures and 31 bits on 32-bit
architectures).

```lean
Int : Type
```

## Depends on

- [Natural number](natural-number.md)

## Sources

- [Mathlib documentation: `Int`](https://leanprover-community.github.io/mathlib4_docs/Init/Data/Int/Basic.html#Int)
- [Mathlib overview: General algebra › Numbers](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L22)
