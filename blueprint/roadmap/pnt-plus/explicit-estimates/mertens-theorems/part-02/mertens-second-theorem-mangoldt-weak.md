---
declaration: theorem
origin: cited
lean: Mertens.sum_mangoldt_div_log_eq_log_log, Mertens.sum_mangoldt_div_log_eq_log_log', Mertens.sum_mangoldt_div_log_eq_log_log''
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1321
---

# Mertens' second theorem (weak von Mangoldt form)

For any $x \geq 2$, one has

$$
\sum_{n \leq x} \frac{\Lambda(n)}{n \log n} = \log \log x + O(1).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [The remainder term in Mertens second theorem (von Mangoldt form)](../part-01/mertens-second-error-mangoldt.md)
- [Alternate Formula for Euler-Mascheroni constant](../part-01/euler-mascheroni-const-alt.md)
- [The remainder term in Mertens first theorem (von Mangoldt form)](../part-01/mertens-first-error-mangoldt.md)
- [Compatibility with Mathlib Euler-Mascheroni constant](euler-mascheroni-eq.md)
- [Bound for second Mertens error (von Mangoldt form)](mertens-second-error-mangoldt-bound.md)

## Proof

Immediate from previous two corollaries.

## Lean

Formalized as [`Mertens.sum_mangoldt_div_log_eq_log_log`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.sum_mangoldt_div_log_eq_log_log), [`Mertens.sum_mangoldt_div_log_eq_log_log'`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.sum_mangoldt_div_log_eq_log_log'), [`Mertens.sum_mangoldt_div_log_eq_log_log''`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.sum_mangoldt_div_log_eq_log_log'').

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
