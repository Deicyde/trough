---
catalog: module
lean: Batteries.CodeAction.tacticCodeActionProvider
statement: formalized
proof: formalized
---

# Initial setup for code actions

`Batteries.CodeAction.Basic`, in [Batteries/CodeAction/Basic.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/CodeAction/Basic.lean), by Mario Carneiro.

> This declares a code action provider that calls all `@[hole_code_action]` definitions
> on each occurrence of a hole (`_`, `?_` or `sorry`).
>
> (This is in a separate file from `Batteries.CodeAction.Hole.Attr` so that the server does not
> attempt to use this code action provider when browsing the `Batteries.CodeAction.Hole.Attr` file
> itself.)

`Batteries.CodeAction.tacticCodeActionProvider` (definition, [line 30](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/CodeAction/Basic.lean#L30))

> A code action which calls `@[tactic_code_action]` code actions.

```lean
def tacticCodeActionProvider : CodeActionProvider
```

## Depends on

- [Initial setup for code action attributes](attr.md)

## Sources

- [Batteries/CodeAction/Basic.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/CodeAction/Basic.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.CodeAction.Basic.json)
