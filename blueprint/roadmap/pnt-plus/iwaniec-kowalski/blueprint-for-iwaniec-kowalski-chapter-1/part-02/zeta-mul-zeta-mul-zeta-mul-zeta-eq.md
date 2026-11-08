---
declaration: theorem
origin: cited
lean: ArithmeticFunction.zeta_mul_zeta_mul_zeta_mul_zeta_eq
statement: formalized
---

# zeta mul zeta mul zeta mul zeta eq

Ramanujan formula: $\zeta(s)\zeta(s-\alpha)\zeta(s-\beta)\zeta(s-\alpha-\beta)=\zeta(2s-\alpha-\beta) \sum_{n=1}^{\infty} \sigma_\alpha(n)\sigma_\beta(n)n^{-s}$ for $\Re(s) > 1$, $\Re(s-\alpha) > 1$, $\Re(s-\beta) > 1$, and $\Re(s-\alpha-\beta) > 1$.

```
This is IK (1.28).
```

## Depends on

- [sigmaR](../part-01/sigmar.md)

## Proof

This is a direct consequence of the multiplicative properties of the functions involved and the definition of the L-series. The left-hand side can be expressed as a product of L-series corresponding to the functions $\zeta$, $n \mapsto n^{-\alpha}$, and $n \mapsto n^{-\beta}$. The right-hand side involves the L-series of the convolution of $\sigma_\alpha$ and $\sigma_\beta$, which can be expressed in terms of the L-series of $\zeta$ and the power functions. By carefully applying the properties of Dirichlet convolutions and the definitions of the L-series, we can derive the stated formula.

## Lean

Stated as [`ArithmeticFunction.zeta_mul_zeta_mul_zeta_mul_zeta_eq`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.zeta_mul_zeta_mul_zeta_mul_zeta_eq); the blueprint does not mark its proof formalized.

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
