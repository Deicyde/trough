---
catalog: module
lean: Lean.TSyntax.replaceM
statement: formalized
proof: formalized
---

# Helper functions for working with typed syntaxes

`Batteries.Lean.Syntax`, in [Batteries/Lean/Syntax.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Syntax.lean), by Gabriel Ebner.

`Lean.TSyntax.replaceM` (definition, [line 24](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Syntax.lean#L24))

> Applies the given function to every subsyntax.
>
> Like `Syntax.replaceM` but for typed syntax.
> (Note there are no guarantees of type correctness here.)

```lean
def TSyntax.replaceM [Monad M] (f : Syntax → M (Option Syntax)) (stx : TSyntax k) : M (TSyntax k)
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Lean/Syntax.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Syntax.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Lean.Syntax.json)
