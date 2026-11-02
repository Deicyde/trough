---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Primrec
mathlib_file: Mathlib/Computability/Primrec/Basic.lean
---

# Primitive recursive function

`Primrec f` means `f` is primitive recursive (after
encoding its input and output as natural numbers).

```lean
Primrec.{u_1, u_2} {α : Type u_1} {β : Type u_2} [Primcodable α] [Primcodable β] (f : α → β) : Prop
```

## Depends on

- [Natural number](../../general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Primrec`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Computability/Primrec/Basic.html#Primrec)
- [Source of `Primrec` in Mathlib/Computability/Primrec/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Computability/Primrec/Basic.lean#L172)
- [Mathlib overview: Logic and computation › Computability](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L604)
