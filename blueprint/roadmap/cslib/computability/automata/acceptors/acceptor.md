---
catalog: module
lean: Cslib.Automata.Acceptor, Cslib.Automata.Acceptor.language, Cslib.Automata.Acceptor.mem_language
statement: formalized
proof: formalized
---

# Acceptor

`Cslib.Computability.Automata.Acceptors.Acceptor`, in [Cslib/Computability/Automata/Acceptors/Acceptor.lean](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Automata/Acceptors/Acceptor.lean), by Fabrizio Montesi.

`Cslib.Automata.Acceptor` (class, [line 19](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Automata/Acceptors/Acceptor.lean#L19))

> An `Acceptor` is a machine that recognises strings (lists of symbols in an alphabet).

```lean
class Acceptor (A : Type u) (Symbol : outParam (Type v)) where
  /-- Predicate that establishes whether a string `xs` is accepted. -/
  Accepts (a : A) (xs : List Symbol) : Prop
```

`Cslib.Automata.Acceptor.language` (definition, [line 29](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Automata/Acceptors/Acceptor.lean#L29))

> The language of an `Acceptor` is the set of strings it `Accepts`.

```lean
def language [Acceptor A Symbol] (a : A) : Language Symbol
```

`Cslib.Automata.Acceptor.mem_language` (theorem, [line 34](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Automata/Acceptors/Acceptor.lean#L34))

> A string is in the language of an acceptor iff the acceptor accepts it.

```lean
theorem mem_language [Acceptor A Symbol] (a : A) (xs : List Symbol) :
  xs ∈ language a ↔ Accepts a xs
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Computability/Automata/Acceptors/Acceptor.lean at 7c95c37f](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Automata/Acceptors/Acceptor.lean)
- [Declaration ledger](../../../../../sources/cslib/Cslib.Computability.Automata.Acceptors.Acceptor.json)
