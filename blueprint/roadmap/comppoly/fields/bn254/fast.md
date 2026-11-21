---
catalog: module
lean: BN254.Fast.instGcdData, BN254.Fast.instMont64x8Field, BN254.Fast.ScalarField, BN254.Fast.ofField, BN254.Fast.ringEquiv
statement: formalized
proof: formalized
---

# Fast BN254 Scalar Field

`CompPoly.Fields.BN254.Fast`, in [CompPoly/Fields/BN254/Fast.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BN254/Fast.lean), by Georgios Raikos.

> A native eight-limb Montgomery implementation of BN254 scalar arithmetic
> (`CompPoly.Fields.Montgomery.Native64x8Field`). This module supplies the BN254 constants.

> ## Parameters and carrier

`BN254.Fast.instGcdData` (instance, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BN254/Fast.lean#L29))

> Divstep schedule of the binary-GCD inverse candidate.

```lean
instance instGcdData : GcdData BN254.scalarFieldSize
```

`BN254.Fast.instMont64x8Field` (instance, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BN254/Fast.lean#L37))

> The per-field data realizing BN254's scalar field as a fast eight-limb (32-bit-limb)
> Montgomery field.

```lean
instance instMont64x8Field : Mont64x8Field BN254.scalarFieldSize
```

`BN254.Fast.ScalarField` (abbreviation, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BN254/Fast.lean#L51))

> The eight-limb BN254 scalar field carrier, stored as a Montgomery residue.

```lean
abbrev ScalarField : Type
```

`BN254.Fast.ofField` (definition, [line 55](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BN254/Fast.lean#L55))

> Convert from the canonical `BN254.ScalarField` field into fast Montgomery form.

```lean
def ofField (x : BN254.ScalarField) : ScalarField
```

`BN254.Fast.ringEquiv` (definition, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BN254/Fast.lean#L60))

> Ring equivalence between the eight-limb representation and the canonical
> `BN254.ScalarField`.

```lean
def ringEquiv : ScalarField ≃+* BN254.ScalarField
```

## Depends on

- [The BN254 scalar prime field](basic.md)
- [Fast eight-limb Montgomery fields](../montgomery/native64x8field.md)
- [Eight-limb inversion: runtime definitions (Mathlib-free)](../montgomery/native64x8invdefs.md)

## Sources

- [CompPoly/Fields/BN254/Fast.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BN254/Fast.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.BN254.Fast.json)
