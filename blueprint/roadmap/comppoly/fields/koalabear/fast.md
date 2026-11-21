---
catalog: module
lean: KoalaBear.Fast.instMont32Field, KoalaBear.Fast.Field, KoalaBear.Fast.ofUInt32, KoalaBear.Fast.ofField, KoalaBear.Fast.ringEquiv, KoalaBear.Fast.twoAdicGenerators, KoalaBear.Fast.twoAdicGenerators_eq_map
statement: formalized
proof: formalized
---

# Fast KoalaBear Field

`CompPoly.Fields.KoalaBear.Fast`, in [CompPoly/Fields/KoalaBear/Fast.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Fast.lean), by Valerii Huhnin.

> A native-word Montgomery implementation of KoalaBear arithmetic. The shared algorithms and
> proofs live in `CompPoly.Fields.Montgomery.Native32Field`; this module supplies the KoalaBear
> constants and its concrete API.

> ## Parameters and carrier

`KoalaBear.Fast.instMont32Field` (instance, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Fast.lean#L29))

> The per-field data realizing KoalaBear as a fast 32-bit-word Montgomery field.

```lean
instance instMont32Field : Mont32Field KoalaBear.fieldSize
```

`KoalaBear.Fast.Field` (abbreviation, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Fast.lean#L38))

> The fast native-word KoalaBear field carrier, stored as a Montgomery residue.

```lean
abbrev Field : Type
```

> ## Conversions

`KoalaBear.Fast.ofUInt32` (definition, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Fast.lean#L44))

> Convert a 32-bit word into fast Montgomery representation.

```lean
def ofUInt32 (x : UInt32) : Field
```

`KoalaBear.Fast.ofField` (definition, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Fast.lean#L49))

> Convert from the canonical `ZMod` KoalaBear field into fast Montgomery form.

```lean
def ofField (x : KoalaBear.Field) : Field
```

> ## Canonical bridge

`KoalaBear.Fast.ringEquiv` (definition, [line 55](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Fast.lean#L55))

> Ring equivalence between the fast Montgomery representation and canonical `KoalaBear.Field`.

```lean
def ringEquiv : Field ≃+* KoalaBear.Field
```

> ## Two-adic roots

`KoalaBear.Fast.twoAdicGenerators` (definition, [line 61](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Fast.lean#L61))

> Precomputed KoalaBear two-adic generators in Montgomery representation.

```lean
def twoAdicGenerators : List Field
```

`KoalaBear.Fast.twoAdicGenerators_eq_map` (theorem, [line 91](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Fast.lean#L91))

> The Montgomery root table represents the canonical KoalaBear roots.

```lean
theorem twoAdicGenerators_eq_map :
    twoAdicGenerators = KoalaBear.twoAdicGenerators.map ofField
```

## Depends on

- [KoalaBear Field `2^{31} - 2^{24} + 1`](basic.md)
- [Fast 32-bit Montgomery Fields](../montgomery/native32field.md)

## Sources

- [CompPoly/Fields/KoalaBear/Fast.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Fast.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.KoalaBear.Fast.json)
