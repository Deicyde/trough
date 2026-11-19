---
catalog: module
lean: Batteries.Linter.UnreachableTactic.getLinterUnreachableTactic, Batteries.Linter.UnreachableTactic.M, Batteries.Linter.UnreachableTactic.isIgnoreTacticKind, Batteries.Linter.UnreachableTactic.addIgnoreTacticKind, Batteries.Linter.UnreachableTactic.getTactics, Batteries.Linter.UnreachableTactic.eraseUsedTacticsList, Batteries.Linter.UnreachableTactic.eraseUsedTactics, Batteries.Linter.UnreachableTactic.unreachableTacticLinter
statement: formalized
proof: formalized
---

# UnreachableTactic

`Batteries.Linter.UnreachableTactic`, in [Batteries/Linter/UnreachableTactic.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Linter/UnreachableTactic.lean), by Mario Carneiro.

`Batteries.Linter.UnreachableTactic.getLinterUnreachableTactic` (definition, [line 34](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Linter/UnreachableTactic.lean#L34))

> Gets the value of the `linter.unreachableTactic` option.

```lean
def getLinterUnreachableTactic (o : LinterOptions) : Bool
```

`Batteries.Linter.UnreachableTactic.M` (abbreviation, [line 38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Linter/UnreachableTactic.lean#L38))

> The monad for collecting used tactic syntaxes.

```lean
abbrev M
```

`Batteries.Linter.UnreachableTactic.isIgnoreTacticKind` (definition, [line 56](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Linter/UnreachableTactic.lean#L56))

> Is this a syntax kind that contains intentionally unevaluated tactic subterms?

```lean
def isIgnoreTacticKind (ignoreTacticKinds : NameHashSet) (k : SyntaxNodeKind) : Bool
```

`Batteries.Linter.UnreachableTactic.addIgnoreTacticKind` (definition, [line 65](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Linter/UnreachableTactic.lean#L65))

> Adds a new syntax kind whose children will be ignored by the `unreachableTactic` linter.
> This should be called from an `initialize` block.

```lean
def addIgnoreTacticKind (kind : SyntaxNodeKind) : IO Unit
```

`Batteries.Linter.UnreachableTactic.getTactics` (definition, [line 70](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Linter/UnreachableTactic.lean#L70))

> Accumulates the set of tactic syntaxes that should be evaluated at least once.

```lean
partial def getTactics (stx : Syntax) : M Unit
```

`Batteries.Linter.UnreachableTactic.eraseUsedTacticsList` (definition, [line 81](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Linter/UnreachableTactic.lean#L81))

> Search for tactic executions in the info tree and remove executed tactic syntaxes.

```lean
partial def eraseUsedTacticsList (trees : PersistentArray InfoTree) : M Unit
```

`Batteries.Linter.UnreachableTactic.eraseUsedTactics` (definition, [line 85](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Linter/UnreachableTactic.lean#L85))

> Search for tactic executions in the info tree and remove executed tactic syntaxes.

```lean
partial def eraseUsedTactics : InfoTree → M Unit
```

`Batteries.Linter.UnreachableTactic.unreachableTacticLinter` (definition, [line 97](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Linter/UnreachableTactic.lean#L97))

```lean
def unreachableTacticLinter : Linter
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Linter/UnreachableTactic.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Linter/UnreachableTactic.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Linter.UnreachableTactic.json)
