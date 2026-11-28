---
catalog: module
lean: Lean.Meta.SavedState.runMetaM, Lean.Meta.SavedState.runMetaM', Lean.Meta.getIntroducedExprMVars, Lean.Meta.getAssignedExprMVars
statement: formalized
proof: formalized
---

# SavedState

`Batteries.Lean.Meta.SavedState`, in [Batteries/Lean/Meta/SavedState.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/SavedState.lean), by Jannis Limperg.

`Lean.Meta.SavedState.runMetaM` (definition, [line 19](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/SavedState.lean#L19))

> Run the action `x` in state `s`. Returns the result of `x` and the state after
> `x` was executed. The global state remains unchanged.

```lean
def runMetaM (s : Meta.SavedState) (x : MetaM α) :
    MetaM (α × Meta.SavedState)
```

`Lean.Meta.SavedState.runMetaM'` (definition, [line 27](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/SavedState.lean#L27))

> Run the action `x` in state `s`. Returns the result of `x`. The global state
> remains unchanged.

```lean
def runMetaM' (s : Meta.SavedState) (x : MetaM α) : MetaM α
```

`Lean.Meta.getIntroducedExprMVars` (definition, [line 37](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/SavedState.lean#L37))

> Returns the mvars that are not declared in `preState`, but declared and
> unassigned in `postState`. Delayed-assigned mvars are considered assigned.

```lean
def getIntroducedExprMVars (preState postState : SavedState) :
    MetaM (Array MVarId)
```

`Lean.Meta.getAssignedExprMVars` (definition, [line 47](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/SavedState.lean#L47))

> Returns the mvars that are declared but unassigned in `preState`, and
> assigned in `postState`. Delayed-assigned mvars are considered assigned.

```lean
def getAssignedExprMVars (preState postState : SavedState) :
    MetaM (Array MVarId)
```

## Depends on

- [Meta/Basic](basic.md)
- [MonadBacktrack](../monadbacktrack.md)

## Sources

- [Batteries/Lean/Meta/SavedState.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/SavedState.lean)
- [Declaration ledger](../../../../sources/batteries/Batteries.Lean.Meta.SavedState.json)
