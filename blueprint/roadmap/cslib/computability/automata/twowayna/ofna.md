---
catalog: module
lean: Cslib.Automata.NA.FinAcc.toTwoWayNA, Cslib.Automata.TwoWayNA.mTr_take_of_mTr_toCfgNA, Cslib.Automata.TwoWayNA.mTr_toCfgNA_of_mTr, Cslib.Automata.TwoWayNA.accepts_toTwoWayNA_iff, Cslib.Automata.TwoWayNA.language_toTwoWayNA
statement: formalized
proof: formalized
---

# Finite acceptors as two-way automata

`Cslib.Computability.Automata.TwoWayNA.OfNA`, in [Cslib/Computability/Automata/TwoWayNA/OfNA.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/OfNA.lean), by Christian Reitwiessner.

> A nondeterministic finite acceptor (`NA.FinAcc`) is the special case of a nondeterministic two-way
> automaton (`TwoWayNA`) that moves its head one symbol to the right in every step,
> `NA.FinAcc.toTwoWayNA`.
>
> The head of `a.toTwoWayNA` is thus at position `i` exactly when `a` has read the first `i`
> symbols of the input, so the runs of the two-way automaton are in lockstep with the multistep
> transitions of `a` (`TwoWayNA.mTr_take_of_mTr_toCfgNA`, `TwoWayNA.mTr_toCfgNA_of_mTr`) and the two
> accept the same words (`TwoWayNA.accepts_toTwoWayNA_iff`, `TwoWayNA.language_toTwoWayNA`).

`Cslib.Automata.NA.FinAcc.toTwoWayNA` (definition, [line 31](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/OfNA.lean#L31))

> The two-way automaton that performs the transitions of the nondeterministic finite acceptor
> `n`, always moving its head one symbol to the right.

```lean
def NA.FinAcc.toTwoWayNA (n : NA.FinAcc State Symbol) : TwoWayNA State Symbol
```

`Cslib.Automata.TwoWayNA.mTr_take_of_mTr_toCfgNA` (theorem, [line 42](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/OfNA.lean#L42))

> A run of `a.toTwoWayNA` that starts in an initial configuration reads a multistep transition
> of `a` over the prefix of `input` that its head has scanned.

```lean
theorem mTr_take_of_mTr_toCfgNA {c c' : TwoWayNACfg State Symbol}
    {μs : List (Symbol × SignType)}
    (hstart : c ∈ (a.toTwoWayNA.toCfgNA input).start)
    (hrun : (a.toTwoWayNA.toCfgNA input).MTr c μs c') :
    a.MTr c.state (input.take c'.pos) c'.state
```

`Cslib.Automata.TwoWayNA.mTr_toCfgNA_of_mTr` (theorem, [line 62](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/OfNA.lean#L62))

> A multistep transition of `a` over a prefix of `input` is read by the run of `a.toTwoWayNA`
> that takes its head from the beginning of the input to the end of that prefix, moving one symbol
> to the right in every step.

```lean
theorem mTr_toCfgNA_of_mTr {s s' : State} {pre : List Symbol} (hpre : pre <+: input)
    (hmtr : a.MTr s pre s') :
    (a.toTwoWayNA.toCfgNA input).MTr ⟨input, s, 0⟩ (pre.map (·, SignType.pos))
      ⟨input, s', ⟨pre.length, by grind⟩⟩
```

`Cslib.Automata.TwoWayNA.accepts_toTwoWayNA_iff` (theorem, [line 86](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/OfNA.lean#L86))

> A nondeterministic finite acceptor and its two-way rendering accept the same words.

```lean
theorem accepts_toTwoWayNA_iff (a : NA.FinAcc State Symbol) (input : List Symbol) :
    Accepts a.toTwoWayNA input ↔ Accepts a input
```

`Cslib.Automata.TwoWayNA.language_toTwoWayNA` (theorem, [line 100](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/OfNA.lean#L100))

> A nondeterministic finite acceptor and its two-way rendering recognise the same language.

```lean
theorem language_toTwoWayNA (a : NA.FinAcc State Symbol) : language a.toTwoWayNA = language a
```

## Depends on

- [Nondeterministic Two-Way Automaton](basic.md)

## Sources

- [Cslib/Computability/Automata/TwoWayNA/OfNA.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/OfNA.lean)
