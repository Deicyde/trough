---
catalog: module
lean: Batteries.Linter.UnnecessarySeqFocus.getLinterUnnecessarySeqFocus, Batteries.Linter.UnnecessarySeqFocus.M, Batteries.Linter.UnnecessarySeqFocus.getPath, Batteries.Linter.UnnecessarySeqFocus.markUsedTacticsList, Batteries.Linter.UnnecessarySeqFocus.markUsedTactics, Batteries.Linter.UnnecessarySeqFocus.unnecessarySeqFocusLinter
statement: formalized
proof: formalized
---

# UnnecessarySeqFocus

`Batteries.Linter.UnnecessarySeqFocus`, in [Batteries/Linter/UnnecessarySeqFocus.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/UnnecessarySeqFocus.lean), by Mario Carneiro.

`Batteries.Linter.UnnecessarySeqFocus.getLinterUnnecessarySeqFocus` (definition, [line 53](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/UnnecessarySeqFocus.lean#L53))

> Gets the value of the `linter.unnecessarySeqFocus` option.

```lean
def getLinterUnnecessarySeqFocus (o : LinterOptions) : Bool
```

`Batteries.Linter.UnnecessarySeqFocus.M` (abbreviation, [line 83](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/UnnecessarySeqFocus.lean#L83))

> The monad for collecting used tactic syntaxes.
> - `some stx` means that this `<;>` syntax has only been used unnecessarily.
> - `none` means that this `<;>` syntax was necessary at least once, so we won't warn about it.

```lean
abbrev M
```

`Batteries.Linter.UnnecessarySeqFocus.getPath` (definition, [line 89](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/UnnecessarySeqFocus.lean#L89))

> Traverse the info tree down a given path.
> Each `(n, i)` means that the array must have length `n` and we will descend into the `i`'th child.

```lean
def getPath : Info → PersistentArray InfoTree → List ((n : Nat) × Fin n) → Option Info
```

`Batteries.Linter.UnnecessarySeqFocus.markUsedTacticsList` (definition, [line 99](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/UnnecessarySeqFocus.lean#L99))

> Search for tactic executions in the info tree and remove executed tactic syntaxes.

```lean
partial def markUsedTacticsList (trees : PersistentArray InfoTree) : M Unit
```

`Batteries.Linter.UnnecessarySeqFocus.markUsedTactics` (definition, [line 103](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/UnnecessarySeqFocus.lean#L103))

> Search for tactic executions in the info tree and remove executed tactic syntaxes.

```lean
partial def markUsedTactics : InfoTree → M Unit
```

`Batteries.Linter.UnnecessarySeqFocus.unnecessarySeqFocusLinter` (definition, [line 135](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/UnnecessarySeqFocus.lean#L135))

```lean
def unnecessarySeqFocusLinter : Linter
```

## Depends on

- [AttributeExtra](../lean/attributeextra.md)

## Sources

- [Batteries/Linter/UnnecessarySeqFocus.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/UnnecessarySeqFocus.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Linter.UnnecessarySeqFocus.json)
