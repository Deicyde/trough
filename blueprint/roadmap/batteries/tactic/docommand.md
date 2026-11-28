---
catalog: module
lean: Batteries.Tactic.DoCommand.MonadStateStack, Batteries.Tactic.DoCommand.DoCommandExtensionState, Batteries.Tactic.DoCommand.Data, Batteries.Tactic.DoCommand.Data.getValue, Batteries.Tactic.DoCommand.Data.getValueLetImpl, Batteries.Tactic.DoCommand.Data.getValueLet, Batteries.Tactic.DoCommand.Data.empty, Batteries.Tactic.DoCommand.Data.push, Batteries.Tactic.DoCommand.DoCommandExtensionState.eval, Batteries.Tactic.DoCommand.ContinuationResult, Batteries.Tactic.DoCommand.elabDoCommandCore, Batteries.Tactic.DoCommand.elabDoCommand, Batteries.Tactic.DoCommand.elabDoBangCommand, Batteries.Tactic.DoCommand.elabDoMetaCommand, Batteries.Tactic.DoCommand.elabDoMetaBangCommand
statement: formalized
proof: formalized
---

# The `#do` command

`Batteries.Tactic.DoCommand`, in [Batteries/Tactic/DoCommand.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/DoCommand.lean), by Robin Arnez.

> The `#do` command is like `run_cmd` but allows using variables from previous uses of `#do`.
> Furthermore, `#do_meta` is like `#do` and shares its variable state while operating in `MetaM`.
> Finally, `#clear_do` can be used to remove all variables from the current do state.

`Batteries.Tactic.DoCommand.MonadStateStack` (structure, [line 28](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/DoCommand.lean#L28))

> The part of the `DoCommandExtensionState` used for monad state

```lean
structure MonadStateStack where
  /-- The meta state used for `#do_meta` -/
  metaState : Meta.State := {}
deriving Inhabited
```

`Batteries.Tactic.DoCommand.DoCommandExtensionState` (structure, [line 34](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/DoCommand.lean#L34))

> The state for `#do`

```lean
structure DoCommandExtensionState where
  /--
  The current local context for `#do`.

  Invariant: `lctx` does not contain metavariables or level parameters or non-dependent `ldecl`s.
  -/
  lctx : LocalContext := {}
  /-- The local instances for `lctx` -/
  localInstances : LocalInstances := #[]
  /--
  The values associated to free variables in `lctx`.

  Invariant: every free variable in `lctx` has a corresponding value in `values`
  -/
  values : FVarIdMap NonScalar := {}
  /-- See `Lean.Elab.Do.Context.mutVars` -/
  mutVars : Array MutVar := #[]
  /-- See `Lean.Elab.Do.Context.mutVarDefs` -/
  mutVarDefs : Std.HashMap Name MutVar := {}
  /-- Monad state for use in e.g. `#do_meta` -/
  monadState : MonadStateStack := {}
deriving Inhabited
```

`Batteries.Tactic.DoCommand.Data` (abbreviation, [line 62](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/DoCommand.lean#L62))

> Implementation detail of `#do`

```lean
abbrev Data
```

`Batteries.Tactic.DoCommand.Data.getValue` (definition, [line 65](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/DoCommand.lean#L65))

> Implementation detail of `#do`

```lean
unsafe def Data.getValue.{u} {α : Sort u} (vs : Data) (i : Nat) : α
```

`Batteries.Tactic.DoCommand.Data.getValueLetImpl` (definition, [line 69](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/DoCommand.lean#L69))

```lean
unsafe def Data.getValueLetImpl.{u} {α : Sort u} (vs : Data) (i : Nat) (_v : α) : α
```

`Batteries.Tactic.DoCommand.Data.getValueLet` (abbreviation, [line 74](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/DoCommand.lean#L74))

> Implementation detail of `#do`

```lean
unsafe abbrev Data.getValueLet.{u} {α : Sort u} (_vs : Data) (_i : Nat) (v : α) : α
```

`Batteries.Tactic.DoCommand.Data.empty` (definition, [line 77](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/DoCommand.lean#L77))

> Implementation detail of `#do`

```lean
def Data.empty : Data
```

`Batteries.Tactic.DoCommand.Data.push` (definition, [line 80](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/DoCommand.lean#L80))

> Implementation detail of `#do`

```lean
unsafe nonrec def Data.push.{u} {α : Sort u} (d : Data) (x : α) : Data
```

`Batteries.Tactic.DoCommand.DoCommandExtensionState.eval` (definition, [line 86](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/DoCommand.lean#L86))

> Given `value : type` which may depend on free variables in `state.lctx`, evaluates it to a value
> of type `α` (assuming `type` is equivalent to `α`).

```lean
unsafe def DoCommandExtensionState.eval (state : DoCommandExtensionState)
    (α : Type) (type : Expr) (value : Expr) (checkMeta := true)
    (allowSorry := false) (alternative? : Option String := none) : MetaM α
```

`Batteries.Tactic.DoCommand.ContinuationResult` (structure, [line 160](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/DoCommand.lean#L160))

> Implementation detail of `#do`

```lean
structure ContinuationResult where
  /-- All new free variables in the order they are stored in the resulting array -/
  newFVars : Array FVarId
  /-- The new state, with updated local context and mutable variables -/
  newState : DoCommandExtensionState
```

`Batteries.Tactic.DoCommand.elabDoCommandCore` (definition, [line 195](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/DoCommand.lean#L195))

> Monad-generic version of the `#do` command

```lean
def elabDoCommandCore (m : Type → Type)
    (lift : ∀ {α}, m α → MonadStateStack → CommandElabM (α × MonadStateStack))
    (mExpr : Expr) (doSeq : TSyntax ``Lean.Parser.Term.doSeq)
    (allowSorry : Bool) (alternative? : Option String := none) :
    CommandElabM Unit
```

`Batteries.Tactic.DoCommand.elabDoCommand` (definition, [line 283](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/DoCommand.lean#L283))

```lean
def elabDoCommand : CommandElab
```

`Batteries.Tactic.DoCommand.elabDoBangCommand` (definition, [line 289](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/DoCommand.lean#L289))

```lean
def elabDoBangCommand : CommandElab
```

`Batteries.Tactic.DoCommand.elabDoMetaCommand` (definition, [line 321](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/DoCommand.lean#L321))

```lean
def elabDoMetaCommand : CommandElab
```

`Batteries.Tactic.DoCommand.elabDoMetaBangCommand` (definition, [line 327](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/DoCommand.lean#L327))

```lean
def elabDoMetaBangCommand : CommandElab
```

## Depends on

- [Eval](../util/eval.md)
- [A utility for simple incremental commands](../util/incremental.md)

## Sources

- [Batteries/Tactic/DoCommand.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/DoCommand.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Tactic.DoCommand.json)
