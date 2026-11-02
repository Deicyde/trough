---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Equiv.Perm.sign
mathlib_file: Mathlib/GroupTheory/Perm/Sign.lean
---

# Signature

`SignType.sign` of a permutation returns the signature or parity of a permutation, `1` for even
permutations, `-1` for odd permutations. It is the unique surjective group homomorphism from
`Perm α` to the group with two elements.

```lean
Equiv.Perm.sign.{u} {α : Type u} [DecidableEq α] [Fintype α] : Equiv.Perm α →* ℤˣ
```

## Depends on

- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Group](../../../overview/general-algebra/group-theory/part-01/group.md)
- [Group morphism](../../../overview/general-algebra/group-theory/part-01/group-morphism.md)
- [Permutation group of a type](../../../overview/general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Ring structure $\Z$](../../ring-theory/fundamentals/ring-structure.md)
- [Set](../../../overview/data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `Equiv.Perm.sign`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Sign.html#Equiv.Perm.sign)
- [Source of `Equiv.Perm.sign` in Mathlib/GroupTheory/Perm/Sign.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/Perm/Sign.lean#L355)
- [Mathlib undergraduate list: Group Theory › Permutation group](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L102)
