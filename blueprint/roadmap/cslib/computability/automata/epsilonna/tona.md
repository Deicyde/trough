---
catalog: module
lean: Cslib.Automata.εNA.FinAcc.toNAFinAcc, Cslib.Automata.εNA.FinAcc.toNAFinAcc_language_eq
statement: formalized
proof: formalized
---

# Translation of εNA into NA

`Cslib.Computability.Automata.EpsilonNA.ToNA`, in [Cslib/Computability/Automata/EpsilonNA/ToNA.lean](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Automata/EpsilonNA/ToNA.lean), by Fabrizio Montesi.

`Cslib.Automata.εNA.FinAcc.toNAFinAcc` (definition, [line 22](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Automata/EpsilonNA/ToNA.lean#L22))

> Any `εNA.FinAcc` can be converted into an `NA.FinAcc` that does not use ε-transitions.

```lean
def toNAFinAcc (a : εNA.FinAcc State Symbol) : NA.FinAcc State Symbol
```

`Cslib.Automata.εNA.FinAcc.toNAFinAcc_language_eq` (theorem, [line 31](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Automata/EpsilonNA/ToNA.lean#L31))

> Correctness of `toNAFinAcc`.

```lean
theorem toNAFinAcc_language_eq {a : εNA.FinAcc State Symbol} :
    language a.toNAFinAcc = language a
```

## Depends on

- [Nondeterministic automata with ε-transitions](basic.md)
- [Label homomorphism map for LTS](../../../foundations/semantics/lts/maphom.md)

## Sources

- [Cslib/Computability/Automata/EpsilonNA/ToNA.lean at 7c95c37f](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Automata/EpsilonNA/ToNA.lean)
- [Declaration ledger](../../../../../sources/cslib/Cslib.Computability.Automata.EpsilonNA.ToNA.json)
