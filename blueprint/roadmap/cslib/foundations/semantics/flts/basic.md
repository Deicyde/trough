---
catalog: module
lean: Cslib.FLTS, Cslib.FLTS.mtr, Cslib.FLTS.mtr_nil_eq, Cslib.FLTS.mtr_concat_eq, Cslib.FLTS.mtr_append_eq
statement: formalized
proof: formalized
---

# Functional Labelled Transition System (FLTS)

`Cslib.Foundations.Semantics.FLTS.Basic`, in [Cslib/Foundations/Semantics/FLTS/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/Basic.lean), by Fabrizio Montesi.

> A Functional Labelled Transition System is a special case of an `LTS` where transitions are
> determined by a function.
>
> This is a generalisation of deterministic finite-state machines.
>
> ## References
>
> * [J. E. Hopcroft, R. Motwani, J. D. Ullman,
>   *Introduction to Automata Theory, Languages, and Computation*][Hopcroft2006]

`Cslib.FLTS` (structure, [line 32](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/Basic.lean#L32))

> A Functional Labelled Transition System (`FLTS`) for a type of states (`State`) and a type of
> transition labels (`Label`) consists of a labelled transition function (`tr`).

```lean
structure FLTS (State Label : Type*) where
  /-- The transition function. -/
  tr : State → Label → State
```

`Cslib.FLTS.mtr` (definition, [line 46](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/Basic.lean#L46))

> Extended transition function.
>
> Implementation note: compared to [Hopcroft2006], the definition consumes the input list of symbols
> from the left (instead of the right), in order to match the way lists are constructed.

```lean
def mtr (flts : FLTS State Label) (s : State) (μs : List Label)
```

`Cslib.FLTS.mtr_nil_eq` (theorem, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/Basic.lean#L49))

```lean
theorem mtr_nil_eq {flts : FLTS State Label} {s : State} : flts.mtr s [] = s
```

`Cslib.FLTS.mtr_concat_eq` (theorem, [line 52](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/Basic.lean#L52))

```lean
theorem mtr_concat_eq {flts : FLTS State Label} {s : State} {μs : List Label} {μ : Label} :
    flts.mtr s (μs ++ [μ]) = flts.tr (flts.mtr s μs) μ
```

`Cslib.FLTS.mtr_append_eq` (theorem, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/Basic.lean#L56))

```lean
theorem mtr_append_eq {flts : FLTS State Label} {s : State} {μs1 μs2 : List Label} :
    flts.mtr s (μs1 ++ μs2) = flts.mtr (flts.mtr s μs1) μs2
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Semantics/FLTS/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/Basic.lean)
