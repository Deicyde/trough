---
catalog: module
lean: Cslib.Automata.ωAcceptor, Cslib.Automata.ωAcceptor.language, Cslib.Automata.ωAcceptor.mem_language
statement: formalized
proof: formalized
---

# OmegaAcceptor

`Cslib.Computability.Automata.Acceptors.OmegaAcceptor`, in [Cslib/Computability/Automata/Acceptors/OmegaAcceptor.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Automata/Acceptors/OmegaAcceptor.lean), by Fabrizio Montesi.

`Cslib.Automata.ωAcceptor` (class, [line 18](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Automata/Acceptors/OmegaAcceptor.lean#L18))

> An `ωAcceptor` is a machine that recognises infinite sequences of symbols.

```lean
class ωAcceptor (A : Type u) (Symbol : outParam (Type v)) where
  /-- Predicate that establishes whether a string `xs` is accepted. -/
  Accepts (a : A) (xs : ωSequence Symbol) : Prop
```

`Cslib.Automata.ωAcceptor.language` (definition, [line 28](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Automata/Acceptors/OmegaAcceptor.lean#L28))

> The language of an `ωAcceptor` is the set of sequences it `Accepts`.

```lean
def language [ωAcceptor A Symbol] (a : A) : ωLanguage Symbol
```

`Cslib.Automata.ωAcceptor.mem_language` (theorem, [line 33](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Automata/Acceptors/OmegaAcceptor.lean#L33))

> A string is in the language of an acceptor iff the acceptor accepts it.

```lean
theorem mem_language [ωAcceptor A Symbol] (a : A) (xs : ωSequence Symbol) :
  xs ∈ language a ↔ Accepts a xs
```

## Depends on

- [ωLanguage](../../languages/omegalanguage.md)

## Sources

- [Cslib/Computability/Automata/Acceptors/OmegaAcceptor.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Automata/Acceptors/OmegaAcceptor.lean)
- [Declaration ledger](../../../../../sources/cslib/Cslib.Computability.Automata.Acceptors.OmegaAcceptor.json)
