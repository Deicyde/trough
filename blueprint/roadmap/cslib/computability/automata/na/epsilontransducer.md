---
catalog: module
lean: Cslib.Automata.NA.εTransducer, List.dropTaus, Cslib.Automata.NA.εTransducer.MTransl, Cslib.Automata.NA.εTransducer.MTransl.comp
statement: formalized
proof: formalized
---

# Nondeterministic finite ε-transducers

`Cslib.Computability.Automata.NA.EpsilonTransducer`, in [Cslib/Computability/Automata/NA/EpsilonTransducer.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/EpsilonTransducer.lean), by Fabrizio Montesi.

> Transducers based on `NA` with an invisible symbol in their input and output alphabets.

`Cslib.Automata.NA.εTransducer` (structure, [line 24](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/EpsilonTransducer.lean#L24))

> A nondeterministic ε-transducer of finite strings where the input and output alphabets include
> an invisible symbol, modelled as `HasTau.τ` (typically called `ε`).

```lean
structure εTransducer (State InSymbol OutSymbol : Type*)
    extends NA State (InSymbol × OutSymbol) where
  /-- The set of accepting states. -/
  accept : Set State
```

`List.dropTaus` (definition, [line 31](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/EpsilonTransducer.lean#L31))

> Removes all `τ`s from a list.

```lean
def _root_.List.dropTaus [HasTau α] [DecidableEqTau α] (l : List α) : List α
```

`Cslib.Automata.NA.εTransducer.MTransl` (definition, [line 42](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/EpsilonTransducer.lean#L42))

> An `εTransducer` translates `xs` into `ys` from state `s` to state `s'` if there is a
> multistep transition from `s` to `s'` whose visible projection is `(xs, ys)`.
> `MTransl` is short for Multistep Translation relation.

```lean
def MTransl [DecidableEqTau InSymbol] [DecidableEqTau OutSymbol]
    (a : εTransducer State InSymbol OutSymbol) (s : State)
    (xs : List InSymbol) (ys : List OutSymbol) (s' : State) : Prop
```

`Cslib.Automata.NA.εTransducer.MTransl.comp` (theorem, [line 57](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/EpsilonTransducer.lean#L57))

> Composition of multistep translations.

```lean
theorem MTransl.comp [DecidableEqTau InSymbol] [DecidableEqTau OutSymbol]
    {a : εTransducer State InSymbol OutSymbol}
    {s₁ s₂ s₃ : State} {xs xs' : List InSymbol} {ys ys' : List OutSymbol} :
    a.MTransl s₁ xs ys s₂ → a.MTransl s₂ xs' ys' s₃ →
    a.MTransl s₁ (xs ++ xs') (ys ++ ys') s₃
```

## Depends on

- [Nondeterministic Automaton](basic.md)
- [Transducers](../transducers/transducer.md)
- [LTS with a special "internal" transition `τ`](../../../foundations/semantics/lts/hastau.md)

## Sources

- [Cslib/Computability/Automata/NA/EpsilonTransducer.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/EpsilonTransducer.lean)
