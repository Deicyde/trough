---
catalog: module
lean: Batteries.CodeAction.deprecatedCodeActionProvider
statement: formalized
proof: formalized
---

# Code action for @\[deprecated\] replacements

`Batteries.CodeAction.Deprecated`, in [Batteries/CodeAction/Deprecated.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/CodeAction/Deprecated.lean), by Mario Carneiro.

> This is an opt-in mechanism for making machine-applicable `@[deprecated]` definitions. When enabled
> (by setting the `machineApplicableDeprecated` tag attribute), a code action will be triggered
> whenever the deprecation lint also fires, allowing the user to replace the usage of the deprecated
> constant.

`Batteries.CodeAction.deprecatedCodeActionProvider` (definition, [line 33](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/CodeAction/Deprecated.lean#L33))

> A code action which applies replacements for `@[deprecated]` definitions.

```lean
def deprecatedCodeActionProvider : CodeActionProvider
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/CodeAction/Deprecated.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/CodeAction/Deprecated.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.CodeAction.Deprecated.json)
