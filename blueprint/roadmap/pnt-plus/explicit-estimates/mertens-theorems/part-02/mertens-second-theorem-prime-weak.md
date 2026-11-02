---
declaration: theorem
origin: cited
lean: Mertens.sum_prime_div_eq_log_log, Mertens.sum_prime_div_eq_log_log', Mertens.sum_prime_div_eq_log_log''
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1327
---

# Mertens' second theorem (weak prime form)

For any $x \geq 2$, one has

$$
\sum_{p \leq x} \frac{1}{p} = \log \log x + O(1).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [The remainder term in Mertens second theorem (von Mangoldt form)](../part-01/mertens-second-error-mangoldt.md)
- [Bound for second error (prime form)](mertens-second-error-prime-abs-le.md)
- [The Meissel-Mertens constant](meissel-mertens-constant.md)

## Proof

Immediate from previous two corollaries.

## Lean

Formalized as [`Mertens.sum_prime_div_eq_log_log`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.sum_prime_div_eq_log_log), [`Mertens.sum_prime_div_eq_log_log'`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.sum_prime_div_eq_log_log'), [`Mertens.sum_prime_div_eq_log_log''`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.sum_prime_div_eq_log_log'').

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
