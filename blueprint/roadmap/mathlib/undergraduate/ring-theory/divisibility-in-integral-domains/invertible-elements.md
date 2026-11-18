# Invertible elements

`Invertible a` gives a two-sided multiplicative inverse of `a`.

```lean
Invertible.{u} {α : Type u} [Mul α] [One α] (a : α) : Type u
```

## Depends on

- [Natural number](../../../overview/general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Invertible`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Invertible/Defs.html#Invertible)
- [Source of `Invertible` in Mathlib/Algebra/Group/Invertible/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Algebra/Group/Invertible/Defs.lean#L85)
- [Mathlib undergraduate list: Ring Theory › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L142)
