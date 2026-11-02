---
declaration: theorem
origin: cited
lean: ArithmeticFunction.LSeries_powR_eq
statement: formalized
proof: formalized
---

# LSeries powR eq

$L(\text{pow}^R(\nu), s) = \zeta(s - \nu)$ for $\Re(s - \nu) > 1$.

```
This is IK (1.27).
```

## Depends on

- [powR](powr.md)

## Proof

The function $\text{pow}^R(\nu)$ is defined as $n \mapsto n^\nu$ for $n \neq 0$ and $0$ for $n = 0$. The L-series of $\text{pow}^R(\nu)$ at $s$ is given by the sum $\sum_{n=1}^{\infty} n^{\nu - s}$. This series converges to the Riemann zeta function $\zeta(s - \nu)$ for $\Re(s - \nu) > 1$, since the zeta function is defined as $\zeta(s) = \sum_{n=1}^{\infty} n^{-s}$ for $\Re(s) > 1$. Therefore, we have $L(\text{pow}^R(\nu), s) = \zeta(s - \nu)$ under the condition that $\Re(s - \nu) > 1$.

## Lean

Formalized as [`ArithmeticFunction.LSeries_powR_eq`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.LSeries_powR_eq).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
