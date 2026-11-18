---
catalog: module
lean: Cslib.Automata.NA.totalize, Cslib.Automata.NA.totalize_run_mtr, Cslib.Automata.NA.totalize_mtr_run, Cslib.Automata.NA.FinAcc.totalize_language_eq
statement: formalized
proof: formalized
---

# Making a nondeterministic automaton total

`Cslib.Computability.Automata.NA.Total`, in [Cslib/Computability/Automata/NA/Total.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Total.lean), by Ching-Tsun Chou.

`Cslib.Automata.NA.totalize` (definition, [line 25](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Total.lean#L25))

> `NA.totalize` makes the original NA total by replacing its LTS with `LTS.totalize`
> and its starting states with their lifted non-sink versions.

```lean
def totalize (na : NA State Symbol) : NA (Option State) Symbol
```

`Cslib.Automata.NA.totalize_run_mtr` (theorem, [line 33](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Total.lean#L33))

> In an infinite execution of `NA.totalize`, as long as the NA stays in a non-sink state,
> the execution so far corresponds to a finite execution of the original NA.

```lean
theorem totalize_run_mtr {xs : ωSequence Symbol} {ss : ωSequence (Option State)} {n : ℕ}
    (h : na.totalize.Run xs ss) (hl : (ss n).isSome) :
    ∃ s t, na.MTr s (xs.take n) t ∧ s ∈ na.start ∧ ss 0 = some s ∧ ss n = some t
```

`Cslib.Automata.NA.totalize_mtr_run` (theorem, [line 46](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Total.lean#L46))

> Any finite execution of the original NA can be extended to an infinite execution of
> `NA.totalize`, provided that the alphabet is inbabited.

```lean
theorem totalize_mtr_run [Inhabited Symbol] {xl : List Symbol} {s t : State}
    (hs : s ∈ na.start) (hm : na.MTr s xl t) :
    ∃ xs ss, na.totalize.Run (xl ++ω xs) ss ∧ ss 0 = some s ∧ ss xl.length = some t
```

`Cslib.Automata.NA.FinAcc.totalize_language_eq` (theorem, [line 55](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Total.lean#L55))

> `NA.totalize` and the original NA accept the same language of finite words,
> as long as the accepting states are also lifted in the obvious way.

```lean
theorem totalize_language_eq {na : FinAcc State Symbol} :
    language (FinAcc.mk na.totalize (some '' na.accept)) = language na
```

## Depends on

- [Nondeterministic Automaton](basic.md)
- [Total LTS](../../../foundations/semantics/lts/total.md)

## Sources

- [Cslib/Computability/Automata/NA/Total.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Total.lean)
