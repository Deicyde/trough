---
catalog: module
lean: BF64.BaseCert.modulus, BF64.BaseCert.traceSteps, BF64.BaseCert.cop32Steps, BF64.BaseCert.cop32Rp, BF64.BaseCert.cop32W, BF64.BaseCert.cop32U, BF64.BaseCert.cop32V
statement: formalized
proof: formalized
---

# Rabin certificate data for `p = 2` (BaseCertificate)

`CompPoly.Fields.Binary.BF64.BaseCertificate`, in [CompPoly/Fields/Binary/BF64/BaseCertificate.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/BaseCertificate.lean), by Nicolas Schleicher.

> The modulus `f` has little-endian coefficients `[1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
> 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
> 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]`.
>
> `d = 64` is composite, so Rabin's coprimality condition needs one certificate per
> prime factor of `d` (2), at exponents p^32 respectively. Checking only the
> linear-factor case would admit a product of equal-degree factors.
>
> GENERATED. Do not edit by hand; regenerate with:
>
> ```sh
> uv run --no-project --python 3.12 python scripts/gen_rabin_certificate.py --p 2 \
>   --f='1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'\
> '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1' \
>   --lean <this file> --namespace BF64.BaseCert \
>   --binary \
>   --authors 'Nicolas Schleicher'
> ```
>
> Polynomials are `GF(2)` bitmasks: bit `i` is the coefficient of `X^i`.
>
> This data is untrusted. Consumers validate it with kernel-checked
> `CompPoly.RabinCert.Binary.runChain` equations and certificate-soundness
> theorems for their specified polynomial. Defining it alone establishes no such
> theorem.

`BF64.BaseCert.modulus` (definition, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/BaseCertificate.lean#L47))

> The modulus `f`.

```lean
def modulus : ℕ
```

`BF64.BaseCert.traceSteps` (definition, [line 50](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/BaseCertificate.lean#L50))

> Square-and-multiply chain for `X^(p^64) mod f` (64 steps).

```lean
def traceSteps : List Step
```

> ### Coprimality with `X^(p^32) - X`, for the prime factor `2` of `d = 64`.

`BF64.BaseCert.cop32Steps` (definition, [line 119](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/BaseCertificate.lean#L119))

> Square-and-multiply chain for `X^(p^32) mod f` (32 steps).

```lean
def cop32Steps : List Step
```

`BF64.BaseCert.cop32Rp` (definition, [line 154](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/BaseCertificate.lean#L154))

> The residue `X^(p^32) mod f`.

```lean
def cop32Rp : ℕ
```

`BF64.BaseCert.cop32W` (definition, [line 157](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/BaseCertificate.lean#L157))

> `cop32W = (X^(p^32) mod f) - X`, the reduced form of `X^(p^32) - X`.

```lean
def cop32W : ℕ
```

`BF64.BaseCert.cop32U` (definition, [line 160](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/BaseCertificate.lean#L160))

> Bézout coefficient: `cop32U·f + cop32V·cop32W = 1`.

```lean
def cop32U : ℕ
```

`BF64.BaseCert.cop32V` (definition, [line 163](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/BaseCertificate.lean#L163))

> Bézout coefficient: `cop32U·f + cop32V·cop32W = 1`.

```lean
def cop32V : ℕ
```

## Depends on

- [Rabin certificates over `GF(2)` on `ℕ` bitmasks](../../../data/polynomial/rabincertificatebinary.md)

## Sources

- [CompPoly/Fields/Binary/BF64/BaseCertificate.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/BaseCertificate.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Fields.Binary.BF64.BaseCertificate.json)
