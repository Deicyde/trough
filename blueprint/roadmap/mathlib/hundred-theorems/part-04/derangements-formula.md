# Derangements Formula

Mathlib records this with 2 declarations.

`card_derangements_eq_numDerangements`.

```lean
card_derangements_eq_numDerangements.{u_2} (α : Type u_2) [Fintype α] [DecidableEq α] :
  Fintype.card ↑(derangements α) = numDerangements (Fintype.card α)
```

`numDerangements_sum`.

```lean
numDerangements_sum (n : ℕ) :
  ↑(numDerangements n) = ∑ k ∈ Finset.range (n + 1), (-1) ^ k * ↑((k + 1).ascFactorial (n - k))
```

## Depends on

- [Finite set](../../overview/data-structures/sets/finite-set.md)
- [Integer](../../overview/general-algebra/numbers/integer.md)
- [Permutation group of a type](../../overview/general-algebra/group-theory/part-02/permutation-group-of-a-type.md)

## Proof depends on

- [Fixed points](../../overview/dynamics/general-theory/fixed-points.md)
- [Group morphism](../../overview/general-algebra/group-theory/part-01/group-morphism.md)
- [Ring structure $\Z$](../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)

## Sources

- [Mathlib documentation: `card_derangements_eq_numDerangements`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Derangements/Finite.html#card_derangements_eq_numDerangements)
- [Source of `card_derangements_eq_numDerangements` in Mathlib/Combinatorics/Derangements/Finite.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Derangements/Finite.lean#L102)
- [Mathlib documentation: `numDerangements_sum`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Derangements/Finite.html#numDerangements_sum)
- [Source of `numDerangements_sum` in Mathlib/Combinatorics/Derangements/Finite.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Derangements/Finite.lean#L107)
- [Freek Wiedijk's 100 theorems, no. 88](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L451)
