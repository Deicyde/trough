# Finitely supported function

`Finsupp α M`, denoted `α →₀ M`, is the type of functions `f : α → M` such that
`f x = 0` for all but finitely many `x`.

```lean
Finsupp.{u_8, u_9} (α : Type u_8) (M : Type u_9) [Zero M] : Type (max u_8 u_9)
```

## Depends on

- [Finite set](../sets/finite-set.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Finsupp`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finsupp/Defs.html#Finsupp)
- [Source of `Finsupp` in Mathlib/Data/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Data/Finsupp/Defs.lean#L86)
- [Mathlib overview: Data structures › Maps](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L589)
