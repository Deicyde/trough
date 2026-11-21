---
catalog: module
lean: AesField.modulus, AesField.modulus_natDegree, AesField.modulus_ne_zero, AesField.params_poly, AesField.modulus_irreducible, AesField.nat_card, AesField.aeval_gen, AesField.ringEquivQuot
statement: formalized
proof: formalized
---

# The certified AES polynomial field

`CompPoly.Fields.Binary.Aes.Basic`, in [CompPoly/Fields/Binary/Aes/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Basic.lean), by CompPoly Contributors.

> The degree-eight modulus `X^8 + X^4 + X^3 + X + 1` is irreducible over `GF(2)`.
> Rabin's general criterion uses eight Frobenius squarings and the coprimality condition
> at `X^16 - X`, since two is the sole prime divisor of eight. The existing kernel-checked
> certificate API verifies those conditions; generated data lives in `Aes.Certificate`. The
> criterion is applied as `irreducible_of_rabin_prime_power`, which handles `d = 2 ^ 3`
> and takes the field size as the numeral `2`, so each certificate discharges its condition
> directly with no cardinality rewrite around it; see `CompPoly/Data/Polynomial/Rabin.lean`.
>
> The monic-extension framework supplies executable field operations and the quotient bridge
> for the nominal `AesField` carrier. Its byte coordinates and raw arithmetic can be imported
> separately from `Aes.Arithmetic`. Field numerals are characteristic-two sums of ones, whereas
> `ofBitVec` explicitly interprets the eight polynomial coefficients of a byte.
>
> ## References
>
> * NIST, *Advanced Encryption Standard (AES)*, FIPS 197, updated May 9, 2023, Section 4.
>   https://doi.org/10.6028/NIST.FIPS.197-upd1

`AesField.modulus` (definition, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Basic.lean#L43))

> The AES defining polynomial over `GF(2)`.

```lean
noncomputable def modulus : Polynomial (ZMod 2)
```

`AesField.modulus_natDegree` (theorem, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Basic.lean#L46))

> The defining polynomial has degree eight.

```lean
theorem modulus_natDegree : modulus.natDegree = 8
```

`AesField.modulus_ne_zero` (theorem, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Basic.lean#L51))

> The defining polynomial is nonzero.

```lean
theorem modulus_ne_zero : modulus ≠ 0
```

`AesField.params_poly` (theorem, [line 58](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Basic.lean#L58))

> The extension's lower coefficient vector encodes exactly the AES defining polynomial.

```lean
theorem params_poly : params.poly = modulus
```

`AesField.modulus_irreducible` (theorem, [line 73](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Basic.lean#L73))

> The AES defining polynomial is irreducible over `GF(2)`.

```lean
theorem modulus_irreducible : Irreducible modulus
```

`AesField.nat_card` (theorem, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Basic.lean#L93))

> The AES field has exactly 256 elements, without choosing an enumeration.

```lean
theorem nat_card : Nat.card AesField = 256
```

`AesField.aeval_gen` (theorem, [line 98](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Basic.lean#L98))

> The polynomial generator is a root of the AES modulus.

```lean
theorem aeval_gen : aeval gen modulus = 0
```

`AesField.ringEquivQuot` (definition, [line 103](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Basic.lean#L103))

> The field is isomorphic to the quotient by its certified defining polynomial.

```lean
noncomputable def ringEquivQuot : AesField ≃+* AdjoinRoot params.poly
```

## Depends on

- [AES polynomial-basis coordinates and arithmetic](arithmetic.md)
- [The field structure on an extension](../../extension/field.md)

## Proof depends on

- [Rabin certificate data for `p = 2` (Certificate)](certificate.md)

## Sources

- [CompPoly/Fields/Binary/Aes/Basic.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Basic.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Fields.Binary.Aes.Basic.json)
