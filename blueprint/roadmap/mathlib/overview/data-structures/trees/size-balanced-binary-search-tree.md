# Size-balanced binary search tree

An `Ordnode α` is a finite set of values, represented as a tree.
The operations on this type maintain that the tree is balanced
and correctly stores subtree sizes at each level.

This is a copy of `BinaryTree` with a cached `size` field for `BinaryTree.numNodes`.

```lean
Ordnode.{u} (α : Type u) : Type u
```

## Depends on

- [Natural number](../../general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Ordnode`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Ordmap/Ordnode.html#Ordnode)
- [Source of `Ordnode` in Mathlib/Data/Ordmap/Ordnode.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Data/Ordmap/Ordnode.lean#L70)
- [Mathlib overview: Data structures › Trees](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L596)
