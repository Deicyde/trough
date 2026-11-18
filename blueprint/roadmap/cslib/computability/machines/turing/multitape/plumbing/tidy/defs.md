---
catalog: module
lean: Turing.MultiTapeTM.ComputesTidilyInTimeAndSpace, Turing.MultiTapeTM.computesTidily_iff, Turing.MultiTapeTM.ComputesTidilyInTimeAndSpace.mono, Turing.MultiTapeTM.ComputesFunTidilyInTimeAndSpace, Turing.MultiTapeTM.ComputesFunTidilyInTimeAndSpace.mono, Turing.MultiTapeTM.ComputableTidilyInTimeAndSpace, Turing.MultiTapeTM.ComputableTidilyInTimeAndSpaceOfLength, Turing.MultiTapeTM.ComputableTidilyInTimeAndSpace.mono
statement: formalized
proof: formalized
---

# Tidy computations

`Cslib.Computability.Machines.Turing.MultiTape.Plumbing.Tidy.Defs`, in [Cslib/Computability/Machines/Turing/MultiTape/Plumbing/Tidy/Defs.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/Tidy/Defs.lean), by Christian Reitwiessner.

> A machine computes *tidily* if it clears its work tapes before halting and moves all tape heads
> to their initial position.
> This means tidy computations can easily be iterated and when applied to a subset of work tapes,
> a combinator can run a tidy machine as a subroutine and rely on nothing but the word it emits.
>
> A tidy computation is defined as a `Turing.MultiTapeTM.TransformsTapes` from blank work tapes to
> blank work tapes, so the lemmas about tape transformations apply to it directly. The three
> notions below add tidiness to `Turing.MultiTapeTM.ComputesInTimeAndSpace`,
> `Turing.MultiTapeTM.ComputesFunInTimeAndSpace` and `Turing.MultiTapeTM.ComputableInTimeAndSpace`.
>
> ## Main definitions
>
> * `Turing.MultiTapeTM.ComputesTidilyInTimeAndSpace`: a machine computes an output tidily.
> * `Turing.MultiTapeTM.ComputesFunTidilyInTimeAndSpace`: a machine computes a function tidily.
> * `Turing.MultiTapeTM.ComputableTidilyInTimeAndSpace`: some machine with binary alphabet and
>   finitely many states computes a function tidily.
> * `Turing.MultiTapeTM.ComputableTidilyInTimeAndSpaceOfLength`: the same, with bounds on the length
>   of the encoded input.
>
> ## Main results
>
> * `Turing.MultiTapeTM.computesTidily_iff`: a tidy computation is a single run path between
>   `Turing.MultiTapeTM.wordsCfg` configurations within the time and space bounds.

> ### Tidy computations

`Turing.MultiTapeTM.ComputesTidilyInTimeAndSpace` (abbreviation, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/Tidy/Defs.lean#L50))

> `ComputesTidilyInTimeAndSpace tm input output t s`: started on `input` with blank work tapes,
> `tm` halts within `t` steps and `s` work-tape cells, having emitted `output`, with every work tape
> blank and every head back at its starting cell.

```lean
abbrev ComputesTidilyInTimeAndSpace (tm : MultiTapeTM k Symbol State)
    (input output : List Symbol) (t s : ℕ) : Prop
```

`Turing.MultiTapeTM.computesTidily_iff` (theorem, [line 57](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/Tidy/Defs.lean#L57))

> A tidy computation is a single run path between `Turing.MultiTapeTM.wordsCfg` configurations
> with blank work tapes, which emits the output, within the time and space bounds.

```lean
theorem computesTidily_iff {input output : List Symbol} :
    tm.ComputesTidilyInTimeAndSpace input output t s ↔
      ∃ p : tm.RunPath input, p.head = wordsCfg input (some tm.q₀) (fun _ => []) [] ∧
        p.last = wordsCfg input none (fun _ => []) output ∧ p.time ≤ t ∧ p.space ≤ s
```

`Turing.MultiTapeTM.ComputesTidilyInTimeAndSpace.mono` (theorem, [line 69](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/Tidy/Defs.lean#L69))

> Resource bounds can be weakened.

```lean
theorem ComputesTidilyInTimeAndSpace.mono {input output : List Symbol} {t' s' : ℕ}
    (h : tm.ComputesTidilyInTimeAndSpace input output t s) (ht : t ≤ t') (hs : s ≤ s') :
    tm.ComputesTidilyInTimeAndSpace input output t' s'
```

> ### Tidily computing a function

`Turing.MultiTapeTM.ComputesFunTidilyInTimeAndSpace` (definition, [line 80](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/Tidy/Defs.lean#L80))

> `ComputesFunTidilyInTimeAndSpace tm encIn encOut f t s`: for every `a`, the machine computes
> `encOut (f a)` from `encIn a` tidily, within `t a` steps and `s a` cells.

```lean
def ComputesFunTidilyInTimeAndSpace (tm : MultiTapeTM k Symbol State)
    (encIn : α ↪ List Symbol) (encOut : β ↪ List Symbol) (f : α → β) (t s : α → ℕ) : Prop
```

`Turing.MultiTapeTM.ComputesFunTidilyInTimeAndSpace.mono` (theorem, [line 85](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/Tidy/Defs.lean#L85))

> Resource bounds can be weakened independently on every input.

```lean
theorem ComputesFunTidilyInTimeAndSpace.mono {encIn : α ↪ List Symbol} {encOut : β ↪ List Symbol}
    {f : α → β} {t s t' s' : α → ℕ} (h : ComputesFunTidilyInTimeAndSpace tm encIn encOut f t s)
    (ht : ∀ a, t a ≤ t' a) (hs : ∀ a, s a ≤ s' a) :
    ComputesFunTidilyInTimeAndSpace tm encIn encOut f t' s'
```

> ### Tidy computability

`Turing.MultiTapeTM.ComputableTidilyInTimeAndSpace` (definition, [line 95](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/Tidy/Defs.lean#L95))

> Some machine with binary alphabet and finitely many states computes `f` tidily within the
> bounds `t` and `s`. The bounds include the cost of restoring the tapes.

```lean
def ComputableTidilyInTimeAndSpace (f : α → β) (encIn : α ↪ List Bool) (encOut : β ↪ List Bool)
    (t s : α → ℕ) : Prop
```

`Turing.MultiTapeTM.ComputableTidilyInTimeAndSpaceOfLength` (abbreviation, [line 103](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/Tidy/Defs.lean#L103))

> `Turing.MultiTapeTM.ComputableTidilyInTimeAndSpace` with the bounds `t` and `s` evaluated at the
> length of the encoded input: the tidy analog of
> `Turing.MultiTapeTM.ComputableInTimeAndSpaceOfLength`.

```lean
abbrev ComputableTidilyInTimeAndSpaceOfLength (f : α → β) (encIn : α ↪ List Bool)
    (encOut : β ↪ List Bool) (t s : ℕ → ℕ) : Prop
```

`Turing.MultiTapeTM.ComputableTidilyInTimeAndSpace.mono` (theorem, [line 109](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/Tidy/Defs.lean#L109))

> Tidy computability is monotone in the resource bounds.

```lean
theorem ComputableTidilyInTimeAndSpace.mono {f : α → β} {encIn : α ↪ List Bool}
    {encOut : β ↪ List Bool} {t s t' s' : α → ℕ}
    (h : ComputableTidilyInTimeAndSpace f encIn encOut t s)
    (ht : ∀ a, t a ≤ t' a) (hs : ∀ a, s a ≤ s' a) :
    ComputableTidilyInTimeAndSpace f encIn encOut t' s'
```

## Depends on

- [Machines as transformers of tape words](../transformstapes.md)

## Sources

- [Cslib/Computability/Machines/Turing/MultiTape/Plumbing/Tidy/Defs.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/Tidy/Defs.lean)
