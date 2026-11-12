---
catalog: module
lean: Cslib.Automata.NA, Cslib.Automata.NA.Run, Cslib.Automata.NA.FinAcc, Cslib.Automata.NA.Buchi, Cslib.Automata.NA.Muller
statement: formalized
proof: formalized
---

# Nondeterministic Automaton

`Cslib.Computability.Automata.NA.Basic`, in [Cslib/Computability/Automata/NA/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Basic.lean), by Fabrizio Montesi, Ching-Tsun Chou, Chris Henson.

> A Nondeterministic Automaton (NA) is a transition relation equipped with a set of initial states.
>
> Automata with different accepting conditions are then defined as extensions of `NA`.
> These include, for example, a generalised version of NFA as found in the literature (without
> finiteness assumptions), nondeterministic Buchi automata, and nondeterministic Muller automata.
>
> This definition extends `LTS` and thus stores the transition system as a relation `Tr` of the form
> `State → Symbol → State → Prop`. Note that you can also instantiate `Tr` by passing an argument of
> type `State → Symbol → Set State`; it gets automatically expanded to the former shape.
>
> ## References
>
> * [J. E. Hopcroft, R. Motwani, J. D. Ullman,
>   *Introduction to Automata Theory, Languages, and Computation*][Hopcroft2006]

`Cslib.Automata.NA` (structure, [line 39](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Basic.lean#L39))

> A nondeterministic automaton extends a `LTS` with a set of initial states.

```lean
structure NA (State Symbol : Type*) extends LTS State Symbol where
  /-- The set of initial states of the automaton. -/
  start : Set State
```

`Cslib.Automata.NA.Run` (structure, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Basic.lean#L48))

> Infinite run.

```lean
structure Run (na : NA State Symbol) (xs : ωSequence Symbol) (ss : ωSequence State) where
  start : ss 0 ∈ na.start
  trans : na.OmegaExecution ss xs
```

`Cslib.Automata.NA.FinAcc` (structure, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Basic.lean#L53))

> A nondeterministic automaton that accepts finite strings (lists of symbols).

```lean
structure FinAcc (State Symbol : Type*) extends NA State Symbol where
  /-- The set of accepting states. -/
  accept : Set State
```

`Cslib.Automata.NA.Buchi` (structure, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Basic.lean#L71))

> Nondeterministic Buchi automaton.

```lean
structure Buchi (State Symbol : Type*) extends NA State Symbol where
  /-- The set of accepting states. -/
  accept : Set State
```

`Cslib.Automata.NA.Muller` (structure, [line 86](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Basic.lean#L86))

> Nondeterministic Muller automaton.

```lean
structure Muller (State Symbol : Type*) extends NA State Symbol where
  /-- The set of sets of accepting states. -/
  accept : Set (Set State)
```

## Depends on

- [Acceptor](../acceptors/acceptor.md)
- [OmegaAcceptor](../acceptors/omegaacceptor.md)
- [Infinite executions of LTS](../../../foundations/semantics/lts/omegaexecution.md)

## Proof depends on

- [Infinite occurrences](../../../foundations/data/omegasequence/infocc.md)

## Sources

- [Cslib/Computability/Automata/NA/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Basic.lean)
