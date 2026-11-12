---
catalog: module
lean: Cslib.Automata.DA, Cslib.Automata.DA.run', Cslib.Automata.DA.run, Cslib.Automata.DA.run_zero, Cslib.Automata.DA.run_succ, Cslib.Automata.DA.mtr_extract_eq_run, Cslib.Automata.DA.FinAcc, Cslib.Automata.DA.Buchi, Cslib.Automata.DA.Muller
statement: formalized
proof: formalized
---

# Deterministic Automata

`Cslib.Computability.Automata.DA.Basic`, in [Cslib/Computability/Automata/DA/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/Basic.lean), by Fabrizio Montesi, Ching-Tsun Chou.

> A Deterministic Automaton (`DA`) is an automaton defined by a transition function equipped with an
> initial state.
>
> Automata with different accepting conditions are then defined as extensions of `DA`.
> These include, for example, a generalised version of DFA as found in the literature (without
> finiteness assumptions), deterministic Buchi automata, and deterministic Muller automata.
>
> ## References
>
> * [J. E. Hopcroft, R. Motwani, J. D. Ullman,
>   *Introduction to Automata Theory, Languages, and Computation*][Hopcroft2006]

`Cslib.Automata.DA` (structure, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/Basic.lean#L37))

> A deterministic automaton extends a `FLTS` with a unique initial state.

```lean
structure DA (State Symbol : Type*) extends FLTS State Symbol where
  /-- The initial state of the automaton. -/
  start : State
```

`Cslib.Automata.DA.run'` (definition, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/Basic.lean#L47))

> Helper function for defining `run` below.

```lean
def run' (da : DA State Symbol) (xs : ωSequence Symbol) : ℕ → State
```

`Cslib.Automata.DA.run` (definition, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/Basic.lean#L53))

> Infinite run.

```lean
def run (da : DA State Symbol) (xs : ωSequence Symbol) : ωSequence State
```

`Cslib.Automata.DA.run_zero` (theorem, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/Basic.lean#L56))

```lean
theorem run_zero {da : DA State Symbol} {xs : ωSequence Symbol} :
    da.run xs 0 = da.start
```

`Cslib.Automata.DA.run_succ` (theorem, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/Basic.lean#L61))

```lean
theorem run_succ {da : DA State Symbol} {xs : ωSequence Symbol} {n : ℕ} :
    da.run xs (n + 1) = da.tr (da.run xs n) (xs n)
```

`Cslib.Automata.DA.mtr_extract_eq_run` (theorem, [line 66](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/Basic.lean#L66))

```lean
theorem mtr_extract_eq_run {da : DA State Symbol} {xs : ωSequence Symbol} {n : ℕ} :
    da.mtr da.start (xs.extract 0 n) = da.run xs n
```

`Cslib.Automata.DA.FinAcc` (structure, [line 73](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/Basic.lean#L73))

> A deterministic automaton that accepts finite strings (lists of symbols).

```lean
structure FinAcc (State Symbol : Type*) extends DA State Symbol where
  /-- The set of accepting states. -/
  accept : Set State
```

`Cslib.Automata.DA.Buchi` (structure, [line 91](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/Basic.lean#L91))

> Deterministic Buchi automaton.

```lean
structure Buchi (State Symbol : Type*) extends DA State Symbol where
  /-- The set of accepting states. -/
  accept : Set State
```

`Cslib.Automata.DA.Muller` (structure, [line 106](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/Basic.lean#L106))

> Deterministic Muller automaton.

```lean
structure Muller (State Symbol : Type*) extends DA State Symbol where
  /-- The set of sets of accepting states. -/
  accept : Set (Set State)
```

## Depends on

- [Acceptor](../acceptors/acceptor.md)
- [OmegaAcceptor](../acceptors/omegaacceptor.md)
- [Functional Labelled Transition System (FLTS)](../../../foundations/semantics/flts/basic.md)

## Proof depends on

- [Infinite occurrences](../../../foundations/data/omegasequence/infocc.md)

## Sources

- [Cslib/Computability/Automata/DA/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/Basic.lean)
