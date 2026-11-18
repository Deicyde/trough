---
catalog: module
lean: Batteries.CodeAction.tacticCodeActionProvider
statement: formalized
proof: formalized
---

# Initial setup for code actions

`Batteries.CodeAction.Basic`, in [Batteries/CodeAction/Basic.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Basic.lean), by Mario Carneiro.

> This declares a code action provider that calls all `@[hole_code_action]` definitions
> on each occurrence of a hole (`_`, `?_` or `sorry`).
>
> (This is in a separate file from `Batteries.CodeAction.Hole.Attr` so that the server does not
> attempt to use this code action provider when browsing the `Batteries.CodeAction.Hole.Attr` file
> itself.)

`Batteries.CodeAction.tacticCodeActionProvider` (definition, [line 30](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Basic.lean#L30))

> A code action which calls `@[tactic_code_action]` code actions.

```lean
def tacticCodeActionProvider : CodeActionProvider
```

## Depends on

- [Initial setup for code action attributes](attr.md)

## Sources

- [Batteries/CodeAction/Basic.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Basic.lean)
