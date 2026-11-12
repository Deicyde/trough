---
catalog: module
lean: Cslib.Automata.NA.toDA, Cslib.Automata.NA.FinAcc.toDAFinAcc, Cslib.Automata.NA.FinAcc.toDAFinAcc_language_eq
statement: formalized
proof: formalized
---

# Translation of Nondeterministic Automata for finite strings into Deterministic Automata

`Cslib.Computability.Automata.NA.ToDA`, in [Cslib/Computability/Automata/NA/ToDA.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/ToDA.lean), by Fabrizio Montesi.

> This file implements the standard subset construction.

`Cslib.Automata.NA.toDA` (definition, [line 28](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/ToDA.lean#L28))

> Converts an `NA` into a `DA` using the subset construction.

```lean
def toDA (a : NA State Symbol) : DA (Set State) Symbol
```

`Cslib.Automata.NA.FinAcc.toDAFinAcc` (definition, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/ToDA.lean#L35))

> Converts an `NA.FinAcc` into a `DA.FinAcc` using the subset construction.

```lean
def toDAFinAcc (a : NA.FinAcc State Symbol) : DA.FinAcc (Set State) Symbol
```

`Cslib.Automata.NA.FinAcc.toDAFinAcc_language_eq` (theorem, [line 42](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/ToDA.lean#L42))

> The `DA` constructed from an `NA` has the same language.

```lean
theorem toDAFinAcc_language_eq {na : NA.FinAcc State Symbol} :
  language na.toDAFinAcc = language na
```

## Depends on

- [Deterministic Automata](../da/basic.md)
- [Nondeterministic Automaton](basic.md)
- [LTSToFLTS](../../../foundations/semantics/flts/ltstoflts.md)

## Sources

- [Cslib/Computability/Automata/NA/ToDA.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/ToDA.lean)
