---
catalog: module
lean: Lean.withoutModifyingState'
statement: formalized
proof: formalized
---

# MonadBacktrack

`Batteries.Lean.MonadBacktrack`, in [Batteries/Lean/MonadBacktrack.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/MonadBacktrack.lean), by Jannis Limperg.

`Lean.withoutModifyingState'` (definition, [line 18](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/MonadBacktrack.lean#L18))

> Execute the action `x`, then restore the initial state. Returns the state after
> `x` finished.

```lean
def withoutModifyingState' [Monad m] [MonadBacktrack s m] [MonadFinally m]
    (x : m α) : m (α × s)
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Lean/MonadBacktrack.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/MonadBacktrack.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Lean.MonadBacktrack.json)
