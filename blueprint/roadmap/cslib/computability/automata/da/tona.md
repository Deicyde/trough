---
catalog: module
lean: Cslib.Automata.DA.toNA, Cslib.Automata.DA.toNA_run, Cslib.Automata.DA.FinAcc.toNAFinAcc, Cslib.Automata.DA.FinAcc.toNAFinAcc_language_eq, Cslib.Automata.DA.Buchi.toNABuchi, Cslib.Automata.DA.Buchi.toNABuchi_language_eq
statement: formalized
proof: formalized
---

# Translation of Deterministic Automata into Nonodeterministic Automata

`Cslib.Computability.Automata.DA.ToNA`, in [Cslib/Computability/Automata/DA/ToNA.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/ToNA.lean), by Fabrizio Montesi.

> This is the general version of the standard translation of DFAs into NFAs.

`Cslib.Automata.DA.toNA` (definition, [line 27](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/ToNA.lean#L27))

> `DA` is a special case of `NA`.

```lean
def toNA (a : DA State Symbol) : NA State Symbol
```

`Cslib.Automata.DA.toNA_run` (theorem, [line 36](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/ToNA.lean#L36))

```lean
theorem toNA_run {a : DA State Symbol} {xs : ωSequence Symbol} {ss : ωSequence State} :
    a.toNA.Run xs ss ↔ a.run xs = ss
```

`Cslib.Automata.DA.FinAcc.toNAFinAcc` (definition, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/ToNA.lean#L50))

> `DA.FinAcc` is a special case of `NA.FinAcc`.

```lean
def toNAFinAcc (a : DA.FinAcc State Symbol) : NA.FinAcc State Symbol
```

`Cslib.Automata.DA.FinAcc.toNAFinAcc_language_eq` (theorem, [line 57](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/ToNA.lean#L57))

> The `NA.FinAcc` constructed from a `DA.FinAcc` has the same language.

```lean
theorem toNAFinAcc_language_eq {a : DA.FinAcc State Symbol} :
    language a.toNAFinAcc = language a
```

`Cslib.Automata.DA.Buchi.toNABuchi` (definition, [line 68](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/ToNA.lean#L68))

> `DA.Buchi` is a special case of `NA.Buchi`.

```lean
def toNABuchi (a : DA.Buchi State Symbol) : NA.Buchi State Symbol
```

`Cslib.Automata.DA.Buchi.toNABuchi_language_eq` (theorem, [line 74](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/ToNA.lean#L74))

> The `NA.Buchi` constructed from a `DA.Buchi` has the same ω-language.

```lean
theorem toNABuchi_language_eq {a : DA.Buchi State Symbol} :
    language a.toNABuchi = language a
```

## Depends on

- [Deterministic Automata](basic.md)
- [Nondeterministic Automaton](../na/basic.md)
- [FLTSToLTS](../../../foundations/semantics/flts/fltstolts.md)

## Sources

- [Cslib/Computability/Automata/DA/ToNA.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/ToNA.lean)
