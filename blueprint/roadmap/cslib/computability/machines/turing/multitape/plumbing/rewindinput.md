---
catalog: module
lean: Turing.MultiTapeTM.RewindState, Turing.MultiTapeTM.rewindInput, Turing.MultiTapeTM.runFrom_rewindInput, Turing.MultiTapeTM.exists_runPath_rewindInput
statement: formalized
proof: formalized
---

# A machine that rewinds the input head

`Cslib.Computability.Machines.Turing.MultiTape.Plumbing.RewindInput`, in [Cslib/Computability/Machines/Turing/MultiTape/Plumbing/RewindInput.lean](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/RewindInput.lean), by Christian Reitwiessner.

> A two-state machine that, when started in its initial state at any input-head position, returns the
> head to position 1 (the first input symbol when the input is nonempty, otherwise the right boundary)
> and halts there. It has no work tapes at all and never outputs, so running it in between two phases
> of a computation re-normalizes the input head without disturbing anything else: place it inside a
> machine with `k` work tapes with `Turing.MultiTapeTM.noTapes` and transport its run with
> `Turing.MultiTapeTM.runFrom_noTapes`, which leaves every work tape and work head where it was.
>
> In its initial state `start` the machine moves the input head one cell left and enters state `walk`.
> The input head is clamped at the left boundary, so this has no effect if the head already is at
> position `0`, and it moves a head at the right boundary `input.length + 1` back onto the input.
> In state `walk` the machine moves left over symbols. Since the input tape holds a list of
> (non-blank) symbols, the first blank to the left of the head is the cell at position `0`; the
> halting transition moves right, onto position `1`.
>
> From position `p` the run halts after `p + 1` steps, or after `2` steps if `p = 0`.
>
> ## Main results
>
> * `Turing.MultiTapeTM.rewindInput`: the machine that rewinds the input head.
> * `Turing.MultiTapeTM.runFrom_rewindInput`: its run from the initial state.
> * `Turing.MultiTapeTM.exists_runPath_rewindInput`: its run path inside a machine with `k` work
>   tapes, started on any configuration.

`Turing.MultiTapeTM.RewindState` (inductive type, [line 44](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/RewindInput.lean#L44))

> The control states of the rewinding machine: `start` takes one unconditional step left,
> `walk` moves left towards the left boundary of the input.

```lean
public inductive RewindState : Type
  | start
  | walk
  deriving DecidableEq
```

`Turing.MultiTapeTM.rewindInput` (definition, [line 59](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/RewindInput.lean#L59))

> The rewinding machine. In state `start` it moves the input head left, unconditionally, and
> enters `walk`. In state `walk` it moves left over a symbol; on the first blank it moves right and
> halts. The machine has no work tapes and nothing is output.

```lean
public def rewindInput (Symbol : Type*) : MultiTapeTM 0 Symbol RewindState
```

`Turing.MultiTapeTM.runFrom_rewindInput` (theorem, [line 101](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/RewindInput.lean#L101))

> From its initial state at input position `p` the machine halts after `p - 1 + 2` steps, with
> the input head at position `1` and everything else unchanged.

```lean
public theorem runFrom_rewindInput (p : Fin (input.length + 2))
    (tapes : Fin 0 → ℤ → Option Symbol) (heads : Fin 0 → ℤ) (out : List Symbol) :
    (rewindInput Symbol).runFrom ⟨some (rewindInput Symbol).q₀, p, tapes, heads, out⟩
      (p.val - 1 + 2) = ⟨none, 1, tapes, heads, out⟩
```

`Turing.MultiTapeTM.exists_runPath_rewindInput` (theorem, [line 114](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/RewindInput.lean#L114))

> **Rewinding the input inside a machine with `k` work tapes.** Started on any configuration, the
> rewinding machine halts after `p - 1 + 2` steps, where `p` is the position of the input head. The
> input head ends at position `1`; the work tapes, their heads and the output are unchanged, and
> each work tape costs one cell.

```lean
public theorem exists_runPath_rewindInput {k : ℕ} {State : Type*}
    (c : Cfg k Symbol State input) :
    ∃ p : ((rewindInput Symbol).extendTapes (noTapes k)).RunPath input,
      p.head = c.withState (some (rewindInput Symbol).q₀) ∧
      p.last = ⟨none, 1, c.workTapes, c.workTapePos, c.output⟩ ∧
      p.length = c.inputPos.val - 1 + 2 ∧ p.space ≤ k
```

## Depends on

- [Extending a machine with additional work tapes](extendtapes.md)

## Sources

- [Cslib/Computability/Machines/Turing/MultiTape/Plumbing/RewindInput.lean at 7c95c37f](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/RewindInput.lean)
- [Declaration ledger](../../../../../../../sources/cslib/Cslib.Computability.Machines.Turing.MultiTape.Plumbing.RewindInput.json)
