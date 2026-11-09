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
- [Source of `Primrec` in Mathlib/Computability/Primrec/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Computability/Primrec/Basic.lean#L172)
- [Mathlib overview: Logic and computation › Computability](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L604)
