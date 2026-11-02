---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: MLList
---

# Lazy list

A monadic lazy list, controlled by an arbitrary monad.

```lean
MLList.{u} (m : Type u → Type u) (α : Type u) : Type u
```

## Depends on

Its statement uses no other concept on these lists.

## Sources

- [Mathlib documentation: `MLList`](https://leanprover-community.github.io/mathlib4_docs/Batteries/Data/MLList/Basic.html#MLList)
- [Mathlib overview: Data structures › List-like structures](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L573)
