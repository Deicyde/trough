---
declaration: theorem
origin: cited
lean: ArithmeticFunction.zeta_pow_three_eq
statement: formalized
proof: formalized
---

# zeta pow three eq

Zeta cubed: $\zeta(s)^3 = \zeta(2s) \sum_{n=1}^{\infty}\tau(n^2) n^{-s}$ for $\Re(s) > 1$.

```
This is IK (1.30).
```

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [d apply prime pow](../part-01/d-apply-prime-pow.md)
- [d](../part-01/d.md)
- [LSeries.term-isMultiplicative-if-fun-isMultiplicative](lseries-term-ismultiplicative-if-fun-ismultiplic.md)
- [LSeries d summable](../part-01/lseries-d-summable.md)
- [d isMultiplicative](../part-01/d-ismultiplicative.md)
- [LSeriesSummable-two-pow-omega](lseriessummable-two-pow-omega.md)
- [Complex.one-add-prime-cpow-ne-zero](complex-one-add-prime-cpow-ne-zero.md)
- [sumOnPrimePows-apply](sumonprimepows-apply.md)
- [sumOnPrimePows](sumonprimepows.md)

## Proof

Direct Euler-product proof (independent of Ramanujan / Baby Rankin–Selberg). Locally $\tau((p^k)^2)=\tau(p^{2k})=2k+1$, and $\sum_k(2k+1)x^k=(1+x)/(1-x)^2$ for $|x|<1$. Multiplying by the local factor $1/(1-x^2)$ of $\zeta(2s)$ recovers $1/(1-x)^3$, the local factor of $\zeta(s)^3$. Absolute convergence follows by comparing $\tau(n^2)\le d_3(n)$.

## Lean

Formalized as [`ArithmeticFunction.zeta_pow_three_eq`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.zeta_pow_three_eq).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
