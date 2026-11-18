# Additive energy

The additive energy `E[s, t]` of two finsets `s` and `t` in a group is the number of quadruples
`(a₁, a₂, b₁, b₂) ∈ s × s × t × t` such that `a₁ + b₁ = a₂ + b₂`.

The notation `E[s, t]` is available in scope `Combinatorics.Additive`.

```lean
Finset.addEnergy.{u_1} {α : Type u_1} [DecidableEq α] [Add α] (s t : Finset α) : ℕ
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Finset.addEnergy`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Additive/Energy.html#Finset.addEnergy)
- [Source of `Finset.addEnergy` in Mathlib/Combinatorics/Additive/Energy.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Combinatorics/Additive/Energy.lean#L51)
- [Mathlib overview: Combinatorics › Additive combinatorics](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L552)
