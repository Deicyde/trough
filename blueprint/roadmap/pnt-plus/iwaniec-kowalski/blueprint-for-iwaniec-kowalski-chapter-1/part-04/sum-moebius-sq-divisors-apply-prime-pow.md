---
declaration: theorem
origin: cited
lean: ArithmeticFunction.sum_moebius_sq_divisors_apply_prime_pow
statement: formalized
proof: formalized
---

# sum-moebius-sq-divisors-apply-prime-pow

Applied at prime powers, sum-moebius-sq-divisors coincides with $\mu^2$.

## Depends on

- [sum-moebius-sq-divisors](sum-moebius-sq-divisors.md)

## Proof depends on

- [sum-moebius-sq-divisors-apply](sum-moebius-sq-divisors-apply.md)

## Proof

For a prime power $p^k$, note that if $k\leq 1$ then the only square divisor is $1$, so the sum evaluates as $\mu(1)=1$. If $k\geq 2$, then $1$ and $p^2$ are square divisors of $p^k$. Thus, the sum evaluates as $\mu(1)+\mu(p)+\ldots$ where the remaining terms are moebius of higher powers (if necessary). Since $\mu(p)=-1$ and $\mu$ of higher powers of $p$ is zero, this is $0$. This agrees with $\mu(p^k)^2$, which is simply an indicator function for $k\leq 1$ (i.e. $p^k$ is squarefree).

## Lean

Formalized as [`ArithmeticFunction.sum_moebius_sq_divisors_apply_prime_pow`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.sum_moebius_sq_divisors_apply_prime_pow).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
