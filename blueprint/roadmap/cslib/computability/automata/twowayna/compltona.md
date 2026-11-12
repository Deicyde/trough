---
catalog: module
lean: Cslib.Automata.TwoWayNA.IsStepClosed, Cslib.Automata.TwoWayNA.IsRejectionCert, Cslib.Automata.TwoWayNA.IsRejectionCert.not_accepts, Cslib.Automata.TwoWayNA.reachable, Cslib.Automata.TwoWayNA.isRejectionCert_reachable, Cslib.Automata.TwoWayNA.not_accepts_iff_exists_isRejectionCert, Cslib.Automata.TwoWayNA.LocalOK, Cslib.Automata.TwoWayNA.isStepClosed_iff_localOK, Cslib.Automata.TwoWayNA.complToNA, Cslib.Automata.TwoWayNA.exists_accepting_mTr_iff, Cslib.Automata.TwoWayNA.accepts_complToNA_iff, Cslib.Automata.TwoWayNA.language_complToNA
statement: formalized
proof: formalized
---

# A finite acceptor for the complement of the language of a two-way automaton

`Cslib.Computability.Automata.TwoWayNA.ComplToNA`, in [Cslib/Computability/Automata/TwoWayNA/ComplToNA.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/ComplToNA.lean), by Christian Reitwiessner.

> For every nondeterministic two-way automaton (`TwoWayNA`) `a`, this file constructs a
> nondeterministic finite acceptor (`NA.FinAcc`) that accepts exactly the words rejected by `a`
> (`TwoWayNA.complToNA`, `TwoWayNA.language_complToNA`). We follow Vardi's proof, which --
> unlike Shepherdson's crossing-sequence argument -- characterises non-acceptance in a way that can
> be checked by a single left-to-right sweep over the input.
>
> This result is the main ingredient in proving equivalence of two-way and one-way automata, which
> can be found in `Cslib.Computability.Languages.RegularLanguages`.
>
> ## Vardi's condition of non-acceptance
>
> Fix a `TwoWayNA` `a` and an input word `input` of length `n`. A *rejection certificate* is a family
> of subsets `cert i ⊆ State`, one for every head position `i ∈ {0, …, n}`, subject to three
> conditions:
>
> 1. `cert` contains every initial state at position `0` (`IsRejectionCert.start_mem`);
> 2. `cert` is an invariant of the transitions of `a`: if the state `c.state` is in `cert c.pos` and
>   `a` can step from the configuration `c` to the configuration `c'`, then `c'.state` is in
>   `cert c'.pos` (`TwoWayNA.IsStepClosed`, `IsRejectionCert.step_closed`);
> 3. no state in `cert n`, i.e. at the position just past the end of the input, is accepting
>    (`IsRejectionCert.accept_notMem`).
>
> Intuitively, `cert i` over-approximates the set of states in which `a` can be while its head sits at
> position `i`: conditions 1 and 2 make `cert` an inductive invariant of the reachable configurations,
> and condition 3 says that this invariant rules out acceptance -- being preserved by every step, it
> holds at the end of every run (`LTS.mtrInv_of_trInv`). Conversely, the reachable states
> (`TwoWayNA.reachable`) themselves form the least such family, so a certificate exists exactly when
> `a` rejects (`TwoWayNA.not_accepts_iff_exists_isRejectionCert`).
>
> ## The finite acceptor for the complement
>
> The point of the reformulation is locality: `TwoWayNA.isStepClosed_iff_localOK` turns condition 2
> into a condition `TwoWayNA.LocalOK` relating only `cert (i - 1)`, `cert i` and `cert (i + 1)` with
> the symbol at position `i`. A finite acceptor can therefore guess the certificate while scanning the
> input, keeping only the last two subsets in its state. This is `TwoWayNA.complToNA`, and
> `TwoWayNA.accepts_complToNA_iff` shows that it accepts exactly the words rejected by `a`.
>
> ## Implementation notes
>
> A rejection certificate is an `ωSequence`, i.e. indexed by `ℕ` rather than by
> `Fin (input.length + 1)`, the type of `TwoWayNACfg.pos`: positions past the end of the input are
> simply left unconstrained, which avoids casts when the certificate is compared along a run, whose
> configurations carry their own input. The subset for the missing position to the left of the input
> is supplied by prepending `Set.univ` with `ωSequence.cons`.
>
> `TwoWayNA.exists_accepting_mTr_iff` is proved by induction on the input word, prepending a subset
> to the certificate at each step with `ωSequence.cons` and dropping one with `ωSequence.tail`.
>
> ## References
>
> * [M. Y. Vardi, *A note on the reduction of two-way automata to one-way automata*][Vardi1989]

> ## Vardi's condition of non-acceptance

`Cslib.Automata.TwoWayNA.IsStepClosed` (definition, [line 85](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/ComplToNA.lean#L85))

> Every step of `a` on `input` out of a state that `cert` attaches to the head position lands in a
> state that `cert` attaches to the new head position. The conjunct on the input restricts the
> invariant to the configurations that run on `input`.

```lean
def IsStepClosed (a : TwoWayNA State Symbol) (input : List Symbol)
    (cert : ωSequence (Set State)) : Prop
```

`Cslib.Automata.TwoWayNA.IsRejectionCert` (structure, [line 92](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/ComplToNA.lean#L92))

> A family of subsets of the state set, one for every position of the input head on `input`,
> which contains all initial states, is closed under the transitions of `a`, and contains no
> accepting state at the position just past the end of the input.

```lean
structure IsRejectionCert (a : TwoWayNA State Symbol) (input : List Symbol)
    (cert : ωSequence (Set State)) : Prop where
  /-- Every initial state occurs at the initial head position. -/
  start_mem : ∀ s ∈ a.start, s ∈ cert 0
  /-- The family is an invariant of the transitions of `a`. -/
  step_closed : a.IsStepClosed input cert
  /-- No accepting state occurs past the end of the input. -/
  accept_notMem : ∀ s ∈ cert input.length, s ∉ a.accept
```

`Cslib.Automata.TwoWayNA.IsRejectionCert.not_accepts` (theorem, [line 104](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/ComplToNA.lean#L104))

> If a rejection certificate for `input` exists, then `a` does not accept `input`.

```lean
theorem IsRejectionCert.not_accepts (hT : a.IsRejectionCert input cert) :
    ¬ Accepts a input
```

`Cslib.Automata.TwoWayNA.reachable` (definition, [line 114](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/ComplToNA.lean#L114))

> The set of states that `a` can be in while its head sits at position `i` of `input`, having
> started in an initial configuration.

```lean
def reachable (a : TwoWayNA State Symbol) (input : List Symbol) : ωSequence (Set State)
```

`Cslib.Automata.TwoWayNA.isRejectionCert_reachable` (theorem, [line 120](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/ComplToNA.lean#L120))

> If `a` does not accept `input`, then its reachable states form a rejection certificate.

```lean
theorem isRejectionCert_reachable (h : ¬ Accepts a input) :
    a.IsRejectionCert input (a.reachable input)
```

`Cslib.Automata.TwoWayNA.not_accepts_iff_exists_isRejectionCert` (theorem, [line 138](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/ComplToNA.lean#L138))

> A two-way automaton rejects an input exactly when a rejection certificate for it exists.

```lean
theorem not_accepts_iff_exists_isRejectionCert (a : TwoWayNA State Symbol)
    (input : List Symbol) :
    ¬ Accepts a input ↔ ∃ T, a.IsRejectionCert input T
```

> ## Localising the closure condition

`Cslib.Automata.TwoWayNA.LocalOK` (definition, [line 148](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/ComplToNA.lean#L148))

> Every move of `a` out of a state in `cur` while reading `x` lands in `left`, in `cur` or in
> `right`, according to whether it moves the head to the left, keeps it in place, or moves it to the
> right.

```lean
def LocalOK (a : TwoWayNA State Symbol) (x : Symbol) (left cur right : Set State) : Prop
```

`Cslib.Automata.TwoWayNA.isStepClosed_iff_localOK` (theorem, [line 154](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/ComplToNA.lean#L154))

> Closure of `cert` under the transitions of `a` is the same as local consistency of `cert` at
> every position carrying an input symbol.

```lean
theorem isStepClosed_iff_localOK :
    a.IsStepClosed input cert ↔
      ∀ i : Fin input.length,
        a.LocalOK input[i] ((Set.univ ::ω cert) i) (cert i) (cert (i + 1))
```

> ## The finite acceptor for the complement

`Cslib.Automata.TwoWayNA.complToNA` (definition, [line 199](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/ComplToNA.lean#L199))

> The nondeterministic finite acceptor that guesses a rejection certificate `cert` for `a` while
> scanning the input, keeping the pair `(cert (i - 1), cert i)` in its state after reading `i`
> symbols.
> Reading the symbol at position `i` guesses `cert (i + 1)` and checks local consistency at `i`.

```lean
def complToNA (a : TwoWayNA State Symbol) : NA.FinAcc (Set State × Set State) Symbol
```

`Cslib.Automata.TwoWayNA.exists_accepting_mTr_iff` (theorem, [line 208](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/ComplToNA.lean#L208))

> An accepting multistep transition of `a.complToNA` out of `(left, cur)` over `xs` is the same
> thing as a certificate starting with `left` and `cur` that is locally consistent at every position
> of `xs` and has no accepting state at the position just past `xs`.

```lean
theorem exists_accepting_mTr_iff (a : TwoWayNA State Symbol) (xs : List Symbol)
    (left cur : Set State) :
    (∃ f ∈ a.complToNA.accept, a.complToNA.MTr (left, cur) xs f) ↔
      ∃ cert : ωSequence (Set State), cert 0 = left ∧ cert 1 = cur ∧
        (∀ i, ∀ hi : i < xs.length, a.LocalOK xs[i] (cert i) (cert (i + 1)) (cert (i + 2))) ∧
          ∀ s ∈ cert (xs.length + 1), s ∉ a.accept
```

`Cslib.Automata.TwoWayNA.accepts_complToNA_iff` (theorem, [line 252](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/ComplToNA.lean#L252))

> `a.complToNA` accepts exactly the words that `a` rejects.

```lean
theorem accepts_complToNA_iff (a : TwoWayNA State Symbol) (input : List Symbol) :
    Accepts a.complToNA input ↔ ¬ Accepts a input
```

`Cslib.Automata.TwoWayNA.language_complToNA` (theorem, [line 278](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/ComplToNA.lean#L278))

> `a.complToNA` recognises the complement of the language of `a`.

```lean
theorem language_complToNA (a : TwoWayNA State Symbol) : language a.complToNA = (language a)ᶜ
```

## Depends on

- [Nondeterministic Two-Way Automaton](basic.md)

## Proof depends on

- [Conversions between `LTS` and `Relation`](../../../foundations/semantics/lts/relation.md)

## Sources

- [Cslib/Computability/Automata/TwoWayNA/ComplToNA.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/TwoWayNA/ComplToNA.lean)
