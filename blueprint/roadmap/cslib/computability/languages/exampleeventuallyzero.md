---
catalog: module
lean: Cslib.ωLanguage.Example.eventuallyZero, Cslib.ωLanguage.Example.eventuallyZeroNa, Cslib.ωLanguage.Example.eventuallyZero_accepted_by_na_buchi, Cslib.ωLanguage.Example.eventuallyZero_not_omegaLim
statement: formalized
proof: formalized
---

# An ω-regular language that is not accepted by any deterministic Buchi automaton

`Cslib.Computability.Languages.ExampleEventuallyZero`, in [Cslib/Computability/Languages/ExampleEventuallyZero.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/ExampleEventuallyZero.lean), by Ching-Tsun Chou.

> This example is adapted from Example 4.2 of [Thomas1990].
>
> ## References
> * [W. Thomas, "Automata on infinite objects"][Thomas1990]

`Cslib.ωLanguage.Example.eventuallyZero` (definition, [line 31](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/ExampleEventuallyZero.lean#L31))

> A sequence `xs` is in `eventuallyZero` iff `xs k = 0` for all large `k`.

```lean
def eventuallyZero : ωLanguage (Fin 2)
```

`Cslib.ωLanguage.Example.eventuallyZeroNa` (definition, [line 36](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/ExampleEventuallyZero.lean#L36))

> `eventuallyZero` is accepted by a 2-state nondeterministic Buchi automaton.

```lean
def eventuallyZeroNa : NA.Buchi (Fin 2) (Fin 2)
```

`Cslib.ωLanguage.Example.eventuallyZero_accepted_by_na_buchi` (theorem, [line 43](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/ExampleEventuallyZero.lean#L43))

```lean
theorem eventuallyZero_accepted_by_na_buchi :
    language eventuallyZeroNa = eventuallyZero
```

`Cslib.ωLanguage.Example.eventuallyZero_not_omegaLim` (theorem, [line 98](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/ExampleEventuallyZero.lean#L98))

```lean
theorem eventuallyZero_not_omegaLim :
    ¬ ∃ l : Language (Fin 2), l↗ω = eventuallyZero
```

## Depends on

- [Nondeterministic Automaton](../automata/na/basic.md)

## Sources

- [Cslib/Computability/Languages/ExampleEventuallyZero.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/ExampleEventuallyZero.lean)
