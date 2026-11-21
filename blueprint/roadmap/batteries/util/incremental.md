---
catalog: module
lean: Batteries.Tactic.CommandElabResultSnapshot, Batteries.Tactic.SimpleIncrementalSnapshot, Batteries.Tactic.simpleIncrementalElab
statement: formalized
proof: formalized
---

# A utility for simple incremental commands

`Batteries.Util.Incremental`, in [Batteries/Util/Incremental.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Util/Incremental.lean), by Robin Arnez.

`Batteries.Tactic.CommandElabResultSnapshot` (structure, [line 21](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Util/Incremental.lean#L21))

> A snapshot for the result of command elaboration

```lean
structure CommandElabResultSnapshot extends Language.Snapshot where
  /-- The syntax that was being elaborated -/
  stx : Syntax
  /-- The state after command elaboration -/
  state : Command.State
  /-- The exception thrown during command elaboration, if any -/
  error? : Option Exception
  /-- Snapshot tasks produced by `logSnapshotTask` during command elaboration -/
  moreSnaps : Array (Language.SnapshotTask Language.SnapshotTree)
deriving Nonempty
```

`Batteries.Tactic.SimpleIncrementalSnapshot` (structure, [line 33](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Util/Incremental.lean#L33))

> The snapshot type for `simpleIncrementalElab`

```lean
structure SimpleIncrementalSnapshot extends Language.Snapshot where
  /-- The result for the previous execution of the command -/
  result : Language.SnapshotTask (Option CommandElabResultSnapshot)
  /-- The last result that didn't error because of missing syntax -/
  lastNoSyntaxErrorResult? : Option CommandElabResultSnapshot
deriving TypeName
```

`Batteries.Tactic.simpleIncrementalElab` (definition, [line 69](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Util/Incremental.lean#L69))

> Wraps `cmd` with simple incrementality handling that makes the command not re-run if only trailing
> whitespace was changed or when a syntax error gets introduced and then removed again.
>
> To make this work, `cmd` doesn't receive the trailing whitespace of the command and doesn't have
> access to incrementality itself.
>
> To make use of this, you have to write an explicit elaborator (i.e. a declaration with a
> `@[command_elab]`) and tag it with `@[incremental]` and then wrap the body in
> `simpleIncrementalElab`. Example:
> ```
> syntax (name := expensiveCmd) "#expensive_command" : command
>
> @[command_elab expensiveCmd, incremental]
> def elabExpensiveCmd : CommandElab := simpleIncrementalElab fun stx => do
>   ...
> ```

```lean
def simpleIncrementalElab (cmd : CommandElab) : CommandElab
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Util/Incremental.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Util/Incremental.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Util.Incremental.json)
