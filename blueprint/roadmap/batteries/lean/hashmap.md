---
catalog: module
lean: Std.HashMap.mergeWithM, Std.HashMap.mergeWith
statement: formalized
proof: formalized
---

# HashMap

`Batteries.Lean.HashMap`, in [Batteries/Lean/HashMap.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/HashMap.lean), by Jannis Limperg.

`Std.HashMap.mergeWithM` (definition, [line 20](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/HashMap.lean#L20))

> `O(|other|)` amortized. Merge two `HashMap`s.
> The values of keys which appear in both maps are combined using the monadic function `f`.

```lean
def mergeWithM {m α β} [BEq α] [Hashable α] [Monad m] (f : α → β → β → m β)
    (self other : HashMap α β) : m (HashMap α β)
```

`Std.HashMap.mergeWith` (definition, [line 32](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/HashMap.lean#L32))

> `O(|other|)` amortized. Merge two `HashMap`s.
> The values of keys which appear in both maps are combined using `f`.

```lean
def mergeWith (f : α → β → β → β) (self other : HashMap α β) : HashMap α β
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Lean/HashMap.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/HashMap.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Lean.HashMap.json)
