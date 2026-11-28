---
catalog: module
lean: Turing.MultiTapeTM.emitChunk, Turing.MultiTapeTM.ofSubsequential, Turing.MultiTapeTM.transducerCfg, Turing.MultiTapeTM.transducerHaltCfg, Turing.MultiTapeTM.runFrom_ofSubsequential_tr, Turing.MultiTapeTM.runFrom_ofSubsequential, Turing.MultiTapeTM.computesInTimeAndSpace_ofSubsequential, Turing.MultiTapeTM.computableInTimeAndSpace_of_subsequential, Turing.MultiTapeTM.computableInTimeAndSpace_of_sequential
statement: formalized
proof: formalized
---

# Turing machine simulation of finite sequential and subsequential transducers

`Cslib.Computability.Machines.Turing.MultiTape.Transducer`, in [Cslib/Computability/Machines/Turing/MultiTape/Transducer.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Transducer.lean), by Christian Reitwiessner.

> A function on Boolean words computed by a finite sequential or
> subsequential transducer is computable by a multitape Turing machine in zero work space
> and at most one step per input and output symbol, plus one step to halt.
>
> The machine spends one step per emitted symbol with its input head stationary. A separate step
> advances the head after each input symbol or halts after the final output. An empty chunk thus
> takes one step.
>
> ## Main definitions
>
> * `Turing.MultiTapeTM.emitChunk` is the machine action that writes one output word symbol by
>   symbol and then moves the input head.
> * `Turing.MultiTapeTM.ofSubsequential` compiles a subsequential transducer to a machine with zero
>   work tapes. Its finite control stores the position within the output word.
> * `Turing.MultiTapeTM.transducerCfg` describes the machine between chunks using the transducer
>   state, input head position, and output written so far. `Turing.MultiTapeTM.transducerHaltCfg`
>   describes the machine after it halts.
>
> ## Main results
>
> * `Turing.MultiTapeTM.runFrom_ofSubsequential_tr` simulates one transition.
>   `Turing.MultiTapeTM.runFrom_ofSubsequential` simulates reading the rest of the input,
>   including the final output and the halting step.
> * `Turing.MultiTapeTM.computesInTimeAndSpace_ofSubsequential` gives a time bound
>   of input length plus output length plus one, including the final output and halting step.
> * `Turing.MultiTapeTM.computableInTimeAndSpace_of_subsequential` gives this time bound and zero
>   work space for functions on Boolean words realized by finite subsequential transducers.
>   `Turing.MultiTapeTM.computableInTimeAndSpace_of_sequential` derives the same bound for
>   sequential transducers by adding empty final output.

`Turing.MultiTapeTM.emitChunk` (definition, [line 57](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Transducer.lean#L57))

> A TM `Action` to output the words emitted by a transducer symbol by symbol:
> If `i` is in range, emit symbol `i` of `out` while holding the input head still. Otherwise,
> move the input head by `move` and enter `next`.

```lean
def emitChunk {m : ℕ} (out : List Symbol) (i : Fin (m + 1)) (q : State) (move : SignType)
    (next : Option State) : Action 0 Symbol (State × Fin (m + 1))
```

`Turing.MultiTapeTM.ofSubsequential` (definition, [line 97](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Transducer.lean#L97))

> Compile a subsequential transducer to a machine with zero work tapes. The machine emits
> `finalOut q` at end of input in state `q`. For correct simulation, `m` must bound the length of
> every transition output and every final output.

```lean
def ofSubsequential (transducer : SubsequentialTransducer State Symbol Symbol) (m : ℕ) :
    MultiTapeTM 0 Symbol (State × Fin (m + 1))
```

`Turing.MultiTapeTM.transducerCfg` (definition, [line 105](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Transducer.lean#L105))

> A configuration between output chunks, with the counter reset to zero.

```lean
def transducerCfg (q : State) (pos : Fin (input.length + 2)) (written : List Symbol) :
    Cfg 0 Symbol (State × Fin (m + 1)) input
```

`Turing.MultiTapeTM.transducerHaltCfg` (definition, [line 111](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Transducer.lean#L111))

> The halted configuration at the end of the input with `written` on the output tape.

```lean
def transducerHaltCfg (written : List Symbol) : Cfg 0 Symbol (State × Fin (m + 1)) input
```

`Turing.MultiTapeTM.runFrom_ofSubsequential_tr` (theorem, [line 115](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Transducer.lean#L115))

> A transition consumes one input symbol and appends its output chunk.

```lean
theorem runFrom_ofSubsequential_tr (q : State) (a : Symbol)
    (hlen : (transducer.emit q a).length ≤ m) (pre post written : List Symbol)
    (hin : input = pre ++ a :: post) :
    (ofSubsequential transducer m).runFrom
        (transducerCfg (input := input) q ⟨pre.length + 1, by simp +arith [hin]⟩ written)
        ((transducer.emit q a).length + 1) =
      transducerCfg (transducer.tr q a) ⟨(pre ++ [a]).length + 1, by simp +arith [hin]⟩
        (written ++ transducer.emit q a)
```

`Turing.MultiTapeTM.runFrom_ofSubsequential` (theorem, [line 135](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Transducer.lean#L135))

> Reading the rest of the input appends its output, including the final output, in one step
> per input and output symbol plus one step to halt.

```lean
theorem runFrom_ofSubsequential (hbound : transducer.OutputBoundedBy m)
    (q : State) (w pre written : List Symbol) (hin : input = pre ++ w) :
    (ofSubsequential transducer m).runFrom
        (transducerCfg (input := input) q ⟨pre.length + 1, by simp +arith [hin]⟩ written)
        (w.length + (transducer.evalFrom q w).length + 1) =
      transducerHaltCfg (written ++ transducer.evalFrom q w)
```

`Turing.MultiTapeTM.computesInTimeAndSpace_ofSubsequential` (theorem, [line 161](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Transducer.lean#L161))

> The compiled machine computes the transducer output in at most one step per input and
> output symbol plus one, using zero work space.

```lean
theorem computesInTimeAndSpace_ofSubsequential
    (hbound : transducer.OutputBoundedBy m) (w : List Symbol) :
    (ofSubsequential transducer m).ComputesInTimeAndSpace w (transducer.eval w)
      (w.length + (transducer.eval w).length + 1) 0
```

`Turing.MultiTapeTM.computableInTimeAndSpace_of_subsequential` (theorem, [line 176](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Transducer.lean#L176))

> A function on binary words realized by a finite subsequential transducer is computable
> in time linear in the input and output lengths and in zero work space.

```lean
theorem computableInTimeAndSpace_of_subsequential {State : Type} [Finite State]
    (transducer : SubsequentialTransducer State Bool Bool) (f : List Bool → List Bool)
    (h : ∀ w, transducer.eval w = f w) :
    ComputableInTimeAndSpace f (Function.Embedding.refl _) (Function.Embedding.refl _)
      (fun w => w.length + (f w).length + 1) (fun _ => 0)
```

`Turing.MultiTapeTM.computableInTimeAndSpace_of_sequential` (theorem, [line 187](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Transducer.lean#L187))

> A function realized by a finite sequential transducer has the same time and space bounds
> as its subsequential extension with empty final output.

```lean
theorem computableInTimeAndSpace_of_sequential {State : Type} [Finite State]
    (transducer : SequentialTransducer State Bool Bool) (f : List Bool → List Bool)
    (h : ∀ w, transducer.eval w = f w) :
    ComputableInTimeAndSpace f (Function.Embedding.refl _) (Function.Embedding.refl _)
      (fun w => w.length + (f w).length + 1) (fun _ => 0)
```

## Depends on

- [Sequential and subsequential transducers](../../../automata/da/transducer.md)
- [Deterministic Multi-Tape Turing Machines](deterministic.md)

## Sources

- [Cslib/Computability/Machines/Turing/MultiTape/Transducer.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Transducer.lean)
- [Declaration ledger](../../../../../../sources/cslib/Cslib.Computability.Machines.Turing.MultiTape.Transducer.json)
