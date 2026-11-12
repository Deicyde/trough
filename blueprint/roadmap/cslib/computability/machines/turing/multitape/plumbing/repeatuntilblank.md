---
catalog: module
lean: Turing.MultiTapeTM.RepeatUntilBlank.blankTest, Turing.MultiTapeTM.repeatUntilBlank, Turing.MultiTapeTM.RepeatUntilBlank.step_check, Turing.MultiTapeTM.RepeatUntilBlank.exists_round, Turing.MultiTapeTM.transformsTapes_repeatUntilBlank
statement: formalized
proof: formalized
---

# Repeating a machine until a tape goes blank

`Cslib.Computability.Machines.Turing.MultiTape.Plumbing.RepeatUntilBlank`, in [Cslib/Computability/Machines/Turing/MultiTape/Plumbing/RepeatUntilBlank.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/RepeatUntilBlank.lean), by Christian Reitwiessner.

> `repeatUntilBlank i tm` runs `tm` repeatedly. After each round it reads the cell under the head of
> work tape `i` and halts if that cell is blank. Each round of a `Turing.MultiTapeTM.TransformsTapes`
> specification ends with every head on the first cell of its word, so the loop halts exactly when
> the word on tape `i` is empty. The body always runs at least once.
>
> ## Main results
>
> * `Turing.MultiTapeTM.transformsTapes_repeatUntilBlank`: a loop invariant preserved by every round
>   gives a specification of `repeatUntilBlank i tm`, with time bound `(rounds + 1) * (t + 1)` and
>   space bound `2 * k * s + k`.

`Turing.MultiTapeTM.RepeatUntilBlank.blankTest` (definition, [line 32](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/RepeatUntilBlank.lean#L32))

> The test of tape `i`: it halts if the cell under the head of tape `i` is blank and otherwise
> stays in its only state, moving no head.

```lean
public def RepeatUntilBlank.blankTest (i : Fin k) : MultiTapeTM k Symbol Unit
```

`Turing.MultiTapeTM.repeatUntilBlank` (abbreviation, [line 39](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/RepeatUntilBlank.lean#L39))

> `tm` combined with the test of tape `i`: halting of `tm` goes to the test, which halts the loop
> if the cell under the head of tape `i` is blank and otherwise restarts `tm`.

```lean
public noncomputable abbrev repeatUntilBlank (i : Fin k) (tm : MultiTapeTM k Symbol State) :
    MultiTapeTM k Symbol (State ⊕ Unit)
```

`Turing.MultiTapeTM.RepeatUntilBlank.step_check` (lemma, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/RepeatUntilBlank.lean#L50))

> From the test on a `wordsCfg` configuration, the machine halts if the word on tape `i` is empty
> and otherwise restarts `tm`, leaving the words unchanged.

```lean
lemma step_check (ws : Fin k → List Symbol) (out : List Symbol) :
    (repeatUntilBlank i tm).step (wordsCfg input (some (.inr ())) ws out) =
      wordsCfg input (if ws i = [] then none else some (.inl tm.q₀)) ws out
```

`Turing.MultiTapeTM.RepeatUntilBlank.exists_round` (lemma, [line 62](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/RepeatUntilBlank.lean#L62))

> One round of the loop. If `tm` transforms words satisfying `P` within `t` steps and `s` cells,
> then from `tm`'s initial state on such words `w` the loop has a run path of at most `t + 1` steps
> within `[-s, s]` to the words `w'` that `tm` leaves: the running steps of `tm`, and then reading
> tape `i`, which halts the loop if `w' i` is empty and otherwise starts the next round.

```lean
lemma exists_round {P : (input : List Symbol) → (Fin k → List Symbol) → Prop}
    {Q : (input : List Symbol) → (Fin k → List Symbol) → (Fin k → List Symbol) →
      List Symbol → Prop} {t s : ℕ}
    (h : TransformsTapes tm P Q t s) {w : Fin k → List Symbol} (out : List Symbol)
    (hP : P input w) :
    ∃ w' e, Q input w w' e ∧ ∃ p : (repeatUntilBlank i tm).RunPath input,
      p.head = wordsCfg input (some (.inl tm.q₀)) w out ∧
      p.last = wordsCfg input (if w' i = [] then none else some (.inl tm.q₀)) w' (out ++ e) ∧
      p.length ≤ t + 1 ∧ p.InWindow s
```

`Turing.MultiTapeTM.transformsTapes_repeatUntilBlank` (theorem, [line 97](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/RepeatUntilBlank.lean#L97))

> Let `P n` be a loop invariant after `n` rounds, on the words on the tapes and the word emitted
> so far. If each round `n < rounds` takes `P n` to `P (n + 1)` and leaves tape `i` non-empty, and
> the round after that takes `P rounds` to `R` and empties tape `i`, then `repeatUntilBlank i tm`
> takes `P 0` to `R`.
>
> Each of the `rounds + 1` rounds takes at most `t + 1` steps. No head leaves `[-s, s]`, since every
> round starts with all heads at cell `0` and uses at most `s` cells.

```lean
public theorem transformsTapes_repeatUntilBlank (i : Fin k) {tm : MultiTapeTM k Symbol State}
    {P : ℕ → (input : List Symbol) → (Fin k → List Symbol) → List Symbol → Prop}
    {R : (input : List Symbol) → (Fin k → List Symbol) → List Symbol → Prop} {rounds t s : ℕ}
    (hround : ∀ n < rounds, ∀ emitted, TransformsTapes tm (fun input ws => P n input ws emitted)
      (fun input _ ws' e => P (n + 1) input ws' (emitted ++ e) ∧ ws' i ≠ []) t s)
    (hstop : ∀ emitted, TransformsTapes tm (fun input ws => P rounds input ws emitted)
      (fun input _ ws' e => R input ws' (emitted ++ e) ∧ ws' i = []) t s) :
    TransformsTapes (repeatUntilBlank i tm) (fun input ws => P 0 input ws [])
      (fun input _ ws' emitted => R input ws' emitted)
      ((rounds + 1) * (t + 1)) (2 * k * s + k)
```

## Depends on

- [Machines as transformers of tape words](transformstapes.md)

## Proof depends on

- [Head movement along run paths](../tapelemmas.md)

## Sources

- [Cslib/Computability/Machines/Turing/MultiTape/Plumbing/RepeatUntilBlank.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/RepeatUntilBlank.lean)
