# Univariate

101 modules under `CompPoly/Univariate/`, with 1,508 public declarations.

These modules declare nothing public by name, so they have no article: [`CompPoly.Univariate.BatchEval`](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/BatchEval.lean), [`CompPoly.Univariate.ManyEval`](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ManyEval.lean), [`CompPoly.Univariate.Raw`](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw.lean), [`CompPoly.Univariate.Roots`](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots.lean) and [`CompPoly.Univariate.ToPoly`](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly.lean).

Its [README](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/README.md) opens:

> Formally verified computable univariate polynomials for [CompPoly](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/README.md), built on array-backed coefficient representation.

The docstrings, Lean statements and README text are quoted from [Verified-zkEVM/CompPoly](https://github.com/Verified-zkEVM/CompPoly) at commit [c72a7652](https://github.com/Verified-zkEVM/CompPoly/tree/c72a765272497b4c52201be11be47af5718c7488), under its Apache-2.0 license.

## [Barycentric Interpolation to Reed-Solomon Codes](part-01/README.md)

- [Barycentric Interpolation](part-01/barycentric.md)
- [Computable Univariate Polynomials](part-01/basic.md)
- [BatchEval](part-01/batcheval/README.md)
- [Serialization of univariate polynomials](part-01/bytes.md)
- [Equivalence between `CPolynomial` and `CMvPolynomial 1`](part-01/cmvequiv.md)
- [Coefficient-Form Interpolation from a Vanishing Polynomial](part-01/coefficientinterpolation.md)
- [Univariate Algorithm Contexts](part-01/context.md)
- [Formal Derivative and Taylor Shift of Computable Univariate Polynomials](part-01/deriv.md)
- [Univariate Division Correctness](part-01/divisioncorrectness.md)
- [Extended Euclidean Algorithm for `CPolynomial`](part-01/euclideanalgorithm.md)
- [Lagrange Interpolation](part-01/lagrange.md)
- [Array Wrappers for Computable Lagrange Interpolation](part-01/lagrangearray.md)
- [Linear Algebra API for Computable Univariate Polynomials](part-01/linear.md)
- [ManyEval](part-01/manyeval/README.md)
- [Modular Operations on Univariate Polynomials](part-01/modular.md)
- [NTT](part-01/ntt/README.md)
- [NTTFast](part-01/nttfast/README.md)
- [Quotient](part-01/quotient/README.md)
- [Raw](part-01/raw/README.md)
- [Reed-Solomon Codes](part-01/reedsolomon.md)

## [ReedSolomon to Vanishing Polynomials for Array…](part-02/README.md)

- [ReedSolomon](part-02/reedsolomon/README.md)
- [Roots](part-02/roots/README.md)
- [ToPoly](part-02/topoly/README.md)
- [Vanishing Polynomials for Array Nodes](part-02/vanishing.md)
