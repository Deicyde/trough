---
catalog: module
lean: Cslib.Automata.NA.iProd, Cslib.Automata.NA.iProd_run_iff
statement: formalized
proof: formalized
---

# Product of nondeterministic automata

`Cslib.Computability.Automata.NA.Prod`, in [Cslib/Computability/Automata/NA/Prod.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Prod.lean), by Ching-Tsun Chou.

`Cslib.Automata.NA.iProd` (definition, [line 24](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Prod.lean#L24))

> The product of an indexed family of nondeterministic automata.

```lean
def iProd (na : (i : I) → NA (State i) Symbol) : NA (Π i, State i) Symbol
```

`Cslib.Automata.NA.iProd_run_iff` (theorem, [line 31](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Prod.lean#L31))

> Every run of the product automaton projects onto runs of its component automata,
> and vice versa.

```lean
theorem iProd_run_iff {na : (i : I) → NA (State i) Symbol}
    {xs : ωSequence Symbol} {ss : ωSequence (Π i, State i)} :
    (iProd na).Run xs ss ↔ ∀ i, (na i).Run xs (ss.map (· i))
```

## Depends on

- [Nondeterministic Automaton](basic.md)

## Sources

- [Cslib/Computability/Automata/NA/Prod.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Prod.lean)
