---
catalog: module
lean: Cslib.Automata.NA.FinAcc.loop, Cslib.Automata.NA.loop_run_left_left, Cslib.Automata.NA.loop_run_left_right, Cslib.Automata.NA.loop_run_left_right_left, Cslib.Automata.NA.loop_run_from_left, Cslib.Automata.NA.loop_run_one_iter, Cslib.Automata.NA.loop_fin_run_exists, Cslib.Automata.NA.loop_fin_run_mtr, Cslib.Automata.NA.loop_run_exists, Cslib.Automata.NA.Buchi.loop_language_eq, Cslib.Automata.NA.FinAcc.finLoop, Cslib.Automata.NA.FinAcc.loop_language_eq
statement: formalized
proof: formalized
---

# Loop construction on nondeterministic automata

`Cslib.Computability.Automata.NA.Loop`, in [Cslib/Computability/Automata/NA/Loop.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Loop.lean), by Ching-Tsun Chou.

`Cslib.Automata.NA.FinAcc.loop` (definition, [line 27](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Loop.lean#L27))

> `na.loop` mimics `na`, but can nondeterministically decide to "loop back" by identifying
> an accepting state of `na` with a starting state of `na`.  This identification is achieved
> via a new dummy state `()`, which is the sole starting state and the sole accepting state
> of `na.loop`.

```lean
def FinAcc.loop (na : FinAcc State Symbol) : NA (Unit ⊕ State) Symbol
```

`Cslib.Automata.NA.loop_run_left_left` (lemma, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Loop.lean#L37))

```lean
lemma loop_run_left_left {xs : ωSequence Symbol} {ss : ωSequence (Unit ⊕ State)}
    (h : na.loop.Run xs ss) (h1 : (ss 1).isLeft) : [xs 0] ∈ language na
```

`Cslib.Automata.NA.loop_run_left_right` (lemma, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Loop.lean#L47))

```lean
lemma loop_run_left_right {xs : ωSequence Symbol} {ss : ωSequence (Unit ⊕ State)}
    (h : na.loop.Run xs ss) (n : ℕ) (h1 : 0 < n) (h2 : ∀ k, 0 < k → k ≤ n → (ss k).isRight) :
    ∃ s t, na.MTr s (xs.take n) t ∧ s ∈ na.start ∧ ss n = inr t
```

`Cslib.Automata.NA.loop_run_left_right_left` (lemma, [line 63](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Loop.lean#L63))

```lean
lemma loop_run_left_right_left {xs : ωSequence Symbol} {ss : ωSequence (Unit ⊕ State)}
    (h : na.loop.Run xs ss) (n : ℕ) (h1 : 0 < n ∧ (ss n).isLeft)
    (h2 : ∀ k, 0 < k → k < n → (ss k).isRight) : xs.take n ∈ language na
```

`Cslib.Automata.NA.loop_run_from_left` (lemma, [line 73](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Loop.lean#L73))

```lean
lemma loop_run_from_left {xs : ωSequence Symbol} {ss : ωSequence (Unit ⊕ State)}
    (h : na.loop.Run xs ss) (n : ℕ) (h1 : (ss n).isLeft) :
    na.loop.Run (xs.drop n) (ss.drop n)
```

`Cslib.Automata.NA.loop_run_one_iter` (theorem, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Loop.lean#L82))

> A run of `na.loop` containing at least one non-initial `()` state is the concatenation
> of a nonempty finite run of `na` followed by a run of `na.loop`.

```lean
theorem loop_run_one_iter {xs : ωSequence Symbol} {ss : ωSequence (Unit ⊕ State)} {k : ℕ}
    (h : na.loop.Run xs ss) (h1 : 0 < k) (h2 : (ss k).isLeft) :
    ∃ n, n ≤ k ∧ xs.take n ∈ language na - 1 ∧ na.loop.Run (xs.drop n) (ss.drop n)
```

`Cslib.Automata.NA.loop_fin_run_exists` (theorem, [line 98](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Loop.lean#L98))

> For any finite word in `language na`, there is a corresponding finite run of `na.loop`.

```lean
theorem loop_fin_run_exists {xl : List Symbol} (h : xl ∈ language na) :
    ∃ sl : List (Unit ⊕ State), ∃ _ : sl.length = xl.length + 1,
    sl[0] = inl () ∧ sl[xl.length] = inl () ∧
    ∀ k, (_ : k < xl.length) → na.loop.Tr sl[k] xl[k] sl[k + 1]
```

`Cslib.Automata.NA.loop_fin_run_mtr` (theorem, [line 117](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Loop.lean#L117))

> For any finite word in `language na`, there is a corresponding multistep transition
> of `na.loop`.

```lean
theorem loop_fin_run_mtr {xl : List Symbol} (h : xl ∈ language na) :
    na.loop.MTr (inl ()) xl (inl ())
```

`Cslib.Automata.NA.loop_run_exists` (theorem, [line 127](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Loop.lean#L127))

> For any infinite sequence `xls` of nonempty finite words from `language na`,
> there is an infinite run of `na.loop` corresponding to `xls.flatten` in which
> the state `()` marks the boundaries between the finite words in `xls`.

```lean
theorem loop_run_exists [Inhabited Symbol] {xls : ωSequence (List Symbol)}
    (h : ∀ k, (xls k) ∈ language na - 1) :
    ∃ ss, na.loop.Run xls.flatten ss ∧ ∀ k, ss (xls.cumLen k) = inl ()
```

`Cslib.Automata.NA.Buchi.loop_language_eq` (theorem, [line 144](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Loop.lean#L144))

> The Buchi ω-language accepted by `na.loop` is the ω-power of the language accepted by `na`.

```lean
theorem loop_language_eq [Inhabited Symbol] :
    language (Buchi.mk na.loop {inl ()}) = (language na)^ω
```

`Cslib.Automata.NA.FinAcc.finLoop` (definition, [line 173](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Loop.lean#L173))

> `finLoop na` is the loop construction applied to the "totalized" version of `na`.

```lean
def finLoop (na : FinAcc State Symbol) : NA (Unit ⊕ Option State) Symbol
```

`Cslib.Automata.NA.FinAcc.loop_language_eq` (theorem, [line 184](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Loop.lean#L184))

> `finLoop na` accepts the Kleene star of the language of `na`, assuming that
> the latter is nonempty.

```lean
theorem loop_language_eq [Inhabited Symbol] (h : ¬ language na = 0) :
    language (FinAcc.mk na.finLoop {inl ()}) = (language na)∗
```

## Depends on

- [Making a nondeterministic automaton total](total.md)

## Proof depends on

- [Temporal reasoning over infinite sequences](../../../foundations/data/omegasequence/temporal.md)

## Sources

- [Cslib/Computability/Automata/NA/Loop.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Loop.lean)
