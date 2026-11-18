# VC dimension

The Vapnik-Chervonenkis dimension of a set family is the maximal size of a set it shatters.

```lean
Finset.vcDim.{u_1} {α : Type u_1} [DecidableEq α] (𝒜 : Finset (Finset α)) : ℕ
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Finset.vcDim`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SetFamily/Shatter.html#Finset.vcDim)
- [Source of `Finset.vcDim` in Mathlib/Combinatorics/SetFamily/Shatter.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Combinatorics/SetFamily/Shatter.lean#L185)
- [Mathlib overview: Combinatorics › Set families](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L519)
