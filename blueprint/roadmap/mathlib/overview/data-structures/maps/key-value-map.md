# Key-value map

`AList β` is a key-value map stored as a `List` (i.e. a linked list).
It is a wrapper around certain `List` functions with the added constraint
that the list have unique keys.

```lean
AList.{u, v} {α : Type u} (β : α → Type v) : Type (max u v)
```

## Depends on

- [List](../list-like-structures/list.md)

## Sources

- [Mathlib documentation: `AList`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/List/AList.html#AList)
- [Source of `AList` in Mathlib/Data/List/AList.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Data/List/AList.lean#L45)
- [Mathlib overview: Data structures › Maps](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L585)
