---
catalog: module
lean: Cslib.Automata.NA.FinAcc.reverse, Cslib.Automata.NA.FinAcc.reverse_reverse, Cslib.Automata.NA.FinAcc.reverse_involutive, Cslib.Automata.NA.FinAcc.reverse_start, Cslib.Automata.NA.FinAcc.reverse_accept, Cslib.Automata.NA.FinAcc.reverse_mTr, Cslib.Automata.NA.FinAcc.accepts_reverse, Cslib.Automata.NA.FinAcc.reverse_language_eq
statement: formalized
proof: formalized
---

# Reversal of nondeterministic automata

`Cslib.Computability.Automata.NA.Reverse`, in [Cslib/Computability/Automata/NA/Reverse.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Reverse.lean), by Vignesh Karri.

> This file defines `Cslib.Automata.NA.FinAcc.reverse`, which reverses every transition of a
> nondeterministic automaton and swaps its start and accept states. Its underlying transition system
> is `Cslib.LTS.reverse`, so the transition results are inherited from
> `Cslib/Foundations/Semantics/LTS/Reverse.lean`.
>
> The main result is `FinAcc.reverse_language_eq`: the language accepted by `na.reverse` is the
> `Language.reverse` of the language accepted by `na`. It follows from `FinAcc.accepts_reverse`,
> the statement that `na.reverse` accepts `xs` iff `na` accepts `xs.reverse`.

`Cslib.Automata.NA.FinAcc.reverse` (definition, [line 38](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Reverse.lean#L38))

> `na.reverse` reverses every transition of `na` and swaps its start and accept states,
> so that it accepts exactly the reversals of the words accepted by `na`.

```lean
def reverse (na : FinAcc State Symbol) : FinAcc State Symbol
```

`Cslib.Automata.NA.FinAcc.reverse_reverse` (theorem, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Reverse.lean#L45))

> Reversing an automaton twice gives back the original automaton.

```lean
theorem reverse_reverse (na : FinAcc State Symbol) : na.reverse.reverse = na
```

`Cslib.Automata.NA.FinAcc.reverse_involutive` (theorem, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Reverse.lean#L48))

> Reversal of an automaton is an involution.

```lean
theorem reverse_involutive : Function.Involutive (reverse (State := State) (Symbol := Symbol))
```

`Cslib.Automata.NA.FinAcc.reverse_start` (theorem, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Reverse.lean#L53))

> The start states of `na.reverse` are the accept states of `na`.

```lean
theorem reverse_start (na : FinAcc State Symbol) : na.reverse.start = na.accept
```

`Cslib.Automata.NA.FinAcc.reverse_accept` (theorem, [line 57](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Reverse.lean#L57))

> The accept states of `na.reverse` are the start states of `na`.

```lean
theorem reverse_accept (na : FinAcc State Symbol) : na.reverse.accept = na.start
```

`Cslib.Automata.NA.FinAcc.reverse_mTr` (theorem, [line 62](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Reverse.lean#L62))

> The multistep transitions of `na.reverse` are exactly the reversed multistep transitions
> of `na`.

```lean
theorem reverse_mTr (na : FinAcc State Symbol) {xs : List Symbol} {s s' : State} :
    na.reverse.MTr s' xs s ↔ na.MTr s xs.reverse s'
```

`Cslib.Automata.NA.FinAcc.accepts_reverse` (theorem, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Reverse.lean#L67))

> `na.reverse` accepts a word iff `na` accepts its reversal.

```lean
theorem accepts_reverse {na : FinAcc State Symbol} {xs : List Symbol} :
    Accepts na.reverse xs ↔ Accepts na xs.reverse
```

`Cslib.Automata.NA.FinAcc.reverse_language_eq` (theorem, [line 73](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Reverse.lean#L73))

> `na.reverse` accepts exactly the reversals of the words accepted by `na`.

```lean
theorem reverse_language_eq (na : FinAcc State Symbol) :
    language na.reverse = (language na).reverse
```

## Depends on

- [Nondeterministic Automaton](basic.md)
- [Reverse operation for LTS](../../../foundations/semantics/lts/reverse.md)

## Sources

- [Cslib/Computability/Automata/NA/Reverse.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Reverse.lean)
