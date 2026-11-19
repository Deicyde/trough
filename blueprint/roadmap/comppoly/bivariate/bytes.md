---
catalog: module
lean: CompPoly.CBivariate.encode_eq
statement: formalized
proof: formalized
---

# Serialization of bivariate polynomials

`CompPoly.Bivariate.Bytes`, in [CompPoly/Bivariate/Bytes.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Bytes.lean), by Derek Sorensen.

> `CBivariate R` is `CPolynomial (CPolynomial R)`, so its self-delimiting encoding is the
> univariate one nested: a `u64` count of `Y`-coefficients, each a `u64` count of
> `X`-coefficients followed by those coefficients. Nothing new is defined; the instance is the
> univariate codec at coefficient type `CPolynomial R`, which is what the delimited-codec design
> exists for.

`CompPoly.CBivariate.encode_eq` (theorem, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Bytes.lean#L30))

```lean
theorem encode_eq [DelimitedCodec R] (p : CBivariate R) :
    DelimitedCodec.encode p = DelimitedCodec.encode (p : CPolynomial (CPolynomial R))
```

## Depends on

- [Computable Bivariate Polynomials](basic.md)
- [Self-delimiting byte codecs](../data/bytes/delimited.md)

## Proof depends on

- [Serialization of univariate polynomials](../univariate/part-01/bytes.md)

## Sources

- [CompPoly/Bivariate/Bytes.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Bytes.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Bivariate.Bytes.json)
