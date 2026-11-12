---
catalog: module
lean: Cslib.Automata.εNA.FinAcc.toSingleStartAccept, Cslib.Automata.εNA.FinAcc.toSingleStartAccept_start, Cslib.Automata.εNA.FinAcc.toSingleStartAccept_accept, Cslib.Automata.εNA.FinAcc.toSingleStartAccept_tr_inr_inr, Cslib.Automata.εNA.FinAcc.toSingleStartAccept_tr_start, Cslib.Automata.εNA.FinAcc.toSingleStartAccept_tr_accept, Cslib.Automata.εNA.FinAcc.toSingleStartAccept_tr_inl_false, Cslib.Automata.εNA.FinAcc.toSingleStartAccept_not_tr_inl_false, Cslib.Automata.εNA.FinAcc.toSingleStartAccept_not_tr_inl_true, Cslib.Automata.εNA.FinAcc.toSingleStartAccept_mTr_inr_inl_true, Cslib.Automata.εNA.FinAcc.toSingleStartAccept_language_eq
statement: formalized
proof: formalized
---

# Translation of εNA into εNA with a single start and a single accept state

`Cslib.Computability.Automata.EpsilonNA.ToSingleStartAccept`, in [Cslib/Computability/Automata/EpsilonNA/ToSingleStartAccept.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ToSingleStartAccept.lean), by Fabrizio Montesi, Yusuf Demir.

> Defines the transformation `toSingleStartAccept` for `εNA.FinAcc`, which adds a start state with
> ε-transitions to the original start states and no incoming transitions, and an accept state with
> ε-transitions from the original accept states and no outgoing transitions. The transformation
> preserves the language of the automaton.

`Cslib.Automata.εNA.FinAcc.toSingleStartAccept` (definition, [line 30](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ToSingleStartAccept.lean#L30))

> Any `εNA.FinAcc` can be converted into an `εNA.FinAcc` with a single start state and a single
> accept state. The original states are wrapped in `inr`, and the fresh state `inl b` is accepting
> exactly when `b`: the start state `inl false` has ε-transitions to the original start states, and
> the original accept states have ε-transitions to the accept state `inl true`.

```lean
def toSingleStartAccept (a : εNA.FinAcc State Symbol) : εNA.FinAcc (Bool ⊕ State) Symbol
```

`Cslib.Automata.εNA.FinAcc.toSingleStartAccept_start` (theorem, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ToSingleStartAccept.lean#L41))

```lean
theorem toSingleStartAccept_start : a.toSingleStartAccept.start = {.inl false}
```

`Cslib.Automata.εNA.FinAcc.toSingleStartAccept_accept` (theorem, [line 43](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ToSingleStartAccept.lean#L43))

```lean
theorem toSingleStartAccept_accept : a.toSingleStartAccept.accept = {.inl true}
```

`Cslib.Automata.εNA.FinAcc.toSingleStartAccept_tr_inr_inr` (theorem, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ToSingleStartAccept.lean#L45))

```lean
theorem toSingleStartAccept_tr_inr_inr {s s' : State} {μ : Option Symbol} :
    a.toSingleStartAccept.Tr (.inr s) μ (.inr s') ↔ a.Tr s μ s'
```

`Cslib.Automata.εNA.FinAcc.toSingleStartAccept_tr_start` (theorem, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ToSingleStartAccept.lean#L48))

```lean
theorem toSingleStartAccept_tr_start {s : State} (hs : s ∈ a.start) :
    a.toSingleStartAccept.Tr (.inl false) none (.inr s)
```

`Cslib.Automata.εNA.FinAcc.toSingleStartAccept_tr_accept` (theorem, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ToSingleStartAccept.lean#L51))

```lean
theorem toSingleStartAccept_tr_accept {s : State} (hs : s ∈ a.accept) :
    a.toSingleStartAccept.Tr (.inr s) none (.inl true)
```

`Cslib.Automata.εNA.FinAcc.toSingleStartAccept_tr_inl_false` (theorem, [line 55](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ToSingleStartAccept.lean#L55))

> The transitions from the start state are ε-transitions to the original start states.

```lean
theorem toSingleStartAccept_tr_inl_false {μ : Option Symbol} {y : Bool ⊕ State}
    (h : a.toSingleStartAccept.Tr (.inl false) μ y) :
    μ = none ∧ ∃ s, y = .inr s ∧ s ∈ a.start
```

`Cslib.Automata.εNA.FinAcc.toSingleStartAccept_not_tr_inl_false` (theorem, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ToSingleStartAccept.lean#L61))

> No transition leads to the start state.

```lean
theorem toSingleStartAccept_not_tr_inl_false {x : Bool ⊕ State} {μ : Option Symbol} :
    ¬a.toSingleStartAccept.Tr x μ (.inl false)
```

`Cslib.Automata.εNA.FinAcc.toSingleStartAccept_not_tr_inl_true` (theorem, [line 66](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ToSingleStartAccept.lean#L66))

> No transition leaves the accept state.

```lean
theorem toSingleStartAccept_not_tr_inl_true {μ : Option Symbol} {y : Bool ⊕ State} :
    ¬a.toSingleStartAccept.Tr (.inl true) μ y
```

`Cslib.Automata.εNA.FinAcc.toSingleStartAccept_mTr_inr_inl_true` (theorem, [line 72](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ToSingleStartAccept.lean#L72))

> A run from an original state to the accept state is a run of the original automaton to an
> original accept state, followed by the ε-transition to the accept state.

```lean
theorem toSingleStartAccept_mTr_inr_inl_true {s : State} {μs : List (Option Symbol)}
    (h : a.toSingleStartAccept.MTr (.inr s) μs (.inl true)) :
    ∃ t ∈ a.accept, ∃ μs', μs = μs' ++ [none] ∧ a.MTr s μs' t
```

`Cslib.Automata.εNA.FinAcc.toSingleStartAccept_language_eq` (theorem, [line 95](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ToSingleStartAccept.lean#L95))

> `toSingleStartAccept` preserves the language of the input automaton.

```lean
theorem toSingleStartAccept_language_eq : language a.toSingleStartAccept = language a
```

## Depends on

- [Nondeterministic automata with ε-transitions](basic.md)

## Proof depends on

- [IsSimulation and Similarity](../../../foundations/semantics/lts/simulation.md)

## Sources

- [Cslib/Computability/Automata/EpsilonNA/ToSingleStartAccept.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ToSingleStartAccept.lean)
