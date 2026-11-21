---
catalog: module
lean: Pallas.baseFieldSize, Pallas.BaseField, Pallas.baseFieldSize_is_prime, Vesta.baseFieldSize, Vesta.BaseField, Vesta.baseFieldSize_is_prime, Pallas.scalarFieldSize, Pallas.ScalarField, Vesta.scalarFieldSize, Vesta.ScalarField
statement: formalized
proof: formalized
---

# The Pasta (Pallas / Vesta) base prime fields

`CompPoly.Fields.Pasta.Basic`, in [CompPoly/Fields/Pasta/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Pasta/Basic.lean), by Daira-Emma Hopwood, Gregor Mitscha-Baude.

> The Pallas and Vesta curves form a 2-cycle: the base field of one is the scalar field of the
> other.  This module defines the two underlying 255-bit primes together with their Lucas/Pratt
> primality certificates, following the pattern of `CompPoly.Fields.Secp256k1`.
>
> * `Pallas.baseFieldSize` is the Pallas base field size, equal to the Vesta scalar field size;
> * `Vesta.baseFieldSize` is the Vesta base field size, equal to the Pallas scalar field size.
>
> Both primes are `1 mod 2 ^ 32` and have 2-adicity 32.  The certificates were generated from
> the factorizations of `p - 1` and `q - 1`; see <https://github.com/zcash/pasta>.

`Pallas.baseFieldSize` (definition, [line 31](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Pasta/Basic.lean#L31))

> The base field size of the Pallas curve, which is the scalar field size of Vesta.

```lean
def baseFieldSize : Nat
```

`Pallas.BaseField` (abbreviation, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Pasta/Basic.lean#L35))

> The Pallas base field as a `ZMod`.

```lean
abbrev BaseField
```

`Pallas.baseFieldSize_is_prime` (theorem, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Pasta/Basic.lean#L38))

> The Pallas base field size is prime.

```lean
theorem baseFieldSize_is_prime : Nat.Prime baseFieldSize
```

`Vesta.baseFieldSize` (definition, [line 117](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Pasta/Basic.lean#L117))

> The base field size of the Vesta curve, which is the scalar field size of Pallas.

```lean
def baseFieldSize : Nat
```

`Vesta.BaseField` (abbreviation, [line 121](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Pasta/Basic.lean#L121))

> The Vesta base field as a `ZMod`.

```lean
abbrev BaseField
```

`Vesta.baseFieldSize_is_prime` (theorem, [line 124](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Pasta/Basic.lean#L124))

> The Vesta base field size is prime.

```lean
theorem baseFieldSize_is_prime : Nat.Prime baseFieldSize
```

`Pallas.scalarFieldSize` (abbreviation, [line 202](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Pasta/Basic.lean#L202))

> The scalar field size of Pallas is the base field size of Vesta.

```lean
abbrev scalarFieldSize : Nat
```

`Pallas.ScalarField` (abbreviation, [line 205](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Pasta/Basic.lean#L205))

> The Pallas scalar field is the Vesta base field.

```lean
abbrev ScalarField
```

`Vesta.scalarFieldSize` (abbreviation, [line 212](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Pasta/Basic.lean#L212))

> The scalar field size of Vesta is the base field size of Pallas.

```lean
abbrev scalarFieldSize : Nat
```

`Vesta.ScalarField` (abbreviation, [line 215](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Pasta/Basic.lean#L215))

> The Vesta scalar field is the Pallas base field.

```lean
abbrev ScalarField
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Proof depends on

- [The Lucas test for primes](../prattcertificate.md)

## Sources

- [CompPoly/Fields/Pasta/Basic.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Pasta/Basic.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Pasta.Basic.json)
