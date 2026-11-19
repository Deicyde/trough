---
catalog: module
lean: CompPoly.CPolynomial.NTTFast.Raw.fastMulImpl, CompPoly.CPolynomial.NTTFast.fastMulImpl, CompPoly.CPolynomial.NTTFast.safeFastMul, CompPoly.CPolynomial.NTTFast.withFallback
statement: formalized
proof: formalized
---

# Fast multiplication via NTT

`CompPoly.Univariate.NTTFast.FastMul`, in [CompPoly/Univariate/NTTFast/FastMul.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTTFast/FastMul.lean), by Valerii Huhnin.

> This file exposes the one-shot `NTTFast` multiplication entry point. …

`CompPoly.CPolynomial.NTTFast.Raw.fastMulImpl` (definition, [line 33](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTTFast/FastMul.lean#L33))

> Raw pipeline for NTT-based multiplication.
>
> Correctness as ordinary polynomial multiplication requires `NTT.Domain.fits D p q`.
> This raw API deliberately does not trim.

```lean
def fastMulImpl [BEq R]
    (D : NTT.Domain R) (p q : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.NTTFast.fastMulImpl` (definition, [line 41](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTTFast/FastMul.lean#L41))

> Pipeline for NTT-based multiplication as a canonical polynomial.

```lean
def fastMulImpl [BEq R] [LawfulBEq R]
    (D : NTT.Domain R) (p q : CPolynomial R) : CPolynomial R
```

`CompPoly.CPolynomial.NTTFast.safeFastMul` (definition, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTTFast/FastMul.lean#L52))

> Safe NTT-based multiplication wrapper.
>
> The domain-fit proof requires the caller to show that the domain covers the
> convolution length.

```lean
def safeFastMul [BEq R] [LawfulBEq R]
    (D : NTT.Domain R) (p q : CPolynomial R) (_hfit : NTT.Domain.fits D p.val q.val) :
    CPolynomial R
```

`CompPoly.CPolynomial.NTTFast.withFallback` (definition, [line 64](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTTFast/FastMul.lean#L64))

> NTTFast-backed multiplication with canonical multiplication as a fallback.
>
> The selector should return a domain fitting the required convolution length.
> When it does, this uses `fastMulImpl`; otherwise it falls back to canonical
> `CPolynomial` multiplication.

```lean
def withFallback [BEq R] [LawfulBEq R]
    (bestDomainForLength? : (requiredLen : Nat) →
      Option (NTT.FittingDomain R requiredLen))
    (p q : CPolynomial R) : CPolynomial R
```

## Depends on

- [Planned NTTFast multiplication](plan.md)

## Sources

- [CompPoly/Univariate/NTTFast/FastMul.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTTFast/FastMul.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.NTTFast.FastMul.json)
