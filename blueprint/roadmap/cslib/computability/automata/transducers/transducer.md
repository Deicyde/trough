---
catalog: module
lean: Cslib.Automata.Transducer
statement: formalized
proof: formalized
---

# Transducers

`Cslib.Computability.Automata.Transducers.Transducer`, in [Cslib/Computability/Automata/Transducers/Transducer.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/Transducers/Transducer.lean), by Fabrizio Montesi.

`Cslib.Automata.Transducer` (class, [line 19](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/Transducers/Transducer.lean#L19))

> A `Transducer` is an automaton that translates strings (lists of symbols, from an input to an
> output alphabet).

```lean
class Transducer (A : Type u) (InSymbol OutSymbol : outParam (Type v)) where
  /-- The string `xs` can be translated into `ys` by `a`. -/
  Translates (a : A) (xs : List InSymbol) (ys : List OutSymbol) : Prop
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Computability/Automata/Transducers/Transducer.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/Transducers/Transducer.lean)
