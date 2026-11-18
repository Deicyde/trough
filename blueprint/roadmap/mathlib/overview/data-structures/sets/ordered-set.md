# Ordered set

An `Ordset α` is a finite set of values, represented as a tree. The operations on this type
maintain that the tree is balanced and correctly stores subtree sizes at each level. The
correctness property of the tree is baked into the type, so all operations on this type are correct
by construction.

```lean
Ordset.{u_2} (α : Type u_2) [Preorder α] : Type u_2
```

## Depends on

- [Size-balanced binary search tree](../trees/size-balanced-binary-search-tree.md)

## Sources

- [Mathlib documentation: `Ordset`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Ordmap/Ordset.html#Ordset)
- [Source of `Ordset` in Mathlib/Data/Ordmap/Ordset.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Data/Ordmap/Ordset.lean#L652)
- [Mathlib overview: Data structures › Sets](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L582)
