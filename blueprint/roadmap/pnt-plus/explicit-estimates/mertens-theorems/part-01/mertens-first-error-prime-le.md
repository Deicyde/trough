---
declaration: corollary
origin: cited
lean: Mertens.E₁p.le
statement: formalized
proof: formalized
---

# Partial sum of $\frac{\log p}{p}$ upper bound

For any $x \geq 1$, one has

$$
E_{1,p}(x) \leq \log 4 + 4.
$$

## Depends on

- [The remainder term in Mertens first theorem (prime form)](mertens-first-error-prime.md)

## Proof depends on

- [Prime error for Mertens first theorem bounded by von Mangoldt error](mertens-first-error-prime-le-mangoldt.md)
- [The remainder term in Mertens first theorem (von Mangoldt form)](mertens-first-error-mangoldt.md)
- [Partial sum of $\Lambda(d)/d$ upper bound](mertens-first-error-mangoldt-le.md)

## Proof

Drop all terms in Lemma Mertens-sum-mangoldt-div-le arising from prime powers.

## Lean

Formalized as [`Mertens.E₁p.le`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.E₁p.le).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
