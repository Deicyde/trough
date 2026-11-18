---
catalog: module
lean: Batteries.Tactic.Lint.LintVerbosity, Batteries.Tactic.Lint.getChecks, Batteries.Tactic.Lint.traceLintCore, Batteries.Tactic.Lint.traceLint, Batteries.Tactic.Lint.lintBatchSize, Batteries.Tactic.Lint.mapOnWorkers, Batteries.Tactic.Lint.lintDecl, Batteries.Tactic.Lint.lintCore, Batteries.Tactic.Lint.sortResults, Batteries.Tactic.Lint.printWarning, Batteries.Tactic.Lint.printWarnings, Batteries.Tactic.Lint.groupedByFilename, Batteries.Tactic.Lint.formatLinterResults, Batteries.Tactic.Lint.getDeclsInCurrModule, Batteries.Tactic.Lint.getAllDecls, Batteries.Tactic.Lint.getDeclsInPackage
statement: formalized
proof: formalized
---

# Linter frontend and commands

`Batteries.Tactic.Lint.Frontend`, in [Batteries/Tactic/Lint/Frontend.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Frontend.lean), by Floris van Doorn, Robert Y. Lewis, Gabriel Ebner.

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
> A linter defined with the name `Batteries.Tactic.Lint.myNewCheck` can be run with `#lint myNewCheck`
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

`Batteries.Tactic.Lint.LintVerbosity` (inductive type, [line 61](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Frontend.lean#L61))

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

`Batteries.Tactic.Lint.getChecks` (definition, [line 78](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Frontend.lean#L78))

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

`Batteries.Tactic.Lint.traceLintCore` (definition, [line 101](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Frontend.lean#L101))

> Traces via `IO.println` if `inIO` is `true`, and via `trace[...]` otherwise. It seems that
> `trace` messages in a running `CoreM` are not propagated through to `IO` in the current setup. We
> use `IO.println` directly instead of running `printTraces` at the end of our `CoreM` action so that
> trace messages are printed to stdout immediately, and are not lost if any part of the action hangs.
>
> This declaration is `macro_inline`, so it should have the same thunky behavior as `trace[...]`.

```lean
def traceLintCore (msg : String) (inIO : Bool) : CoreM Unit
```

`Batteries.Tactic.Lint.traceLint` (definition, [line 113](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Frontend.lean#L113))

> Traces via `IO.println` if `inIO` is `true`, and via `trace[...]` otherwise. Prepends
> `currentModule` and `linter` (if present).
>
> This declaration is `macro_inline`, so it should have the same thunky behavior as `trace[...]`.

```lean
def traceLint (msg : String) (inIO : Bool) (currentModule linterName : Option Name := none) :
    CoreM Unit
```

`Batteries.Tactic.Lint.lintBatchSize` (definition, [line 126](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Frontend.lean#L126))

> The number of declarations that a lint worker takes at a time. A larger batch means fewer updates
> to the shared job counter. A smaller batch spreads the work more evenly across the workers at the
> end of the run. The value 64 is not tuned. One counter update costs little next to the checks on
> 64 declarations, and a large library still gives each worker many batches.

```lean
def lintBatchSize : Nat
```

`Batteries.Tactic.Lint.mapOnWorkers` (definition, [line 134](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Frontend.lean#L134))

> Maps `f` over `jobs` on at most `numWorkers` workers (at least one), and returns the results in
> no fixed order. Each worker takes the next job that no worker has taken, until no jobs remain.
> The workers use the cancellation token of the caller. An exception from `f` stops its worker and
> propagates. Changes that `f` makes to the Core state are discarded.

```lean
def mapOnWorkers (jobs : Array α) (numWorkers : Nat) (f : α → CoreM β) : CoreM (Array β)
```

`Batteries.Tactic.Lint.lintDecl` (definition, [line 155](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Frontend.lean#L155))

> Runs `linter` on `decl` with separate Core and Meta state, a distinct name generator, and its own
> heartbeat budget. An exception from the linter becomes a `LINTER FAILED` message, except for an
> interrupt, which propagates.

```lean
def lintDecl (linter : NamedLinter) (decl : Name) (inIO : Bool) : CoreM (Option MessageData)
```

`Batteries.Tactic.Lint.lintCore` (definition, [line 184](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Frontend.lean#L184))

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

`Batteries.Tactic.Lint.sortResults` (definition, [line 249](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Frontend.lean#L249))

> Sorts a map with declaration keys as names by line number.

```lean
def sortResults (results : Std.HashMap Name α) : CoreM <| Array (Name × α)
```

`Batteries.Tactic.Lint.printWarning` (definition, [line 257](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Frontend.lean#L257))

> Formats a linter warning as `#check` command with comment.

```lean
def printWarning (declName : Name) (warning : MessageData) (useErrorFormat : Bool := false)
  (filePath : System.FilePath := default) : CoreM MessageData
```

`Batteries.Tactic.Lint.printWarnings` (definition, [line 268](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Frontend.lean#L268))

> Formats a map of linter warnings using `print_warning`, sorted by line number.

```lean
def printWarnings (results : Std.HashMap Name MessageData) (filePath : System.FilePath := default)
    (useErrorFormat : Bool := false) : CoreM MessageData
```

`Batteries.Tactic.Lint.groupedByFilename` (definition, [line 278](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Frontend.lean#L278))

> Formats a map of linter warnings grouped by filename with `-- filename` comments.
> The first `drop_fn_chars` characters are stripped from the filename.

```lean
def groupedByFilename (results : Std.HashMap Name MessageData) (useErrorFormat : Bool := false) :
    CoreM MessageData
```

`Batteries.Tactic.Lint.formatLinterResults` (definition, [line 301](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Frontend.lean#L301))

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

`Batteries.Tactic.Lint.getDeclsInCurrModule` (definition, [line 333](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Frontend.lean#L333))

> Get the list of declarations in the current module.

```lean
def getDeclsInCurrModule : CoreM (Array Name)
```

`Batteries.Tactic.Lint.getAllDecls` (definition, [line 337](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Frontend.lean#L337))

> Get the list of all declarations in the environment.

```lean
def getAllDecls : CoreM (Array Name)
```

`Batteries.Tactic.Lint.getDeclsInPackage` (definition, [line 341](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Frontend.lean#L341))

> Get the list of all declarations in the specified package.

```lean
def getDeclsInPackage (pkg : Name) : CoreM (Array Name)
```

## Depends on

- [Basic linter types and attributes](basic.md)

## Sources

- [Batteries/Tactic/Lint/Frontend.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Frontend.lean)
