---
catalog: module
lean: Goldilocks.fieldSize, Goldilocks.Field, Goldilocks.is_prime
statement: formalized
proof: formalized
---

# Goldilocks prime field `2^{64} - 2^{32} + 1`

`CompPoly.Fields.Goldilocks.Basic`, in [CompPoly/Fields/Goldilocks/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Goldilocks/Basic.lean), by Quang Dao, Varun Thakore.

> This is the field used in Plonky2/3.

`Goldilocks.fieldSize` (definition, [line 25](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Goldilocks/Basic.lean#L25))

> The Goldilocks prime modulus, `2^64 - 2^32 + 1`.

```lean
def fieldSize : Nat
```

`Goldilocks.Field` (abbreviation, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Goldilocks/Basic.lean#L29))

> The canonical mathematical Goldilocks field, implemented as integers modulo
> `fieldSize`.

```lean
abbrev Field
```

`Goldilocks.is_prime` (theorem, [line 32](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Goldilocks/Basic.lean#L32))

> The Goldilocks modulus is prime, verified by a Pratt certificate.

```lean
theorem is_prime : Nat.Prime fieldSize
```

## Depends on

- [Non-binary fields and polynomial utilities](../basic.md)

## Proof depends on

- [The Lucas test for primes](../prattcertificate.md)

## Sources

- [CompPoly/Fields/Goldilocks/Basic.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Goldilocks/Basic.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Goldilocks.Basic.json)
