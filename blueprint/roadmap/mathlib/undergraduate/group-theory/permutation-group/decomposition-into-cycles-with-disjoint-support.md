---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Equiv.Perm.truncCycleFactors
mathlib_file: Mathlib/GroupTheory/Perm/Cycle/Factors.lean
---

# Decomposition into cycles with disjoint support

Factors a permutation `f` into a list of disjoint cyclic permutations that multiply to `f`,
without a linear order.

```lean
Equiv.Perm.truncCycleFactors.{u_1} {α : Type u_1} [DecidableEq α] [Fintype α] (f : Equiv.Perm α) :
  Trunc { l // l.prod = f ∧ (∀ g ∈ l, g.IsCycle) ∧ List.Pairwise Equiv.Perm.Disjoint l }
```

## Depends on

- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Group morphism](../../../overview/general-algebra/group-theory/part-01/group-morphism.md)
- [Permutation group of a type](../../../overview/general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Set](../../../overview/data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `Equiv.Perm.truncCycleFactors`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Factors.html#Equiv.Perm.truncCycleFactors)
- [Source of `Equiv.Perm.truncCycleFactors` in Mathlib/GroupTheory/Perm/Cycle/Factors.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/Perm/Cycle/Factors.lean#L464)
- [Mathlib undergraduate list: Group Theory › Permutation group](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L101)
