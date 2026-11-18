---
catalog: module
lean: Cslib.Automata.NA.addHist, Cslib.Automata.NA.hist_run_proj, Cslib.Automata.NA.makeHist, Cslib.Automata.NA.hist_run_exists
statement: formalized
proof: formalized
---

# Adding a history states to a nondeterministic automaton

`Cslib.Computability.Automata.NA.Hist`, in [Cslib/Computability/Automata/NA/Hist.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Hist.lean), by Ching-Tsun Chou.

> The evolution of the history state can depend on both the original state and the past history
> state. But the evolution of the original state is not constrained by the history state.

`Cslib.Automata.NA.addHist` (definition, [line 30](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Hist.lean#L30))

> The construction of adding a history state.  Note that `start'` can depend on the initial
> value of the original state and `tr'` can depend on the new value of the original state.
> So there is no loss of generality in their being functions, rather than relations.

```lean
def addHist (na : NA State Symbol) (start' : State → Hist)
    (tr' : State × Hist → Symbol → State → Hist) : NA (State × Hist) Symbol
```

`Cslib.Automata.NA.hist_run_proj` (theorem, [line 39](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Hist.lean#L39))

> Every run of the history automaton projects onto a run of the original automaton.

```lean
theorem hist_run_proj {xs : ωSequence Symbol} {ss : ωSequence (State × Hist)}
    (h_run : (na.addHist start' tr').Run xs ss) : na.Run xs (ss.map fst)
```

`Cslib.Automata.NA.makeHist` (definition, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Hist.lean#L45))

> Given a run of the original automaton, `makeHist` builds a run of the history state.

```lean
def makeHist (start' : State → Hist) (tr' : State × Hist → Symbol → State → Hist)
    (xs : ωSequence Symbol) (ss : ωSequence State) : ℕ → Hist
```

`Cslib.Automata.NA.hist_run_exists` (theorem, [line 52](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Hist.lean#L52))

> For every run `ss` of the original automaton, there exists a run `ss'` of the history automaton
> which projects back onto `ss`.

```lean
theorem hist_run_exists {xs : ωSequence Symbol} {ss : ωSequence State}
    (h_run : na.Run xs ss) : ∃ ss', (na.addHist start' tr').Run xs ss' ∧ ss'.map fst = ss
```

## Depends on

- [Nondeterministic Automaton](basic.md)

## Sources

- [Cslib/Computability/Automata/NA/Hist.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Hist.lean)
