---
declaration: corollary
origin: cited
lean: Mertens.sum_mangoldt_div_eq_log
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1309
---

# Mertens' first theorem (von Mangoldt form)

For any $x \geq 1$, one has

$$
\sum_{n \leq x} \frac{\Lambda(n)}{n} = \log x + O(1).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [The remainder term in Mertens first theorem (von Mangoldt form)](mertens-first-error-mangoldt.md)
- [Partial sum of $\Lambda(d)/d$ upper bound](mertens-first-error-mangoldt-le.md)
- [Partial sum of $\Lambda(d)/d$ lower bound](mertens-first-error-mangoldt-ge.md)

## Proof

Immediate from previous two corollaries.

## Lean

Formalized as [`Mertens.sum_mangoldt_div_eq_log`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.sum_mangoldt_div_eq_log).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
