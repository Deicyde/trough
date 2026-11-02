---
declaration: corollary
origin: cited
lean: Mertens.E₂Λ.eq
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1317
---

# Integral form for second error (von Mangoldt form)

For any $x \geq 2$, one has

$$
E_{2,\Lambda}(x) = \frac{E_{1,\Lambda}(x)}{\log x} - \int_x^\infty \frac{E_{1,\Lambda}(t)}{t \log^2 t}\ dt
$$

## Depends on

- [The remainder term in Mertens second theorem (von Mangoldt form)](mertens-second-error-mangoldt.md)
- [The remainder term in Mertens first theorem (von Mangoldt form)](mertens-first-error-mangoldt.md)

## Proof depends on

- [Alternate Formula for Euler-Mascheroni constant](euler-mascheroni-const-alt.md)
- [Integral identity involving inverse log weight](mertens-integral-ident.md)
- [Mertens' first theorem (von Mangoldt form)](mertens-first-theorem-mangoldt.md)

## Proof

From Lemma [Integral identity involving inverse log weight](mertens-integral-ident.md) one has

$$
\sum_{n \leq x} \frac{\Lambda(n)}{n \log n} = \frac{1}{\log x} \sum_{n \leq x} \frac{\Lambda(n)}{n} + \int_2^x \frac{1}{t \log^2 t} \sum_{n \leq t} \frac{\Lambda(n)}{n} \, dt.
$$

Now substitute the definitions of $E_{1,\Lambda}$, $E_{2,\Lambda}$, $\gamma$ and simplify.

## Lean

Formalized as [`Mertens.E₂Λ.eq`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.E₂Λ.eq).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
