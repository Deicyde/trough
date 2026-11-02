---
declaration: theorem
origin: cited
lean: ArithmeticFunction.two_pow_omega_tsum_prime_pow
statement: formalized
proof: formalized
---

# two-pow-omega-tsum-prime-pow

For $1\lt \Re(s)$ and $p$ prime, we have that

$$
\sum_{0\leq k}2^{\omega(p^k)}p^{-ks}=\frac{1+p^{-s}}{1-p^{-s}}.
$$

## Depends on

- [sumOnPrimePows](sumonprimepows.md)

## Proof depends on

- [LSeriesSummable-two-pow-omega](lseriessummable-two-pow-omega.md)
- [sumOnPrimePows-apply](sumonprimepows-apply.md)

## Proof

Note that $\omega(p^0)=0$ and $\omega(p^k)=1$ whenever $0\lt k$. Thus,

$$
\sum_{0\leq k}2^{\omega(p^k)}p^{-ks}=1+2p^{-s}+2p^{-2s}+\ldots.
$$

Now apply a geometric sum to the non-constant terms and simplify. We have the necessary convergence as $1\lt \Re(s)$.

## Lean

Formalized as [`ArithmeticFunction.two_pow_omega_tsum_prime_pow`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.two_pow_omega_tsum_prime_pow).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
