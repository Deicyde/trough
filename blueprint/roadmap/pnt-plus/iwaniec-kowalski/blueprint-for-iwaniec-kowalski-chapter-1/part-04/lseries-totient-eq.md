---
declaration: theorem
origin: cited
lean: ArithmeticFunction.LSeries_totient_eq
statement: formalized
proof: formalized
---

# LSeries totient eq

Euler totient series: $\sum_{n=1}^{\infty} \varphi(n) n^{-s} = \zeta(s-1)/\zeta(s)$ for $\Re(s) > 2$.

```
This is IK (1.35). The L-series converges absolutely for Re(s) > 2
(using φ(n) ≤ n to bound terms; the original hypothesis 1 < Re(s) is incorrect).
```

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [LSeries powR eq](../part-02/lseries-powr-eq.md)
- [powR](../part-02/powr.md)

## Proof

The Euler totient function $\varphi(n)$ counts the positive integers up to $n$ that are relatively prime to $n$. It is a multiplicative function, and its value at prime powers is given by $\varphi(p^k) = p^k - p^{k-1}$. The Dirichlet series of $\varphi$ can be expressed as an Euler product over primes:

$$
L(\varphi, s) = \prod_{p} \left(1 + \varphi(p)p^{-s} + \varphi(p^2)p^{-2s} + \ldots\right) = \prod_{p} \left(1 - p^{-s  +1}\right)^{-1} \left(1 - p^{-s}\right) = \frac{\zeta(s-1)}{\zeta(s)}.
$$

The L-series converges absolutely for Re(s) $>$ 2, using φ(n) ≤ n to bound the terms.

## Lean

Formalized as [`ArithmeticFunction.LSeries_totient_eq`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.LSeries_totient_eq).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
