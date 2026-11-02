---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Finset.ruzsa_triangle_inequality_sub_sub_sub
mathlib_file: Mathlib/Combinatorics/Additive/PluenneckeRuzsa.lean
---

# Ruzsa triangle inequality

**Ruzsa's triangle inequality**. Subtraction version.

```lean
Finset.ruzsa_triangle_inequality_sub_sub_sub.{u_1} {G : Type u_1} [DecidableEq G] [AddGroup G]
  (A B C : Finset G) : (A - C).card * B.card ≤ (A - B).card * (C - B).card
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Integer](../../general-algebra/numbers/integer.md)

## Proof depends on

- [Ordered ring](../../general-algebra/rings/ordered-ring.md)
- [Set](../../data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `Finset.ruzsa_triangle_inequality_sub_sub_sub`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Additive/PluenneckeRuzsa.html#Finset.ruzsa_triangle_inequality_sub_sub_sub)
- [Source of `Finset.ruzsa_triangle_inequality_sub_sub_sub` in Mathlib/Combinatorics/Additive/PluenneckeRuzsa.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Additive/PluenneckeRuzsa.lean#L53)
- [Mathlib overview: Combinatorics › Additive combinatorics](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L546)
