# Difference list

A difference List is a Function that, given a List, returns the original
contents of the difference List prepended to the given List.
This structure supports `O(1)` `append` and `push` operations on lists, making it
useful for append-heavy uses such as logging and pretty printing.

```lean
Batteries.DList.{u} (α : Type u) : Type u
```

## Depends on

- [List](list.md)

## Sources

- [Mathlib documentation: `Batteries.DList`](https://leanprover-community.github.io/mathlib4_docs/Batteries/Data/DList/Basic.html#Batteries.DList)
- [Mathlib overview: Data structures › List-like structures](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L572)
