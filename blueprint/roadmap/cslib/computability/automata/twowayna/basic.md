---
catalog: module
lean: Cslib.Automata.TwoWayNA, Cslib.Automata.TwoWayNACfg, Cslib.Automata.TwoWayNACfg.IsInitialForInput, Cslib.Automata.TwoWayNACfg.IsAccepting, Cslib.Automata.TwoWayNA.toCfgNA, Cslib.Automata.TwoWayNA.toCfgNA_input_eq, Cslib.Automata.TwoWayNACfg.eta, Cslib.Automata.TwoWayNA.getElem_of_tr
statement: formalized
proof: formalized
---

# Nondeterministic Two-Way Automaton

`Cslib.Computability.Automata.TwoWayNA.Basic`, in [Cslib/Computability/Automata/TwoWayNA/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/Basic.lean), by Christian Reitwiessner.

> A Nondeterministic Two-Way Automaton (`TwoWayNA`) reads a finite input word on a tape and may move
> its input head in either direction. A transition reads the symbol under the head and, besides
> changing the state, moves the head one cell to the left, keeps it in place, or moves it one cell to
> the right.
>
> The input head cannot leave the input word to the left (in the sense that execution gets stuck in
> this case) and once it leaves the word to the right, it stops. A run is accepting if and only if it
> ends in an accepting state with the head just past the end of the input.
>
> ## Main definitions
>
> * `TwoWayNA`, the automaton itself
> * `TwoWayNACfg`, a configuration of a `TwoWayNA`: Its input plus a state and the head position.
> * `TwoWayNA.toCfgNA`, the finite acceptor on configurations whose runs on a fixed input are
>   the runs of the two-way automaton on that input. It also provides the `Acceptor` instance.
>
> ## Implementation notes
>
> The definition of `TwoWayNA` is kept close to [Vardi][Vardi1989]'s, because the main point is to
> prove that it accepts the same languages as `NA.FinAcc` via his proof. This means we do not allow
> the head to move off the input to the left (in the sense that if the transition relation has an
> entry that would cause that, there is no successor configuration, the computation is stuck), but
> also do not provide an end marker. Once the head moves off to the right, the machine instantly
> stops, so it also cannot move back into the word.
>
> ## References
>
> * [Moshe Y. Vardi, *A Note on the Reduction of Two-Way Automata to One-Way Automata*][Vardi1989]

`Cslib.Automata.TwoWayNA` (structure, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/Basic.lean#L56))

> A nondeterministic two-way automaton: a transition relation that reads an input symbol and
> moves the input head, together with a set of initial and a set of accepting states.

```lean
structure TwoWayNA (State Symbol : Type*) where
  /-- The transition relation. `Tr q x m q'` means that, while reading the symbol `x`, the
  automaton attempts to transition from state `q` to state `q'` and move its head according to
  `m`. -/
  Tr (q : State) (x : Symbol) (m : SignType) (q' : State) : Prop
  /-- The set of initial states of the automaton. -/
  start : Set State
  /-- The set of accepting states of the automaton. -/
  accept : Set State
```

`Cslib.Automata.TwoWayNACfg` (structure, [line 68](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/Basic.lean#L68))

> The configuration of a two-way nondeterministic automaton.

```lean
structure TwoWayNACfg (State Symbol : Type*) where
  /-- The original input to the automaton. -/
  input : List Symbol
  /-- The state of the automaton. -/
  state : State
  /-- The input head position of the automaton: it can be on any symbol of the input or on the
  position one step to the right of the input. -/
  pos : Fin (input.length + 1)
```

`Cslib.Automata.TwoWayNACfg.IsInitialForInput` (definition, [line 78](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/Basic.lean#L78))

> This defines the set of initial configurations on a specific input.

```lean
def TwoWayNACfg.IsInitialForInput (a : TwoWayNA State Symbol) (c : TwoWayNACfg State Symbol)
    (input : List Symbol) : Prop
```

`Cslib.Automata.TwoWayNACfg.IsAccepting` (definition, [line 83](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/Basic.lean#L83))

> If a configuration is a accepting.

```lean
def TwoWayNACfg.IsAccepting (a : TwoWayNA State Symbol) (c : TwoWayNACfg State Symbol) : Prop
```

`Cslib.Automata.TwoWayNA.toCfgNA` (definition, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/Basic.lean#L88))

> Returns a nondeterministic finite acceptor on the configurations as states, accepting exactly
> the runs of the two-way automaton on `input` that end in an accepting configuration.

```lean
def TwoWayNA.toCfgNA {State Symbol : Type*} (a : TwoWayNA State Symbol)
    (input : List Symbol) :
    NA.FinAcc (TwoWayNACfg State Symbol) (Symbol × SignType)
```

`Cslib.Automata.TwoWayNA.toCfgNA_input_eq` (lemma, [line 111](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/Basic.lean#L111))

> Any reachable state of `a.toCfgNA input` contains the original input.

```lean
lemma TwoWayNA.toCfgNA_input_eq {State Symbol : Type*} (a : TwoWayNA State Symbol)
    (input : List Symbol) :
    (a.toCfgNA input).TrInv (fun c => c.input = input)
```

`Cslib.Automata.TwoWayNACfg.eta` (theorem, [line 118](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/Basic.lean#L118))

> A configuration running on `input` is the one determined by its state and head position.

```lean
theorem TwoWayNACfg.eta {input : List Symbol} {c : TwoWayNACfg State Symbol}
    (h : c.input = input) (h' : (c.pos : ℕ) < input.length + 1) :
    ({ input := input, pos := ⟨c.pos, h'⟩, state := c.state } : TwoWayNACfg State Symbol) = c
```

`Cslib.Automata.TwoWayNA.getElem_of_tr` (theorem, [line 126](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/Basic.lean#L126))

> A step reads the symbol at the head position, which therefore lies inside the input.

```lean
theorem TwoWayNA.getElem_of_tr {a : TwoWayNA State Symbol} {input : List Symbol}
    {c c' : TwoWayNACfg State Symbol} {x : Symbol} {m : SignType}
    (htr : (a.toCfgNA input).Tr c (x, m) c') (hc : c.input = input) :
    ∃ h : (c.pos : ℕ) < input.length, input[(c.pos : ℕ)] = x
```

## Depends on

- [Nondeterministic Automaton](../na/basic.md)

## Sources

- [Cslib/Computability/Automata/TwoWayNA/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/Basic.lean)
