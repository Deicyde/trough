---
catalog: module
lean: Lean.Meta.collectPrivateIn, Lean.Environment.moduleIdxForModule?, Lean.Environment.declsInModuleIdx, Lean.Elab.addModuleInfo, Lean.Elab.Command.elabOpenPrivateLike, Lean.Elab.Command.elabOpenPrivate, Lean.Elab.Command.elabExportPrivate
statement: formalized
proof: formalized
---

# OpenPrivate

`Batteries.Tactic.OpenPrivate`, in [Batteries/Tactic/OpenPrivate.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/OpenPrivate.lean), by Mario Carneiro.

`Lean.Meta.collectPrivateIn` (definition, [line 18](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/OpenPrivate.lean#L18))

> Collects the names of private declarations referenced in definition `n`.

```lean
def Meta.collectPrivateIn [Monad m] [MonadEnv m] [MonadError m]
  (n : Name) (set := NameSet.empty) : m NameSet
```

`Lean.Environment.moduleIdxForModule?` (definition, [line 29](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/OpenPrivate.lean#L29))

> Get the module index given a module name.

```lean
def Environment.moduleIdxForModule? (env : Environment) (mod : Name) : Option ModuleIdx
```

`Lean.Environment.declsInModuleIdx` (definition, [line 35](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/OpenPrivate.lean#L35))

> Get the list of declarations in a module (referenced by index).

```lean
def Environment.declsInModuleIdx (env : Environment) (idx : ModuleIdx) : List Name
```

`Lean.Elab.addModuleInfo` (definition, [line 39](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/OpenPrivate.lean#L39))

> Add info to the info tree corresponding to a module name.

```lean
def Elab.addModuleInfo [Monad m] [MonadInfoTree m] (stx : Ident) : m Unit
```

`Lean.Elab.Command.elabOpenPrivateLike` (definition, [line 51](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/OpenPrivate.lean#L51))

> Core elaborator for `open private` and `export private`.

```lean
def elabOpenPrivateLike (ids : Array Ident) (tgts mods : Option (Array Ident))
  (f : (priv full user : Name) → CommandElabM Name) : CommandElabM Unit
```

`Lean.Elab.Command.elabOpenPrivate` (definition, [line 129](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/OpenPrivate.lean#L129))

> Elaborator for `open private`.

```lean
def elabOpenPrivate : CommandElab
```

`Lean.Elab.Command.elabExportPrivate` (definition, [line 149](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/OpenPrivate.lean#L149))

> Elaborator for `export private`.

```lean
def elabExportPrivate : CommandElab
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Tactic/OpenPrivate.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/OpenPrivate.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Tactic.OpenPrivate.json)
