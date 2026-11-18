---
catalog: module
lean: Language.NerodeCongruence, Language.NerodeQuotient, Language.NerodeCongruenceDA, Language.nerodeCongruenceDA_language_eq, Language.da_nerodeCongruence_iff, Language.IsRegular.finite_nerodeQuotient, Language.IsRegular.iff_finite_nerodeQuotient, Language.dfa_num_state_ge, Language.dfa_num_state_min, Cslib.Automata.DA.FinAcc.IsMinimalAutomaton, Cslib.Automata.DA.FinAcc.StateCongruence, Cslib.Automata.DA.FinAcc.stateCongruence_le_nerodeCongruence, Cslib.Automata.DA.FinAcc.unique_minimal
statement: formalized
proof: formalized
---

# Myhill-Nerode Theorem

`Cslib.Computability.Languages.MyhillNerode`, in [Cslib/Computability/Languages/MyhillNerode.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/MyhillNerode.lean), by Akhilesh Balaji, Ching-Tsun Chou.

> Let `l` be a language on an alphabet `α`. The Nerode congruence (referred to as `c_l`
> in comments below) of a language `l` is a right congruence on strings where two strings are
> related iff all their right extensions are either both in the language or both not in it.
>
> The Myhill-Nerode theorem has three parts [WikipediaMyhillNerode2026]:
>
> (1) `l` is regular iff `c_l` has a finite number `N` of equivalence classes.
>
> (2) `N` is the number of states of the minimal DFA accepting `l`.
>
> (3) The minimal DFA is unique up to unique isomorphism. That is, for any
>     minimal DFA accepting `l`, there exists exactly an isomorphism from it to the
>     canonical DFA whose states are the equivalence classes of `c_l`, whose
>     state transitions are of the form `⟦ x ⟧ → ⟦ x ++ [a] ⟧` (where `a : α`
>     and `x : List α`), whose initial state is `⟦ [] ⟧`, and whose accepting states
>     are `{ ⟦ x ⟧ | x ∈ l }`.
>
> ## References
>
> * [J. E. Hopcroft, R. Motwani, J. D. Ullman,
>   *Introduction to Automata Theory, Languages, and Computation*][Hopcroft2006]
> * [T. Malkin, *COMS W3261: Computer Science Theory, Handout 3: The Myhill-Nerode Theorem
>    and Implications*][Malkin2024]
> * [Wikipedia contributors, Myhill–Nerode theorem][WikipediaMyhillNerode2026]

`Language.NerodeCongruence` (definition, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/MyhillNerode.lean#L53))

> The Nerode congruence (henceforth called `c_l`) of a language `l` is a right congruence on
> strings where two strings are related iff all their right extensions are either both in the language
> or both not in it.

```lean
def NerodeCongruence (l : Language α) : RightCongruence α
```

`Language.NerodeQuotient` (abbreviation, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/MyhillNerode.lean#L61))

> The quotient type of a Nerode congruence.

```lean
abbrev NerodeQuotient (l : Language α)
```

`Language.NerodeCongruenceDA` (definition, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/MyhillNerode.lean#L67))

> The Nerode congruence of a language `l` gives rise to a DFA where each state corresponds to an
> equivalence class of the language under the Nerode congruence. Note that this is simply the DFA
> given rise to by the underlying right congruence with only the accept states specified here as
> `{⟦ x ⟧ | x ∈ l}`.

```lean
def NerodeCongruenceDA (l : Language α) : DA.FinAcc (l.NerodeQuotient) α
```

`Language.nerodeCongruenceDA_language_eq` (theorem, [line 74](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/MyhillNerode.lean#L74))

> The DFA constructed from the Nerode congruence `c_l` on `l` accepts `l`.

```lean
theorem nerodeCongruenceDA_language_eq (l : Language α) :
    language (l.NerodeCongruenceDA) = l
```

`Language.da_nerodeCongruence_iff` (theorem, [line 89](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/MyhillNerode.lean#L89))

> The statement (two strings are related by the Nerode congruence `c_l` on `l` iff all their right
> extensions are either both in the language or both not in it) is equivalent to stating that (all
> their right extensions are either both accepted or rejected by the DFA given rise to by `c_l`.)

```lean
theorem da_nerodeCongruence_iff {State : Type*} (M : DA.FinAcc State α) (x y : List α) :
    ((language M).NerodeCongruence).r x y ↔
    ∀ z, M.mtr (M.mtr M.start x) z ∈ M.accept ↔ M.mtr (M.mtr M.start y) z ∈ M.accept
```

`Language.IsRegular.finite_nerodeQuotient` (theorem, [line 96](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/MyhillNerode.lean#L96))

> If `l` is regular then the Nerode congruence on `l` has finitely many equivalence classes.

```lean
theorem IsRegular.finite_nerodeQuotient (h : l.IsRegular) :
    Finite (l.NerodeQuotient)
```

`Language.IsRegular.iff_finite_nerodeQuotient` (theorem, [line 113](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/MyhillNerode.lean#L113))

> `l` is regular iff the Nerode congruence on `l` has finitely many equivalence classes.

```lean
theorem IsRegular.iff_finite_nerodeQuotient {l : Language α} :
    l.IsRegular ↔ Finite (l.NerodeQuotient)
```

`Language.dfa_num_state_ge` (theorem, [line 125](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/MyhillNerode.lean#L125))

> Given a set of strings all distinguishable by `l` (i.e., not related to each other by the Nerode
> congruence on `l`), the number of states in the DFA accepting `l` is at least the number of strings
> in the set.

```lean
theorem dfa_num_state_ge
    {l : Language α} {ws : Set (List α)} [Finite ws]
    (hws : ws.Pairwise (¬ (l.NerodeCongruence).r · ·))
    {State : Type*} [Finite State] {M : DA.FinAcc State α} (hm : language M = l) :
    Nat.card ws ≤ Nat.card State
```

`Language.dfa_num_state_min` (theorem, [line 146](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/MyhillNerode.lean#L146))

> All DFAs accepting `l` must have at least as many states as the number of equivalence classes
> of the Nerode congruence on `l`.

```lean
theorem dfa_num_state_min {State : Type} {M : DA.FinAcc State α} [Finite State] :
    Nat.card (language M).NerodeQuotient ≤ Nat.card State
```

`Cslib.Automata.DA.FinAcc.IsMinimalAutomaton` (definition, [line 168](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/MyhillNerode.lean#L168))

> The minimal DFA accepting `l` has the same number of states as the number of equivalence classes
> of the Nerode congruence on `l`.

```lean
def IsMinimalAutomaton {State : Type*} (M : FinAcc State α) (l : Language α)
```

`Cslib.Automata.DA.FinAcc.StateCongruence` (definition, [line 174](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/MyhillNerode.lean#L174))

> Given a DFA `M`, two strings are related iff they reach the same state under when run through
> `M`. The Nerode congruence is the state congruence with respect to the minimal DFA accepting `l`.

```lean
def StateCongruence (M : FinAcc State α) : RightCongruence α
```

`Cslib.Automata.DA.FinAcc.stateCongruence_le_nerodeCongruence` (theorem, [line 184](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/MyhillNerode.lean#L184))

> The Nerode congruence is the most coarse state congruence given a language.

```lean
theorem stateCongruence_le_nerodeCongruence {x y : List α}
    (h : (StateCongruence M).r x y) : ((language M).NerodeCongruence).r x y
```

`Cslib.Automata.DA.FinAcc.unique_minimal` (theorem, [line 192](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/MyhillNerode.lean#L192))

> The minimal DFA `M` accepting the language `l` is unique up to unique isomorphism.

```lean
theorem unique_minimal [Finite State]
    (l : Language α) (hr : l.IsRegular) (hm : M.IsMinimalAutomaton l) :
    ∃! φ : State ≃ l.NerodeQuotient, ∀ x, φ (M.mtr M.start x) = ⟦ x ⟧
```

## Depends on

- [Deterministic automaton corresponding to a right congruence](../automata/da/congr.md)

## Proof depends on

- [Buchi Congruence](congruences/buchicongruence.md)

## Sources

- [Cslib/Computability/Languages/MyhillNerode.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/MyhillNerode.lean)
