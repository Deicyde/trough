---
declaration: theorem
origin: cited
lean: Mertens.M.eq
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1328
---

# Formula for Meissel-Mertens constant

One has $M = \gamma + \sum_p \log(1-\frac{1}{p}) + \frac{1}{p}$.

## Depends on

- [Alternate Formula for Euler-Mascheroni constant](../part-01/euler-mascheroni-const-alt.md)
- [The Meissel-Mertens constant](meissel-mertens-constant.md)

## Proof depends on

- [The remainder term in Mertens second theorem (von Mangoldt form)](../part-01/mertens-second-error-mangoldt.md)
- [Bound for second error (prime form)](mertens-second-error-prime-abs-le.md)
- [The remainder term in Mertens first theorem (von Mangoldt form)](../part-01/mertens-first-error-mangoldt.md)
- [Bound for second Mertens error (von Mangoldt form)](mertens-second-error-mangoldt-bound.md)

## Proof

The RHS can be Taylor expanded as $\sum_{j=2}^\infty \sum_p \frac{1}{jp^j}$. Meanwhile, the difference between $\sum_{n \leq x} \frac{\Lambda(n)}{n \log n}$ and $\sum_{p \leq x} \frac{1}{p}$ is equal to $\sum_{j=2}^\infty \sum_{p: p^j \leq x} \frac{1}{j p^j}$. Applying the monotone convergence theorem, Lemma [Bound for second error (prime form)](mertens-second-error-prime-abs-le.md), and Lemma [Bound for second Mertens error (von Mangoldt form)](mertens-second-error-mangoldt-bound.md) gives the claim.

## Lean

Formalized as [`Mertens.M.eq`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.M.eq).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
