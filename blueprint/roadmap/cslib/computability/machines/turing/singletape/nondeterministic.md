---
catalog: module
lean: Cslib.Computability.Turing.SingleTape.SingleTapeNTM, Cslib.Computability.Turing.SingleTape.SingleTapeNTM.Yields, Cslib.Computability.Turing.SingleTape.SingleTapeNTM.yields_tr, Cslib.Computability.Turing.SingleTape.SingleTapeNTM.MYields, Cslib.Computability.Turing.SingleTape.SingleTapeNTM.mYields_mTr, Cslib.Computability.Turing.SingleTape.SingleTapeNTM.AcceptsInSteps, Cslib.Computability.Turing.SingleTape.SingleTapeNTM.AcceptsInAtMostSteps
statement: formalized
proof: formalized
---

# Single-Tape Nondeterministic Turing Machines (NTMs)

`Cslib.Computability.Machines.Turing.SingleTape.NonDeterministic`, in [Cslib/Computability/Machines/Turing/SingleTape/NonDeterministic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/NonDeterministic.lean), by Fabrizio Montesi.

> Nondeterministic Turing Machines (NTMs), defined as nondeterministic automata (`NA`) that act on a
> bidirectional tape (`BiTape`).
>
> ## References
>
> * [M. Sipser, *Introduction to Theory of Computation*][Sipser2013]

`Cslib.Computability.Turing.SingleTape.SingleTapeNTM` (structure, [line 32](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/NonDeterministic.lean#L32))

> A (single-tape) Nondeterministic Turing Machine (NTM) is a nondeterministic automaton equipped
> with a set of accepting halting states.

```lean
structure SingleTapeNTM (State Symbol : Type*)
    extends NA State (TrLabel Symbol) where
  /-- The set of accepting states. -/
  accept : Set State
  /-- Proof that all accepting states are halting states. -/
  accept_halting (hmem : s ∈ accept) : ¬∃ μ s', Tr s μ s'
```

`Cslib.Computability.Turing.SingleTape.SingleTapeNTM.Yields` (definition, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/NonDeterministic.lean#L47))

> An NTM yields a small-step operational semantics on configurations, which codifies an execution
> step. This formalises the 'yields' relation from [Sipser2013].

```lean
def Yields (m : SingleTapeNTM State Symbol)
    (c c' : Cfg State Symbol) : Prop
```

`Cslib.Computability.Turing.SingleTape.SingleTapeNTM.yields_tr` (theorem, [line 52](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/NonDeterministic.lean#L52))

```lean
theorem yields_tr {m : SingleTapeNTM State Symbol} :
    m.Yields c c' ↔ ∃ μ, m.Tr c.state μ c'.state ∧ μ.applyToTape c.tape = c'.tape
```

`Cslib.Computability.Turing.SingleTape.SingleTapeNTM.MYields` (definition, [line 58](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/NonDeterministic.lean#L58))

> Multistep execution of an NTM, defined as the reflexive and transitive closure of one-step
> execution.

```lean
def MYields (m : SingleTapeNTM State Symbol)
```

`Cslib.Computability.Turing.SingleTape.SingleTapeNTM.mYields_mTr` (theorem, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/NonDeterministic.lean#L64))

> Characterisation of executions in terms of multistep transitions.

```lean
theorem mYields_mTr {m : SingleTapeNTM State Symbol} :
    m.MYields c c' ↔ ∃ μs, m.MTr c.state μs c'.state ∧
    μs.foldl TrLabel.applyToTape (some c.tape) = c'.tape
```

`Cslib.Computability.Turing.SingleTape.SingleTapeNTM.AcceptsInSteps` (definition, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/NonDeterministic.lean#L101))

> The NTM `m` accepts `xs` in `n` execution steps.

```lean
def AcceptsInSteps (m : SingleTapeNTM State Symbol) (xs : List Symbol) (n : ℕ) : Prop
```

`Cslib.Computability.Turing.SingleTape.SingleTapeNTM.AcceptsInAtMostSteps` (definition, [line 105](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/NonDeterministic.lean#L105))

> The NTM `m` accepts `xs` in at most `n` execution steps.

```lean
def AcceptsInAtMostSteps (m : SingleTapeNTM State Symbol) (xs : List Symbol) (n : ℕ) : Prop
```

## Depends on

- [Nondeterministic Automaton](../../../automata/na/basic.md)
- [Transducers](../../../automata/transducers/transducer.md)
- [Basic definitions for Turing Machines (TMs)](defs.md)
- [Relations Across Steps](../../../../foundations/relation/relatesinsteps.md)

## Sources

- [Cslib/Computability/Machines/Turing/SingleTape/NonDeterministic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/NonDeterministic.lean)
