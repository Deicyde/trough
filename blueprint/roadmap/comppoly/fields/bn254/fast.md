---
catalog: module
lean: BN254.Fast.instGcdData, BN254.Fast.instMont64x4Field, BN254.Fast.ScalarField, BN254.Fast.ofField, BN254.Fast.ringEquiv
statement: formalized
proof: formalized
---

# Fast BN254 Scalar Field

`CompPoly.Fields.BN254.Fast`, in [CompPoly/Fields/BN254/Fast.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/BN254/Fast.lean), by Georgios Raikos.

> A native four-limb Montgomery implementation of BN254 scalar arithmetic
> (`CompPoly.Fields.Montgomery.Native64x4Field`). This module supplies the BN254 constants.

> ## Parameters and carrier

`BN254.Fast.instGcdData` (instance, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/BN254/Fast.lean#L29))

> Divstep schedule of the binary-GCD inverse candidate.

```lean
instance instGcdData : GcdData BN254.scalarFieldSize
```

`BN254.Fast.instMont64x4Field` (instance, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/BN254/Fast.lean#L35))

> The per-field data realizing BN254's scalar field as a fast four-limb Montgomery
> field.

```lean
instance instMont64x4Field : Mont64x4Field BN254.scalarFieldSize
```

`BN254.Fast.ScalarField` (abbreviation, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/BN254/Fast.lean#L46))

> The four-limb BN254 scalar field carrier, stored as a Montgomery residue.

```lean
abbrev ScalarField : Type
```

`BN254.Fast.ofField` (definition, [line 50](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/BN254/Fast.lean#L50))

> Convert from the canonical `BN254.ScalarField` field into fast Montgomery form.

```lean
def ofField (x : BN254.ScalarField) : ScalarField
```

`BN254.Fast.ringEquiv` (definition, [line 55](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/BN254/Fast.lean#L55))

> Ring equivalence between the four-limb representation and the canonical
> `BN254.ScalarField`.

```lean
def ringEquiv : ScalarField ≃+* BN254.ScalarField
```

## Depends on

- [The BN254 scalar prime field](basic.md)
- [Fast four-limb Montgomery fields](../montgomery/native64x4field.md)
- [Four-limb inversion: runtime definitions (Mathlib-free)](../montgomery/native64x4invdefs.md)

## Sources

- [CompPoly/Fields/BN254/Fast.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/BN254/Fast.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.BN254.Fast.json)
