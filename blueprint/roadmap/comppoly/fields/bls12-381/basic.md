---
catalog: module
lean: BLS12_381.scalarFieldSize, BLS12_381.ScalarField, BLS12_381.ScalarField_is_prime
statement: formalized
proof: formalized
---

# The BLS12-381 scalar prime field

`CompPoly.Fields.BLS12_381.Basic`, in [CompPoly/Fields/BLS12_381/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/BLS12_381/Basic.lean), by Quang Dao.

> `r` of the BLS12-381 curve, 255-bit, 2-adicity 32
> ([IETF pairing-friendly-curves draft](https://datatracker.ietf.org/doc/draft-irtf-cfrg-pairing-friendly-curves/)).

`BLS12_381.scalarFieldSize` (definition, [line 22](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/BLS12_381/Basic.lean#L22))

```lean
def scalarFieldSize : Nat
```

`BLS12_381.ScalarField` (abbreviation, [line 25](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/BLS12_381/Basic.lean#L25))

```lean
abbrev ScalarField
```

`BLS12_381.ScalarField_is_prime` (theorem, [line 27](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/BLS12_381/Basic.lean#L27))

```lean
theorem ScalarField_is_prime : Nat.Prime scalarFieldSize
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Proof depends on

- [The Lucas test for primes](../prattcertificate.md)

## Sources

- [CompPoly/Fields/BLS12_381/Basic.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/BLS12_381/Basic.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.BLS12_381.Basic.json)
