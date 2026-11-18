---
catalog: module
lean: Cslib.Automata.NA.iSum, Cslib.Automata.NA.iSum_run_iff, Cslib.Automata.NA.Buchi.iSum_language_eq
statement: formalized
proof: formalized
---

# Sum of nondeterministic automata

`Cslib.Computability.Automata.NA.Sum`, in [Cslib/Computability/Automata/NA/Sum.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Sum.lean), by Ching-Tsun Chou.

`Cslib.Automata.NA.iSum` (definition, [line 24](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Sum.lean#L24))

> The sum of an indexed family of nondeterministic automata.

```lean
def iSum (na : (i : I) → NA (State i) Symbol) : NA (Σ i, State i) Symbol
```

`Cslib.Automata.NA.iSum_run_iff` (theorem, [line 31](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Sum.lean#L31))

> An infinite run of the sum automaton is an infinite run of one of its component automata.

```lean
theorem iSum_run_iff {na : (i : I) → NA (State i) Symbol}
    {xs : ωSequence Symbol} {ss : ωSequence (Σ i, State i)} :
    (iSum na).Run xs ss ↔ ∃ i ss_i, (na i).Run xs ss_i ∧ ss_i.map (Sigma.mk i) = ss
```

`Cslib.Automata.NA.Buchi.iSum_language_eq` (theorem, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Sum.lean#L65))

> The ω-language accepted by the Buchi sum automata is the union of the ω-languages accepted
> by its component automata.

```lean
theorem iSum_language_eq {na : (i : I) → NA (State i) Symbol} {acc : (i : I) → Set (State i)} :
    language (Buchi.mk (iSum na) (⋃ i, Sigma.mk i '' (acc i))) =
    ⨆ i, language (Buchi.mk (na i) (acc i))
```

## Depends on

- [Nondeterministic Automaton](basic.md)

## Sources

- [Cslib/Computability/Automata/NA/Sum.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Sum.lean)
