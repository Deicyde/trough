---
declaration: theorem
origin: cited
lean: ArithmeticFunction.LSeries_d_eq_riemannZeta_pow
statement: formalized
proof: formalized
---

# LSeries d eq riemannZeta pow

The $L$-series of $d_k$ equals $\zeta(s)^k$ for $\Re(s) > 1$.

## Depends on

- [d](d.md)

## Proof depends on

- [d succ](d-succ.md)
- [LSeries d summable](lseries-d-summable.md)
- [d zero](d-zero.md)

## Proof

From the definition of $d_k$ as the $k$-fold Dirichlet convolution of $\zeta$, we can express $d_k$ as $\zeta^k$. The L-series of a Dirichlet convolution corresponds to the product of the L-series of the individual functions. Since $L(\zeta, s)$ is the Riemann zeta function $\zeta(s)$, it follows that $L(d_k, s) = L(\zeta^k, s) = (L(\zeta, s))^k = \zeta(s)^k$ for $\Re(s) > 1$ where the series converges.

## Lean

Formalized as [`ArithmeticFunction.LSeries_d_eq_riemannZeta_pow`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.LSeries_d_eq_riemannZeta_pow).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
