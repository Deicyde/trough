---
catalog: module
lean: Mersenne31.fieldSize, Mersenne31.Field, Mersenne31.is_prime
statement: formalized
proof: formalized
---

# Mersenne prime field `2^{31} - 1`

`CompPoly.Fields.Mersenne31.Basic`, in [CompPoly/Fields/Mersenne31/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Mersenne31/Basic.lean), by Quang Dao, Varun Thakore.

> This is the field used in Circle STARKs.

`Mersenne31.fieldSize` (definition, [line 25](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Mersenne31/Basic.lean#L25))

> The Mersenne31 prime modulus `2^31 - 1`.

```lean
def fieldSize : Nat
```

`Mersenne31.Field` (abbreviation, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Mersenne31/Basic.lean#L29))

> The canonical mathematical Mersenne31 field, implemented as integers modulo
> `fieldSize`.

```lean
abbrev Field
```

`Mersenne31.is_prime` (theorem, [line 32](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Mersenne31/Basic.lean#L32))

> The Mersenne31 modulus is prime, verified by a Pratt certificate.

```lean
theorem is_prime : Nat.Prime fieldSize
```

## Depends on

- [Non-binary fields and polynomial utilities](../basic.md)

## Proof depends on

- [The Lucas test for primes](../prattcertificate.md)

## Sources

- [CompPoly/Fields/Mersenne31/Basic.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Mersenne31/Basic.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Mersenne31.Basic.json)
