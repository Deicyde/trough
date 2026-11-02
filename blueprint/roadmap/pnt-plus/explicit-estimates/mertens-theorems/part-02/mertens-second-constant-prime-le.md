---
declaration: corollary
origin: cited
lean: Mertens.M.le
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1323
---

# Upper bound for $M$

One has $M \leq \frac{\log 4 + 4}{\log 2} + 1 - \log \log 2$.

## Depends on

- [The Meissel-Mertens constant](meissel-mertens-constant.md)

## Proof depends on

- [Partial sum of $\frac{\log p}{p}$ upper bound](../part-01/mertens-first-error-prime-le.md)
- [Error term in Mertens' first theorem bounded (prime form)](../part-01/mertens-first-theorem-prime-bounded.md)
- [The remainder term in Mertens first theorem (prime form)](../part-01/mertens-first-error-prime.md)

## Proof

Insert Lemma [Partial sum of $\frac{\log p}{p}$ upper bound](../part-01/mertens-first-error-prime-le.md) into the definition of $M$ and use the fact that $\int_2^\infty \frac{dt}{t \log^2 t} = 1/\log 2$.

## Lean

Formalized as [`Mertens.M.le`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.M.le).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
