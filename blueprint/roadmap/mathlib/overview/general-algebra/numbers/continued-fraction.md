---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: ContFract
mathlib_file: Mathlib/Algebra/ContinuedFractions/Basic.lean
---

# Continued fraction

A *(regular) continued fraction* ((r)cf) is a simple continued fraction (scf) whose partial
denominators are all positive. It is the subtype of scfs that satisfy `SimpContFract.IsContFract`.

```lean
ContFract.{u_1} (α : Type u_1) [One α] [Zero α] [LT α] : Type u_1
```

## Depends on

- [Sequence](../../data-structures/list-like-structures/sequence.md)

## Sources

- [Mathlib documentation: `ContFract`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/ContinuedFractions/Basic.html#ContFract)
- [Source of `ContFract` in Mathlib/Algebra/ContinuedFractions/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/ContinuedFractions/Basic.lean#L227)
- [Mathlib overview: General algebra › Numbers](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L24)
