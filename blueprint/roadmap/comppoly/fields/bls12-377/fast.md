---
catalog: module
lean: BLS12_377.Fast.instGcdData, BLS12_377.Fast.instMont64x4Field, BLS12_377.Fast.ScalarField, BLS12_377.Fast.ofField, BLS12_377.Fast.ringEquiv
statement: formalized
proof: formalized
---

# Fast BLS12-377 Scalar Field

`CompPoly.Fields.BLS12_377.Fast`, in [CompPoly/Fields/BLS12_377/Fast.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/BLS12_377/Fast.lean), by Georgios Raikos.

> A native four-limb Montgomery implementation of BLS12-377 scalar arithmetic
> (`CompPoly.Fields.Montgomery.Native64x4Field`). This module supplies the BLS12-377
> constants.

> ## Parameters and carrier

`BLS12_377.Fast.instGcdData` (instance, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/BLS12_377/Fast.lean#L30))

> Divstep schedule of the binary-GCD inverse candidate.

```lean
instance instGcdData : GcdData BLS12_377.scalarFieldSize
```

`BLS12_377.Fast.instMont64x4Field` (instance, [line 36](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/BLS12_377/Fast.lean#L36))

> The per-field data realizing BLS12-377's scalar field as a fast four-limb Montgomery
> field.

```lean
instance instMont64x4Field : Mont64x4Field BLS12_377.scalarFieldSize
```

`BLS12_377.Fast.ScalarField` (abbreviation, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/BLS12_377/Fast.lean#L47))

> The four-limb BLS12-377 scalar field carrier, stored as a Montgomery residue.

```lean
abbrev ScalarField : Type
```

`BLS12_377.Fast.ofField` (definition, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/BLS12_377/Fast.lean#L51))

> Convert from the canonical `BLS12_377.ScalarField` field into fast Montgomery form.

```lean
def ofField (x : BLS12_377.ScalarField) : ScalarField
```

`BLS12_377.Fast.ringEquiv` (definition, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/BLS12_377/Fast.lean#L56))

> Ring equivalence between the four-limb representation and the canonical
> `BLS12_377.ScalarField`.

```lean
def ringEquiv : ScalarField ≃+* BLS12_377.ScalarField
```

## Depends on

- [The BLS12-377 scalar prime field](basic.md)
- [Fast four-limb Montgomery fields](../montgomery/native64x4field.md)
- [Four-limb inversion: runtime definitions (Mathlib-free)](../montgomery/native64x4invdefs.md)

## Sources

- [CompPoly/Fields/BLS12_377/Fast.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/BLS12_377/Fast.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.BLS12_377.Fast.json)
