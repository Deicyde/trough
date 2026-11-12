---
catalog: module
lean: Cslib.FLTS.prod, Cslib.FLTS.prod_mtr_eq
statement: formalized
proof: formalized
---

# Product of functional labelled transition systems

`Cslib.Foundations.Semantics.FLTS.Prod`, in [Cslib/Foundations/Semantics/FLTS/Prod.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/Prod.lean), by Ching-Tsun Chou, Fabrizio Montesi.

`Cslib.FLTS.prod` (definition, [line 21](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/Prod.lean#L21))

> The product of two FLTS with the same label type.

```lean
def prod (flts1 : FLTS State1 Label) (flts2 : FLTS State2 Label) :
    FLTS (State1 × State2) Label
```

`Cslib.FLTS.prod_mtr_eq` (theorem, [line 28](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/Prod.lean#L28))

> A state is reachable by the product FLTS iff its components are reachable by
> the respective FLTS components.

```lean
theorem prod_mtr_eq (flts1 : FLTS State1 Label) (flts2 : FLTS State2 Label)
    (s : State1 × State2) (μs : List Label) :
    (flts1.prod flts2).mtr s μs = (flts1.mtr s.fst μs, flts2.mtr s.snd μs)
```

## Depends on

- [Functional Labelled Transition System (FLTS)](basic.md)

## Sources

- [Cslib/Foundations/Semantics/FLTS/Prod.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/Prod.lean)
