# Invertible elements

`Invertible a` gives a two-sided multiplicative inverse of `a`.

```lean
Invertible.{u} {α : Type u} [Mul α] [One α] (a : α) : Type u
```

## Depends on

- [Natural number](../../../overview/general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Invertible`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Invertible/Defs.html#Invertible)
- [Source of `Invertible` in Mathlib/Algebra/Group/Invertible/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Algebra/Group/Invertible/Defs.lean#L86)
- [Mathlib undergraduate list: Ring Theory › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L142)
