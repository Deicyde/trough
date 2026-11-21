---
catalog: module
lean: IO.Process.runCmdWithInput', IO.Process.runCmdWithInput
statement: formalized
proof: formalized
---

# Running external commands

`Batteries.Lean.IO.Process`, in [Batteries/Lean/IO/Process.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/IO/Process.lean), by Kim Morrison.

`IO.Process.runCmdWithInput'` (definition, [line 22](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/IO/Process.lean#L22))

> Pipe `input` into stdin of the spawned process,
> then return `(exitCode, stdout, stdErr)` upon completion.

```lean
def runCmdWithInput' (cmd : String) (args : Array String)
    (input : String := "") (throwFailure := true) : IO Output
```

`IO.Process.runCmdWithInput` (definition, [line 42](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/IO/Process.lean#L42))

> Pipe `input` into stdin of the spawned process,
> then return the entire content of stdout as a `String` upon completion.

```lean
def runCmdWithInput (cmd : String) (args : Array String)
    (input : String := "") (throwFailure := true) : IO String
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Lean/IO/Process.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/IO/Process.lean)
- [Declaration ledger](../../../../sources/batteries/Batteries.Lean.IO.Process.json)
