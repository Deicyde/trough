---
catalog: module
lean: Std.HashSet.anyM, Std.HashSet.allM
statement: formalized
proof: formalized
---

# HashSet

`Batteries.Lean.HashSet`, in [Batteries/Lean/HashSet.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/HashSet.lean), by Jannis Limperg.

`Std.HashSet.anyM` (definition, [line 20](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/HashSet.lean#L20))

> `O(n)`. Returns `true` if `f` returns `true` for any element of the set.

```lean
def anyM [Monad m] (s : HashSet α) (f : α → m Bool) : m Bool
```

`Std.HashSet.allM` (definition, [line 30](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/HashSet.lean#L30))

> `O(n)`. Returns `true` if `f` returns `true` for all elements of the set.

```lean
def allM [Monad m] (s : HashSet α) (f : α → m Bool) : m Bool
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Lean/HashSet.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/HashSet.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Lean.HashSet.json)
