---
catalog: module
lean: Turing.MultiTapeTM.forwardWork, Turing.MultiTapeTM.ForwardWork.runFrom_walk, Turing.MultiTapeTM.runFrom_forwardWork, Turing.MultiTapeTM.workTapePos_runFrom_forwardWork
statement: formalized
proof: formalized
---

# A machine that moves to the end of a word

`Cslib.Computability.Machines.Turing.MultiTape.Plumbing.ForwardWork`, in [Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ForwardWork.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ForwardWork.lean), by Christian Reitwiessner.

> `forwardWork Symbol` moves the head of its work tape to the right over the word it holds and halts
> on the frontier, the first blank cell just past the word. It never modifies a tape, never moves the
> input head and never outputs.
>
> On a word of length `l`, started with the head at cell `p ≤ l`, the machine takes `l - p + 1` steps
> and the head stays within the cells `p, …, l`.
>
> This is a one-tape machine; to move the head of tape `i` of a `k`-tape machine to the end of its
> word, place it there with `Turing.MultiTapeTM.tapeEmb` and transport its run with
> `Turing.MultiTapeTM.runFrom_tapeEmb`. The input head, the output and every other tape are then
> untouched by construction.
>
> ## Main results
>
> * `Turing.MultiTapeTM.forwardWork`: the one-tape machine that moves its head to the frontier of
>   its word.
> * `Turing.MultiTapeTM.runFrom_forwardWork`: its run from the initial state.
> * `Turing.MultiTapeTM.workTapePos_runFrom_forwardWork`: its head stays within `[p, w.length]`.

`Turing.MultiTapeTM.forwardWork` (definition, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ForwardWork.lean#L41))

> The one-tape machine that moves its head to the end of its word. Over a symbol it moves right;
> on the first blank it halts without moving.

```lean
public def forwardWork (Symbol : Type*) : MultiTapeTM 1 Symbol Unit
```

`Turing.MultiTapeTM.ForwardWork.runFrom_walk` (lemma, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ForwardWork.lean#L53))

> Walking right over the word: from cell `p`, after `n` steps with `p + n ≤ w.length` the head
> is at cell `p + n`.

```lean
lemma runFrom_walk {w : List Symbol} {p : ℕ} (n : ℕ) (hn : p + n ≤ w.length) :
    (forwardWork Symbol).runFrom
        ⟨some (), inpos, fun _ => tapeOfList w, fun _ => (p : ℤ), out⟩ n =
      ⟨some (), inpos, fun _ => tapeOfList w, fun _ => (p : ℤ) + n, out⟩
```

`Turing.MultiTapeTM.runFrom_forwardWork` (theorem, [line 72](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ForwardWork.lean#L72))

> **The run of the machine that moves to the end of the word.** Started with the tape holding a
> word `w` and the head at a cell `p` with `p + n = w.length`, after `n + 1` steps the machine has
> halted with the head on the frontier `w.length` and nothing else changed.

```lean
public theorem runFrom_forwardWork (inpos : Fin (input.length + 2)) (w : List Symbol)
    (out : List Symbol) {p n : ℕ} (hpn : p + n = w.length) :
    (forwardWork Symbol).runFrom
        ⟨some (forwardWork Symbol).q₀, inpos, fun _ => tapeOfList w, fun _ => (p : ℤ), out⟩
        (n + 1) =
      ⟨none, inpos, fun _ => tapeOfList w, fun _ => (w.length : ℤ), out⟩
```

`Turing.MultiTapeTM.workTapePos_runFrom_forwardWork` (theorem, [line 83](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ForwardWork.lean#L83))

> At every step, the head is within `[p, w.length]`.

```lean
public theorem workTapePos_runFrom_forwardWork (inpos : Fin (input.length + 2))
    (w : List Symbol) (out : List Symbol) {p : ℕ} (hp : p ≤ w.length) (m : ℕ) :
    ((forwardWork Symbol).runFrom
        ⟨some (forwardWork Symbol).q₀, inpos, fun _ => tapeOfList w, fun _ => (p : ℤ), out⟩
        m).workTapePos 0 ∈ Set.Icc (p : ℤ) w.length
```

## Depends on

- [Deterministic Multi-Tape Turing Machines](../deterministic.md)
- [Tapes holding words and configurations of such tapes](wordscfg.md)

## Sources

- [Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ForwardWork.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ForwardWork.lean)
