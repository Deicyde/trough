---
catalog: module
lean: Cslib.LTS.pairLang, Cslib.LTS.mem_pairLang, Cslib.LTS.pairLang_regular, Cslib.LTS.pairViaLang, Cslib.LTS.mem_pairViaLang, Cslib.LTS.pairViaLang_regular, Cslib.LTS.pairLang_append, Cslib.LTS.pairLang_split, Cslib.LTS.pairViaLang_append_pairLang, Cslib.LTS.pairLang_append_pairViaLang, Cslib.LTS.pairViaLang_split, Cslib.Automata.NA.Buchi.language_eq_fin_iSup_hmul_omegaPow
statement: formalized
proof: formalized
---

# Languages determined by pairs of states

`Cslib.Computability.Automata.NA.Pair`, in [Cslib/Computability/Automata/NA/Pair.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Pair.lean), by Ching-Tsun Chou.

`Cslib.LTS.pairLang` (definition, [line 25](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Pair.lean#L25))

> `LTS.pairLang s t` is the language of finite words that can take the LTS
> from state `s` to state `t`.

```lean
def LTS.pairLang (lts : LTS State Symbol) (s t : State) : Language Symbol
```

`Cslib.LTS.mem_pairLang` (theorem, [line 29](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Pair.lean#L29))

```lean
theorem LTS.mem_pairLang {lts : LTS State Symbol} {s t : State} {xs : List Symbol} :
    xs ∈ lts.pairLang s t ↔ lts.MTr s xs t
```

`Cslib.LTS.pairLang_regular` (theorem, [line 34](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Pair.lean#L34))

> `LTS.pairLang s t` is a regular language if there are only finitely many states.

```lean
theorem LTS.pairLang_regular [Finite State] {lts : LTS State Symbol} {s t : State} :
    (lts.pairLang s t).IsRegular
```

`Cslib.LTS.pairViaLang` (definition, [line 43](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Pair.lean#L43))

> `LTS.pairViaLang via s t` is the language of finite words that can take the LTS
> from state `s` to state `t` via a state in `via`.

```lean
def LTS.pairViaLang (lts : LTS State Symbol) (via : Set State) (s t : State) : Language Symbol
```

`Cslib.LTS.mem_pairViaLang` (theorem, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Pair.lean#L47))

```lean
theorem LTS.mem_pairViaLang {lts : LTS State Symbol} {via : Set State}
    {s t : State} {xs : List Symbol} : xs ∈ lts.pairViaLang via s t ↔
      ∃ r ∈ via, ∃ xs1 xs2, lts.MTr s xs1 r ∧ lts.MTr r xs2 t ∧ xs1 ++ xs2 = xs
```

`Cslib.LTS.pairViaLang_regular` (theorem, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Pair.lean#L54))

> `LTS.pairViaLang via s t` is a regular language if there are only finitely many states.

```lean
theorem LTS.pairViaLang_regular [Finite State] {lts : LTS State Symbol}
    {via : Set State} {s t : State} : (lts.pairViaLang via s t).IsRegular
```

`Cslib.LTS.pairLang_append` (theorem, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Pair.lean#L59))

```lean
theorem LTS.pairLang_append {lts : LTS State Symbol} {s0 s1 s2 : State} {xs1 xs2 : List Symbol}
    (h1 : xs1 ∈ lts.pairLang s0 s1) (h2 : xs2 ∈ lts.pairLang s1 s2) :
    xs1 ++ xs2 ∈ lts.pairLang s0 s2
```

`Cslib.LTS.pairLang_split` (theorem, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Pair.lean#L64))

```lean
theorem LTS.pairLang_split {lts : LTS State Symbol} {s0 s2 : State} {xs1 xs2 : List Symbol}
    (h : xs1 ++ xs2 ∈ lts.pairLang s0 s2) :
    ∃ s1, xs1 ∈ lts.pairLang s0 s1 ∧ xs2 ∈ lts.pairLang s1 s2
```

`Cslib.LTS.pairViaLang_append_pairLang` (theorem, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Pair.lean#L71))

```lean
theorem LTS.pairViaLang_append_pairLang {lts : LTS State Symbol}
    {s0 s1 s2 : State} {xs1 xs2 : List Symbol} {via : Set State}
    (h1 : xs1 ∈ lts.pairViaLang via s0 s1) (h2 : xs2 ∈ lts.pairLang s1 s2) :
    xs1 ++ xs2 ∈ lts.pairViaLang via s0 s2
```

`Cslib.LTS.pairLang_append_pairViaLang` (theorem, [line 80](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Pair.lean#L80))

```lean
theorem LTS.pairLang_append_pairViaLang {lts : LTS State Symbol}
    {s0 s1 s2 : State} {xs1 xs2 : List Symbol} {via : Set State}
    (h1 : xs1 ∈ lts.pairLang s0 s1) (h2 : xs2 ∈ lts.pairViaLang via s1 s2) :
    xs1 ++ xs2 ∈ lts.pairViaLang via s0 s2
```

`Cslib.LTS.pairViaLang_split` (theorem, [line 86](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Pair.lean#L86))

```lean
theorem LTS.pairViaLang_split {lts : LTS State Symbol} {s0 s2 : State} {xs1 xs2 : List Symbol}
    {via : Set State} (h : xs1 ++ xs2 ∈ lts.pairViaLang via s0 s2) :
    ∃ s1, xs1 ∈ lts.pairViaLang via s0 s1 ∧ xs2 ∈ lts.pairLang s1 s2 ∨
          xs1 ∈ lts.pairLang s0 s1 ∧ xs2 ∈ lts.pairViaLang via s1 s2
```

`Cslib.Automata.NA.Buchi.language_eq_fin_iSup_hmul_omegaPow` (theorem, [line 106](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Pair.lean#L106))

> The ω-language accepted by a finite-state Büchi automaton is the finite union of ω-languages
> of the form `L * M^ω`, where all `L`s and `M`s are regular languages.

```lean
theorem language_eq_fin_iSup_hmul_omegaPow
    [Inhabited Symbol] [Finite State] (na : Buchi State Symbol) :
    language na = ⨆ s ∈ na.start, ⨆ t ∈ na.accept, (na.pairLang s t) * (na.pairLang t t)^ω
```

## Depends on

- [Nondeterministic Automaton](basic.md)

## Proof depends on

- [Regular languages](../../languages/regularlanguage.md)
- [Temporal reasoning over infinite sequences](../../../foundations/data/omegasequence/temporal.md)

## Sources

- [Cslib/Computability/Automata/NA/Pair.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Pair.lean)
