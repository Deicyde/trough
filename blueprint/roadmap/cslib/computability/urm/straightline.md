---
catalog: module
lean: Cslib.URM.Program.IsStraightLine, Cslib.URM.Program.IsStraightLine.append, Cslib.URM.Program.IsStraightLine.cons, Cslib.URM.Program.IsStraightLine.singleton, Cslib.URM.Step.of_nonJump, Cslib.URM.straight_line_halts_from_regs, Cslib.URM.straight_line_halts, Cslib.URM.straightLinefinalState, Cslib.URM.straightLinefinalState_spec, Cslib.URM.straightLineFinalRegs, Cslib.URM.straightLineFinalRegs_eq_of_halted, Cslib.URM.straight_line_state_at_pc
statement: formalized
proof: formalized
---

# Straight-Line Programs

`Cslib.Computability.URM.StraightLine`, in [Cslib/Computability/URM/StraightLine.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StraightLine.lean), by Jesse Alama.

> This file defines straight-line programs (those without jumps) and proves
> they always halt exactly at their length.
>
> ## Main definitions
>
> - `Program.IsStraightLine`: a program contains no jump instructions
>
> ## Main results
>
> - `straight_line_halts`: straight-line programs always halt
> - `straightLinefinalState`: final state after running a straight-line program

> ## Straight-Line Programs

`Cslib.URM.Program.IsStraightLine` (definition, [line 33](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StraightLine.lean#L33))

> A program is "straight-line" if it contains no jump instructions.

```lean
def Program.IsStraightLine (p : Program) : Prop
```

`Cslib.URM.Program.IsStraightLine.append` (theorem, [line 40](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StraightLine.lean#L40))

> Append preserves straight-line property.

```lean
theorem Program.IsStraightLine.append {p q : Program}
    (hp : p.IsStraightLine) (hq : q.IsStraightLine) :
    (p ++ q).IsStraightLine
```

`Cslib.URM.Program.IsStraightLine.cons` (theorem, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StraightLine.lean#L48))

> Cons of non-jumping instruction preserves straight-line.

```lean
theorem Program.IsStraightLine.cons {instr : Instr} {p : Program}
    (hinstr : ¬instr.IsJump) (hp : p.IsStraightLine) :
    Program.IsStraightLine (instr :: p)
```

`Cslib.URM.Program.IsStraightLine.singleton` (theorem, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StraightLine.lean#L56))

> Singleton non-jumping instruction is straight-line.

```lean
theorem Program.IsStraightLine.singleton {instr : Instr}
    (h : ¬instr.IsJump) : Program.IsStraightLine [instr]
```

> ## Straight-Line Program Execution

`Cslib.URM.Step.of_nonJump` (theorem, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StraightLine.lean#L65))

> A non-jumping instruction produces a step that increments PC by 1.

```lean
theorem Step.of_nonJump {p : Program} {s : State} (hlt : s.pc < p.length)
    (hnonjump : ¬(p[s.pc]'hlt).IsJump) :
    ∃ s', Step p s s' ∧ s'.pc = s.pc + 1
```

`Cslib.URM.straight_line_halts_from_regs` (theorem, [line 83](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StraightLine.lean#L83))

> Straight-line programs halt from any starting registers, not just State.init.
> Useful for chaining: after running one program, we can run the next
> straight-line segment from whatever registers we're in.

```lean
theorem straight_line_halts_from_regs {p : Program} (hsl : p.IsStraightLine) (r : Regs) :
    ∃ s, Steps p ⟨0, r⟩ s ∧ s.isHalted p ∧ s.pc = p.length
```

`Cslib.URM.straight_line_halts` (theorem, [line 99](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StraightLine.lean#L99))

> A straight-line program halts on any input.

```lean
theorem straight_line_halts {p : Program} (hsl : p.IsStraightLine) (inputs : List ℕ) :
    Halts p inputs
```

`Cslib.URM.straightLinefinalState` (definition, [line 106](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StraightLine.lean#L106))

> The halting state for a straight-line program starting from registers r.
> Wraps Classical.choose to hide it from the API.

```lean
noncomputable def straightLinefinalState {p : Program}
    (hsl : p.IsStraightLine) (r : Regs) : State
```

`Cslib.URM.straightLinefinalState_spec` (theorem, [line 112](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StraightLine.lean#L112))

> Specification: the state from straightLinefinalState satisfies Steps, isHalted,
> and has pc = p.length.

```lean
theorem straightLinefinalState_spec {p : Program} (hsl : p.IsStraightLine) (r : Regs) :
    let s := straightLinefinalState hsl r
    Steps p ⟨0, r⟩ s ∧ s.isHalted p ∧ s.pc = p.length
```

`Cslib.URM.straightLineFinalRegs` (definition, [line 118](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StraightLine.lean#L118))

> The final registers after running a straight-line program from given starting registers.

```lean
noncomputable def straightLineFinalRegs {p : Program} (hsl : p.IsStraightLine) (r : Regs) : Regs
```

`Cslib.URM.straightLineFinalRegs_eq_of_halted` (theorem, [line 122](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StraightLine.lean#L122))

> For a straight-line program, s.regs equals straightLineFinalRegs if halted from r.

```lean
theorem straightLineFinalRegs_eq_of_halted {p : Program} (hsl : p.IsStraightLine)
    (r : Regs) (s : State) (hsteps : Steps p ⟨0, r⟩ s) (hhalted : s.isHalted p) :
    s.regs = straightLineFinalRegs hsl r
```

`Cslib.URM.straight_line_state_at_pc` (theorem, [line 130](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StraightLine.lean#L130))

> In a straight-line program, we can characterize the state at any intermediate pc.
> This gives us the state after executing instructions 0..pc-1.

```lean
theorem straight_line_state_at_pc {p : Program} (hsl : p.IsStraightLine)
    (r : Regs) (targetPc : ℕ) (htarget : targetPc ≤ p.length) :
    ∃ s, Steps p ⟨0, r⟩ s ∧ s.pc = targetPc
```

## Depends on

- [URM Basic Lemmas](basic.md)
- [URM Execution Semantics](execution.md)

## Sources

- [Cslib/Computability/URM/StraightLine.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StraightLine.lean)
