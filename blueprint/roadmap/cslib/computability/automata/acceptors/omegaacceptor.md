---
catalog: module
lean: Cslib.Automata.ωAcceptor, Cslib.Automata.ωAcceptor.language, Cslib.Automata.ωAcceptor.mem_language
statement: formalized
proof: formalized
---

# OmegaAcceptor

`Cslib.Computability.Automata.Acceptors.OmegaAcceptor`, in [Cslib/Computability/Automata/Acceptors/OmegaAcceptor.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/Acceptors/OmegaAcceptor.lean), by Fabrizio Montesi.

`Cslib.Automata.ωAcceptor` (class, [line 18](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/Acceptors/OmegaAcceptor.lean#L18))

> An `ωAcceptor` is a machine that recognises infinite sequences of symbols.

```lean
class ωAcceptor (A : Type u) (Symbol : outParam (Type v)) where
  /-- Predicate that establishes whether a string `xs` is accepted. -/
  Accepts (a : A) (xs : ωSequence Symbol) : Prop
```

`Cslib.Automata.ωAcceptor.language` (definition, [line 28](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/Acceptors/OmegaAcceptor.lean#L28))

> The language of an `ωAcceptor` is the set of sequences it `Accepts`.

```lean
def language [ωAcceptor A Symbol] (a : A) : ωLanguage Symbol
```

`Cslib.Automata.ωAcceptor.mem_language` (theorem, [line 33](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/Acceptors/OmegaAcceptor.lean#L33))

> A string is in the language of an acceptor iff the acceptor accepts it.

```lean
theorem mem_language [ωAcceptor A Symbol] (a : A) (xs : ωSequence Symbol) :
  xs ∈ language a ↔ Accepts a xs
```

## Depends on

- [ωLanguage](../../languages/omegalanguage.md)

## Sources

- [Cslib/Computability/Automata/Acceptors/OmegaAcceptor.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/Acceptors/OmegaAcceptor.lean)
