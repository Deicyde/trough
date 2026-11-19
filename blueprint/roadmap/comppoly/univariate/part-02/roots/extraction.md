---
catalog: module
lean: CompPoly.CPolynomial.linearRootOfFactor?, CompPoly.CPolynomial.validateRootCandidates, CompPoly.CPolynomial.rootsFromLinearFactors
statement: formalized
proof: formalized
---

# Root Extraction Helpers

`CompPoly.Univariate.Roots.Extraction`, in [CompPoly/Univariate/Roots/Extraction.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Extraction.lean), by Valerii Huhnin.

> Candidate extraction, validation, and deduplication helpers for univariate root
> finding.

`CompPoly.CPolynomial.linearRootOfFactor?` (definition, [line 24](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Extraction.lean#L24))

> Extract the root of a represented nonconstant linear factor.

```lean
def linearRootOfFactor? {F : Type*} [Field F] [BEq F]
    (factor : CPolynomial F) : Option F
```

`CompPoly.CPolynomial.validateRootCandidates` (definition, [line 32](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Extraction.lean#L32))

> Keep only candidates that are actual roots of the original polynomial.

```lean
def validateRootCandidates {F : Type*} [Field F] [BEq F]
    (p : CPolynomial F) (candidates : Array F) : Array F
```

`CompPoly.CPolynomial.rootsFromLinearFactors` (definition, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Extraction.lean#L37))

> Extract, validate, and deduplicate roots from a list of linear factors.

```lean
def rootsFromLinearFactors {F : Type*} [Field F] [BEq F]
    (p : CPolynomial F) (factors : Array (CPolynomial F)) : Array F
```

## Depends on

- [Computable Univariate Polynomials](../../part-01/basic.md)

## Sources

- [CompPoly/Univariate/Roots/Extraction.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Extraction.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.Roots.Extraction.json)
