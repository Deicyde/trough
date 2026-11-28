---
catalog: module
lean: Batteries.Linter.LintVerbosity, Batteries.Linter.getChecks, Batteries.Linter.traceLintCore, Batteries.Linter.traceLint, Batteries.Linter.lintBatchSize, Batteries.Linter.mapOnWorkers, Batteries.Linter.lintDecl, Batteries.Linter.lintCore, Batteries.Linter.sortResults, Batteries.Linter.printWarning, Batteries.Linter.printWarnings, Batteries.Linter.groupedByFilename, Batteries.Linter.formatLinterResults, Batteries.Linter.getDeclsInCurrModule, Batteries.Linter.getAllDecls, Batteries.Linter.getDeclsInPackage, Batteries.Tactic.Lint.LintVerbosity, Batteries.Tactic.Lint.LintVerbosity.low, Batteries.Tactic.Lint.LintVerbosity.medium, Batteries.Tactic.Lint.LintVerbosity.high, Batteries.Tactic.Lint.getChecks, Batteries.Tactic.Lint.lintBatchSize, Batteries.Tactic.Lint.mapOnWorkers, Batteries.Tactic.Lint.lintDecl, Batteries.Tactic.Lint.lintCore, Batteries.Tactic.Lint.sortResults, Batteries.Tactic.Lint.printWarning, Batteries.Tactic.Lint.printWarnings, Batteries.Tactic.Lint.groupedByFilename, Batteries.Tactic.Lint.formatLinterResults, Batteries.Tactic.Lint.getDeclsInCurrModule, Batteries.Tactic.Lint.getAllDecls, Batteries.Tactic.Lint.getDeclsInPackage, Batteries.Tactic.Lint.inProject, Batteries.Tactic.Lint.traceLintCore, Batteries.Tactic.Lint.traceLint
statement: formalized
proof: formalized
---

# Linter frontend and commands

`Batteries.Linter.Frontend`, in [Batteries/Linter/Frontend.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean), by Floris van Doorn, Robert Y. Lewis, Gabriel Ebner.

> This file defines the linter commands which spot common mistakes in the code.
> * `#lint`: check all declarations in the current file
> * `#lint in Pkg`: check all declarations in the package `Pkg`
>   (so excluding core or other projects, and also excluding the current file)
> * `#lint in all`: check all declarations in the environment
>   (the current file and all imported files)
>
> For a list of default / non-default linters, see the "Linting Commands" user command doc entry.
>
> The command `#list_linters` prints a list of the names of all available linters.
>
> You can append a `*` to any command (e.g. `#lint* in Batteries`) to omit the slow tests.
>
> You can append a `-` to any command (e.g. `#lint- in Batteries`) to run a silent lint
> that suppresses the output if all checks pass.
> A silent lint will fail if any test fails.
>
> You can append a `+` to any command (e.g. `#lint+ in Batteries`) to run a verbose lint
> that reports the result of each linter, including  the successes.
>
> You can append a sequence of linter names to any command to run extra tests, in addition to the
> default ones. e.g. `#lint doc_blame_thm` will run all default tests and `doc_blame_thm`.
>
> You can append `only name1 name2 ...` to any command to run a subset of linters, e.g.
> `#lint only unused_arguments in Batteries`
>
> You can add custom linters by defining a term of type `Linter` with the
> `@[env_linter]` attribute.
> A linter defined with the name `Batteries.Linter.myNewCheck` can be run with `#lint myNewCheck`
> or `#lint only myNewCheck`.
> If you add the attribute `@[env_linter disabled]` to `linter.myNewCheck` it will be
> registered, but not run by default.
>
> Adding the attribute `@[nolint doc_blame unused_arguments]` to a declaration
> omits it from only the specified linter checks.
>
> ## Tags
>
> sanity check, lint, cleanup, command, tactic

`Batteries.Linter.LintVerbosity` (inductive type, [line 62](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L62))

> Verbosity for the linter output.

```lean
inductive LintVerbosity
  /-- `low`: only print failing checks, print nothing on success. -/
  | low
  /-- `medium`: only print failing checks, print confirmation on success. -/
  | medium
  /-- `high`: print output of every check. -/
  | high
  deriving Inhabited, DecidableEq, Repr
```

`Batteries.Linter.getChecks` (definition, [line 79](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L79))

> `getChecks slow runOnly runAlways` produces a list of linters.
> `runOnly` is an optional list of names that should resolve to declarations with type `NamedLinter`.
> If populated, only these linters are run (regardless of the default configuration).
> `runAlways` is an optional list of names that should resolve to declarations with type
> `NamedLinter`. If populated, these linters are always run (regardless of their configuration).
> Specifying a linter in `runAlways` but not `runOnly` is an error.
> Otherwise, it uses all enabled linters in the environment tagged with `@[env_linter]`.
> If `slow` is false, it only uses the fast default tests.

```lean
def getChecks (slow : Bool) (runOnly : Option (List Name)) (runAlways : Option (List Name)) :
    CoreM (Array NamedLinter)
```

`Batteries.Linter.traceLintCore` (definition, [line 102](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L102))

> Traces via `IO.println` if `inIO` is `true`, and via `trace[...]` otherwise. It seems that
> `trace` messages in a running `CoreM` are not propagated through to `IO` in the current setup. We
> use `IO.println` directly instead of running `printTraces` at the end of our `CoreM` action so that
> trace messages are printed to stdout immediately, and are not lost if any part of the action hangs.
>
> This declaration is `macro_inline`, so it should have the same thunky behavior as `trace[...]`.

```lean
def traceLintCore (msg : String) (inIO : Bool) : CoreM Unit
```

`Batteries.Linter.traceLint` (definition, [line 114](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L114))

> Traces via `IO.println` if `inIO` is `true`, and via `trace[...]` otherwise. Prepends
> `currentModule` and `linter` (if present).
>
> This declaration is `macro_inline`, so it should have the same thunky behavior as `trace[...]`.

```lean
def traceLint (msg : String) (inIO : Bool) (currentModule linterName : Option Name := none) :
    CoreM Unit
```

`Batteries.Linter.lintBatchSize` (definition, [line 127](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L127))

> The number of declarations that a lint worker takes at a time. A larger batch means fewer updates
> to the shared job counter. A smaller batch spreads the work more evenly across the workers at the
> end of the run. The value 64 is not tuned. One counter update costs little next to the checks on
> 64 declarations, and a large library still gives each worker many batches.

```lean
def lintBatchSize : Nat
```

`Batteries.Linter.mapOnWorkers` (definition, [line 135](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L135))

> Maps `f` over `jobs` on at most `numWorkers` workers (at least one), and returns the results in
> no fixed order. Each worker takes the next job that no worker has taken, until no jobs remain.
> The workers use the cancellation token of the caller. An exception from `f` stops its worker and
> propagates. Changes that `f` makes to the Core state are discarded.

```lean
def mapOnWorkers (jobs : Array α) (numWorkers : Nat) (f : α → CoreM β) : CoreM (Array β)
```

`Batteries.Linter.lintDecl` (definition, [line 156](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L156))

> Runs `linter` on `decl` with separate Core and Meta state, a distinct name generator, and its own
> heartbeat budget. An exception from the linter becomes a `LINTER FAILED` message, except for an
> interrupt, which propagates.

```lean
def lintDecl (linter : NamedLinter) (decl : Name) (inIO : Bool) : CoreM (Option MessageData)
```

`Batteries.Linter.lintCore` (definition, [line 185](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L185))

> Runs the linters on the declarations in parallel, and returns the failures of each linter as a map
> from declaration to message. A linter skips a declaration whose `nolint` attribute names it.
> `LEAN_NUM_THREADS` sets the number of workers (by default, the hardware concurrency). Each worker
> lints batches of `lintBatchSize` declarations.
>
> If `localDecls` is given, linters with `isLocal` lint only those declarations (for example, the
> declarations of the modules a change touched), while the other linters still lint all of `decls`.

```lean
def lintCore (decls : Array Name) (linters : Array NamedLinter)
    -- For tracing:
    (currentModule : Option Name := none) (inIO : Bool := false)
    (localDecls : Option (Array Name) := none) :
    CoreM (Array (NamedLinter × Std.HashMap Name MessageData))
```

`Batteries.Linter.sortResults` (definition, [line 250](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L250))

> Sorts a map with declaration keys as names by line number.

```lean
def sortResults (results : Std.HashMap Name α) : CoreM <| Array (Name × α)
```

`Batteries.Linter.printWarning` (definition, [line 258](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L258))

> Formats a linter warning as `#check` command with comment.

```lean
def printWarning (declName : Name) (warning : MessageData) (useErrorFormat : Bool := false)
  (filePath : System.FilePath := default) : CoreM MessageData
```

`Batteries.Linter.printWarnings` (definition, [line 269](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L269))

> Formats a map of linter warnings using `print_warning`, sorted by line number.

```lean
def printWarnings (results : Std.HashMap Name MessageData) (filePath : System.FilePath := default)
    (useErrorFormat : Bool := false) : CoreM MessageData
```

`Batteries.Linter.groupedByFilename` (definition, [line 279](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L279))

> Formats a map of linter warnings grouped by filename with `-- filename` comments.
> The first `drop_fn_chars` characters are stripped from the filename.

```lean
def groupedByFilename (results : Std.HashMap Name MessageData) (useErrorFormat : Bool := false) :
    CoreM MessageData
```

`Batteries.Linter.formatLinterResults` (definition, [line 302](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L302))

> Formats the linter results as Lean code with comments and `#check` commands.

```lean
def formatLinterResults
    (results : Array (NamedLinter × Std.HashMap Name MessageData))
    (decls : Array Name)
    (groupByFilename : Bool)
    (whereDesc : String) (runSlowLinters : Bool)
    (verbose : LintVerbosity) (numLinters : Nat) (useErrorFormat : Bool := false) :
    CoreM MessageData
```

`Batteries.Linter.getDeclsInCurrModule` (definition, [line 334](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L334))

> Get the list of declarations in the current module.

```lean
def getDeclsInCurrModule : CoreM (Array Name)
```

`Batteries.Linter.getAllDecls` (definition, [line 338](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L338))

> Get the list of all declarations in the environment.

```lean
def getAllDecls : CoreM (Array Name)
```

`Batteries.Linter.getDeclsInPackage` (definition, [line 342](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L342))

> Get the list of all declarations in the specified package.

```lean
def getDeclsInPackage (pkg : Name) : CoreM (Array Name)
```

> Deprecated aliases for the former `Batteries.Tactic.Lint` namespace.

`Batteries.Tactic.Lint.LintVerbosity` (abbreviation, [line 420](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L420))

> Deprecated alias of `Batteries.Linter.LintVerbosity`.

```lean
abbrev LintVerbosity
```

`Batteries.Tactic.Lint.LintVerbosity.low` (alias, [line 423](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L423))

```lean
alias LintVerbosity.low
```

`Batteries.Tactic.Lint.LintVerbosity.medium` (alias, [line 425](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L425))

```lean
alias LintVerbosity.medium
```

`Batteries.Tactic.Lint.LintVerbosity.high` (alias, [line 427](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L427))

```lean
alias LintVerbosity.high
```

`Batteries.Tactic.Lint.getChecks` (alias, [line 429](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L429))

```lean
alias getChecks
```

`Batteries.Tactic.Lint.lintBatchSize` (alias, [line 431](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L431))

```lean
alias lintBatchSize
```

`Batteries.Tactic.Lint.mapOnWorkers` (alias, [line 433](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L433))

```lean
alias mapOnWorkers
```

`Batteries.Tactic.Lint.lintDecl` (alias, [line 435](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L435))

```lean
alias lintDecl
```

`Batteries.Tactic.Lint.lintCore` (alias, [line 437](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L437))

```lean
alias lintCore
```

`Batteries.Tactic.Lint.sortResults` (alias, [line 439](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L439))

```lean
alias sortResults
```

`Batteries.Tactic.Lint.printWarning` (alias, [line 441](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L441))

```lean
alias printWarning
```

`Batteries.Tactic.Lint.printWarnings` (alias, [line 443](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L443))

```lean
alias printWarnings
```

`Batteries.Tactic.Lint.groupedByFilename` (alias, [line 445](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L445))

```lean
alias groupedByFilename
```

`Batteries.Tactic.Lint.formatLinterResults` (alias, [line 447](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L447))

```lean
alias formatLinterResults
```

`Batteries.Tactic.Lint.getDeclsInCurrModule` (alias, [line 449](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L449))

```lean
alias getDeclsInCurrModule
```

`Batteries.Tactic.Lint.getAllDecls` (alias, [line 451](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L451))

```lean
alias getAllDecls
```

`Batteries.Tactic.Lint.getDeclsInPackage` (alias, [line 453](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L453))

```lean
alias getDeclsInPackage
```

`Batteries.Tactic.Lint.inProject` (alias, [line 455](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L455))

```lean
alias inProject
```

`Batteries.Tactic.Lint.traceLintCore` (alias, [line 457](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L457))

```lean
alias traceLintCore
```

`Batteries.Tactic.Lint.traceLint` (alias, [line 459](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean#L459))

```lean
alias traceLint
```

## Depends on

- [Basic linter types and attributes](basic.md)

## Sources

- [Batteries/Linter/Frontend.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Frontend.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Linter.Frontend.json)
