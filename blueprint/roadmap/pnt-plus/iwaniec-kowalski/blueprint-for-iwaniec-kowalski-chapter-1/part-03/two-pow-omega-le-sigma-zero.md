---
declaration: theorem
origin: cited
lean: ArithmeticFunction.two_pow_omega_le_sigma_zero
statement: formalized
proof: formalized
---

# two-pow-omega-le-sigma-zero

We have the inequality $2^{\omega(n)}\leq\sigma_0(n)$ when $n\neq 0$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Recall that $\omega(n)$ is the number of distinct prime factors of $n$. Thus,

$$
2^{\omega(n)}=\prod_{p|n}2.
$$

Likewise, $\sigma_0(n)$ is the number of divisors of $n$. We can write this as

$$
\prod_{p|n}(1+v_p(n))=\sigma_0(n)
$$

where $v_p(n)$ denotes the $p$-adic valuation of $n$. For $p|n$ we have that $2\leq 1+v_p(n)$. Thus the result immediately follows.

## Lean

Formalized as [`ArithmeticFunction.two_pow_omega_le_sigma_zero`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.two_pow_omega_le_sigma_zero).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
