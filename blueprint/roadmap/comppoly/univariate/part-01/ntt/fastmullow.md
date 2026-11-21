---
catalog: module
lean: CompPoly.CPolynomial.NTT.FastMulLow.run, CompPoly.CPolynomial.NTT.FastMulLow.withFallback
statement: formalized
proof: formalized
---

# Low Product via NTT

`CompPoly.Univariate.NTT.FastMulLow`, in [CompPoly/Univariate/NTT/FastMulLow.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/FastMulLow.lean), by Valerii Huhnin.

> This file exposes an NTT-backed `Raw.MulLowContext` for computing the low
> coefficients of a raw polynomial product.

`CompPoly.CPolynomial.NTT.FastMulLow.run` (definition, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/FastMulLow.lean#L48))

```lean
def run
    (bestDomainForLength? : (requiredLen : Nat) →
      Option (FittingDomain R requiredLen))
    (k : Nat) (p q : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.NTT.FastMulLow.withFallback` (definition, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/FastMulLow.lean#L69))

> NTT-backed low-product context with low-convolution as a fallback.
>
> This truncates both inputs to the requested output precision, multiplies them
> with the selected fitting NTT domain when one is available, and truncates the
> result back to the requested precision. If the domain table cannot cover the
> requested product length, it falls back to the low-convolution backend.

```lean
def withFallback
    (bestDomainForLength? : (requiredLen : Nat) →
      Option (FittingDomain R requiredLen)) :
    CPolynomial.Raw.MulLowContext R
```

## Depends on

- [Fast Multiplication via NTT](fastmul.md)
- [Raw Univariate Polynomial Proofs](../raw/proofs.md)

## Sources

- [CompPoly/Univariate/NTT/FastMulLow.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/FastMulLow.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.NTT.FastMulLow.json)
