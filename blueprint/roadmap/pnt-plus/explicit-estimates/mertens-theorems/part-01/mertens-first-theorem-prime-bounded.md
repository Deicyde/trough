---
declaration: theorem
origin: cited
lean: Mertens.sum_log_prime_div_eq_log, Mertens.sum_log_prime_div_eq_log', Mertens.sum_log_prime_div_eq_log''
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1313
---

# Error term in Mertens' first theorem bounded (prime form)

For any $x \geq 1$, one has

$$
\sum_{p \leq x} \frac{\log p}{p} = \log x + O(1).
$$

## Depends on

- [The remainder term in Mertens first theorem (prime form)](mertens-first-error-prime.md)

## Proof depends on

- [Partial sum of $\frac{\log p}{p}$ upper bound](mertens-first-error-prime-le.md)
- [Upper bound on $E_1$](e1-bound.md)
- [The remainder term in Mertens first theorem (von Mangoldt form)](mertens-first-error-mangoldt.md)
- [Partial sum of $\frac{\log p}{p}$ lower bound](mertens-first-error-prime-ge.md)
- [Partial sum of $\Lambda(d)/d$ lower bound](mertens-first-error-mangoldt-ge.md)

## Proof

Immediate from previous two corollaries.

## Lean

Formalized as [`Mertens.sum_log_prime_div_eq_log`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.sum_log_prime_div_eq_log), [`Mertens.sum_log_prime_div_eq_log'`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.sum_log_prime_div_eq_log'), [`Mertens.sum_log_prime_div_eq_log''`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.sum_log_prime_div_eq_log'').

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
