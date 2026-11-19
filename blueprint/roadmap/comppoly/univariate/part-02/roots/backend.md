---
catalog: module
lean: CompPoly.CPolynomial.Roots.FiniteField.rootsInFiniteFieldWith, CompPoly.CPolynomial.Roots.FiniteField.rootsInFiniteField
statement: formalized
proof: formalized
---

# Finite-Field Root Backend

`CompPoly.Univariate.Roots.Backend`, in [CompPoly/Univariate/Roots/Backend.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Backend.lean), by Valerii Huhnin.

> Executable field-root extraction over finite fields. The public operation
> handles zero, constant, and linear cases explicitly, computes the finite-field
> root product modulo the input polynomial, splits the product into linear
> factors, then validates and deduplicates candidates against the original input.

`CompPoly.CPolynomial.Roots.FiniteField.rootsInFiniteFieldWith` (definition, [line 31](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Backend.lean#L31))

> Executable roots of a univariate polynomial over a finite field.

```lean
def rootsInFiniteFieldWith {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : FiniteFieldContext F) (splitter : LinearFactorProductSplitter F)
    (p : CPolynomial F) : Array F
```

`CompPoly.CPolynomial.Roots.FiniteField.rootsInFiniteField` (definition, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Backend.lean#L47))

> Executable roots using the default raw multiplication and monic-remainder backends.

```lean
def rootsInFiniteField {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (ctx : FiniteFieldContext F) (splitter : LinearFactorProductSplitter F)
    (p : CPolynomial F) : Array F
```

## Depends on

- [Root Extraction Helpers](extraction.md)
- [Finite-Field Root Products](rootproduct.md)

## Sources

- [CompPoly/Univariate/Roots/Backend.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Backend.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.Roots.Backend.json)
