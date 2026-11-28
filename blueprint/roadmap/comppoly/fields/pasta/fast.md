---
catalog: module
lean: Pallas.Fast.instMont64x4Field, Pallas.Fast.Field, Pallas.Fast.ofField, Pallas.Fast.ringEquiv, Vesta.Fast.instMont64x4Field, Vesta.Fast.Field, Vesta.Fast.ofField, Vesta.Fast.ringEquiv
statement: formalized
proof: formalized
---

# Fast Pasta base fields

`CompPoly.Fields.Pasta.Fast`, in [CompPoly/Fields/Pasta/Fast.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Pasta/Fast.lean), by Gregor Mitscha-Baude.

> Native-word Montgomery implementations of the Pallas and Vesta base field arithmetic.  The
> shared algorithms and proofs live in `CompPoly.Fields.Montgomery.Native64x4Field`; this module
> supplies the two sets of constants and the concrete API.

> ## Parameters and carrier

`Pallas.Fast.instMont64x4Field` (instance, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Pasta/Fast.lean#L29))

> The per-field data realizing the Pallas base field as a fast four-limb Montgomery
> field.

```lean
instance instMont64x4Field : Mont64x4Field Pallas.baseFieldSize
```

`Pallas.Fast.Field` (abbreviation, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Pasta/Fast.lean#L39))

> The fast native-word Pallas base field carrier, stored as a Montgomery residue.

```lean
abbrev Field : Type
```

> ## Conversions

`Pallas.Fast.ofField` (definition, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Pasta/Fast.lean#L45))

> Convert from the canonical `ZMod` Pallas base field into fast Montgomery form.

```lean
def ofField (x : Pallas.BaseField) : Field
```

> ## Canonical bridge

`Pallas.Fast.ringEquiv` (definition, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Pasta/Fast.lean#L51))

> Ring equivalence between the fast Montgomery representation and `Pallas.BaseField`.

```lean
def ringEquiv : Field ≃+* Pallas.BaseField
```

> ## Parameters and carrier

`Vesta.Fast.instMont64x4Field` (instance, [line 64](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Pasta/Fast.lean#L64))

> The per-field data realizing the Vesta base field as a fast four-limb Montgomery
> field.

```lean
instance instMont64x4Field : Mont64x4Field Vesta.baseFieldSize
```

`Vesta.Fast.Field` (abbreviation, [line 74](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Pasta/Fast.lean#L74))

> The fast native-word Vesta base field carrier, stored as a Montgomery residue.

```lean
abbrev Field : Type
```

> ## Conversions

`Vesta.Fast.ofField` (definition, [line 80](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Pasta/Fast.lean#L80))

> Convert from the canonical `ZMod` Vesta base field into fast Montgomery form.

```lean
def ofField (x : Vesta.BaseField) : Field
```

> ## Canonical bridge

`Vesta.Fast.ringEquiv` (definition, [line 86](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Pasta/Fast.lean#L86))

> Ring equivalence between the fast Montgomery representation and `Vesta.BaseField`.

```lean
def ringEquiv : Field ≃+* Vesta.BaseField
```

## Depends on

- [Fast four-limb Montgomery fields](../montgomery/native64x4field.md)
- [The Pasta (Pallas / Vesta) base prime fields](basic.md)

## Sources

- [CompPoly/Fields/Pasta/Fast.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Pasta/Fast.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Pasta.Fast.json)
