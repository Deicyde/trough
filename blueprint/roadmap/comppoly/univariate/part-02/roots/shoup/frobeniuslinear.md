---
catalog: module
lean: CompPoly.CPolynomial.Roots.FiniteField.isRepresentedLinearFactor_of_dvd_frobenius_unique_root
statement: formalized
proof: formalized
---

# Frobenius Divisors with One Root are Linear

`CompPoly.Univariate.Roots.Shoup.FrobeniusLinear`, in [CompPoly/Univariate/Roots/Shoup/FrobeniusLinear.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/FrobeniusLinear.lean), by Valerii Huhnin.

> This file contains the field-theoretic bridge used by the Shoup trace splitter:
> a nonzero divisor of `X^q - X` over `GF(q)` with exactly one field root is a
> represented nonconstant linear factor.

`CompPoly.CPolynomial.Roots.FiniteField.isRepresentedLinearFactor_of_dvd_frobenius_unique_root` (theorem, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/FrobeniusLinear.lean#L39))

> A nonzero divisor of `X^q - X` with exactly one field root is represented as a
> linear factor.

```lean
theorem isRepresentedLinearFactor_of_dvd_frobenius_unique_root {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (ctx : SmallPrimeTraceContext F) {factor : CPolynomial F} {a : F}
    (hfactorNe : factor ≠ 0)
    (hdvd : factor.toPoly ∣ ((Polynomial.X : Polynomial F) ^ ctx.q - Polynomial.X))
    (hroot : CPolynomial.eval a factor = 0)
    (hunique : ∀ b, CPolynomial.eval b factor = 0 → b = a) :
    isRepresentedLinearFactor factor = true
```

## Depends on

- [Shoup-Style Small-Characteristic Linear-Factor Splitting](basic.md)

## Sources

- [CompPoly/Univariate/Roots/Shoup/FrobeniusLinear.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/FrobeniusLinear.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Univariate.Roots.Shoup.FrobeniusLinear.json)
