---
catalog: module
lean: Secp256k1.baseFieldSize, Secp256k1.BaseField, Secp256k1.BaseField_is_prime, Secp256k1.scalarFieldSize, Secp256k1.ScalarField, Secp256k1.ScalarField_is_prime
statement: formalized
proof: formalized
---

# The Secp256k1 base and scalar prime fields

`CompPoly.Fields.Secp256k1.Basic`, in [CompPoly/Fields/Secp256k1/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Secp256k1/Basic.lean), by Quang Dao.

> We define the two primes underlying the Secp256k1 elliptic curve.
>
> The base prime is the prime on which the elliptic curve is defined.
>
> The scalar prime is the prime that divides the order of the curve.
>
> ## References
>
> `p` is the base prime, and `n` is the scalar prime in [Section 2.4.1](http://www.secg.org/sec2-v2.pdf).

`Secp256k1.baseFieldSize` (definition, [line 33](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Secp256k1/Basic.lean#L33))

```lean
def baseFieldSize : Nat
```

`Secp256k1.BaseField` (abbreviation, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Secp256k1/Basic.lean#L40))

```lean
abbrev BaseField
```

`Secp256k1.BaseField_is_prime` (theorem, [line 78](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Secp256k1/Basic.lean#L78))

```lean
theorem BaseField_is_prime : Nat.Prime baseFieldSize
```

`Secp256k1.scalarFieldSize` (definition, [line 119](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Secp256k1/Basic.lean#L119))

```lean
def scalarFieldSize : Nat
```

`Secp256k1.ScalarField` (abbreviation, [line 121](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Secp256k1/Basic.lean#L121))

```lean
abbrev ScalarField
```

`Secp256k1.ScalarField_is_prime` (theorem, [line 123](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Secp256k1/Basic.lean#L123))

```lean
theorem ScalarField_is_prime : Nat.Prime scalarFieldSize
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Proof depends on

- [The Lucas test for primes](../prattcertificate.md)

## Sources

- [CompPoly/Fields/Secp256k1/Basic.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Secp256k1/Basic.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Secp256k1.Basic.json)
