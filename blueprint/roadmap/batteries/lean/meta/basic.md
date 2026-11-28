---
catalog: module
lean: Lean.Meta.sortFVarsByContextOrder, Lean.MetavarContext.getExprMVarDecl, Lean.MetavarContext.declareExprMVar, Lean.MetavarContext.isExprMVarAssignedOrDelayedAssigned, Lean.MetavarContext.isExprMVarDeclared, Lean.MetavarContext.eraseExprMVarAssignment, Lean.MetavarContext.unassignedExprMVars, Lean.MVarId.isDeclared, Lean.MVarId.eraseAssignment, Lean.MVarId.synthInstance, Lean.MVarId.getTypeCleanup, Lean.Meta.getUnassignedExprMVars, Lean.Meta.unhygienic, Lean.Meta.mkFreshIdWithPrefix, Lean.Meta.saturate1
statement: formalized
proof: formalized
---

# Meta/Basic

`Batteries.Lean.Meta.Basic`, in [Batteries/Lean/Meta/Basic.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/Basic.lean), by Mario Carneiro, Jannis Limperg.

`Lean.Meta.sortFVarsByContextOrder` (definition, [line 25](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/Basic.lean#L25))

> Sort the given `FVarId`s by the order in which they appear in the current local
> context. If any of the `FVarId`s do not appear in the current local context, the
> result is unspecified.

```lean
def Meta.sortFVarsByContextOrder [Monad m] [MonadLCtx m]
    (hyps : Array FVarId) : m (Array FVarId)
```

`Lean.MetavarContext.getExprMVarDecl` (definition, [line 35](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/Basic.lean#L35))

> Get the `MetavarDecl` of `mvarId`. If `mvarId` is not a declared metavariable
> in the given `MetavarContext`, throw an error.

```lean
def getExprMVarDecl [Monad m] [MonadError m] (mctx : MetavarContext)
    (mvarId : MVarId) : m MetavarDecl
```

`Lean.MetavarContext.declareExprMVar` (definition, [line 46](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/Basic.lean#L46))

> Declare a metavariable. You must make sure that the metavariable is not already
> declared.

```lean
def declareExprMVar (mctx : MetavarContext) (mvarId : MVarId)
    (mdecl : MetavarDecl) : MetavarContext
```

`Lean.MetavarContext.isExprMVarAssignedOrDelayedAssigned` (definition, [line 57](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/Basic.lean#L57))

> Check whether a metavariable is assigned or delayed-assigned. A
> delayed-assigned metavariable is already 'solved' but the solution cannot be
> substituted yet because we have to wait for some other metavariables to be
> assigned first. So in most situations you want to treat a delayed-assigned
> metavariable as assigned.

```lean
def isExprMVarAssignedOrDelayedAssigned (mctx : MetavarContext)
    (mvarId : MVarId) : Bool
```

`Lean.MetavarContext.isExprMVarDeclared` (definition, [line 64](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/Basic.lean#L64))

> Check whether a metavariable is declared in the given `MetavarContext`.

```lean
def isExprMVarDeclared (mctx : MetavarContext) (mvarId : MVarId) : Bool
```

`Lean.MetavarContext.eraseExprMVarAssignment` (definition, [line 70](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/Basic.lean#L70))

> Erase any assignment or delayed assignment of the given metavariable.

```lean
def eraseExprMVarAssignment (mctx : MetavarContext) (mvarId : MVarId) :
    MetavarContext
```

`Lean.MetavarContext.unassignedExprMVars` (definition, [line 81](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/Basic.lean#L81))

> Obtain all unassigned metavariables from the given `MetavarContext`. If
> `includeDelayed` is `true`, delayed-assigned metavariables are considered
> unassigned.

```lean
def unassignedExprMVars (mctx : MetavarContext) (includeDelayed := false) :
    Array MVarId
```

`Lean.MVarId.isDeclared` (definition, [line 98](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/Basic.lean#L98))

> Check whether a metavariable is declared.

```lean
def isDeclared [Monad m] [MonadMCtx m] (mvarId : MVarId) : m Bool
```

`Lean.MVarId.eraseAssignment` (definition, [line 104](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/Basic.lean#L104))

> Erase any assignment or delayed assignment of the given metavariable.

```lean
def eraseAssignment [MonadMCtx m] (mvarId : MVarId) : m Unit
```

`Lean.MVarId.synthInstance` (definition, [line 109](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/Basic.lean#L109))

> Solve a goal by synthesizing an instance.

```lean
def synthInstance (g : MVarId) : MetaM Unit
```

`Lean.MVarId.getTypeCleanup` (definition, [line 114](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/Basic.lean#L114))

> Get the type the given metavariable after instantiating metavariables and cleaning up
> annotations.

```lean
def getTypeCleanup (mvarId : MVarId) : MetaM Expr
```

`Lean.Meta.getUnassignedExprMVars` (definition, [line 126](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/Basic.lean#L126))

> Obtain all unassigned metavariables. If `includeDelayed` is `true`,
> delayed-assigned metavariables are considered unassigned.

```lean
def getUnassignedExprMVars [Monad m] [MonadMCtx m] (includeDelayed := false) :
    m (Array MVarId)
```

`Lean.Meta.unhygienic` (definition, [line 133](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/Basic.lean#L133))

> Run a computation with hygiene turned off.

```lean
def unhygienic [MonadWithOptions m] (x : m α) : m α
```

`Lean.Meta.mkFreshIdWithPrefix` (definition, [line 141](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/Basic.lean#L141))

> A variant of `mkFreshId` which generates names with a particular prefix. The
> generated names are unique and have the form `<prefix>.<N>` where `N` is a
> natural number. They are not suitable as user-facing names.

```lean
def mkFreshIdWithPrefix [Monad m] [MonadNameGenerator m] («prefix» : Name) :
    m Name
```

`Lean.Meta.saturate1` (definition, [line 157](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/Basic.lean#L157))

> `saturate1 goal tac` runs `tac` on `goal`, then on the resulting goals, etc.,
> until `tac` does not apply to any goal any more (i.e. it returns `none`). The
> order of applications is depth-first, so if `tac` generates goals `[g₁, g₂, ⋯]`,
> we apply `tac` to `g₁` and recursively to all its subgoals before visiting `g₂`.
> If `tac` does not apply to `goal`, `saturate1` returns `none`. Otherwise it
> returns the generated subgoals to which `tac` did not apply. `saturate1`
> respects the `MonadRecDepth` recursion limit.

```lean
partial def saturate1 [Monad m] [MonadError m] [MonadRecDepth m] [MonadLiftT (ST IO.RealWorld) m]
    (goal : MVarId) (tac : MVarId → m (Option (Array MVarId))) : m (Option (Array MVarId))
```

## Depends on

- [Laws for Monads with Failure](../../control/alternativemonad.md)

## Sources

- [Batteries/Lean/Meta/Basic.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/Basic.lean)
- [Declaration ledger](../../../../sources/batteries/Batteries.Lean.Meta.Basic.json)
