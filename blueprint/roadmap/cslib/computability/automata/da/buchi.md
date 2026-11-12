---
catalog: module
lean: Cslib.Automata.DA.buchi_eq_finAcc_omegaLim
statement: formalized
proof: formalized
---

# Deterministic Buchi automata

`Cslib.Computability.Automata.DA.Buchi`, in [Cslib/Computability/Automata/DA/Buchi.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/Buchi.lean), by Ching-Tsun Chou.

`Cslib.Automata.DA.buchi_eq_finAcc_omegaLim` (theorem, [line 26](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/Buchi.lean#L26))

> The ω-language accepted by a deterministic Buchi automaton is the ω-limit
> of the language accepted by the same automaton.

```lean
theorem buchi_eq_finAcc_omegaLim {da : DA State Symbol} {acc : Set State} :
    language (Buchi.mk da acc) = (language (FinAcc.mk da acc))↗ω
```

## Depends on

- [Deterministic Automata](basic.md)

## Sources

- [Cslib/Computability/Automata/DA/Buchi.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/Buchi.lean)
