---
catalog: module
lean: Cslib.Automata.NA.concat, Cslib.Automata.NA.concat_start_right, Cslib.Automata.NA.concat_run_left, Cslib.Automata.NA.concat_run_left_right, Cslib.Automata.NA.concat_run_right, Cslib.Automata.NA.concat_run_proj, Cslib.Automata.NA.concat_run_exists, Cslib.Automata.NA.Buchi.concat_language_eq, Cslib.Automata.NA.FinAcc.finConcat, Cslib.Automata.NA.FinAcc.finConcat_language_eq
statement: formalized
proof: formalized
---

# Concatenation of nondeterministic automata

`Cslib.Computability.Automata.NA.Concat`, in [Cslib/Computability/Automata/NA/Concat.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Concat.lean), by Ching-Tsun Chou.

`Cslib.Automata.NA.concat` (definition, [line 26](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Concat.lean#L26))

> `concat na1 na2` starts by running `na1` and then nondeterministically switches to `na2`
> by identifying an accepting state of `na1` with an initial state of `na2`. If `na1` accepts the
> empty word, it may also start running `na2` from the beginning. Once it starts running `na2`,
> it cannot go back to `na1`.

```lean
def concat (na1 : FinAcc State1 Symbol) (na2 : NA State2 Symbol) : NA (State1 ⊕ State2) Symbol
```

`Cslib.Automata.NA.concat_start_right` (lemma, [line 36](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Concat.lean#L36))

```lean
lemma concat_start_right {xs : ωSequence Symbol} {ss : ωSequence (State1 ⊕ State2)}
    (hc : (concat na1 na2).Run xs ss) (hr : (ss 0).isRight) : [] ∈ language na1
```

`Cslib.Automata.NA.concat_run_left` (lemma, [line 40](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Concat.lean#L40))

```lean
lemma concat_run_left {xs : ωSequence Symbol} {ss : ωSequence (State1 ⊕ State2)}
    (hc : (concat na1 na2).Run xs ss) (n : ℕ) (hl : ∀ k ≤ n, (ss k).isLeft) :
    ∃ s1 t1, na1.MTr s1 (xs.take n) t1 ∧ s1 ∈ na1.start ∧ ss 0 = inl s1 ∧ ss n = inl t1
```

`Cslib.Automata.NA.concat_run_left_right` (lemma, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Concat.lean#L53))

```lean
lemma concat_run_left_right {xs : ωSequence Symbol} {ss : ωSequence (State1 ⊕ State2)}
    (hc : (concat na1 na2).Run xs ss) (n : ℕ) (hn : 0 < n)
    (hl : ∀ k < n, (ss k).isLeft) (hr : (ss n).isRight) : (xs.take n) ∈ language na1
```

`Cslib.Automata.NA.concat_run_right` (lemma, [line 62](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Concat.lean#L62))

```lean
lemma concat_run_right {xs : ωSequence Symbol} {ss : ωSequence (State1 ⊕ State2)}
    (hc : (concat na1 na2).Run xs ss) (n : ℕ) (hl : ∀ k < n, (ss k).isLeft) (hr : (ss n).isRight) :
    ∃ ss2, na2.Run (xs.drop n) ss2 ∧ ss.drop n = ss2.map inr
```

`Cslib.Automata.NA.concat_run_proj` (theorem, [line 79](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Concat.lean#L79))

> A run of `concat na1 na2` containing at least one `na2` state is the concatenation of
> an accepting finite run of `na1` followed by a run of `na2`.

```lean
theorem concat_run_proj {xs : ωSequence Symbol} {ss : ωSequence (State1 ⊕ State2)} {k : ℕ}
    (hc : (concat na1 na2).Run xs ss) (hr : (ss k).isRight) :
    ∃ n, n ≤ k ∧ xs.take n ∈ language na1 ∧
    ∃ ss2, na2.Run (xs.drop n) ss2 ∧ ss.drop n = ss2.map inr
```

`Cslib.Automata.NA.concat_run_exists` (theorem, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Concat.lean#L101))

> Given an accepting finite run of `na1` and a run of `na2`, there exists a run of
> `concat na1 na2` that is the concatenation of the two runs.

```lean
theorem concat_run_exists {xs1 : List Symbol} {xs2 : ωSequence Symbol} {ss2 : ωSequence State2}
    (h1 : xs1 ∈ language na1) (h2 : na2.Run xs2 ss2) :
    ∃ ss, (concat na1 na2).Run (xs1 ++ω xs2) ss ∧ ss.drop xs1.length = ss2.map inr
```

`Cslib.Automata.NA.Buchi.concat_language_eq` (theorem, [line 134](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Concat.lean#L134))

> The Buchi automaton formed from `concat na1 na2` accepts the ω-language that is
> the concatenation of the language of `na1` and the ω-language of `na2`.

```lean
theorem concat_language_eq {acc2 : Set State2} :
    language (Buchi.mk (concat na1 na2) (inr '' acc2)) =
    language na1 * language (Buchi.mk na2 acc2)
```

`Cslib.Automata.NA.FinAcc.finConcat` (definition, [line 156](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Concat.lean#L156))

> `finConcat na1 na2` is the concatenation of the "totalized" versions of `na1` and `na2`.

```lean
def finConcat (na1 : FinAcc State1 Symbol) (na2 : FinAcc State2 Symbol)
  : NA (Option State1 ⊕ Option State2) Symbol
```

`Cslib.Automata.NA.FinAcc.finConcat_language_eq` (theorem, [line 169](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Concat.lean#L169))

> `finConcat na1 na2` accepts the concatenation of the languages of `na1` and `na2`.

```lean
theorem finConcat_language_eq [Inhabited Symbol] :
    language (FinAcc.mk (finConcat na1 na2) (inr '' (some '' na2.accept))) =
    language na1 * language na2
```

## Depends on

- [Making a nondeterministic automaton total](total.md)

## Proof depends on

- [Temporal reasoning over infinite sequences](../../../foundations/data/omegasequence/temporal.md)

## Sources

- [Cslib/Computability/Automata/NA/Concat.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Concat.lean)
