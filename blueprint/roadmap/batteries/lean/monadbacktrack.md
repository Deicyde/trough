---
catalog: module
lean: Lean.withoutModifyingState'
statement: formalized
proof: formalized
---

# MonadBacktrack

`Batteries.Lean.MonadBacktrack`, in [Batteries/Lean/MonadBacktrack.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/MonadBacktrack.lean), by Jannis Limperg.

`Lean.withoutModifyingState'` (definition, [line 18](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/MonadBacktrack.lean#L18))

> Execute the action `x`, then restore the initial state. Returns the state after
> `x` finished.

```lean
def withoutModifyingState' [Monad m] [MonadBacktrack s m] [MonadFinally m]
    (x : m α) : m (α × s)
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Lean/MonadBacktrack.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/MonadBacktrack.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Lean.MonadBacktrack.json)
