---
declaration: corollary
origin: cited
lean: Mertens.E₁p.le_E₁Λ
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1311
---

# Prime error for Mertens first theorem bounded by von Mangoldt error

For any $x \geq 1$, one has

$$
E_{1,p}(x) \leq E_{1,\Lambda}(x).
$$

## Depends on

- [The remainder term in Mertens first theorem (prime form)](mertens-first-error-prime.md)
- [The remainder term in Mertens first theorem (von Mangoldt form)](mertens-first-error-mangoldt.md)

## Proof

Drop all terms in Lemma [Partial sum of logarithm as sum of $\Lambda(d)/d$](mertens-sum-log-eq-sum-mangoldt.md) arising from prime powers.

## Lean

Formalized as [`Mertens.E₁p.le_E₁Λ`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.E₁p.le_E₁Λ).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
