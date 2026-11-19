---
catalog: module
lean: Cedar.SymCC.Decision, Cedar.SymCC.Solver, Cedar.SymCC.SolverM, Cedar.SymCC.SolverM.run, Cedar.SymCC.Solver.spawn, Cedar.SymCC.Solver.cvc5, Cedar.SymCC.Solver.streamWriter, Cedar.SymCC.Solver.fileWriter, Cedar.SymCC.Solver.bufferWriter, Cedar.SymCC.Solver.dummy, Cedar.SymCC.Solver.setLogic, Cedar.SymCC.Solver.setOption, Cedar.SymCC.Solver.setOptionProduceModels, Cedar.SymCC.Solver.comment, Cedar.SymCC.Solver.assert, Cedar.SymCC.Solver.defineFun, Cedar.SymCC.Solver.declareConst, Cedar.SymCC.Solver.declareFun, Cedar.SymCC.Solver.declareDatatype, Cedar.SymCC.Solver.checkSat, Cedar.SymCC.Solver.reset, Cedar.SymCC.Solver.exit, Cedar.SymCC.Solver.getModel
statement: formalized
proof: formalized
---

# Solver

`Cedar.SymCC.Solver`, in [Cedar/SymCC/Solver.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Solver.lean).

> This file defines a simple interface to an SMT solver running in a separate
> process. Callers communicate with the solver by issuing commands with
> s-expressions encoded as strings. The interface is based on
> [lean-smt](https://github.com/ufmg-smite/lean-smt/).
>
> Currently, we support only CVC5. The function `cvc5` creates a fresh CVC5 solver
> process. This function assumes that the environment variable `CVC5` contains the
> absolute path to the CVC5 executable.

`Cedar.SymCC.Decision` (inductive type, [line 34](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Solver.lean#L34))

```lean
public inductive Decision where
  | sat
  | unsat
  | unknown
deriving DecidableEq, Repr
```

`Cedar.SymCC.Solver` (structure, [line 56](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Solver.lean#L56))

> A Solver is an interpreter for SMTLib scripts, which are passed to the solver
> via its `smtLibInput` stream. Solvers optionally have an `smtLibOutput` stream
> to which they print the results of executing the commands received on the input
> stream. We assume that both the input and output streams conform to the SMTLib
> standard: the inputs are SMTLib script commands encoded as s-expressions, and
> the outputs are the s-expressions whose shape is determined by the standard for
> each command. We don't have an error stream here, since we configure solvers to
> run in quiet mode and not print anything to the error stream.

```lean
public structure Solver where
  smtLibInput : IO.FS.Stream
  smtLibOutput : Option IO.FS.Stream
  /--
    Tear-down action that releases any process/file resources backing the
    solver. For solvers that spawn an external SMT process this reaps the
    child to prevent zombie accumulation; for in-memory writer/dummy
    solvers this is a no-op. Run by `SolverM.run` after the user's
    `SolverM` action completes (success or failure).
  -/
  cleanup : IO Unit := pure ()
```

`Cedar.SymCC.SolverM` (abbreviation, [line 68](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Solver.lean#L68))

```lean
public abbrev SolverM (α)
```

`Cedar.SymCC.SolverM.run` (definition, [line 76](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Solver.lean#L76))

> Runs a `SolverM` action against `solver` and then invokes `solver.cleanup`.
> For process-backed solvers, cleanup tears down the underlying child process,
> so those solver values are single-use: callers must spawn a fresh solver
> (e.g. via `Solver.cvc5`) for each `SolverM.run` invocation.

```lean
public def SolverM.run (solver : Solver) (x : SolverM α) : IO α
```

`Cedar.SymCC.Solver.spawn` (definition, [line 89](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Solver.lean#L89))

> Returns a Solver for the given path and arguments. This function expects
> `path` to point to an SMT solver executable, and `args` to specify valid
> arguments to that solver.

```lean
public def spawn (path : String) (args : Array String) : IO Solver
```

`Cedar.SymCC.Solver.cvc5` (definition, [line 120](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Solver.lean#L120))

> Returns an instance of the CVC5 solver that is backed by the executable
> specified in the environment variable "CVC5".

```lean
public def cvc5 : IO Solver
```

`Cedar.SymCC.Solver.streamWriter` (definition, [line 132](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Solver.lean#L132))

> Returns a solver that writes all issued commands to the given stream `s`.
> Commands that produce output, such as `checkSat`, write the command to `s` and
> return values that are sound according to the SMTLib spec (but generally not
> useful). For example, `Solver.checkSat` returns `Decision.unknown`. This
> function expects `s` to be write-enabled.

```lean
public def streamWriter (s : IO.FS.Stream) : IO Solver
```

`Cedar.SymCC.Solver.fileWriter` (definition, [line 142](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Solver.lean#L142))

> Returns a solver that writes all issued commands to the given file handle `h`.
> Commands that produce output, such as `checkSat`, write the command to `h` and
> return values that are sound according to the SMTLib spec (but generally not
> useful). For example, `Solver.checkSat` returns `Decision.unknown`. This
> function expects `h` to be write-enabled.

```lean
public def fileWriter (h : IO.FS.Handle) : IO Solver
```

`Cedar.SymCC.Solver.bufferWriter` (definition, [line 151](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Solver.lean#L151))

> Returns a solver that writes all issued commands to the given buffer `b`.
> Commands that produce output, such as `checkSat`, write the command to `b` and
> return values that are sound according to the SMTLib spec (but generally not
> useful). For example, `Solver.checkSat` returns `Decision.unknown`.

```lean
public def bufferWriter (b : IO.Ref IO.FS.Stream.Buffer) : IO Solver
```

`Cedar.SymCC.Solver.dummy` (definition, [line 160](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Solver.lean#L160))

> Returns a solver that drops/ignores all issued commands.
> Commands that produce output, such as `checkSat`, return values that are sound
> according to the SMTLib spec (but generally not useful). For example,
> `Solver.checkSat` returns `Decision.unknown`.

```lean
public def dummy : IO Solver
```

`Cedar.SymCC.Solver.setLogic` (definition, [line 173](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Solver.lean#L173))

```lean
public def setLogic (logic : String) : SolverM Unit
```

`Cedar.SymCC.Solver.setOption` (definition, [line 176](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Solver.lean#L176))

```lean
public def setOption (opt val : String) : SolverM Unit
```

`Cedar.SymCC.Solver.setOptionProduceModels` (definition, [line 179](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Solver.lean#L179))

```lean
public def setOptionProduceModels (b : Bool) : SolverM Unit
```

`Cedar.SymCC.Solver.comment` (definition, [line 182](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Solver.lean#L182))

```lean
public def comment (comment : String) : SolverM Unit
```

`Cedar.SymCC.Solver.assert` (definition, [line 186](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Solver.lean#L186))

```lean
public def assert (expr : String) : SolverM Unit
```

`Cedar.SymCC.Solver.defineFun` (definition, [line 189](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Solver.lean#L189))

```lean
public def defineFun (id : String) (args : List (String × String)) (type expr : String) : SolverM Unit
```

`Cedar.SymCC.Solver.declareConst` (definition, [line 193](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Solver.lean#L193))

```lean
public def declareConst (id type : String) : SolverM Unit
```

`Cedar.SymCC.Solver.declareFun` (definition, [line 196](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Solver.lean#L196))

```lean
public def declareFun (id : String) (args : List String) (type : String) : SolverM Unit
```

`Cedar.SymCC.Solver.declareDatatype` (definition, [line 200](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Solver.lean#L200))

```lean
public def declareDatatype (id : String) (params : List String) (constructors : List String) : SolverM Unit
```

`Cedar.SymCC.Solver.checkSat` (definition, [line 212](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Solver.lean#L212))

```lean
public def checkSat : SolverM Decision
```

`Cedar.SymCC.Solver.reset` (definition, [line 221](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Solver.lean#L221))

```lean
public def reset : SolverM Unit
```

`Cedar.SymCC.Solver.exit` (definition, [line 224](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Solver.lean#L224))

```lean
public def exit : SolverM Unit
```

`Cedar.SymCC.Solver.getModel` (definition, [line 234](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Solver.lean#L234))

> Returns the model from the SMT solver, assuming that `checkSat` produced
> a `.sat` decision.  Note that this model extraction procedure assumes that
> the model strings follow the CVC5 format, where the model is enclosed in
> parentheses that are on a single line by themselves, i.e., opens with the line
> `(\n` and closes with the line `)\n`.

```lean
public def getModel : SolverM String
```

## Depends on

Its statements use no other Cedar module's declarations.

## Sources

- [Cedar/SymCC/Solver.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Solver.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.SymCC.Solver.json)
