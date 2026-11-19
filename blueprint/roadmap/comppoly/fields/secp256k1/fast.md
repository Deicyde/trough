---
catalog: module
lean: Secp256k1.Fast.instScalarGcdData, Secp256k1.Fast.instScalarMont64x8Field, Secp256k1.Fast.ScalarField, Secp256k1.Fast.ofScalarField, Secp256k1.Fast.scalarRingEquiv, Secp256k1.Fast.instBaseGcdData, Secp256k1.Fast.instBaseMont64x8Field, Secp256k1.Fast.BaseField, Secp256k1.Fast.ofBaseField, Secp256k1.Fast.baseRingEquiv
statement: formalized
proof: formalized
---

# Fast secp256k1 Fields

`CompPoly.Fields.Secp256k1.Fast`, in [CompPoly/Fields/Secp256k1/Fast.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Secp256k1/Fast.lean), by Georgios Raikos.

> Native eight-limb Montgomery implementations of the secp256k1 scalar and base fields
> (`CompPoly.Fields.Montgomery.Native64x8Field`). This module supplies the constants.

> ## Scalar field

`Secp256k1.Fast.instScalarGcdData` (instance, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Secp256k1/Fast.lean#L29))

> Divstep schedule of the binary-GCD inverse candidate over the scalar field.

```lean
instance instScalarGcdData : GcdData Secp256k1.scalarFieldSize
```

`Secp256k1.Fast.instScalarMont64x8Field` (instance, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Secp256k1/Fast.lean#L37))

> The per-field data realizing the secp256k1 scalar field as a fast eight-limb Montgomery
> field.

```lean
instance instScalarMont64x8Field : Mont64x8Field Secp256k1.scalarFieldSize
```

`Secp256k1.Fast.ScalarField` (abbreviation, [line 50](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Secp256k1/Fast.lean#L50))

> The eight-limb secp256k1 scalar field carrier, stored as a Montgomery residue.

```lean
abbrev ScalarField : Type
```

`Secp256k1.Fast.ofScalarField` (definition, [line 54](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Secp256k1/Fast.lean#L54))

> Convert from the canonical `Secp256k1.ScalarField` into fast Montgomery form.

```lean
def ofScalarField (x : Secp256k1.ScalarField) : ScalarField
```

`Secp256k1.Fast.scalarRingEquiv` (definition, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Secp256k1/Fast.lean#L59))

> Ring equivalence between the eight-limb representation and the canonical
> `Secp256k1.ScalarField`.

```lean
def scalarRingEquiv : ScalarField ≃+* Secp256k1.ScalarField
```

> ## Base field

`Secp256k1.Fast.instBaseGcdData` (instance, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Secp256k1/Fast.lean#L65))

> Divstep schedule of the binary-GCD inverse candidate over the base field.

```lean
instance instBaseGcdData : GcdData Secp256k1.baseFieldSize
```

`Secp256k1.Fast.instBaseMont64x8Field` (instance, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Secp256k1/Fast.lean#L71))

> The per-field data realizing the secp256k1 base field as a fast eight-limb Montgomery
> field.

```lean
instance instBaseMont64x8Field : Mont64x8Field Secp256k1.baseFieldSize
```

`Secp256k1.Fast.BaseField` (abbreviation, [line 81](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Secp256k1/Fast.lean#L81))

> The eight-limb secp256k1 base field carrier, stored as a Montgomery residue.

```lean
abbrev BaseField : Type
```

`Secp256k1.Fast.ofBaseField` (definition, [line 85](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Secp256k1/Fast.lean#L85))

> Convert from the canonical `Secp256k1.BaseField` into fast Montgomery form.

```lean
def ofBaseField (x : Secp256k1.BaseField) : BaseField
```

`Secp256k1.Fast.baseRingEquiv` (definition, [line 90](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Secp256k1/Fast.lean#L90))

> Ring equivalence between the eight-limb representation and the canonical
> `Secp256k1.BaseField`.

```lean
def baseRingEquiv : BaseField ≃+* Secp256k1.BaseField
```

## Depends on

- [Fast eight-limb Montgomery fields](../montgomery/native64x8field.md)
- [Eight-limb inversion: runtime definitions (Mathlib-free)](../montgomery/native64x8invdefs.md)
- [The Secp256k1 base and scalar prime fields](basic.md)

## Sources

- [CompPoly/Fields/Secp256k1/Fast.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Secp256k1/Fast.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Secp256k1.Fast.json)
