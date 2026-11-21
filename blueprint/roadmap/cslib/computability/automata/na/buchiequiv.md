---
catalog: module
lean: Cslib.Automata.NA.Buchi.reindex, Cslib.Automata.NA.Buchi.reindex_run_iff, Cslib.Automata.NA.Buchi.reindex_run_iff', Cslib.Automata.NA.Buchi.reindex_language_eq
statement: formalized
proof: formalized
---

# Equivalence of nondeterministic Buchi automata (NBAs)

`Cslib.Computability.Automata.NA.BuchiEquiv`, in [Cslib/Computability/Automata/NA/BuchiEquiv.lean](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Automata/NA/BuchiEquiv.lean), by Ching-Tsun Chou.

`Cslib.Automata.NA.Buchi.reindex` (definition, [line 26](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Automata/NA/BuchiEquiv.lean#L26))

> Lifts an equivalence on states to an equivalence on NBAs.

```lean
def reindex (f : State ≃ State') : Buchi State Symbol ≃ Buchi State' Symbol
```

`Cslib.Automata.NA.Buchi.reindex_run_iff` (theorem, [line 40](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Automata/NA/BuchiEquiv.lean#L40))

```lean
theorem reindex_run_iff {f : State ≃ State'} {nba : Buchi State Symbol}
    {xs : ωSequence Symbol} {ss' : ωSequence State'} :
    (nba.reindex f).Run xs ss' ↔ nba.Run xs (ss'.map f.symm)
```

`Cslib.Automata.NA.Buchi.reindex_run_iff'` (theorem, [line 50](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Automata/NA/BuchiEquiv.lean#L50))

```lean
theorem reindex_run_iff' {f : State ≃ State'} {nba : Buchi State Symbol}
    {xs : ωSequence Symbol} {ss : ωSequence State} :
    (nba.reindex f).Run xs (ss.map f) ↔ nba.Run xs ss
```

`Cslib.Automata.NA.Buchi.reindex_language_eq` (theorem, [line 56](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Automata/NA/BuchiEquiv.lean#L56))

```lean
theorem reindex_language_eq {f : State ≃ State'} {nba : Buchi State Symbol} :
    language (nba.reindex f) = language nba
```

## Depends on

- [Nondeterministic Automaton](basic.md)

## Sources

- [Cslib/Computability/Automata/NA/BuchiEquiv.lean at 7c95c37f](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Automata/NA/BuchiEquiv.lean)
- [Declaration ledger](../../../../../sources/cslib/Cslib.Computability.Automata.NA.BuchiEquiv.json)
