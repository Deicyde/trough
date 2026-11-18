---
declaration: theorem
origin: cited
lean: ArithmeticFunction.moebius_sq_tsum_prime_pow
statement: formalized
proof: formalized
---

# moebius-sq-tsum-prime-pow

For $p$ prime, we have that

$$
\sum_{0\leq k}\mu^2(p^k)p^{-ks}=1+p^{-s}.
$$

## Depends on

- [sumOnPrimePows](sumonprimepows.md)

## Proof depends on

- [sumOnPrimePows-apply](sumonprimepows-apply.md)

## Proof

Note that $\mu^2(p^0)=1$ and $\mu^2(p^1)=1$ but $\mu^2(p^k)=0$ whenever $1\lt k$. Thus,

$$
\sum_{0\leq k}\mu^2(p^k)p^{-ks}=1+p^{-s}.
$$

## Lean

Formalized as [`ArithmeticFunction.moebius_sq_tsum_prime_pow`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.moebius_sq_tsum_prime_pow).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
