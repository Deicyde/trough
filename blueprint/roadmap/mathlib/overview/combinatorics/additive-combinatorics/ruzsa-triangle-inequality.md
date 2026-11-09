# Ruzsa triangle inequality

**Ruzsa's triangle inequality**. Subtraction version.

```lean
Finset.ruzsa_triangle_inequality_sub_sub_sub.{u_1} {G : Type u_1} [DecidableEq G] [AddGroup G]
  (A B C : Finset G) : (A - C).card * B.card ≤ (A - B).card * (C - B).card
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Integer](../../general-algebra/numbers/integer.md)

## Sources

- [Mathlib documentation: `Finset.ruzsa_triangle_inequality_sub_sub_sub`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Additive/PluenneckeRuzsa.html#Finset.ruzsa_triangle_inequality_sub_sub_sub)
- [Source of `Finset.ruzsa_triangle_inequality_sub_sub_sub` in Mathlib/Combinatorics/Additive/PluenneckeRuzsa.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Combinatorics/Additive/PluenneckeRuzsa.lean#L53)
- [Mathlib overview: Combinatorics › Additive combinatorics](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L546)
