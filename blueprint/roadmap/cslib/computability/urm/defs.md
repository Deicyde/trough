---
catalog: module
lean: Cslib.URM.Instr, Cslib.URM.Instr.readsFrom, Cslib.URM.Instr.writesTo, Cslib.URM.Instr.maxRegister, Cslib.URM.Instr.shiftJumps, Cslib.URM.Instr.shiftRegisters, Cslib.URM.Regs, Cslib.URM.Regs.zero, Cslib.URM.Regs.read, Cslib.URM.Regs.write, Cslib.URM.Regs.ofInputs, Cslib.URM.Regs.output, Cslib.URM.Program, Cslib.URM.Program.maxRegister, Cslib.URM.Program.shiftJumps, Cslib.URM.Program.shiftRegisters, Cslib.URM.State, Cslib.URM.State.init, Cslib.URM.State.isHalted
statement: formalized
proof: formalized
---

# URM Core Definitions

`Cslib.Computability.URM.Defs`, in [Cslib/Computability/URM/Defs.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Defs.lean), by Jesse Alama.

> This file contains the core definitions for Unlimited Register Machines (URMs):
> instructions, register state, programs, and machine configurations.
>
> ## Main definitions
>
> - `URM.Instr`: The four URM instructions (Z, S, T, J)
> - `URM.Regs`: Register contents as a function `ℕ → ℕ`
> - `URM.Program`: A finite sequence of instructions
> - `URM.State`: Machine state (program counter + registers)
>
> ## References
>
> * [N.J. Cutland, *Computability: An Introduction to Recursive Function Theory*][Cutland1980]
> * [J.C. Shepherdson and H.E. Sturgis,
>   *Computability of Recursive Functions*][ShepherdsonSturgis1963]

> ## Instructions

`Cslib.URM.Instr` (inductive type, [line 44](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Defs.lean#L44))

> URM instructions.
> - `Z n`: Set register n to zero
> - `S n`: Increment register n by one
> - `T m n`: Transfer (copy) the contents of register m to register n
> - `J m n q`: If registers m and n have equal contents, jump to instruction q;
>              otherwise proceed to the next instruction

```lean
inductive Instr : Type where
  | Z : ℕ → Instr
  | S : ℕ → Instr
  | T : ℕ → ℕ → Instr
  | J : ℕ → ℕ → ℕ → Instr
deriving DecidableEq, Repr
```

`Cslib.URM.Instr.readsFrom` (definition, [line 55](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Defs.lean#L55))

> The registers read by an instruction.

```lean
def readsFrom : Instr → Finset ℕ
```

`Cslib.URM.Instr.writesTo` (definition, [line 63](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Defs.lean#L63))

> The register written to by an instruction, if any.

```lean
def writesTo : Instr → Option ℕ
```

`Cslib.URM.Instr.maxRegister` (definition, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Defs.lean#L71))

> The maximum register index referenced by an instruction.

```lean
def maxRegister : Instr → ℕ
```

`Cslib.URM.Instr.shiftJumps` (definition, [line 80](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Defs.lean#L80))

> Shift all jump targets in an instruction by `offset`.
> Used when concatenating programs to maintain correct jump destinations.

```lean
def shiftJumps (offset : ℕ) : Instr → Instr
```

`Cslib.URM.Instr.shiftRegisters` (definition, [line 89](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Defs.lean#L89))

> Shift all register references in an instruction by `offset`.
> Used to isolate register usage when composing programs.

```lean
def shiftRegisters (offset : ℕ) : Instr → Instr
```

> ## Register Contents

`Cslib.URM.Regs` (abbreviation, [line 103](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Defs.lean#L103))

> Register contents: maps register indices to natural number contents.
>
> Uses the functional representation `ℕ → ℕ` for efficiency with rewrites,
> following the advice from the `grind` tactic documentation.

```lean
abbrev Regs
```

`Cslib.URM.Regs.zero` (definition, [line 109](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Defs.lean#L109))

> The zero registers where all registers contain 0.

```lean
def zero : Regs
```

`Cslib.URM.Regs.read` (definition, [line 113](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Defs.lean#L113))

> Read the contents of register n.

```lean
def read (σ : Regs) (n : ℕ) : ℕ
```

`Cslib.URM.Regs.write` (definition, [line 117](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Defs.lean#L117))

> Write value v to register n.

```lean
def write (σ : Regs) (n : ℕ) (v : ℕ) : Regs
```

`Cslib.URM.Regs.ofInputs` (definition, [line 122](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Defs.lean#L122))

> Initialize registers with input values in registers 0, 1, ..., k-1.
> Registers beyond the inputs are initialized to 0.

```lean
def ofInputs (inputs : List ℕ) : Regs
```

`Cslib.URM.Regs.output` (definition, [line 126](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Defs.lean#L126))

> Extract output from register 0.

```lean
def output (σ : Regs) : ℕ
```

> ## Programs

`Cslib.URM.Program` (abbreviation, [line 133](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Defs.lean#L133))

> A URM program is a list of instructions.

```lean
abbrev Program
```

`Cslib.URM.Program.maxRegister` (definition, [line 139](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Defs.lean#L139))

> The maximum register index referenced by any instruction in the program.

```lean
def maxRegister (p : Program) : ℕ
```

`Cslib.URM.Program.shiftJumps` (definition, [line 146](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Defs.lean#L146))

> Shift all jump targets in a program by `offset`.
> Used when concatenating programs: the second program's jumps must be adjusted
> by the length of the first program.

```lean
def shiftJumps (p : Program) (offset : ℕ) : Program
```

`Cslib.URM.Program.shiftRegisters` (definition, [line 152](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Defs.lean#L152))

> Shift all register references in a program by `offset`.
> Used to isolate register usage when composing programs.

```lean
def shiftRegisters (p : Program) (offset : ℕ) : Program
```

> ## Machine State

`Cslib.URM.State` (structure, [line 160](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Defs.lean#L160))

> Machine state: program counter (0-indexed) and register contents.

```lean
structure State where
  /-- Program counter (0-indexed). -/
  pc : ℕ
  /-- Register contents. -/
  regs : Regs
```

`Cslib.URM.State.init` (definition, [line 171](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Defs.lean#L171))

> Initial state for a program with given inputs.
> The program counter starts at 0, and inputs are loaded into registers 0, 1, ....

```lean
def init (inputs : List ℕ) : State
```

`Cslib.URM.State.isHalted` (definition, [line 175](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Defs.lean#L175))

> A state is halted if the program counter is at or beyond the program length.

```lean
def isHalted (s : State) (p : Program) : Prop
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Computability/URM/Defs.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Defs.lean)
