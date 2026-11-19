---
catalog: module
lean: CompPoly.CPolynomial.NTTFast.FastMulLow.run, CompPoly.CPolynomial.NTTFast.FastMulLow.withFallback
statement: formalized
proof: formalized
---

# Low Product via NTTFast

`CompPoly.Univariate.NTTFast.FastMulLow`, in [CompPoly/Univariate/NTTFast/FastMulLow.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTTFast/FastMulLow.lean), by Valerii Huhnin.

> This file exposes an `NTTFast`-backed `Raw.MulLowContext` for computing the low
> coefficients of a raw polynomial product.

`CompPoly.CPolynomial.NTTFast.FastMulLow.run` (definition, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTTFast/FastMulLow.lean#L49))

```lean
def run
    (bestDomainForLength? : (requiredLen : Nat) →
      Option (NTT.FittingDomain R requiredLen))
    (k : Nat) (p q : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.NTTFast.FastMulLow.withFallback` (definition, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTTFast/FastMulLow.lean#L71))

> NTTFast-backed low-product context with low-convolution as a fallback.
>
> This truncates both inputs to the requested output precision, multiplies them
> with the selected fitting NTT domain when one is available, and truncates the
> result back to the requested precision. If the domain table cannot cover the
> requested product length, it falls back to the low-convolution backend.

```lean
def withFallback
    (bestDomainForLength? : (requiredLen : Nat) →
      Option (NTT.FittingDomain R requiredLen)) :
    CPolynomial.Raw.MulLowContext R
```

## Depends on

- [Fast multiplication via NTT](fastmul.md)
- [Raw Univariate Polynomial Proofs](../raw/proofs.md)

## Proof depends on

- [NTTFast multiplication correctness](correctness/pipeline.md)

## Sources

- [CompPoly/Univariate/NTTFast/FastMulLow.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTTFast/FastMulLow.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.NTTFast.FastMulLow.json)
