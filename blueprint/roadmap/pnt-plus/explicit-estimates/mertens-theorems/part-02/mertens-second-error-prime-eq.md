---
declaration: corollary
origin: cited
lean: Mertens.E₂p.eq
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1325
---

# Integral form for second error (prime form)

For any $x \geq 2$, one has

$$
E_{2,p}(x) = \frac{E_{1,p}(x)}{\log x} - \int_x^\infty \frac{E_{1,p}(t)}{t \log^2 t}\ dt
$$

## Depends on

- [The remainder term in Mertens second theorem (von Mangoldt form)](../part-01/mertens-second-error-mangoldt.md)
- [The remainder term in Mertens first theorem (prime form)](../part-01/mertens-first-error-prime.md)

## Proof depends on

- [Error term in Mertens' first theorem bounded (prime form)](../part-01/mertens-first-theorem-prime-bounded.md)
- [Integral identity involving inverse log weight](../part-01/mertens-integral-ident.md)
- [The Meissel-Mertens constant](meissel-mertens-constant.md)

## Proof

From Lemma [Integral identity involving inverse log weight](../part-01/mertens-integral-ident.md) one has

$$
\sum_{p \leq x} \frac{1}{p} = \frac{1}{\log x} \sum_{p \leq x} \frac{\log p}{p} + \int_2^x \frac{1}{t \log^2 t} \sum_{p \leq t} \frac{\log p}{p} \, dt.
$$

Now substitute the definitions of $E_{1,p}$, $E_{2,p}$, $M$ and simplify.

## Lean

Formalized as [`Mertens.E₂p.eq`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.E₂p.eq).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
