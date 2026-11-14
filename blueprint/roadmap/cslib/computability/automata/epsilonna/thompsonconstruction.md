---
catalog: module
lean: Cslib.Automata.εNA.FinAcc.zero, Cslib.Automata.εNA.FinAcc.epsilon, Cslib.Automata.εNA.FinAcc.char, Cslib.Automata.εNA.FinAcc.language_zero, Cslib.Automata.εNA.FinAcc.language_epsilon, Cslib.Automata.εNA.FinAcc.language_char, Cslib.Automata.εNA.FinAcc.sum, Cslib.Automata.εNA.FinAcc.language_sum, Cslib.Automata.εNA.FinAcc.union, Cslib.Automata.εNA.FinAcc.language_union, Cslib.Automata.εNA.FinAcc.ConcatTr, Cslib.Automata.εNA.FinAcc.concat, Cslib.Automata.εNA.FinAcc.concat_mTr_inr, Cslib.Automata.εNA.FinAcc.concat_mTr_inl, Cslib.Automata.εNA.FinAcc.language_concat, Cslib.Automata.εNA.FinAcc.StarTr, Cslib.Automata.εNA.FinAcc.star, Cslib.Automata.εNA.FinAcc.star_mTr_inr, Cslib.Automata.εNA.FinAcc.reduceOption_mem_kstar_of_star_mTr, Cslib.Automata.εNA.FinAcc.exists_star_mTr_of_mem_kstar, Cslib.Automata.εNA.FinAcc.language_star
statement: formalized
proof: formalized
---

# Thompson's construction

`Cslib.Computability.Automata.EpsilonNA.ThompsonConstruction`, in [Cslib/Computability/Automata/EpsilonNA/ThompsonConstruction.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ThompsonConstruction.lean), by Yusuf Demir.

> Thompson's construction turns a regular expression into an `εNA` with a single initial state and
> at most one accepting state [Thompson1968]. This file defines the automata it is assembled from,
> with their languages.
>
> ## Main definitions
>
> * `εNA.FinAcc.zero`, `εNA.FinAcc.epsilon`, `εNA.FinAcc.char x`: automata for the empty language,
>   the empty word and the word `[x]`.
> * `εNA.FinAcc.sum a b`: the states and transitions of `a` and `b` side by side, through
>   `LTS.unionSum`.
> * `εNA.FinAcc.union a b`: `sum a b` with a single initial and a single accepting state, through
>   `toSingleStartAccept`.
> * `εNA.FinAcc.concat a b`: `ε`-transitions from the accepting states of `a` to the initial states
>   of `b`.
> * `εNA.FinAcc.star a`: a fresh hub state, initial and accepting, with `ε`-transitions to the
>   initial states of `a` and from its accepting states.
>
> ## Main statements
>
> * `εNA.FinAcc.language_zero`, `εNA.FinAcc.language_epsilon`, `εNA.FinAcc.language_char`,
>   `εNA.FinAcc.language_sum`, `εNA.FinAcc.language_union`, `εNA.FinAcc.language_concat` and
>   `εNA.FinAcc.language_star`.
>
> ## References
>
> * [K. Thompson, *Regular expression search algorithm*][Thompson1968]

`Cslib.Automata.εNA.FinAcc.zero` (definition, [line 55](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ThompsonConstruction.lean#L55))

> An automaton with a single state, initial but not accepting, and no transitions.

```lean
def zero : FinAcc Unit Symbol
```

`Cslib.Automata.εNA.FinAcc.epsilon` (definition, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ThompsonConstruction.lean#L61))

> An automaton with a single state, initial and accepting, and no transitions.

```lean
def epsilon : FinAcc Unit Symbol
```

`Cslib.Automata.εNA.FinAcc.char` (definition, [line 68](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ThompsonConstruction.lean#L68))

> An automaton with two states, `false` initial and `true` accepting, joined by an
> `x`-transition.

```lean
def char (x : Symbol) : FinAcc Bool Symbol
```

`Cslib.Automata.εNA.FinAcc.language_zero` (theorem, [line 74](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ThompsonConstruction.lean#L74))

```lean
theorem language_zero : language (zero : FinAcc Unit Symbol) = 0
```

`Cslib.Automata.εNA.FinAcc.language_epsilon` (theorem, [line 80](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ThompsonConstruction.lean#L80))

```lean
theorem language_epsilon : language (epsilon : FinAcc Unit Symbol) = 1
```

`Cslib.Automata.εNA.FinAcc.language_char` (theorem, [line 92](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ThompsonConstruction.lean#L92))

```lean
theorem language_char (x : Symbol) : language (char x) = {[x]}
```

`Cslib.Automata.εNA.FinAcc.sum` (definition, [line 113](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ThompsonConstruction.lean#L113))

> The disjoint sum of `a` and `b`: their states and transitions side by side (`LTS.unionSum`),
> with the initial and the accepting states of both.

```lean
def sum (a : FinAcc S₁ Symbol) (b : FinAcc S₂ Symbol) : FinAcc (S₁ ⊕ S₂) Symbol
```

`Cslib.Automata.εNA.FinAcc.language_sum` (theorem, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ThompsonConstruction.lean#L121))

```lean
theorem language_sum (a : FinAcc S₁ Symbol) (b : FinAcc S₂ Symbol) :
    language (sum a b) = language a + language b
```

`Cslib.Automata.εNA.FinAcc.union` (definition, [line 144](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ThompsonConstruction.lean#L144))

> The union of `a` and `b`: their disjoint sum, with a single initial state and a single
> accepting state added by `toSingleStartAccept`.

```lean
def union (a : FinAcc S₁ Symbol) (b : FinAcc S₂ Symbol) : FinAcc (Bool ⊕ (S₁ ⊕ S₂)) Symbol
```

`Cslib.Automata.εNA.FinAcc.language_union` (theorem, [line 148](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ThompsonConstruction.lean#L148))

```lean
theorem language_union (a : FinAcc S₁ Symbol) (b : FinAcc S₂ Symbol) :
    language (union a b) = language a + language b
```

`Cslib.Automata.εNA.FinAcc.ConcatTr` (inductive type, [line 153](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ThompsonConstruction.lean#L153))

> The transitions of `concat a b`, whose states are those of `a` followed by those of `b`.

```lean
inductive ConcatTr (a : FinAcc S₁ Symbol) (b : FinAcc S₂ Symbol) :
    S₁ ⊕ S₂ → Option Symbol → S₁ ⊕ S₂ → Prop
  | left {s μ s'} : a.Tr s μ s' → ConcatTr a b (.inl s) μ (.inl s')
  | right {s μ s'} : b.Tr s μ s' → ConcatTr a b (.inr s) μ (.inr s')
  | bridge {s s'} : s ∈ a.accept → s' ∈ b.start → ConcatTr a b (.inl s) none (.inr s')
```

`Cslib.Automata.εNA.FinAcc.concat` (definition, [line 161](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ThompsonConstruction.lean#L161))

> The concatenation of `a` and `b`: `ε`-transitions lead from the accepting states of `a` to the
> initial states of `b`.

```lean
def concat (a : FinAcc S₁ Symbol) (b : FinAcc S₂ Symbol) : FinAcc (S₁ ⊕ S₂) Symbol
```

`Cslib.Automata.εNA.FinAcc.concat_mTr_inr` (theorem, [line 167](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ThompsonConstruction.lean#L167))

> A run of `concat a b` between two states of `b` is a run of `b`.

```lean
theorem concat_mTr_inr {s t : S₂} {μs : List (Option Symbol)}
    (h : (concat a b).MTr (.inr s) μs (.inr t)) : b.MTr s μs t
```

`Cslib.Automata.εNA.FinAcc.concat_mTr_inl` (theorem, [line 180](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ThompsonConstruction.lean#L180))

> A run of `concat a b` from a state of `a` to a state of `b` is a run of `a` to an accepting
> state, an `ε`-transition to an initial state of `b`, and a run of `b`.

```lean
theorem concat_mTr_inl {s : S₁} {t : S₂} {μs : List (Option Symbol)}
    (h : (concat a b).MTr (.inl s) μs (.inr t)) :
    ∃ s₁ ∈ a.accept, ∃ s₂ ∈ b.start, ∃ μs₁ μs₂, a.MTr s μs₁ s₁ ∧ b.MTr s₂ μs₂ t ∧
      μs = μs₁ ++ none :: μs₂
```

`Cslib.Automata.εNA.FinAcc.language_concat` (theorem, [line 196](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ThompsonConstruction.lean#L196))

```lean
theorem language_concat (a : FinAcc S₁ Symbol) (b : FinAcc S₂ Symbol) :
    language (concat a b) = language a * language b
```

`Cslib.Automata.εNA.FinAcc.StarTr` (inductive type, [line 221](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ThompsonConstruction.lean#L221))

> The transitions of `star a`, whose states are a fresh hub `inl ()` and the states of `a`.

```lean
inductive StarTr (a : FinAcc S₁ Symbol) : Unit ⊕ S₁ → Option Symbol → Unit ⊕ S₁ → Prop
  | inner {s μ s'} : a.Tr s μ s' → StarTr a (.inr s) μ (.inr s')
  | enter {s} : s ∈ a.start → StarTr a (.inl ()) none (.inr s)
  | exit {s} : s ∈ a.accept → StarTr a (.inr s) none (.inl ())
```

`Cslib.Automata.εNA.FinAcc.star` (definition, [line 228](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ThompsonConstruction.lean#L228))

> The Kleene star of `a`: a fresh hub state, initial and accepting, with `ε`-transitions to the
> initial states of `a` and from its accepting states.

```lean
def star (a : FinAcc S₁ Symbol) : FinAcc (Unit ⊕ S₁) Symbol
```

`Cslib.Automata.εNA.FinAcc.star_mTr_inr` (theorem, [line 235](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ThompsonConstruction.lean#L235))

> A run of `star a` from a state of `a` to the hub is a run of `a` to an accepting state, an
> `ε`-transition to the hub, and a run from the hub back to the hub.

```lean
theorem star_mTr_inr {s : S₁} {μs : List (Option Symbol)}
    (h : (star a).MTr (.inr s) μs (.inl ())) :
    ∃ t ∈ a.accept, ∃ μs₁ μs₂, a.MTr s μs₁ t ∧ (star a).MTr (.inl ()) μs₂ (.inl ()) ∧
      μs = μs₁ ++ none :: μs₂
```

`Cslib.Automata.εNA.FinAcc.reduceOption_mem_kstar_of_star_mTr` (theorem, [line 251](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ThompsonConstruction.lean#L251))

> A run of `star a` from the hub back to the hub reads a word of `(language a)∗`.

```lean
theorem reduceOption_mem_kstar_of_star_mTr {μs : List (Option Symbol)}
    (h : (star a).MTr (.inl ()) μs (.inl ())) : μs.reduceOption ∈ (language a)∗
```

`Cslib.Automata.εNA.FinAcc.exists_star_mTr_of_mem_kstar` (theorem, [line 276](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ThompsonConstruction.lean#L276))

> Every word of `(language a)∗` is read by a run of `star a` from the hub back to the hub.

```lean
theorem exists_star_mTr_of_mem_kstar {xs : List Symbol} (hxs : xs ∈ (language a)∗) :
    ∃ μs : List (Option Symbol), μs.reduceOption = xs ∧ (star a).MTr (.inl ()) μs (.inl ())
```

`Cslib.Automata.εNA.FinAcc.language_star` (theorem, [line 290](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ThompsonConstruction.lean#L290))

```lean
theorem language_star (a : FinAcc S₁ Symbol) : language (star a) = (language a)∗
```

## Depends on

- [Translation of εNA into εNA with a single start and a single accept state](tosinglestartaccept.md)
- [Union of LTSs](../../../foundations/semantics/lts/union.md)

## Sources

- [Cslib/Computability/Automata/EpsilonNA/ThompsonConstruction.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/ThompsonConstruction.lean)
