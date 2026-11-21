---
catalog: module
lean: Lean.withoutModifyingState'
statement: formalized
proof: formalized
---

# MonadBacktrack

`Batteries.Lean.MonadBacktrack`, in [Batteries/Lean/MonadBacktrack.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/MonadBacktrack.lean), by Jannis Limperg.

`Lean.withoutModifyingState'` (definition, [line 18](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/MonadBacktrack.lean#L18))

> Execute the action `x`, then restore the initial state. Returns the state after
> `x` finished.

```lean
def withoutModifyingState' [Monad m] [MonadBacktrack s m] [MonadFinally m]
    (x : m α) : m (α × s)
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Lean/MonadBacktrack.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/MonadBacktrack.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Lean.MonadBacktrack.json)
