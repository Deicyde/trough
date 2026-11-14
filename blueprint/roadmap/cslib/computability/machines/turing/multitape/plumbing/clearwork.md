---
catalog: module
lean: Turing.MultiTapeTM.clearWork, Turing.MultiTapeTM.transformsTapes_clearWork, Turing.MultiTapeTM.transformsTapes_clearWork_tapeEmb
statement: formalized
proof: formalized
---

# A machine that clears a work tape

`Cslib.Computability.Machines.Turing.MultiTape.Plumbing.ClearWork`, in [Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ClearWork.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ClearWork.lean), by Christian Reitwiessner.

> `clearWork Symbol` erases the word on its work tape and returns the head to the start. It never
> moves the input head and never outputs. It is the sequential composition of two one-tape machines:
>
> * `forwardWork Symbol` moves the head right over the word until it reads the first blank, the
>   frontier just past the word, and halts there (see `Plumbing.ForwardWork`).
> * `rewindWork Symbol (some none)` rewinds the head to the start, erasing every symbol it walks
>   over.
>
> On a word of length `l` the forward pass takes `l + 1` steps and the erasing rewind `l + 2` steps.
> The head stays within the cells `-1, …, l`, so the machine runs in time `3 * (l + 1)` and space
> `l + 2`; placed on tape `i` of `k` tapes, the remaining tapes contribute one cell each.
>
> ## Main results
>
> * `Turing.MultiTapeTM.clearWork`: the one-tape machine that clears its tape.
> * `Turing.MultiTapeTM.transformsTapes_clearWork`: `clearWork` replaces the word on its tape by the
>   empty word.
> * `Turing.MultiTapeTM.transformsTapes_clearWork_tapeEmb`: placed on tape `i` of a `k`-tape machine
>   it does so on that tape and leaves every other tape unchanged.

`Turing.MultiTapeTM.clearWork` (definition, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ClearWork.lean#L45))

> The one-tape machine that clears its tape: it moves to the end of the word and erases it on
> the way back.

```lean
public noncomputable def clearWork (Symbol : Type*) :
    MultiTapeTM 1 Symbol (Unit ⊕ RewindWorkState)
```

`Turing.MultiTapeTM.transformsTapes_clearWork` (theorem, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ClearWork.lean#L51))

> **The machine that clears its work tape** replaces the word on it by the empty word, in at most
> `3 * (w.length + 1)` steps and `w.length + 2` cells.

```lean
public theorem transformsTapes_clearWork (w : List Symbol) :
    TransformsTapes (clearWork Symbol) (fun _ ws => ws 0 = w)
      (fun _ _ ws' emitted => ws' = (fun _ => []) ∧ emitted = [])
      (3 * (w.length + 1)) (w.length + 2)
```

> ### Clearing one of several work tapes

`Turing.MultiTapeTM.transformsTapes_clearWork_tapeEmb` (theorem, [line 86](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ClearWork.lean#L86))

> **The machine that clears a work tape**, placed on tape `i` of a `k`-tape machine, replaces the
> word on that tape by the empty word and leaves every other tape unchanged, in at most
> `3 * (w.length + 1)` steps and `w.length + 1 + k` cells.

```lean
public theorem transformsTapes_clearWork_tapeEmb (i : Fin k) (w : List Symbol) :
    TransformsTapes ((clearWork Symbol).extendTapes (tapeEmb i)) (fun _ ws => ws i = w)
      (fun _ ws ws' emitted => ws' = Function.update ws i [] ∧ emitted = [])
      (3 * (w.length + 1)) (w.length + 1 + k)
```

## Depends on

- [Extending a machine with additional work tapes](extendtapes.md)
- [A machine that moves to the end of a word](forwardwork.md)
- [A machine that rewinds a work-tape head](rewindwork.md)
- [Sequential composition of machines on shared tapes](sequential.md)

## Sources

- [Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ClearWork.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ClearWork.lean)
