---
catalog: module
lean: Cslib.Automata.NA.Buchi.histStart, Cslib.Automata.NA.Buchi.interAcc, Cslib.Automata.NA.Buchi.histTrans, Cslib.Automata.NA.Buchi.interNA, Cslib.Automata.NA.Buchi.interAccept, Cslib.Automata.NA.Buchi.inter_freq_acc_freq_acc, Cslib.Automata.NA.Buchi.inter_freq_comp_acc_freq_acc, Cslib.Automata.NA.Buchi.inter_language_eq
statement: formalized
proof: formalized
---

# Intersection of nondeterministic Buchi automata

`Cslib.Computability.Automata.NA.BuchiInter`, in [Cslib/Computability/Automata/NA/BuchiInter.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/BuchiInter.lean), by Ching-Tsun Chou.

> The intersection automaton consists of the product of the two automata to be intersected
> plus a history state which is a pointer to one of the two automata. It waits for the
> accepting condition of the automaton being pointed to by the history state. Once it sees that,
> it toggles the history state to wait for the accepting condition of the other automaton.
> The intersection automaton accepts iff the toggling happens infinitely many times.
>
> The two automata to be intersected are indexed by the type `Bool`.  We choose `Bool`
> simply because toggling can be easily modeled by the boolean operation `not`.

`Cslib.Automata.NA.Buchi.histStart` (definition, [line 36](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/BuchiInter.lean#L36))

> The initial history state.

```lean
def histStart (_ : Π i, State i) : Bool
```

`Cslib.Automata.NA.Buchi.interAcc` (definition, [line 40](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/BuchiInter.lean#L40))

> The two accepting conditions of the intersection automaton.

```lean
def interAcc (j : Bool) (acc : (i : Bool) → Set (State i)) : Set ((Π i, State i) × Bool)
```

`Cslib.Automata.NA.Buchi.histTrans` (definition, [line 46](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/BuchiInter.lean#L46))

> The transition function of the history state.

```lean
noncomputable def histTrans (acc : (i : Bool) → Set (State i))
    (s : (Π i, State i) × Bool) (_ : Symbol) (_ : Π i, State i) : Bool
```

`Cslib.Automata.NA.Buchi.interNA` (definition, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/BuchiInter.lean#L53))

> The intersection automaton.

```lean
noncomputable def interNA (na : (i : Bool) → NA (State i) Symbol)
    (acc : (i : Bool) → Set (State i)) : NA ((Π i, State i) × Bool) Symbol
```

`Cslib.Automata.NA.Buchi.interAccept` (definition, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/BuchiInter.lean#L59))

> The overall accepting condition of the intersection automaton.

```lean
def interAccept (acc : (i : Bool) → Set (State i)) : Set ((Π i, State i) × Bool)
```

`Cslib.Automata.NA.Buchi.inter_freq_acc_freq_acc` (lemma, [line 66](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/BuchiInter.lean#L66))

> If the intersection automaton sees one accepting condition infinitely many times,
> then it sees the other accepting condition infinitely many times as well.

```lean
lemma inter_freq_acc_freq_acc {xs : ωSequence Symbol} {ss : ωSequence ((Π i, State i) × Bool)}
    {i : Bool} (h_run : (interNA na acc).Run xs ss) (h_inf : ∃ᶠ k in atTop, ss k ∈ interAcc i acc) :
    ∃ᶠ k in atTop, ss k ∈ interAcc (!i) acc
```

`Cslib.Automata.NA.Buchi.inter_freq_comp_acc_freq_acc` (lemma, [line 80](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/BuchiInter.lean#L80))

> If the intersection automaton sees the accepting conditions of both component automata
> infinitely many times, then its own accepting condition also happens infinitely many times.

```lean
lemma inter_freq_comp_acc_freq_acc {xs : ωSequence Symbol} {ss : ωSequence ((Π i, State i) × Bool)}
    (h_run : (interNA na acc).Run xs ss)
    (h_inf_f : ∃ᶠ k in atTop, ss k ∈ {s | s.fst false ∈ acc false})
    (h_inf_t : ∃ᶠ k in atTop, ss k ∈ {s | s.fst true ∈ acc true}) :
    ∃ᶠ k in atTop, ss k ∈ interAccept acc
```

`Cslib.Automata.NA.Buchi.inter_language_eq` (theorem, [line 99](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/BuchiInter.lean#L99))

> The language accepted by the intersection automaton is the intersection of
> the languages accepted by the two component automata.

```lean
theorem inter_language_eq :
    language (Buchi.mk (interNA na acc) (interAccept acc)) =
    ⨅ i, language (Buchi.mk (na i) (acc i))
```

## Depends on

- [Adding a history states to a nondeterministic automaton](hist.md)
- [Product of nondeterministic automata](prod.md)

## Proof depends on

- [Temporal reasoning over infinite sequences](../../../foundations/data/omegasequence/temporal.md)

## Sources

- [Cslib/Computability/Automata/NA/BuchiInter.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/BuchiInter.lean)
