---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Ordset
mathlib_file: Mathlib/Data/Ordmap/Ordset.lean
---

# Ordered set

An `Ordset α` is a finite set of values, represented as a tree. The operations on this type
maintain that the tree is balanced and correctly stores subtree sizes at each level. The
correctness property of the tree is baked into the type, so all operations on this type are correct
by construction.

```lean
Ordset.{u_2} (α : Type u_2) [Preorder α] : Type u_2
```

## Depends on

- [Array](../list-like-structures/array.md)
- [Size-balanced binary search tree](../trees/size-balanced-binary-search-tree.md)

## Sources

- [Mathlib documentation: `Ordset`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Ordmap/Ordset.html#Ordset)
- [Source of `Ordset` in Mathlib/Data/Ordmap/Ordset.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Data/Ordmap/Ordset.lean#L652)
- [Mathlib overview: Data structures › Sets](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L582)
