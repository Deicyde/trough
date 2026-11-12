---
catalog: module
lean: List.AllButFirstLast, List.allButFirstLast_iff_getElem, List.allButFirstLast_imp, List.allButFirstLast_append, List.findIdxButFirstLast?, List.findIdxButFirstLast?_isSome, List.findIdxButFirstLast?_eq, List.findIdxButFirstLastRev?, List.findIdxButFirstLastRev?_eq, Cslib.LTS.BddExec, Cslib.LTS.bddLang, Cslib.LTS.bddLang_bound_zero, Cslib.LTS.bddLang_eq_nfa, Cslib.LTS.splitFirstTake, Cslib.LTS.splitFirstDrop, Cslib.LTS.splitFirst_mem, Cslib.LTS.bddLang_splitFirst, Cslib.LTS.splitLastTake, Cslib.LTS.splitLastDrop, Cslib.LTS.splitLast_mem, Cslib.LTS.splitLastDrop_mem_nonempty, Cslib.LTS.bddLang_splitLast, Cslib.LTS.bddLang_kstar, Cslib.LTS.regex, Cslib.LTS.bddLang_eq_regex, Cslib.LTS.fin_nfa_single_start_accept_eq_regex, Cslib.Automata.NA.FinAcc.nfa_single_start_accept_reindex, Cslib.Automata.NA.FinAcc.nfa_single_start_accept_eq_regex, Cslib.Automata.NA.FinAcc.nfa_eq_regex
statement: formalized
proof: formalized
---

# Kleene's Algorithm

`Cslib.Computability.Languages.KleeneAlgorithm`, in [Cslib/Computability/Languages/KleeneAlgorithm.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean), by Brooke Gill, Chi-Yun Hsu.

> Kleene's algorithm constructs a regular expression by induction on a bound that restricts
> which interior states an execution may pass through.
> It is used to prove a direction of `Cslib.Language.IsRegular.iff_regex`, that
> every language accepted by a DFA comprised of finite states is the language of a regular expression.
> We implement Kleene's algorithm for the more general case of an NFA instead of DFA,
> since `Execution` is developed for `LTS` but not `FLTS`.
> The main theorem is `NA.FinAcc.nfa_eq_regex`.
>
> ## Main definitions
> - `LTS.bddLang start last bound`: The language of finite words that are accepted by an execution
> of an LTS with state type `Fin n`, where the start state is `start`, the last state is `last`,
> and all states of the execution except for the first and last are less than `bound`.
> - `LTS.regex s t r`: The regular expression for the executions of an LTS with state type `Fin n`
> from state `s` to state `t`, whose interior states are all under the bound `r`.
>
> ## Main results
> - `NA.FinAcc.nfa_eq_regex`: Any NFA has a matching regular expression.
> - `LTS.bddLang_eq_nfa`: `LTS.bddLang` is equal to the language of an NFA
> when `bound` is greater than or equal to the total number of states.
> - `LTS.bddLang_eq_regex`: `LTS.regex s t r` matches the language `LTS.bddLang s t r`.
>
> ## References
>
> * [J. E. Hopcroft, R. Motwani, J. D. Ullman,
>   *Introduction to Automata Theory, Languages, and Computation*][Hopcroft2006]

`List.AllButFirstLast` (definition, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L51))

> All but the first and last elements of the list `as` satisfy the predicate `p`.

```lean
def AllButFirstLast (p : α → Bool) (as : List α) : Prop
```

`List.allButFirstLast_iff_getElem` (theorem, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L54))

```lean
theorem allButFirstLast_iff_getElem (p : α → Bool) (as : List α) :
    as.AllButFirstLast p ↔ ∀ i (_ : 0 < i ∧ i < as.length - 1), p as[i]
```

`List.allButFirstLast_imp` (theorem, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L65))

```lean
theorem allButFirstLast_imp {p q : α → Bool} {as : List α} (h : ∀ x, p x → q x)
    (hp : as.AllButFirstLast p) : as.AllButFirstLast q
```

`List.allButFirstLast_append` (theorem, [line 69](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L69))

```lean
theorem allButFirstLast_append {p : α → Bool} {as bs : List α} (hlen : 0 < as.length)
    (ha_last : p as[as.length - 1]) (ha : as.AllButFirstLast p) (hb : bs.AllButFirstLast p) :
    (as ++ bs.tail).AllButFirstLast p
```

`List.findIdxButFirstLast?` (definition, [line 85](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L85))

> The index of the first element in a list `as` that satisfies a predicate `p`,
> excluding the first and last element.

```lean
def findIdxButFirstLast? (p : α → Bool) (as : List α) : Option ℕ
```

`List.findIdxButFirstLast?_isSome` (theorem, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L88))

```lean
theorem findIdxButFirstLast?_isSome (p : α → Bool) (as : List α) :
    (as.findIdxButFirstLast? p).isSome ↔ (∃ x ∈ as.tail.dropLast, p x)
```

`List.findIdxButFirstLast?_eq` (theorem, [line 92](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L92))

```lean
theorem findIdxButFirstLast?_eq {p : α → Bool} {as : List α} {i : ℕ} :
    as.findIdxButFirstLast? p = some i ↔
    ∃ _ : 0 < i ∧ i < as.length - 1, p as[i] ∧
      ∀ j (_ : 0 < j ∧ j < i), p as[j] = false
```

`List.findIdxButFirstLastRev?` (definition, [line 113](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L113))

> The index of the last element in a list `as` that satisfies a predicate `p`,
> excluding the first and last element.

```lean
def findIdxButFirstLastRev? (p : α → Bool) (as : List α) : Option ℕ
```

`List.findIdxButFirstLastRev?_eq` (theorem, [line 116](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L116))

```lean
theorem findIdxButFirstLastRev?_eq {p : α → Bool} {as : List α} {i : ℕ} :
    as.findIdxButFirstLastRev? p = some i ↔
    ∃ _ : 0 < i ∧ i < as.length - 1, p as[i] ∧
      ∀ j (_ : i < j ∧ j < as.length - 1), p as[j] = false
```

`Cslib.LTS.BddExec` (definition, [line 148](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L148))

> An execution of an LTS with state type `Fin n`,
> where all states of the execution except for the first and last are less than `bound`.

```lean
def BddExec (lts : LTS (Fin n) Symbol) (start : Fin n) (xs : List Symbol) (last : Fin n)
    (ss : List (Fin n)) (bound : ℕ) : Prop
```

`Cslib.LTS.bddLang` (definition, [line 153](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L153))

> The language of finite words that are accepted by a `BddExec`.

```lean
def bddLang (lts : LTS (Fin n) Symbol) (start last : Fin n) (bound : ℕ) : Language Symbol
```

`Cslib.LTS.bddLang_bound_zero` (theorem, [line 156](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L156))

```lean
theorem bddLang_bound_zero (lts : LTS (Fin n) Symbol) (s t : Fin n) {xs : List Symbol}
   (hxs : ¬xs = []) : xs ∈ lts.bddLang s t 0 ↔ ∃ a, lts.Tr s a t ∧ xs = [a]
```

`Cslib.LTS.bddLang_eq_nfa` (theorem, [line 170](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L170))

```lean
theorem bddLang_eq_nfa (lts : LTS (Fin n) Symbol) (s t : Fin n) {r : ℕ} (_ : n ≤ r) :
    lts.bddLang s t r = language (NA.FinAcc.mk ⟨lts, {s}⟩ {t})
```

`Cslib.LTS.splitFirstTake` (definition, [line 187](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L187))

> With an execution of the string `xs` through states `ss`,
> `splitFirstTake xs ss r` returns a prefix of `xs`
> which ends at the FIRST occurrence (excluding the first and last state) of state `r` in `ss`.
> When no such occurrence of `r` exists, `splitFirstTake` returns the empty string; however,
> the current file does not use the `splitFirstTake` in such situation.
> The actual definition does not require an execution, just the string `xs` and the states `ss`.

```lean
def splitFirstTake (xs : List Symbol) (ss : List (Fin n)) (r : Fin n) : List Symbol
```

`Cslib.LTS.splitFirstDrop` (definition, [line 198](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L198))

> With an execution of the string `xs` through states `ss`,
> `splitFirstDrop xs ss r` returns a suffix of `xs`
> which starts at the FIRST occurrence (excluding the first and last state) of state `r` in `ss`.
> When no such occurrence of `r` exists, `splitFirstDrop` returns the full string; however,
> the current file does not use the `splitFirstDrop` in such situation.
> The actual definition does not require an execution, just the string `xs` and the states `ss`.

```lean
def splitFirstDrop (xs : List Symbol) (ss : List (Fin n)) (r : Fin n) : List Symbol
```

`Cslib.LTS.splitFirst_mem` (theorem, [line 203](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L203))

```lean
theorem splitFirst_mem {lts : LTS (Fin n) Symbol} {s t r : Fin n} {xs : List Symbol}
    {ss : List (Fin n)} (hex : lts.Execution s xs t ss) (hbdd : ss.AllButFirstLast (· ≤ r))
    (hbdd' : ¬ss.AllButFirstLast (· < r)) :
    splitFirstTake xs ss r ∈ lts.bddLang s r r ∧
    splitFirstDrop xs ss r ∈ lts.bddLang r t (r + 1)
```

`Cslib.LTS.bddLang_splitFirst` (theorem, [line 239](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L239))

> Part of the recursion step of Kleene's algorithm.
> A run from `s` to `t` whose interior states are `≤ r` either has all interior states `< r`,
> or it splits at its first visit to `r` into
> an execution from `s` to `r` with all interior states `< r`, followed by
> an execution from `r` to `t` with all interior states `≤ r`.

```lean
theorem bddLang_splitFirst (lts : LTS (Fin n) Symbol) (s t r : Fin n) :
    lts.bddLang s t (r + 1) = lts.bddLang s t r + lts.bddLang s r r * lts.bddLang r t (r + 1)
```

`Cslib.LTS.splitLastTake` (definition, [line 269](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L269))

> With an execution of the string `xs` through states `ss`,
> `splitLastTake xs ss r` returns a prefix of `xs`
> which ends at the LAST occurrence (excluding the first and last state) of state `r` in `ss`.
> When no such occurrence of `r` exists, `splitLastTake` returns the empty string.
> The actual definition does not require an execution, just the string `xs` and the states `ss`.

```lean
def splitLastTake (xs : List Symbol) (ss : List (Fin n)) (r : Fin n) : List Symbol
```

`Cslib.LTS.splitLastDrop` (definition, [line 279](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L279))

> With an execution of the string `xs` through states `ss`,
> `splitLastDrop xs ss r` returns a prefix of `xs`
> which ends at the LAST occurrence (excluding the first and last state) of state `r` in `ss`.
> When no such occurrence of `r` exists, `splitLastDrop` returns the full string.
> The actual definition does not require an execution, just the string `xs` and the states `ss`.

```lean
def splitLastDrop (xs : List Symbol) (ss : List (Fin n)) (r : Fin n) : List Symbol
```

`Cslib.LTS.splitLast_mem` (theorem, [line 284](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L284))

```lean
theorem splitLast_mem {lts : LTS (Fin n) Symbol} {t r : Fin n} {xs : List Symbol}
    {ss : List (Fin n)} (hex : lts.Execution r xs t ss) (hbdd : ss.AllButFirstLast (· ≤ r)) :
    splitLastTake xs ss r ∈ lts.bddLang r r (r + 1) ∧
    splitLastDrop xs ss r ∈ lts.bddLang r t r
```

`Cslib.LTS.splitLastDrop_mem_nonempty` (theorem, [line 318](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L318))

```lean
theorem splitLastDrop_mem_nonempty {lts : LTS (Fin n) Symbol} {t r : Fin n} {xs : List Symbol}
    {ss : List (Fin n)} (hxs : xs ≠ []) (hex : lts.Execution r xs t ss)
    (hbdd : ss.AllButFirstLast (· ≤ r)) : splitLastDrop xs ss r ∈ lts.bddLang r t r - 1
```

`Cslib.LTS.bddLang_splitLast` (theorem, [line 335](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L335))

> Part of the recursion step of Kleene's algorithm.
> An execution from `r` to `t` whose interior states are `≤ r` splits at its last visit to `r` into
> an execution from `r` to `r` with all interior states `≤ r`, followed by
> an execution from `r` to `t` with all interior states `< r`.

```lean
theorem bddLang_splitLast (lts : LTS (Fin n) Symbol) (t r : Fin n) :
    lts.bddLang r t (r + 1) = lts.bddLang r r (r + 1) * lts.bddLang r t r
```

`Cslib.LTS.bddLang_kstar` (theorem, [line 361](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L361))

> Part of the recursion step of Kleene's algorithm.
> An execution from `r` to `r` whose interior states are `≤ r` is
> a concatenation of executions from `r` to `r` whose interior states are all `≤ r`.

```lean
theorem bddLang_kstar (lts : LTS (Fin n) Symbol) (r : Fin n) :
    lts.bddLang r r (r + 1) = (lts.bddLang r r r)∗
```

`Cslib.LTS.regex` (definition, [line 400](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L400))

> `regex s t r` is the regular expression for the path from state `s` to `t`
> passing through states `< r`.
> When `r = 0`, `s = t`, the regex is empty string `ε` union all characters from state `s` to `s`.
> When `r = 0`, `s ≠ t`, the regex is all characters from state `s` to `t`.
> For `r + 1`, the regex is the union of `regex s t r` and
> `(regex s r r) (regex r r r)∗ (regex r t r)`.

```lean
noncomputable def regex (lts : LTS (Fin n) Symbol) (s t : Fin n) : ℕ → RegularExpression Symbol
```

`Cslib.LTS.bddLang_eq_regex` (theorem, [line 411](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L411))

> `LTS.regex s t r` matches the language `LTS.bddLang s t r`.

```lean
theorem bddLang_eq_regex {r : ℕ} {lts : LTS (Fin n) Symbol} {s t : Fin n} :
    lts.bddLang s t r = (regex lts s t r).matches'
```

`Cslib.LTS.fin_nfa_single_start_accept_eq_regex` (theorem, [line 443](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L443))

> An NFA with state type `Fin n` and with exactly one start state `s` and
> exactly one accept state `t` has a matching regular expression given by `LTS.regex s t n`.

```lean
theorem fin_nfa_single_start_accept_eq_regex (lts : LTS (Fin n) Symbol) (s t : Fin n) :
    language (NA.FinAcc.mk ⟨lts, {s}⟩ {t}) = (lts.regex s t n).matches'
```

`Cslib.Automata.NA.FinAcc.nfa_single_start_accept_reindex` (theorem, [line 453](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L453))

```lean
theorem nfa_single_start_accept_reindex (nfa : NA.FinAcc State Symbol) (e : State ≃ State')
    {s t : State} (hstart : nfa.start = {s}) (haccept : nfa.accept = {t}) :
    language nfa = language (NA.FinAcc.mk ⟨(nfa.toLTS.reindex e), {e s}⟩ {e t})
```

`Cslib.Automata.NA.FinAcc.nfa_single_start_accept_eq_regex` (theorem, [line 466](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L466))

> An NFA with exactly one start state and exactly one accept state
> has a matching regular expression.

```lean
theorem nfa_single_start_accept_eq_regex [Finite Symbol] [Finite State]
    (nfa : NA.FinAcc State Symbol) (s t : State)
    (hstart : nfa.start = {s}) (haccept : nfa.accept = {t}) :
    ∃ r : RegularExpression Symbol, language nfa = r.matches'
```

`Cslib.Automata.NA.FinAcc.nfa_eq_regex` (theorem, [line 475](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean#L475))

> Any NFA has a matching regular expression.

```lean
theorem nfa_eq_regex [Finite Symbol] [Finite State] (nfa : NA.FinAcc State Symbol) :
    ∃ r : RegularExpression Symbol, language nfa = r.matches'
```

## Depends on

- [Nondeterministic Automaton](../automata/na/basic.md)
- [Bisimulation and Bisimilarity](../../foundations/semantics/lts/bisimulation.md)

## Proof depends on

- [Regular Expressions (additional definitions and theorems)](regularexpressions.md)

## Sources

- [Cslib/Computability/Languages/KleeneAlgorithm.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/KleeneAlgorithm.lean)
