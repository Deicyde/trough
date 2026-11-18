# Cantor normal form

The Cantor normal form of an ordinal `o` is the list of coefficients and exponents in the
base-`b` expansion of `o`.

We special-case `CNF 0 o = CNF 1 o = [(0, o)]` for `o ≠ 0`.

`CNF b (b ^ u₁ * v₁ + b ^ u₂ * v₂) = [(u₁, v₁), (u₂, v₂)]`

```lean
Ordinal.CNF.{u_1} (b o : Ordinal.{u_1}) : List (Ordinal.{u_1} × Ordinal.{u_1})
```

## Depends on

- [List](../../../data-structures/list-like-structures/list.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)
- [Ordinal](ordinal.md)

## Sources

- [Mathlib documentation: `Ordinal.CNF`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/SetTheory/Ordinal/CantorNormalForm.html#Ordinal.CNF)
- [Source of `Ordinal.CNF` in Mathlib/SetTheory/Ordinal/CantorNormalForm.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/SetTheory/Ordinal/CantorNormalForm.lean#L63)
- [Mathlib overview: Logic and computation › Set theory › Ordinals](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L625)
