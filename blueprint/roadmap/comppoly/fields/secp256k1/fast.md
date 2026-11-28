---
catalog: module
lean: Secp256k1.Fast.instScalarGcdData, Secp256k1.Fast.instScalarMont64x4Field, Secp256k1.Fast.ScalarField, Secp256k1.Fast.ofScalarField, Secp256k1.Fast.scalarRingEquiv, Secp256k1.Fast.instBaseGcdData, Secp256k1.Fast.instBaseMont64x4Field, Secp256k1.Fast.BaseField, Secp256k1.Fast.ofBaseField, Secp256k1.Fast.baseRingEquiv
statement: formalized
proof: formalized
---

# Fast secp256k1 Fields

`CompPoly.Fields.Secp256k1.Fast`, in [CompPoly/Fields/Secp256k1/Fast.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Secp256k1/Fast.lean), by Georgios Raikos.

> Native four-limb Montgomery implementations of the secp256k1 scalar and base fields
> (`CompPoly.Fields.Montgomery.Native64x4Field`). This module supplies the constants.

> ## Scalar field

`Secp256k1.Fast.instScalarGcdData` (instance, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Secp256k1/Fast.lean#L29))

> Divstep schedule of the binary-GCD inverse candidate over the scalar field.

```lean
instance instScalarGcdData : GcdData Secp256k1.scalarFieldSize
```

`Secp256k1.Fast.instScalarMont64x4Field` (instance, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Secp256k1/Fast.lean#L35))

> The per-field data realizing the secp256k1 scalar field as a fast four-limb Montgomery
> field.

```lean
instance instScalarMont64x4Field : Mont64x4Field Secp256k1.scalarFieldSize
```

`Secp256k1.Fast.ScalarField` (abbreviation, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Secp256k1/Fast.lean#L45))

> The four-limb secp256k1 scalar field carrier, stored as a Montgomery residue.

```lean
abbrev ScalarField : Type
```

`Secp256k1.Fast.ofScalarField` (definition, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Secp256k1/Fast.lean#L49))

> Convert from the canonical `Secp256k1.ScalarField` into fast Montgomery form.

```lean
def ofScalarField (x : Secp256k1.ScalarField) : ScalarField
```

`Secp256k1.Fast.scalarRingEquiv` (definition, [line 54](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Secp256k1/Fast.lean#L54))

> Ring equivalence between the four-limb representation and the canonical
> `Secp256k1.ScalarField`.

```lean
def scalarRingEquiv : ScalarField ≃+* Secp256k1.ScalarField
```

> ## Base field

`Secp256k1.Fast.instBaseGcdData` (instance, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Secp256k1/Fast.lean#L60))

> Divstep schedule of the binary-GCD inverse candidate over the base field.

```lean
instance instBaseGcdData : GcdData Secp256k1.baseFieldSize
```

`Secp256k1.Fast.instBaseMont64x4Field` (instance, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Secp256k1/Fast.lean#L66))

> The per-field data realizing the secp256k1 base field as a fast four-limb Montgomery
> field.

```lean
instance instBaseMont64x4Field : Mont64x4Field Secp256k1.baseFieldSize
```

`Secp256k1.Fast.BaseField` (abbreviation, [line 75](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Secp256k1/Fast.lean#L75))

> The four-limb secp256k1 base field carrier, stored as a Montgomery residue.

```lean
abbrev BaseField : Type
```

`Secp256k1.Fast.ofBaseField` (definition, [line 79](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Secp256k1/Fast.lean#L79))

> Convert from the canonical `Secp256k1.BaseField` into fast Montgomery form.

```lean
def ofBaseField (x : Secp256k1.BaseField) : BaseField
```

`Secp256k1.Fast.baseRingEquiv` (definition, [line 84](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Secp256k1/Fast.lean#L84))

> Ring equivalence between the four-limb representation and the canonical
> `Secp256k1.BaseField`.

```lean
def baseRingEquiv : BaseField ≃+* Secp256k1.BaseField
```

## Depends on

- [Fast four-limb Montgomery fields](../montgomery/native64x4field.md)
- [Four-limb inversion: runtime definitions (Mathlib-free)](../montgomery/native64x4invdefs.md)
- [The Secp256k1 base and scalar prime fields](basic.md)

## Sources

- [CompPoly/Fields/Secp256k1/Fast.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Secp256k1/Fast.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Secp256k1.Fast.json)
