---
catalog: module
lean: Batteries.CodeAction.TacticCodeAction, Batteries.CodeAction.TacticSeqCodeAction, Batteries.CodeAction.mkTacticCodeAction, Batteries.CodeAction.mkTacticSeqCodeAction, Batteries.CodeAction.TacticCodeActionEntry, Batteries.CodeAction.TacticCodeActions, Batteries.CodeAction.TacticCodeActions.insert
statement: formalized
proof: formalized
---

# Initial setup for code action attributes

`Batteries.CodeAction.Attr`, in [Batteries/CodeAction/Attr.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/CodeAction/Attr.lean), by Mario Carneiro.

> * `@[hole_code_action]` and `@[command_code_action]` now live in the Lean repository,
>   and are builtin.
>
> * Attribute `@[tactic_code_action]` collects code actions which will be called
>   on each occurrence of a tactic.

`Batteries.CodeAction.TacticCodeAction` (abbreviation, [line 27](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/CodeAction/Attr.lean#L27))

> A tactic code action extension.

```lean
abbrev TacticCodeAction
```

`Batteries.CodeAction.TacticSeqCodeAction` (abbreviation, [line 33](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/CodeAction/Attr.lean#L33))

> A tactic code action extension.

```lean
abbrev TacticSeqCodeAction
```

`Batteries.CodeAction.mkTacticCodeAction` (definition, [line 39](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/CodeAction/Attr.lean#L39))

> Read a tactic code action from a declaration of the right type.

```lean
def mkTacticCodeAction (n : Name) : ImportM TacticCodeAction
```

`Batteries.CodeAction.mkTacticSeqCodeAction` (definition, [line 44](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/CodeAction/Attr.lean#L44))

> Read a tacticSeq code action from a declaration of the right type.

```lean
def mkTacticSeqCodeAction (n : Name) : ImportM TacticSeqCodeAction
```

`Batteries.CodeAction.TacticCodeActionEntry` (structure, [line 49](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/CodeAction/Attr.lean#L49))

> An entry in the tactic code actions extension, containing the attribute arguments.

```lean
structure TacticCodeActionEntry where
  /-- The declaration to tag -/
  declName : Name
  /-- The tactic kinds that this extension supports. If empty it is called on all tactic kinds. -/
  tacticKinds : Array Name
  deriving Inhabited
```

`Batteries.CodeAction.TacticCodeActions` (structure, [line 57](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/CodeAction/Attr.lean#L57))

> The state of the tactic code actions extension.

```lean
structure TacticCodeActions where
  /-- The list of tactic code actions to apply on any tactic. -/
  onAnyTactic : Array TacticCodeAction := {}
  /-- The list of tactic code actions to apply when a particular tactic kind is highlighted. -/
  onTactic : NameMap (Array TacticCodeAction) := {}
  deriving Inhabited
```

`Batteries.CodeAction.TacticCodeActions.insert` (definition, [line 65](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/CodeAction/Attr.lean#L65))

> Insert a tactic code action entry into the `TacticCodeActions` structure.

```lean
def TacticCodeActions.insert (self : TacticCodeActions)
    (tacticKinds : Array Name) (action : TacticCodeAction) : TacticCodeActions
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/CodeAction/Attr.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/CodeAction/Attr.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.CodeAction.Attr.json)
