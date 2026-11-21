---
catalog: module
lean: BN254.scalarFieldSize, BN254.ScalarField, BN254.ScalarField_is_prime
statement: formalized
proof: formalized
---

# The BN254 scalar prime field

`CompPoly.Fields.BN254.Basic`, in [CompPoly/Fields/BN254/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BN254/Basic.lean), by Quang Dao.

> `r` of the BN254 (alt_bn128) curve, 254-bit, 2-adicity 28
> ([EIP-196](https://eips.ethereum.org/EIPS/eip-196)).

`BN254.scalarFieldSize` (definition, [line 23](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BN254/Basic.lean#L23))

```lean
def scalarFieldSize : Nat
```

`BN254.ScalarField` (abbreviation, [line 26](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BN254/Basic.lean#L26))

```lean
abbrev ScalarField
```

`BN254.ScalarField_is_prime` (theorem, [line 28](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BN254/Basic.lean#L28))

```lean
theorem ScalarField_is_prime : Nat.Prime scalarFieldSize
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Proof depends on

- [The Lucas test for primes](../prattcertificate.md)

## Sources

- [CompPoly/Fields/BN254/Basic.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BN254/Basic.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.BN254.Basic.json)
