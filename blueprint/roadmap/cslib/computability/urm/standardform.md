---
catalog: module
lean: Cslib.URM.Program.IsStandardForm, Cslib.URM.Program.toStandardForm, Cslib.URM.Program.toStandardForm_length, Cslib.URM.Program.toStandardForm_isStandardForm, Cslib.URM.Program.getElem?_toStandardForm, Cslib.URM.Program.toStandardForm_idempotent, Cslib.URM.straight_line_IsStandardForm, Cslib.URM.Step.toStandardForm, Cslib.URM.Steps.toStandardForm_halts, Cslib.URM.Halts.toStandardForm, Cslib.URM.Step.from_toStandardForm, Cslib.URM.Steps.from_toStandardForm_halts, Cslib.URM.Halts.of_toStandardForm, Cslib.URM.Halts.toStandardForm_iff, Cslib.URM.evalState_toStandardForm_regs, Cslib.URM.eval_toStandardForm, Cslib.URM.toStandardForm_equiv
statement: formalized
proof: formalized
---

# Standard Form Programs

`Cslib.Computability.URM.StandardForm`, in [Cslib/Computability/URM/StandardForm.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StandardForm.lean), by Jesse Alama.

> This file defines standard-form programs (those with bounded jump targets)
> and proves their execution properties.
>
> ## Main definitions
>
> - `Program.IsStandardForm`: all jump targets are bounded by program length
> - `Program.toStandardForm`: convert a program to standard form
>
> ## Main results
>
> - `straight_line_IsStandardForm`: straight-line programs are standard form
> - `Halts.toStandardForm_iff`: halting equivalence with normalized programs

> ## Standard Form Definitions

`Cslib.URM.Program.IsStandardForm` (definition, [line 36](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StandardForm.lean#L36))

> A program is in standard form if all jump targets are bounded by the program length.
> Jumps can target any instruction (0..length-1) or the "virtual halt" position (length).

```lean
def IsStandardForm (p : Program) : Prop
```

`Cslib.URM.Program.toStandardForm` (definition, [line 43](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StandardForm.lean#L43))

> Convert a program to standard form by capping all jump targets at the program length.

```lean
def toStandardForm (p : Program) : Program
```

`Cslib.URM.Program.toStandardForm_length` (theorem, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StandardForm.lean#L48))

> toStandardForm preserves program length.

```lean
theorem toStandardForm_length (p : Program) : p.toStandardForm.length = p.length
```

`Cslib.URM.Program.toStandardForm_isStandardForm` (theorem, [line 52](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StandardForm.lean#L52))

> toStandardForm produces a standard form program.

```lean
theorem toStandardForm_isStandardForm (p : Program) :
    p.toStandardForm.IsStandardForm
```

`Cslib.URM.Program.getElem?_toStandardForm` (theorem, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StandardForm.lean#L61))

> Accessing an instruction in toStandardForm gives the capJump'd instruction.

```lean
theorem getElem?_toStandardForm (p : Program) (i : ℕ) :
    p.toStandardForm[i]? = (p[i]?).map (Instr.capJump p.length)
```

`Cslib.URM.Program.toStandardForm_idempotent` (theorem, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StandardForm.lean#L67))

> toStandardForm is idempotent: applying it twice equals applying it once.

```lean
theorem toStandardForm_idempotent (p : Program) :
    p.toStandardForm.toStandardForm = p.toStandardForm
```

> ## Standard Form Properties

`Cslib.URM.straight_line_IsStandardForm` (theorem, [line 79](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StandardForm.lean#L79))

> Straight-line programs are in standard form.

```lean
theorem straight_line_IsStandardForm {p : Program} (hsl : p.IsStraightLine) :
    p.IsStandardForm
```

> ## Bisimulation
>
> `p` and `p.toStandardForm` are bisimilar: each step in one program corresponds to a
> step in the other that either reaches the same state or reaches a halted state with the
> same registers. This bisimulation implies functional equivalence (`eval_toStandardForm`).
> The key insight is that jumps with target `q > p.length` land in halted states in both
> programs.

`Cslib.URM.Step.toStandardForm` (theorem, [line 96](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StandardForm.lean#L96))

> Forward step correspondence: if p steps from s to s', then either:
> (1) p.toStandardForm steps from s to s' (same step), or
> (2) s' is halted in p, and p.toStandardForm steps to a state that is also halted
>     with the same registers (this only happens for jumps with unbounded targets).

```lean
theorem Step.toStandardForm {p : Program} {s s' : State} (hstep : Step p s s') :
    Step p.toStandardForm s s' ∨
    (s'.isHalted p ∧ ∃ s₂, Step p.toStandardForm s s₂ ∧
      s₂.isHalted p.toStandardForm ∧ s'.regs = s₂.regs)
```

`Cslib.URM.Steps.toStandardForm_halts` (theorem, [line 128](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StandardForm.lean#L128))

> Forward halting: if p reaches a halted state, p.toStandardForm reaches a halted state
> with the same registers.

```lean
theorem Steps.toStandardForm_halts {p : Program} {s s' : State}
    (hsteps : Steps p s s') (hhalted : s'.isHalted p) :
    ∃ s₂, Steps p.toStandardForm s s₂ ∧
      s₂.isHalted p.toStandardForm ∧ s'.regs = s₂.regs
```

`Cslib.URM.Halts.toStandardForm` (theorem, [line 145](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StandardForm.lean#L145))

> Forward halting theorem.

```lean
theorem Halts.toStandardForm {p : Program} {inputs : List ℕ} (h : Halts p inputs) :
    Halts p.toStandardForm inputs
```

`Cslib.URM.Step.from_toStandardForm` (theorem, [line 156](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StandardForm.lean#L156))

> Reverse step correspondence: if p.toStandardForm steps from s to s', then either:
> (1) p steps from s to s' (same step), or
> (2) s' is halted in p.toStandardForm, and p steps to a state that is also halted
>     with the same registers (this only happens for jumps with unbounded targets).

```lean
theorem Step.from_toStandardForm {p : Program} {s s' : State} (hstep : Step p.toStandardForm s s') :
    Step p s s' ∨
    (s'.isHalted p.toStandardForm ∧ ∃ s₂, Step p s s₂ ∧ s₂.isHalted p ∧ s'.regs = s₂.regs)
```

`Cslib.URM.Steps.from_toStandardForm_halts` (theorem, [line 170](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StandardForm.lean#L170))

> Reverse halting: if p.toStandardForm reaches a halted state, p reaches a halted state
> with the same registers.

```lean
theorem Steps.from_toStandardForm_halts {p : Program} {s s' : State}
    (hsteps : Steps p.toStandardForm s s') (hhalted : s'.isHalted p.toStandardForm) :
    ∃ s₂, Steps p s s₂ ∧ s₂.isHalted p ∧ s'.regs = s₂.regs
```

`Cslib.URM.Halts.of_toStandardForm` (theorem, [line 189](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StandardForm.lean#L189))

> Reverse halting theorem.

```lean
theorem Halts.of_toStandardForm {p : Program} {inputs : List ℕ}
    (h : Halts p.toStandardForm inputs) : Halts p inputs
```

`Cslib.URM.Halts.toStandardForm_iff` (theorem, [line 196](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StandardForm.lean#L196))

> Halting equivalence: original halts iff standard form halts.

```lean
theorem Halts.toStandardForm_iff {p : Program} {inputs : List ℕ} :
    Halts p inputs ↔ Halts p.toStandardForm inputs
```

> ### eval Preservation

`Cslib.URM.evalState_toStandardForm_regs` (theorem, [line 203](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StandardForm.lean#L203))

> Registers preservation: both reach states with the same registers.

```lean
theorem evalState_toStandardForm_regs {p : Program} {inputs : List ℕ}
    (hp : (evalState p inputs).Dom) (hq : (evalState p.toStandardForm inputs).Dom) :
    ((evalState p inputs).get hp).regs =
      ((evalState p.toStandardForm inputs).get hq).regs
```

`Cslib.URM.eval_toStandardForm` (theorem, [line 213](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StandardForm.lean#L213))

> eval equality: both programs produce the same partial result.

```lean
theorem eval_toStandardForm {p : Program} {inputs : List ℕ} :
    eval p inputs = eval p.toStandardForm inputs
```

`Cslib.URM.toStandardForm_equiv` (theorem, [line 225](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StandardForm.lean#L225))

> A program is equivalent to its standard form.

```lean
theorem toStandardForm_equiv (p : Program) : p.toStandardForm ≈ p
```

## Depends on

- [Straight-Line Programs](straightline.md)

## Sources

- [Cslib/Computability/URM/StandardForm.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/StandardForm.lean)
