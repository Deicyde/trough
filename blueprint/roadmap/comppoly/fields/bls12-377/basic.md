---
catalog: module
lean: BLS12_377.scalarFieldSize, BLS12_377.ScalarField, BLS12_377.ScalarField_is_prime
statement: formalized
proof: formalized
---

# The BLS12-377 scalar prime field

`CompPoly.Fields.BLS12_377.Basic`, in [CompPoly/Fields/BLS12_377/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/BLS12_377/Basic.lean), by Quang Dao.

> `r` of the BLS12-377 curve, 253-bit, 2-adicity 47
> ([Zexe, BCGMMW18](https://eprint.iacr.org/2018/962)).

`BLS12_377.scalarFieldSize` (definition, [line 22](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/BLS12_377/Basic.lean#L22))

```lean
def scalarFieldSize : Nat
```

`BLS12_377.ScalarField` (abbreviation, [line 25](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/BLS12_377/Basic.lean#L25))

```lean
abbrev ScalarField
```

`BLS12_377.ScalarField_is_prime` (theorem, [line 27](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/BLS12_377/Basic.lean#L27))

```lean
theorem ScalarField_is_prime : Nat.Prime scalarFieldSize
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Proof depends on

- [The Lucas test for primes](../prattcertificate.md)

## Sources

- [CompPoly/Fields/BLS12_377/Basic.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/BLS12_377/Basic.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.BLS12_377.Basic.json)
