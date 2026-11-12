---
catalog: module
lean: Cslib.Circuits.Signature, Cslib.Circuits.Interpretation, Cslib.Circuits.FullOp, Cslib.Circuits.fullSignature, Cslib.Circuits.fullInterpretation
statement: formalized
proof: formalized
---

# Signatures and interpretations

`Cslib.Computability.Circuit.Signature`, in [Cslib/Computability/Circuit/Signature.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Signature.lean), by Samuel Schlesinger.

> A `Signature` specifies operation symbols with finite arities. The set of symbols
> may be infinite, and their arities need not have a uniform bound.
> An `Interpretation` assigns each symbol an operation on a carrier type.
> Programs and circuits keep the signature separate from its interpretation.

`Cslib.Circuits.Signature` (structure, [line 26](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Signature.lean#L26))

> A collection of operation symbols, each with a fixed finite arity.

```lean
structure Signature where
  /-- The operation symbols of the signature. -/
  Op : Type v
  /-- The number of arguments taken by each operation symbol. -/
  Arity : Op → Nat
```

`Cslib.Circuits.Interpretation` (abbreviation, [line 33](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Signature.lean#L33))

> An interpretation assigns an operation on `Carrier` to every symbol in `σ`.

```lean
abbrev Interpretation (σ : Signature) (Carrier : Type*)
```

`Cslib.Circuits.FullOp` (inductive type, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Signature.lean#L37))

> An operation with labels for all constants and operations of arity k.

```lean
inductive FullOp (k : Nat) Carrier where
  | fn : ((Fin k -> Carrier) -> Carrier) -> FullOp k Carrier
  | con : Carrier → FullOp k Carrier
```

`Cslib.Circuits.fullSignature` (definition, [line 42](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Signature.lean#L42))

> The signature for FullOp.

```lean
def fullSignature (k : Nat) (Carrier : Type v) : Signature
```

`Cslib.Circuits.fullInterpretation` (definition, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Signature.lean#L50))

> The natural interpretation for FullOp, where we evaluate each constant
> and function to itself.

```lean
def fullInterpretation : Interpretation (fullSignature k Carrier) Carrier
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Computability/Circuit/Signature.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Signature.lean)
