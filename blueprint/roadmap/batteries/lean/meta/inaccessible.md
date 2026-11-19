---
catalog: module
lean: Lean.LocalContext.inaccessibleFVars, Lean.Meta.getInaccessibleFVars, Lean.MVarId.renameInaccessibleFVars
statement: formalized
proof: formalized
---

# Inaccessible

`Batteries.Lean.Meta.Inaccessible`, in [Batteries/Lean/Meta/Inaccessible.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Meta/Inaccessible.lean), by Jannis Limperg.

`Lean.LocalContext.inaccessibleFVars` (definition, [line 19](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Meta/Inaccessible.lean#L19))

> Obtain the inaccessible fvars from the given local context. An fvar is
> inaccessible if (a) its user name is inaccessible or (b) it is shadowed by a
> later fvar with the same user name.

```lean
def Lean.LocalContext.inaccessibleFVars (lctx : LocalContext) :
    Array LocalDecl
```

`Lean.Meta.getInaccessibleFVars` (definition, [line 41](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Meta/Inaccessible.lean#L41))

> Obtain the inaccessible fvars from the current local context. An fvar is
> inaccessible if (a) its user name is inaccessible or (b) it is shadowed by a
> later fvar with the same user name.

```lean
def Lean.Meta.getInaccessibleFVars [Monad m] [MonadLCtx m] :
    m (Array LocalDecl)
```

`Lean.MVarId.renameInaccessibleFVars` (definition, [line 51](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Meta/Inaccessible.lean#L51))

> Rename all inaccessible fvars. An fvar is inaccessible if (a) its user name is
> inaccessible or (b) it is shadowed by a later fvar with the same user name. This
> function gives all inaccessible fvars a unique, accessible user name. It returns
> the new goal and the fvars that were renamed.

```lean
def Lean.MVarId.renameInaccessibleFVars (mvarId : MVarId) :
    MetaM (MVarId × Array FVarId)
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Lean/Meta/Inaccessible.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Meta/Inaccessible.lean)
- [Declaration ledger](../../../../sources/batteries/Batteries.Lean.Meta.Inaccessible.json)
