---
declaration: theorem
origin: cited
lean: ArithmeticFunction.zeta_mul_tau_square_eq
statement: formalized
proof: formalized
---

# zeta mul tau square eq

Baby Rankin-Selberg: $\zeta(s)\sum_{n=1}^{\infty}\tau(n^2)n^{-s} = \sum_{n=1}^{\infty}\tau(n)^2 n^{-s}$ for $\Re(s) > 1$.

```
Precursor to IK (1.30).
```

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [d apply prime pow](../part-01/d-apply-prime-pow.md)
- [d](../part-01/d.md)
- [d two](../part-01/d-two.md)
- [LSeries d summable](../part-01/lseries-d-summable.md)
- [d isMultiplicative](../part-01/d-ismultiplicative.md)

## Proof

This follows from the multiplicative properties of the divisor function $\tau$ and the definition of the L-series. The left-hand side can be expressed as a product of L-series corresponding to $\zeta$ and the function $n \mapsto \tau(n^2)$. The right-hand side is the L-series of the function $n \mapsto \tau(n)^2$. By analyzing the Euler products and using the fact that $\tau(n)$ counts divisors, we can derive the stated equality.

## Lean

Formalized as [`ArithmeticFunction.zeta_mul_tau_square_eq`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.zeta_mul_tau_square_eq).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
