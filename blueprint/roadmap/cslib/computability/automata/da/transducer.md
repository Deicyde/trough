---
catalog: module
lean: Cslib.Automata.SequentialTransducer, Cslib.Automata.SubsequentialTransducer, Cslib.Automata.SequentialTransducer.toSubsequential, Cslib.Automata.SubsequentialTransducer.OutputBoundedBy, Cslib.Automata.SubsequentialTransducer.exists_outputBoundedBy_of_finite, Cslib.Automata.SubsequentialTransducer.evalFrom, Cslib.Automata.SubsequentialTransducer.evalFrom_unique, Cslib.Automata.SubsequentialTransducer.eval, Cslib.Automata.SequentialTransducer.evalFrom, Cslib.Automata.SequentialTransducer.evalFrom_unique, Cslib.Automata.SequentialTransducer.eval
statement: formalized
proof: formalized
---

# Sequential and subsequential transducers

`Cslib.Computability.Automata.DA.Transducer`, in [Cslib/Computability/Automata/DA/Transducer.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Automata/DA/Transducer.lean), by Christian Reitwiessner.

> A sequential transducer is a deterministic automaton that emits a word per transition.
> A subsequential transducer can also output a final word at the end of the input. The output on a
> complete input word is the concatenation of the output words along the run of the automaton,
> followed by the final output of the last state. A transducer translates an input word into
> exactly this output.
>
> The transducers here are total. Every state has a transition for each input symbol, and every
> state of a subsequential transducer has a final output. The state type may be infinite.
>
> ## Main definitions
>
> * `Cslib.Automata.SequentialTransducer` extends a deterministic automaton with a word emitted on
>   each transition. `Cslib.Automata.SubsequentialTransducer` adds a final output word per state.
> * `Cslib.Automata.SequentialTransducer.toSubsequential` equips a sequential transducer with
>   empty final output.
> * `Cslib.Automata.SequentialTransducer.evalFrom` and
>   `Cslib.Automata.SubsequentialTransducer.evalFrom` compute the output from a given state.
> * `Cslib.Automata.SequentialTransducer.eval` and `Cslib.Automata.SubsequentialTransducer.eval`
>   compute the output on a complete input word from the start state. They define the translation
>   relation of each kind of transducer.
> * `Cslib.Automata.SubsequentialTransducer.OutputBoundedBy` bounds the length of each word
>   emitted on a transition or at end of input.
>
> ## Main results
>
> * `Cslib.Automata.SubsequentialTransducer.exists_outputBoundedBy_of_finite` bounds the output
>   words of a transducer with finitely many states and input symbols.
> * `Cslib.Automata.SequentialTransducer.evalFrom_unique` and
>   `Cslib.Automata.SubsequentialTransducer.evalFrom_unique` characterize the output by its
>   defining equations.
>
> ## References
>
> * [S. Mihov and K. U. Schulz, *Finite-State Techniques*, Chapter 5][MihovSchulz2019]

`Cslib.Automata.SequentialTransducer` (structure, [line 58](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Automata/DA/Transducer.lean#L58))

> A deterministic automaton that emits a word on each transition.

```lean
structure SequentialTransducer (State InSymbol OutSymbol : Type*) extends DA State InSymbol where
  /-- The output word emitted by a transition. -/
  emit (s : State) (c : InSymbol) : List OutSymbol
```

`Cslib.Automata.SubsequentialTransducer` (structure, [line 63](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Automata/DA/Transducer.lean#L63))

> A sequential transducer that emits a final word at the end of the input.

```lean
structure SubsequentialTransducer (State InSymbol OutSymbol : Type*)
    extends SequentialTransducer State InSymbol OutSymbol where
  /-- The output word at end of input. -/
  finalOut (s : State) : List OutSymbol
```

`Cslib.Automata.SequentialTransducer.toSubsequential` (definition, [line 74](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Automata/DA/Transducer.lean#L74))

> Regard a sequential transducer as subsequential by emitting nothing at end of input.

```lean
def toSubsequential (transducer : SequentialTransducer State InSymbol OutSymbol) :
    SubsequentialTransducer State InSymbol OutSymbol
```

`Cslib.Automata.SubsequentialTransducer.OutputBoundedBy` (definition, [line 87](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Automata/DA/Transducer.lean#L87))

> Every transition output and every final output has length at most `m`. The input `none`
> stands for the end of the input, where the final output is emitted.

```lean
def OutputBoundedBy (m : ℕ) : Prop
```

`Cslib.Automata.SubsequentialTransducer.exists_outputBoundedBy_of_finite` (theorem, [line 92](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Automata/DA/Transducer.lean#L92))

> A transducer with finitely many states and input symbols has a uniform bound on the length
> of its transition and final outputs.

```lean
theorem exists_outputBoundedBy_of_finite [Finite State] [Finite InSymbol] :
    ∃ m, transducer.OutputBoundedBy m
```

`Cslib.Automata.SubsequentialTransducer.evalFrom` (definition, [line 100](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Automata/DA/Transducer.lean#L100))

> The output of `transducer` on an input word when starting from state `q`.

```lean
def evalFrom (transducer : SubsequentialTransducer State InSymbol OutSymbol) (q : State) :
    List InSymbol → List OutSymbol
```

`Cslib.Automata.SubsequentialTransducer.evalFrom_unique` (theorem, [line 106](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Automata/DA/Transducer.lean#L106))

> The defining equations of `evalFrom` uniquely determine it.

```lean
theorem evalFrom_unique {spec : State → List InSymbol → List OutSymbol}
    (hfinal : ∀ q, spec q [] = transducer.finalOut q)
    (hstep : ∀ q a w, spec q (a :: w) = transducer.emit q a ++ spec (transducer.tr q a) w) :
    transducer.evalFrom = spec
```

`Cslib.Automata.SubsequentialTransducer.eval` (abbreviation, [line 116](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Automata/DA/Transducer.lean#L116))

> The output on a complete input word.

```lean
abbrev eval (transducer : SubsequentialTransducer State InSymbol OutSymbol)
```

`Cslib.Automata.SequentialTransducer.evalFrom` (abbreviation, [line 134](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Automata/DA/Transducer.lean#L134))

> The concatenated transition outputs of `transducer` on an input word when starting from
> state `q`.

```lean
abbrev evalFrom (transducer : SequentialTransducer State InSymbol OutSymbol)
```

`Cslib.Automata.SequentialTransducer.evalFrom_unique` (theorem, [line 138](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Automata/DA/Transducer.lean#L138))

> The defining equations of `evalFrom` uniquely determine it.

```lean
theorem evalFrom_unique {spec : State → List InSymbol → List OutSymbol}
    (hnil : ∀ q, spec q [] = [])
    (hstep : ∀ q a w, spec q (a :: w) = transducer.emit q a ++ spec (transducer.tr q a) w) :
    transducer.evalFrom = spec
```

`Cslib.Automata.SequentialTransducer.eval` (abbreviation, [line 145](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Automata/DA/Transducer.lean#L145))

> The concatenated transition outputs from the start state.

```lean
abbrev eval (transducer : SequentialTransducer State InSymbol OutSymbol)
```

## Depends on

- [Deterministic Automata](basic.md)
- [Transducers](../transducers/transducer.md)

## Sources

- [Cslib/Computability/Automata/DA/Transducer.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Automata/DA/Transducer.lean)
- [Declaration ledger](../../../../../sources/cslib/Cslib.Computability.Automata.DA.Transducer.json)
