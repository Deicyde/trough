---
declaration: inductive
origin: cited
mathlib: true
mathlib_declaration: List
---

# List

Linked lists: ordered lists, in which each element has a reference to the next element.

Most operations on linked lists take time proportional to the length of the list, because each
element must be traversed to find the next element.

`List α` is isomorphic to `Array α`, but they are useful for different things:
* `List α` is easier for reasoning, and `Array α` is modeled as a wrapper around `List α`.
* `List α` works well as a persistent data structure, when many copies of the tail are shared. When
  the value is not shared, `Array α` will have better performance because it can do destructive
  updates.

```lean
List.{u} (α : Type u) : Type u
```

## Depends on

Its statement uses no other concept on these lists.

## Sources

- [Mathlib documentation: `List`](https://leanprover-community.github.io/mathlib4_docs/Init/Prelude.html#List)
- [Mathlib overview: Data structures › List-like structures](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L569)
