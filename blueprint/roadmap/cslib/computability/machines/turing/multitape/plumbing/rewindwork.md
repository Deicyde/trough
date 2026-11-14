---
catalog: module
lean: Turing.MultiTapeTM.RewindWorkState, Turing.MultiTapeTM.rewindWork, Turing.MultiTapeTM.runFrom_rewindWork, Turing.MultiTapeTM.runFrom_rewindWork_none, Turing.MultiTapeTM.runFrom_rewindWork_erase, Turing.MultiTapeTM.workTapePos_runFrom_rewindWork
statement: formalized
proof: formalized
---

# A machine that rewinds a work-tape head

`Cslib.Computability.Machines.Turing.MultiTape.Plumbing.RewindWork`, in [Cslib/Computability/Machines/Turing/MultiTape/Plumbing/RewindWork.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/RewindWork.lean), by Christian Reitwiessner, Samuel Schlesinger.

> A machine that moves the head of its work tape to the left end of its contents and halts. It
> optionally writes a certain symbol to or clears the cells it moves over while traveling to the
> left. The input tape is not modified. This machine can be run between two phases of a computation
> to re-normalise a work-tape head without disturbing anything else.
>
> In its initial state `start` the machine takes one unconditional step left, into state `scan`. In
> state `scan` it walks left over symbols, writing `write` to every cell it leaves; on the first
> blank it moves the head right and halts. By default `write` is `none` and the machine writes
> nothing; with `write := some none` it erases the part of the word it walks over.
>
> This is a one-tape machine; to rewind tape `i` of a `k`-tape machine, place it there with
> `Turing.MultiTapeTM.tapeEmb` and transport its run with
> `Turing.MultiTapeTM.runFrom_tapeEmb`. The input head, the output and every other tape are then
> untouched by construction.
>
> ## Main results
>
> * `Turing.MultiTapeTM.rewindWork`: the one-tape machine that rewinds its head to the start of its
>   word.
> * `Turing.MultiTapeTM.runFrom_rewindWork`: its run from the initial state, with the special cases
>   `Turing.MultiTapeTM.runFrom_rewindWork_none` (nothing is written) and
>   `Turing.MultiTapeTM.runFrom_rewindWork_erase` (the whole word is erased).
> * `Turing.MultiTapeTM.workTapePos_runFrom_rewindWork`: the rewound head stays within `[-1, p]`.

`Turing.MultiTapeTM.RewindWorkState` (inductive type, [line 46](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/RewindWork.lean#L46))

> The control states of the work-tape-rewinding machine: `start` takes one unconditional step
> left, `scan` walks left towards the start of the word.

```lean
public inductive RewindWorkState : Type
  | start
  | scan
  deriving DecidableEq
```

`Turing.MultiTapeTM.rewindWork` (definition, [line 57](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/RewindWork.lean#L57))

> The one-tape rewinding machine. In state `start` it moves its head left, unconditionally, and
> enters state `scan`. In state `scan` it writes `write` over a symbol and moves left, staying in
> `scan`; on the first blank it moves right and halts. The input head never moves and nothing is
> ever output.

```lean
public def rewindWork (Symbol : Type*) (write : Option (Option Symbol) := none) :
    MultiTapeTM 1 Symbol RewindWorkState
```

`Turing.MultiTapeTM.runFrom_rewindWork` (theorem, [line 128](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/RewindWork.lean#L128))

> **The run of the one-tape machine that rewinds its head.** Started with the tape holding a word
> `w` and the head at a position `p ≤ w.length` — inside the word or at the frontier just past it —
> after `p + 2` steps the machine has halted with the head back at position `0`, `write` applied to
> the cells `0, …, p - 1` and nothing else changed.

```lean
public theorem runFrom_rewindWork (write : Option (Option Symbol)) (ip : Fin (input.length + 2))
    (t : ℤ → Option Symbol) (out : List Symbol) {w : List Symbol} (hw : t = tapeOfList w) {p : ℕ}
    (hp : p ≤ w.length) :
    (rewindWork Symbol write).runFrom
        ⟨some (rewindWork Symbol write).q₀, ip, fun _ => t, fun _ => (p : ℤ), out⟩ (p + 2) =
      ⟨none, ip, fun _ z => if 0 ≤ z ∧ z < p then write.getD (t z) else t z, fun _ => 0, out⟩
```

`Turing.MultiTapeTM.runFrom_rewindWork_none` (theorem, [line 140](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/RewindWork.lean#L140))

> **Rewinding without writing** changes nothing but the position of the head.

```lean
public theorem runFrom_rewindWork_none (ip : Fin (input.length + 2)) (t : ℤ → Option Symbol)
    (out : List Symbol) {w : List Symbol} (hw : t = tapeOfList w) {p : ℕ} (hp : p ≤ w.length) :
    (rewindWork Symbol).runFrom
        ⟨some (rewindWork Symbol).q₀, ip, fun _ => t, fun _ => (p : ℤ), out⟩ (p + 2) =
      ⟨none, ip, fun _ => t, fun _ => 0, out⟩
```

`Turing.MultiTapeTM.runFrom_rewindWork_erase` (theorem, [line 148](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/RewindWork.lean#L148))

> **Rewinding while erasing** from the frontier of the word leaves the tape blank.

```lean
public theorem runFrom_rewindWork_erase (ip : Fin (input.length + 2)) (t : ℤ → Option Symbol)
    (out : List Symbol) {w : List Symbol} (hw : t = tapeOfList w) :
    (rewindWork Symbol (some none)).runFrom
        ⟨some (rewindWork Symbol (some none)).q₀, ip, fun _ => t, fun _ => (w.length : ℤ), out⟩
        (w.length + 2) =
      ⟨none, ip, fun _ _ => none, fun _ => 0, out⟩
```

`Turing.MultiTapeTM.workTapePos_runFrom_rewindWork` (theorem, [line 165](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/RewindWork.lean#L165))

> At every step, the head is within `[-1, p]`: it walks from its start `p ≤ w.length` down to
> `-1` and back to `0`, where it stays.

```lean
public theorem workTapePos_runFrom_rewindWork (write : Option (Option Symbol))
    (ip : Fin (input.length + 2)) (t : ℤ → Option Symbol) (out : List Symbol) {w : List Symbol}
    (hw : t = tapeOfList w) {p : ℕ} (hp : p ≤ w.length) (m : ℕ) :
    ((rewindWork Symbol write).runFrom
        ⟨some (rewindWork Symbol write).q₀, ip, fun _ => t, fun _ => (p : ℤ), out⟩
        m).workTapePos 0 ∈ Set.Icc (-1) (p : ℤ)
```

## Depends on

- [Deterministic Multi-Tape Turing Machines](../deterministic.md)
- [Tapes holding words and configurations of such tapes](wordscfg.md)

## Sources

- [Cslib/Computability/Machines/Turing/MultiTape/Plumbing/RewindWork.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/RewindWork.lean)
