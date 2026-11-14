---
catalog: module
lean: Turing.MultiTapeTM.TransformsTapes, Turing.MultiTapeTM.TransformsTapes.imp, Turing.MultiTapeTM.TransformsTapes.mono, Turing.MultiTapeTM.transformsTapes_iff_nil_output, Turing.MultiTapeTM.nop, Turing.MultiTapeTM.step_nop, Turing.MultiTapeTM.runFrom_nop_one, Turing.MultiTapeTM.transformsTapes_nop
statement: formalized
proof: formalized
---

# Machines as transformers of tape words

`Cslib.Computability.Machines.Turing.MultiTape.Plumbing.TransformsTapes`, in [Cslib/Computability/Machines/Turing/MultiTape/Plumbing/TransformsTapes.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/TransformsTapes.lean), by Christian Reitwiessner, Samuel Schlesinger.

> The interface through which combinators use machines: a machine reads words from its work tapes
> and leaves words on them. A combinator composing such machines talks about words only, never about
> individual cells, head positions or the set of tapes a machine has touched.
>
> Configurations are described by *equalities*: `wordsCfg input q ws out` is the configuration whose
> work tape `i` holds exactly the word `ws i` (contents `tapeOfList (ws i)`, head at the start), with
> the input head at the start of the input and output `out`. A specification
> `TransformsTapes tm P Q t s` says: started on word-holding tapes satisfying `P`, the machine has a
> run path to the halted *normal form* `wordsCfg input none ws' (out ++ emitted)` (every head reset
> to its initial position, tapes blank outside their words, the word `emitted` appended to the
> output it was handed), with the new words related to the old ones by `Q`, taking at most `t` steps
> and visiting at most `s` work-tape cells. The time and space are those of the path, so
> specifications compose by joining their paths.
> Requiring this normal form is what lets specifications compose by rewriting: the halting
> configuration of one machine is already a valid start for the next, so which words survived a step
> is read off the equation, not re-established cell by cell.
>
> The output is described as the word the machine *appends*, never as an absolute value, so that a
> specification is insensitive to the output it is handed — which is what lets specifications
> compose: along a sequence the emitted words concatenate.
>
> ## Main definitions
>
> * `Turing.MultiTapeTM.TransformsTapes`: the specification format described above.
> * `Turing.MultiTapeTM.nop`: the machine that does nothing.
>
> ## Main results
>
> * `Turing.MultiTapeTM.TransformsTapes.imp`: strengthen the precondition, weaken the postcondition
>   and raise the bounds.
> * `Turing.MultiTapeTM.transformsTapes_iff_nil_output`: the generality in the ambient output is
>   free, so a concrete machine need only be run with no prior output.
> * `Turing.MultiTapeTM.transformsTapes_nop`: `nop` leaves every word as it was, the first machine of
>   the interface and the check that the format is inhabited as intended.

`Turing.MultiTapeTM.TransformsTapes` (definition, [line 66](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/TransformsTapes.lean#L66))

> `TransformsTapes tm P Q t s`: started in its initial state on tapes holding words `ws` that
> satisfy the precondition `P`, the machine has a run path of at most `t` steps, visiting at most `s`
> work-tape cells, to the halted configuration whose tapes hold words `ws'` and which has appended
> `emitted` to the output it was handed, with `Q input ws ws' emitted`.
>
> The bounds are numbers; a specification whose bounds depend on the data is a *family*
> `∀ j, TransformsTapes tm (P j) (Q j) (t j) (s j)` over one fixed machine.

```lean
def TransformsTapes (tm : MultiTapeTM k Symbol State)
    (P : (input : List Symbol) → (Fin k → List Symbol) → Prop)
    (Q : (input : List Symbol) → (Fin k → List Symbol) → (Fin k → List Symbol) →
      List Symbol → Prop)
    (t s : ℕ) : Prop
```

`Turing.MultiTapeTM.TransformsTapes.imp` (theorem, [line 78](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/TransformsTapes.lean#L78))

> A `TransformsTapes` statement can be read with a stronger precondition, a weaker postcondition
> and larger bounds.

```lean
theorem TransformsTapes.imp {tm : MultiTapeTM k Symbol State}
    {P P' : (input : List Symbol) → (Fin k → List Symbol) → Prop}
    {Q Q' : (input : List Symbol) → (Fin k → List Symbol) → (Fin k → List Symbol) →
      List Symbol → Prop}
    {t s t' s' : ℕ} (h : TransformsTapes tm P Q t s)
    (hP : ∀ input ws, P' input ws → P input ws)
    (hQ : ∀ input ws ws' emitted, P' input ws → Q input ws ws' emitted → Q' input ws ws' emitted)
    (ht : t ≤ t') (hs : s ≤ s') :
    TransformsTapes tm P' Q' t' s'
```

`Turing.MultiTapeTM.TransformsTapes.mono` (theorem, [line 93](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/TransformsTapes.lean#L93))

> A `TransformsTapes` statement can be read with larger bounds.

```lean
theorem TransformsTapes.mono {tm : MultiTapeTM k Symbol State}
    {P : (input : List Symbol) → (Fin k → List Symbol) → Prop}
    {Q : (input : List Symbol) → (Fin k → List Symbol) → (Fin k → List Symbol) →
      List Symbol → Prop}
    {t s t' s' : ℕ} (h : TransformsTapes tm P Q t s) (ht : t ≤ t') (hs : s ≤ s') :
    TransformsTapes tm P Q t' s'
```

`Turing.MultiTapeTM.transformsTapes_iff_nil_output` (theorem, [line 108](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/TransformsTapes.lean#L108))

> **The ambient output is a concern of sequencing, not of machines.** A specification holds for
> every prior output as soon as it holds for none, because a machine never reads what it has already
> written. This is where that generality is discharged, once, rather than by every caller: a concrete
> machine enters the interface by proving the right-hand side.
>
> The only consumer of the generality is `Turing.MultiTapeTM.transformsTapes_seq`, which runs the
> second machine after the first has emitted.

```lean
theorem transformsTapes_iff_nil_output {tm : MultiTapeTM k Symbol State}
    {P : (input : List Symbol) → (Fin k → List Symbol) → Prop}
    {Q : (input : List Symbol) → (Fin k → List Symbol) → (Fin k → List Symbol) →
      List Symbol → Prop} {t s : ℕ} :
    TransformsTapes tm P Q t s ↔ ∀ input ws, P input ws → ∃ ws' emitted, Q input ws ws' emitted ∧
      ∃ p : tm.RunPath input, p.head = wordsCfg input (some tm.q₀) ws [] ∧
        p.last = wordsCfg input none ws' emitted ∧ p.time ≤ t ∧ p.space ≤ s
```

`Turing.MultiTapeTM.nop` (definition, [line 128](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/TransformsTapes.lean#L128))

> The machine that does nothing: it halts on its first step, leaving the configuration
> unchanged.

```lean
def nop (k : ℕ) (Symbol : Type*) : MultiTapeTM k Symbol Unit
```

`Turing.MultiTapeTM.step_nop` (lemma, [line 134](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/TransformsTapes.lean#L134))

> A single step of `nop` halts and leaves the words alone.

```lean
lemma step_nop (ws : Fin k → List Symbol) (out : List Symbol) :
    (nop k Symbol).step (wordsCfg input (some ()) ws out) = wordsCfg input none ws out
```

`Turing.MultiTapeTM.runFrom_nop_one` (lemma, [line 141](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/TransformsTapes.lean#L141))

> `nop` reaches its halting configuration after exactly one step.

```lean
lemma runFrom_nop_one (ws : Fin k → List Symbol) (out : List Symbol) :
    (nop k Symbol).runFrom (wordsCfg input (some ()) ws out) 1 = wordsCfg input none ws out
```

`Turing.MultiTapeTM.transformsTapes_nop` (theorem, [line 148](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/TransformsTapes.lean#L148))

> **The machine that does nothing** halts in one step, leaving every word as it was and emitting
> nothing. Its heads never move, so it visits one cell per tape. This is the first machine of the
> interface: it checks that the specification format is inhabited exactly as intended.

```lean
theorem transformsTapes_nop (k : ℕ) (Symbol : Type*) :
    TransformsTapes (nop k Symbol) (fun _ _ => True)
      (fun _ ws ws' emitted => ws' = ws ∧ emitted = []) 1 k
```

## Depends on

- [Deterministic Multi-Tape Turing Machines](../deterministic.md)
- [Tapes holding words and configurations of such tapes](wordscfg.md)

## Sources

- [Cslib/Computability/Machines/Turing/MultiTape/Plumbing/TransformsTapes.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/TransformsTapes.lean)
