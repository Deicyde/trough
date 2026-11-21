---
catalog: module
lean: BabyBear.Fast.instMont32Field, BabyBear.Fast.Field, BabyBear.Fast.ofUInt32, BabyBear.Fast.ofField, BabyBear.Fast.ringEquiv, BabyBear.Fast.twoAdicGenerators, BabyBear.Fast.twoAdicGenerators_eq_map
statement: formalized
proof: formalized
---

# Fast BabyBear Field

`CompPoly.Fields.BabyBear.Fast`, in [CompPoly/Fields/BabyBear/Fast.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Fast.lean), by Valerii Huhnin, Georgios Raikos.

> A native-word Montgomery implementation of BabyBear arithmetic. The shared algorithms and
> proofs live in `CompPoly.Fields.Montgomery.Native32Field`; this module supplies the BabyBear
> constants and its concrete API.

> ## Parameters and carrier

`BabyBear.Fast.instMont32Field` (instance, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Fast.lean#L29))

> The per-field data realizing BabyBear as a fast 32-bit-word Montgomery field.

```lean
instance instMont32Field : Mont32Field BabyBear.fieldSize
```

`BabyBear.Fast.Field` (abbreviation, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Fast.lean#L38))

> The fast native-word BabyBear field carrier, stored as a Montgomery residue.

```lean
abbrev Field : Type
```

> ## Conversions

`BabyBear.Fast.ofUInt32` (definition, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Fast.lean#L44))

> Convert a 32-bit word into fast Montgomery representation.

```lean
def ofUInt32 (x : UInt32) : Field
```

`BabyBear.Fast.ofField` (definition, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Fast.lean#L49))

> Convert from the canonical `ZMod` BabyBear field into fast Montgomery form.

```lean
def ofField (x : BabyBear.Field) : Field
```

> ## Canonical bridge

`BabyBear.Fast.ringEquiv` (definition, [line 55](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Fast.lean#L55))

> Ring equivalence between the fast Montgomery representation and canonical `BabyBear.Field`.

```lean
def ringEquiv : Field ≃+* BabyBear.Field
```

> ## Two-adic roots

`BabyBear.Fast.twoAdicGenerators` (definition, [line 61](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Fast.lean#L61))

> Precomputed BabyBear two-adic generators in Montgomery representation.

```lean
def twoAdicGenerators : List Field
```

`BabyBear.Fast.twoAdicGenerators_eq_map` (theorem, [line 94](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Fast.lean#L94))

> The Montgomery root table represents the canonical BabyBear roots.

```lean
theorem twoAdicGenerators_eq_map :
    twoAdicGenerators = BabyBear.twoAdicGenerators.map ofField
```

## Depends on

- [BabyBear Field `2^{31} - 2^{27} + 1`](basic.md)
- [Fast 32-bit Montgomery Fields](../montgomery/native32field.md)

## Sources

- [CompPoly/Fields/BabyBear/Fast.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Fast.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.BabyBear.Fast.json)
