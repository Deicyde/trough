---
catalog: module
lean: RegularExpression.State, RegularExpression.instFiniteState, RegularExpression.toEpsilonNA, RegularExpression.language_toEpsilonNA
statement: formalized
proof: formalized
---

# The ε-NA of a regular expression

`Cslib.Computability.Automata.EpsilonNA.OfRegularExpression`, in [Cslib/Computability/Automata/EpsilonNA/OfRegularExpression.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Automata/EpsilonNA/OfRegularExpression.lean), by Yusuf Demir.

> Thompson's construction [Thompson1968]: every regular expression is sent to an `εNA` with finitely
> many states that accepts exactly its language, by assembling the automata of
> `Cslib.Computability.Automata.EpsilonNA.ThompsonConstruction`.
>
> ## Main definitions
>
> * `RegularExpression.State r`: the states of the automaton of `r`.
> * `RegularExpression.toEpsilonNA r`: the automaton of `r`.
>
> ## Main statements
>
> * `RegularExpression.language_toEpsilonNA`: the automaton of `r` accepts exactly `r.matches'`.
>
> ## References
>
> * [K. Thompson, *Regular expression search algorithm*][Thompson1968]

`RegularExpression.State` (definition, [line 42](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Automata/EpsilonNA/OfRegularExpression.lean#L42))

> The states of the automaton of a regular expression.

```lean
def State : RegularExpression α → Type
```

`RegularExpression.instFiniteState` (instance, [line 51](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Automata/EpsilonNA/OfRegularExpression.lean#L51))

> The automaton of a regular expression has finitely many states.

```lean
instance instFiniteState : (r : RegularExpression α) → Finite r.State
```

`RegularExpression.toEpsilonNA` (definition, [line 68](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Automata/EpsilonNA/OfRegularExpression.lean#L68))

> Thompson's construction: the `εNA` of a regular expression.

```lean
def toEpsilonNA : (r : RegularExpression α) → FinAcc r.State α
```

`RegularExpression.language_toEpsilonNA` (theorem, [line 78](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Automata/EpsilonNA/OfRegularExpression.lean#L78))

> The automaton of a regular expression accepts exactly its language.

```lean
theorem language_toEpsilonNA (r : RegularExpression α) :
    language r.toEpsilonNA = r.matches'
```

## Depends on

- [Nondeterministic automata with ε-transitions](basic.md)

## Proof depends on

- [Thompson's construction](thompsonconstruction.md)

## Sources

- [Cslib/Computability/Automata/EpsilonNA/OfRegularExpression.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Automata/EpsilonNA/OfRegularExpression.lean)
- [Declaration ledger](../../../../../sources/cslib/Cslib.Computability.Automata.EpsilonNA.OfRegularExpression.json)
