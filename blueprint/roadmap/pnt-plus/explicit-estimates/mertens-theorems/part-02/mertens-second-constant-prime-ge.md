---
declaration: corollary
origin: cited
lean: Mertens.M.ge
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1324
---

# Lower bound for $M$

One has $M \geq -\frac{2 + E_1}{\log 2} + 1 - \log \log 2$.

## Depends on

- [The Meissel-Mertens constant](meissel-mertens-constant.md)

## Proof depends on

- [Error term in Mertens' first theorem bounded (prime form)](../part-01/mertens-first-theorem-prime-bounded.md)
- [The remainder term in Mertens first theorem (prime form)](../part-01/mertens-first-error-prime.md)
- [The remainder term in Mertens first theorem (von Mangoldt form)](../part-01/mertens-first-error-mangoldt.md)
- [Partial sum of $\frac{\log p}{p}$ lower bound](../part-01/mertens-first-error-prime-ge.md)
- [Partial sum of $\Lambda(d)/d$ lower bound](../part-01/mertens-first-error-mangoldt-ge.md)

## Proof

Insert Lemma [Partial sum of $\frac{\log p}{p}$ lower bound](../part-01/mertens-first-error-prime-ge.md) into the definition of $M$ and use the fact that $\int_2^\infty \frac{dt}{t \log^2 t} = 1/\log 2$.

## Lean

Formalized as [`Mertens.M.ge`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.M.ge).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
