---
catalog: module
lean: Batteries.Tactic.Congr.Config, Batteries.Tactic.rcongrCore
statement: formalized
proof: formalized
---

# `congr with` tactic, `rcongr` tactic

`Batteries.Tactic.Congr`, in [Batteries/Tactic/Congr.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/Congr.lean), by Mario Carneiro, Miyahara Kō.

`Batteries.Tactic.Congr.Config` (structure, [line 23](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/Congr.lean#L23))

> Configuration options for `congr` & `rcongr`

```lean
structure Congr.Config where
  /-- If `closePre := true`, it will attempt to close new goals using `Eq.refl`, `HEq.refl`, and
  `assumption` with reducible transparency. -/
  closePre : Bool := true
  /-- If `closePost := true`, it will try again on goals on which `congr` failed to make progress
  with default transparency. -/
  closePost : Bool := true
```

`Batteries.Tactic.rcongrCore` (definition, [line 80](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/Congr.lean#L80))

> Recursive core of `rcongr`. Calls `ext pats <;> congr` and then itself recursively,
> unless `ext pats <;> congr` made no progress.

```lean
partial def rcongrCore (g : MVarId) (config : Congr.Config) (pats : List (TSyntax `rcasesPat))
    (acc : Array MVarId) : TermElabM (Array MVarId)
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Tactic/Congr.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/Congr.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Tactic.Congr.json)
