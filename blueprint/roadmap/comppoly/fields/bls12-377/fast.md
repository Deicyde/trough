---
catalog: module
lean: BLS12_377.Fast.instGcdData, BLS12_377.Fast.instMont64x8Field, BLS12_377.Fast.ScalarField, BLS12_377.Fast.ofField, BLS12_377.Fast.ringEquiv
statement: formalized
proof: formalized
---

# Fast BLS12-377 Scalar Field

`CompPoly.Fields.BLS12_377.Fast`, in [CompPoly/Fields/BLS12_377/Fast.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BLS12_377/Fast.lean), by Georgios Raikos.

> A native eight-limb Montgomery implementation of BLS12-377 scalar arithmetic
> (`CompPoly.Fields.Montgomery.Native64x8Field`). This module supplies the BLS12-377
> constants.

> ## Parameters and carrier

`BLS12_377.Fast.instGcdData` (instance, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BLS12_377/Fast.lean#L30))

> Divstep schedule of the binary-GCD inverse candidate.

```lean
instance instGcdData : GcdData BLS12_377.scalarFieldSize
```

`BLS12_377.Fast.instMont64x8Field` (instance, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BLS12_377/Fast.lean#L38))

> The per-field data realizing BLS12-377's scalar field as a fast eight-limb
> (32-bit-limb) Montgomery field.

```lean
instance instMont64x8Field : Mont64x8Field BLS12_377.scalarFieldSize
```

`BLS12_377.Fast.ScalarField` (abbreviation, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BLS12_377/Fast.lean#L52))

> The eight-limb BLS12-377 scalar field carrier, stored as a Montgomery residue.

```lean
abbrev ScalarField : Type
```

`BLS12_377.Fast.ofField` (definition, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BLS12_377/Fast.lean#L56))

> Convert from the canonical `BLS12_377.ScalarField` field into fast Montgomery form.

```lean
def ofField (x : BLS12_377.ScalarField) : ScalarField
```

`BLS12_377.Fast.ringEquiv` (definition, [line 61](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BLS12_377/Fast.lean#L61))

> Ring equivalence between the eight-limb representation and the canonical
> `BLS12_377.ScalarField`.

```lean
def ringEquiv : ScalarField ≃+* BLS12_377.ScalarField
```

## Depends on

- [The BLS12-377 scalar prime field](basic.md)
- [Fast eight-limb Montgomery fields](../montgomery/native64x8field.md)
- [Eight-limb inversion: runtime definitions (Mathlib-free)](../montgomery/native64x8invdefs.md)

## Sources

- [CompPoly/Fields/BLS12_377/Fast.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BLS12_377/Fast.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.BLS12_377.Fast.json)
