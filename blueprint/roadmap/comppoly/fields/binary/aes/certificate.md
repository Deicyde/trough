---
catalog: module
lean: AesField.Certificate.traceSteps, AesField.Certificate.cop4Steps, AesField.Certificate.cop4Rp, AesField.Certificate.cop4W, AesField.Certificate.cop4U, AesField.Certificate.cop4V
statement: formalized
proof: formalized
---

# Rabin certificate data for `p = 2` (Certificate)

`CompPoly.Fields.Binary.Aes.Certificate`, in [CompPoly/Fields/Binary/Aes/Certificate.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Certificate.lean), by CompPoly Contributors.

> The modulus `f` has little-endian coefficients `[1, 1, 0, 1, 1, 0, 0, 0, 1]`.
>
> `d = 8` is composite, so Rabin's coprimality condition needs one certificate per
> prime factor of `d` (2), at exponents p^4 respectively. Checking only the
> linear-factor case would admit a product of equal-degree factors.
>
> GENERATED. Do not edit by hand; regenerate with:
>
> ```sh
> uv run --no-project --python 3.12 python scripts/gen_rabin_certificate.py --p 2 \
>   --f='1,1,0,1,1,0,0,0,1' \
>   --lean <this file> --namespace AesField.Certificate \
>   --authors 'CompPoly Contributors'
> ```
>
> These lists are untrusted data. Consumers validate them with kernel-checked
> `CompPoly.RabinCert.runChain` equations and certificate-soundness theorems for
> their specified polynomial. Defining the lists alone establishes no such theorem.

`AesField.Certificate.traceSteps` (definition, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Certificate.lean#L40))

> Square-and-multiply chain for `X^(p^8) mod f` (8 steps).

```lean
def traceSteps : List Step
```

> ### Coprimality with `X^(p^4) - X`, for the prime factor `2` of `d = 8`.

`AesField.Certificate.cop4Steps` (definition, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Certificate.lean#L53))

> Square-and-multiply chain for `X^(p^4) mod f` (4 steps).

```lean
def cop4Steps : List Step
```

`AesField.Certificate.cop4Rp` (definition, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Certificate.lean#L60))

> The residue `X^(p^4) mod f`.

```lean
def cop4Rp : List ℕ
```

`AesField.Certificate.cop4W` (definition, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Certificate.lean#L63))

> `cop4W = (X^(p^4) mod f) - X`, the reduced form of `X^(p^4) - X`.

```lean
def cop4W : List ℕ
```

`AesField.Certificate.cop4U` (definition, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Certificate.lean#L66))

> Bézout coefficient: `cop4U·f + cop4V·cop4W = 1`.

```lean
def cop4U : List ℕ
```

`AesField.Certificate.cop4V` (definition, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Certificate.lean#L69))

> Bézout coefficient: `cop4U·f + cop4V·cop4W = 1`.

```lean
def cop4V : List ℕ
```

## Depends on

- [Kernel-checkable Rabin irreducibility certificates over prime fields](../../../data/polynomial/rabincertificate.md)

## Sources

- [CompPoly/Fields/Binary/Aes/Certificate.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Certificate.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Fields.Binary.Aes.Certificate.json)
