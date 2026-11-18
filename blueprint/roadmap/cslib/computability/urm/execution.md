---
catalog: module
lean: Cslib.URM.Step, Cslib.URM.Steps, Cslib.URM.Step.deterministic, Cslib.URM.Step.no_step_of_halted, Cslib.URM.Step.preserves_register, Cslib.URM.isHalted_iff_normal, Cslib.URM.step_confluent, Cslib.URM.Steps.preserves_register, Cslib.URM.Steps.eq_of_halts, Cslib.URM.Halts, Cslib.URM.halts_iff_normalizable, Cslib.URM.Diverges, Cslib.URM.HaltsWithResult, Cslib.URM.HaltsWithResult.toHalts, Cslib.URM.evalState, Cslib.URM.evalState_spec, Cslib.URM.Halts.toHaltsWithResult, Cslib.URM.eval, Cslib.URM.haltsWithResult_iff_eval, Cslib.URM.ProgramEquiv, Cslib.URM.ProgramEquiv.equivalence
statement: formalized
proof: formalized
---

# URM Execution Semantics

`Cslib.Computability.URM.Execution`, in [Cslib/Computability/URM/Execution.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Execution.lean), by Jesse Alama.

> Single-step and multi-step execution semantics for URMs.
>
> ## Main definitions
>
> - `URM.Step`: Single-step execution relation
> - `URM.Steps`: Multi-step execution (reflexive-transitive closure of `Step`)
> - `URM.Halts`: A program halts on given inputs
> - `URM.Diverges`: A program diverges on given inputs
> - `URM.HaltsWithResult`: A program halts on given inputs with a specific result
>
> Bridge lemmas:
> - `isHalted_iff_normal`: `s.isHalted p ↔ Relation.Normal (Step p) s`
> - `halts_iff_normalizable`: `Halts p inputs ↔ Relation.Normalizable (Step p) (State.init inputs)`
> - `step_confluent`: The step relation is confluent (follows from determinism)
>
> ## Notation (scoped to `URM` namespace)
>
> Standard computability theory notation:
> - `p ↓ inputs` — program `p` halts on inputs
> - `p ↑ inputs` — program `p` diverges on inputs
> - `p ↓ inputs ≫ result` — program `p` halts on inputs with result in R[0]
>
> ## Main results
>
> - `Step.deterministic`: The step relation is deterministic
> - `step_confluent`: The step relation is confluent (from determinism)
> - `haltsWithResult_iff_eval`: `p ↓ inputs ≫ result ↔ eval p inputs = Part.some result`

`Cslib.URM.Step` (inductive type, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Execution.lean#L59))

> Single-step execution relation for URMs.
>
> Each constructor corresponds to one of the four instruction types:
> - `zero`: Execute `Z n` (set register n to 0)
> - `succ`: Execute `S n` (increment register n)
> - `transfer`: Execute `T m n` (copy register m to register n)
> - `jump_eq`: Execute `J m n q` when registers m and n are equal (jump to q)
> - `jump_ne`: Execute `J m n q` when registers m and n differ (proceed to next)

```lean
inductive Step : State → State → Prop where
  | zero {s : State} {n : ℕ}
      (h : p[s.pc]? = some (Instr.Z n)) :
      Step s ⟨s.pc + 1, s.regs.write n 0⟩
  | succ {s : State} {n : ℕ}
      (h : p[s.pc]? = some (Instr.S n)) :
      Step s ⟨s.pc + 1, s.regs.write n (s.regs.read n + 1)⟩
  | transfer {s : State} {m n : ℕ}
      (h : p[s.pc]? = some (Instr.T m n)) :
      Step s ⟨s.pc + 1, s.regs.write n (s.regs.read m)⟩
  | jump_eq {s : State} {m n q : ℕ}
      (h : p[s.pc]? = some (Instr.J m n q))
      (heq : s.regs.read m = s.regs.read n) :
      Step s ⟨q, s.regs⟩
  | jump_ne {s : State} {m n q : ℕ}
      (h : p[s.pc]? = some (Instr.J m n q))
      (hne : s.regs.read m ≠ s.regs.read n) :
      Step s ⟨s.pc + 1, s.regs⟩
```

`Cslib.URM.Steps` (abbreviation, [line 79](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Execution.lean#L79))

> Multi-step execution: the reflexive-transitive closure of `Step`.

```lean
abbrev Steps : State → State → Prop
```

`Cslib.URM.Step.deterministic` (theorem, [line 87](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Execution.lean#L87))

> The step relation is deterministic: each state has at most one successor.

```lean
theorem deterministic : Relator.RightUnique (Step p)
```

`Cslib.URM.Step.no_step_of_halted` (theorem, [line 90](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Execution.lean#L90))

> A halted state has no successor in the step relation.

```lean
theorem no_step_of_halted {s s' : State} (hhalted : s.isHalted p) : ¬Step p s s'
```

`Cslib.URM.Step.preserves_register` (theorem, [line 97](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Execution.lean#L97))

> A single step preserves registers not written to by the current instruction.
>
> This is a fundamental property of URM execution: each instruction modifies at most
> one register (Z, S, T write to one register; J writes to none).

```lean
theorem preserves_register {s s' : State} {r : ℕ}
    (hstep : Step p s s')
    (hr : ∀ instr, p[s.pc]? = some instr → instr.writesTo ≠ some r) :
    s'.regs.read r = s.regs.read r
```

> ### Step Properties

`Cslib.URM.isHalted_iff_normal` (theorem, [line 113](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Execution.lean#L113))

> A state is halted iff it is normal (has no successor) in the reduction system.

```lean
theorem isHalted_iff_normal {p : Program} {s : State} :
    s.isHalted p ↔ Relation.Normal (Step p) s
```

`Cslib.URM.step_confluent` (theorem, [line 135](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Execution.lean#L135))

> The step relation is confluent.

```lean
theorem step_confluent (p : Program) : Relation.Confluent (Step p)
```

`Cslib.URM.Steps.preserves_register` (theorem, [line 144](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Execution.lean#L144))

> Multi-step execution preserves registers not written by any executed instruction.

```lean
theorem preserves_register {s s' : State} {r : ℕ}
    (hsteps : Steps p s s')
    (hr : ∀ instr, instr ∈ p → instr.writesTo ≠ some r) :
    s'.regs.read r = s.regs.read r
```

`Cslib.URM.Steps.eq_of_halts` (theorem, [line 156](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Execution.lean#L156))

> If two halted states are reachable from the same start, they are equal.
>
> This follows from confluence: since `Step p` is confluent and both `s₁` and `s₂`
> are normal forms reachable from `init`, they must be equal.

```lean
theorem eq_of_halts {init s₁ s₂ : State}
    (h1 : Steps p init s₁) (hh1 : s₁.isHalted p)
    (h2 : Steps p init s₂) (hh2 : s₂.isHalted p) : s₁ = s₂
```

`Cslib.URM.Halts` (definition, [line 172](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Execution.lean#L172))

> A program halts on given inputs if execution reaches a halted state.
>
> This is equivalent to `(Step p).Normalizable (State.init inputs)` —
> see `halts_iff_normalizable`.

```lean
def Halts (inputs : List ℕ) : Prop
```

`Cslib.URM.halts_iff_normalizable` (theorem, [line 176](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Execution.lean#L176))

> Halting is equivalent to normalizability in the reduction system.

```lean
theorem halts_iff_normalizable {p : Program} {inputs : List ℕ} :
    Halts p inputs ↔ Relation.Normalizable (Step p) (State.init inputs)
```

`Cslib.URM.Diverges` (definition, [line 181](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Execution.lean#L181))

> A program diverges on given inputs if it does not halt.

```lean
def Diverges (inputs : List ℕ) : Prop
```

`Cslib.URM.HaltsWithResult` (definition, [line 184](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Execution.lean#L184))

> A program halts on given inputs with a specific result in R[0].

```lean
def HaltsWithResult (inputs : List ℕ) (result : ℕ) : Prop
```

`Cslib.URM.HaltsWithResult.toHalts` (theorem, [line 200](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Execution.lean#L200))

> If a program halts with a result, it halts.

```lean
theorem toHalts {inputs : List ℕ} {result : ℕ}
    (h : p ↓ inputs ≫ result) : p ↓ inputs
```

`Cslib.URM.evalState` (definition, [line 208](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Execution.lean#L208))

> Evaluation returning the full halting state.

```lean
noncomputable def evalState (inputs : List ℕ) : Part State
```

`Cslib.URM.evalState_spec` (theorem, [line 212](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Execution.lean#L212))

> Specification: the state from evalState satisfies Steps and isHalted.

```lean
theorem evalState_spec {inputs : List ℕ} (h : (evalState p inputs).Dom) :
    let s := (evalState p inputs).get h
    Steps p (State.init inputs) s ∧ s.isHalted p
```

`Cslib.URM.Halts.toHaltsWithResult` (theorem, [line 222](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Execution.lean#L222))

> If a program halts, it halts with the output of the final state.

```lean
theorem toHaltsWithResult {inputs : List ℕ} (h : p ↓ inputs) :
    p ↓ inputs ≫ ((evalState p inputs).get h).regs.output
```

`Cslib.URM.eval` (definition, [line 232](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Execution.lean#L232))

> Evaluation as a partial function using `Part`.
> Defined when the program halts, returning the value in register 0.

```lean
noncomputable def eval (inputs : List ℕ) : Part ℕ
```

`Cslib.URM.haltsWithResult_iff_eval` (theorem, [line 236](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Execution.lean#L236))

> A program halts with result `a` iff evaluation returns `Part.some a`.

```lean
theorem haltsWithResult_iff_eval {inputs : List ℕ} {result : ℕ} :
    p ↓ inputs ≫ result ↔ eval p inputs = Part.some result
```

`Cslib.URM.ProgramEquiv` (definition, [line 252](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Execution.lean#L252))

> Two programs are equivalent if they produce the same result for all inputs.

```lean
def ProgramEquiv (p q : Program) : Prop
```

`Cslib.URM.ProgramEquiv.equivalence` (theorem, [line 256](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Execution.lean#L256))

> Program equivalence is an equivalence relation.

```lean
theorem ProgramEquiv.equivalence : Equivalence ProgramEquiv
```

## Depends on

- [URM Core Definitions](defs.md)
- [Relations: Definitions](../../foundations/relation/defs.md)

## Proof depends on

- [Relations: Confluence](../../foundations/relation/confluence.md)

## Sources

- [Cslib/Computability/URM/Execution.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Execution.lean)
