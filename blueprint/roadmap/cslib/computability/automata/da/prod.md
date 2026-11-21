---
catalog: module
lean: Cslib.Automata.DA.prod, Cslib.Automata.DA.prod_mtr_eq
statement: formalized
proof: formalized
---

# Product of deterministic automata

`Cslib.Computability.Automata.DA.Prod`, in [Cslib/Computability/Automata/DA/Prod.lean](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Automata/DA/Prod.lean), by Fabrizio Montesi, Ching-Tsun Chou.

`Cslib.Automata.DA.prod` (definition, [line 27](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Automata/DA/Prod.lean#L27))

> The product of two deterministic automata.

```lean
def prod (da1 : DA State1 Symbol) (da2 : DA State2 Symbol) : DA (State1 × State2) Symbol
```

`Cslib.Automata.DA.prod_mtr_eq` (theorem, [line 34](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Automata/DA/Prod.lean#L34))

> A state is reachable by the product automaton iff its components are reachable by
> the respective automaton components.

```lean
theorem prod_mtr_eq (da1 : DA State1 Symbol) (da2 : DA State2 Symbol)
    (s : State1 × State2) (xs : List Symbol) :
    (da1.prod da2).mtr s xs = (da1.mtr s.fst xs, da2.mtr s.snd xs)
```

## Depends on

- [Deterministic Automata](basic.md)
- [Product of functional labelled transition systems](../../../foundations/semantics/flts/prod.md)

## Sources

- [Cslib/Computability/Automata/DA/Prod.lean at 7c95c37f](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Automata/DA/Prod.lean)
- [Declaration ledger](../../../../../sources/cslib/Cslib.Computability.Automata.DA.Prod.json)
