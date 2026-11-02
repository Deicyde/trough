---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Equiv.Perm.truncSwapFactors
mathlib_file: Mathlib/GroupTheory/Perm/Sign.lean
---

# Decomposition into transpositions

This computably represents the fact that any permutation can be represented as the product of
a list of transpositions.

```lean
Equiv.Perm.truncSwapFactors.{u} {α : Type u} [DecidableEq α] [Fintype α] (f : Equiv.Perm α) :
  Trunc { l // l.prod = f ∧ ∀ g ∈ l, g.IsSwap }
```

## Depends on

- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Group](../../../overview/general-algebra/group-theory/part-01/group.md)
- [Permutation group of a type](../../../overview/general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Set](../../../overview/data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `Equiv.Perm.truncSwapFactors`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Sign.html#Equiv.Perm.truncSwapFactors)
- [Source of `Equiv.Perm.truncSwapFactors` in Mathlib/GroupTheory/Perm/Sign.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/Perm/Sign.lean#L93)
- [Mathlib undergraduate list: Group Theory › Permutation group](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L100)
