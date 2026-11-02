---
declaration: theorem
origin: cited
lean: ArithmeticFunction.LSeries_d_summable
statement: formalized
proof: formalized
---

# LSeries d summable

The L-series for $d_k$ is summable for $\Re(s) > 1$.

## Depends on

- [d](d.md)

## Proof depends on

- [d succ](d-succ.md)
- [d zero](d-zero.md)

## Proof

Since $d_k$ is defined as the $k$-fold Dirichlet convolution of $\zeta$, and we know that the L-series of $\zeta$ converges for $\Re(s) > 1$, it follows that the L-series of $d_k$ also converges for $\Re(s) > 1$. This is because the convolution of functions with convergent L-series will also have a convergent L-series in the same region. Therefore, we can conclude that $L(d_k, s)$ is summable for $\Re(s) > 1$.

## Lean

Formalized as [`ArithmeticFunction.LSeries_d_summable`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.LSeries_d_summable).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
