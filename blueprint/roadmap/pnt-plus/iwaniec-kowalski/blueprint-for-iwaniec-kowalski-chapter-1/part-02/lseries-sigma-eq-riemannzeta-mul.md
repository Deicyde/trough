---
declaration: theorem
origin: cited
lean: ArithmeticFunction.LSeries_sigma_eq_riemannZeta_mul
statement: formalized
proof: formalized
---

# LSeries sigma eq riemannZeta mul

$\zeta(s)\zeta(s - \nu) = \sum_{n=1}^{\infty} \sigma_\nu(n) n^{-s}$ for $\Re(s) > 1$ and $\Re(s - \nu) > 1$.

## Depends on

- [sigmaR](../part-01/sigmar.md)

## Proof depends on

- [LSeries powR eq](lseries-powr-eq.md)
- [sigmaR-eq-zeta-mul-powR](sigmar-eq-zeta-mul-powr.md)
- [powR](powr.md)
- [abscissa powR le](abscissa-powr-le.md)

## Proof

The divisor power sum function $\sigma_\nu$ is the Dirichlet convolution of the constant function $1$ (i.e., $\zeta$) and the power function $n \mapsto n^\nu$. The L-series of a Dirichlet convolution is the product of the L-series of the individual functions. Since $L(1, s) = \zeta(s)$ and $L(n \mapsto n^\nu, s) = \zeta(s - \nu)$, we have $L(\sigma_\nu, s) = \zeta(s) \cdot \zeta(s - \nu)$ for $\Re(s) > 1$ and $\Re(s - \nu) > 1$.

## Lean

Formalized as [`ArithmeticFunction.LSeries_sigma_eq_riemannZeta_mul`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.LSeries_sigma_eq_riemannZeta_mul).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
