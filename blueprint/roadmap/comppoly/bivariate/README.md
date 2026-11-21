# Bivariate

62 modules under `CompPoly/Bivariate/`, with 741 public declarations.

This module declares nothing public by name, so it has no article: [`CompPoly.Bivariate.GuruswamiSudan`](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan.lean).

Its [README](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/README.md) opens:

> Formally verified computable bivariate polynomials for [CompPoly](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/README.md), represented as `CPolynomial (CPolynomial R)` — polynomials in Y whose coefficients are univariate polynomials in X. Matches Mathlib's `R[X][Y]` and is compatible with [ArkLib](https://github.com/Verified-zkEVM/ArkLib)'s `Polynomial.Bivariate` interface.

The docstrings, Lean statements and README text are quoted from [Verified-zkEVM/CompPoly](https://github.com/Verified-zkEVM/CompPoly) at commit [c72a7652](https://github.com/Verified-zkEVM/CompPoly/tree/c72a765272497b4c52201be11be47af5718c7488), under its Apache-2.0 license.

- [Computable Bivariate Polynomials](basic.md)
- [Serialization of bivariate polynomials](bytes.md)
- [Equivalence between `CBivariate` and `CMvPolynomial 2`](cmvequiv.md)
- [Coefficient Rows for Bivariate Polynomials](coeffrows.md)
- [Partial Derivatives and Multiplicity of Computable Bivariate Polynomials](deriv.md)
- [Factorisation of Computable Bivariate Polynomials](factor.md)
- [Bridge: synthetic linear division equals general monic division](factormonic.md)
- [GuruswamiSudan](guruswamisudan/README.md)
- [Kronecker substitution for bivariate polynomials](kronecker.md)
- [Equivalence with Mathlib Bivariate Polynomials](topoly.md)
