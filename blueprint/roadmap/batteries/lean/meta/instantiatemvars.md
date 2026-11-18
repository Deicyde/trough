---
catalog: module
lean: Lean.MVarId.instantiateMVarsInType, Lean.MVarId.instantiateMVarsInLocalDecl, Lean.MVarId.instantiateMVarsInLocalContext, Lean.MVarId.instantiateMVars
statement: formalized
proof: formalized
---

# InstantiateMVars

`Batteries.Lean.Meta.InstantiateMVars`, in [Batteries/Lean/Meta/InstantiateMVars.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Meta/InstantiateMVars.lean), by Jannis Limperg.

`Lean.MVarId.instantiateMVarsInType` (definition, [line 20](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Meta/InstantiateMVars.lean#L20))

> Instantiate metavariables in the type of the given metavariable, update the
> metavariable's declaration and return the new type.

```lean
def instantiateMVarsInType [Monad m] [MonadMCtx m] [MonadError m]
    (mvarId : MVarId) : m Expr
```

`Lean.MVarId.instantiateMVarsInLocalDecl` (definition, [line 36](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Meta/InstantiateMVars.lean#L36))

> Instantiate metavariables in the `LocalDecl` of the given fvar, update the
> `LocalDecl` and return the new `LocalDecl.`

```lean
def instantiateMVarsInLocalDecl [Monad m] [MonadMCtx m] [MonadError m]
    (mvarId : MVarId) (fvarId : FVarId) : m LocalDecl
```

`Lean.MVarId.instantiateMVarsInLocalContext` (definition, [line 51](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Meta/InstantiateMVars.lean#L51))

> Instantiate metavariables in the local context of the given metavariable, update
> the metavariable's declaration and return the new local context.

```lean
def instantiateMVarsInLocalContext [Monad m] [MonadMCtx m] [MonadError m]
    (mvarId : MVarId) : m LocalContext
```

`Lean.MVarId.instantiateMVars` (definition, [line 62](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Meta/InstantiateMVars.lean#L62))

> Instantiate metavariables in the local context and type of the given
> metavariable.

```lean
def instantiateMVars [Monad m] [MonadMCtx m] [MonadError m] (mvarId : MVarId) :
    m Unit
```

## Depends on

- [Meta/Basic](basic.md)

## Sources

- [Batteries/Lean/Meta/InstantiateMVars.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Meta/InstantiateMVars.lean)
