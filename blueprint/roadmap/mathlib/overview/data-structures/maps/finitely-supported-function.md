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
- [Source of `Finsupp` in Mathlib/Data/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Data/Finsupp/Defs.lean#L87)
- [Mathlib overview: Data structures › Maps](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L589)
