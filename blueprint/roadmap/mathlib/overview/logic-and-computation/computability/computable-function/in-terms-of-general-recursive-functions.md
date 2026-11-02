---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Computable
mathlib_file: Mathlib/Computability/Partrec.lean
---

# In terms of general recursive functions

Computable functions `α → σ` between `Primcodable` types:
a function is computable if and only if it is partially recursive (as a partial function)

```lean
Computable.{u_1, u_2} {α : Type u_1} {σ : Type u_2} [Primcodable α] [Primcodable σ] (f : α → σ) :
  Prop
```

## Depends on

- [Natural number](../../../general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Computable`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Computability/Partrec.html#Computable)
- [Source of `Computable` in Mathlib/Computability/Partrec.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Computability/Partrec.lean#L239)
- [Mathlib overview: Logic and computation › Computability › computable function](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L602)
