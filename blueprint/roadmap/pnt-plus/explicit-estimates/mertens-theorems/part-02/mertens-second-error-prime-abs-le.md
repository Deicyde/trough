---
declaration: corollary
origin: cited
lean: Mertens.E₂p.abs_le, Mertens.E₂p.bound, Mertens.E₂p.bound'
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1326
---

# Bound for second error (prime form)

For any $x \geq 2$, one has

$$
|E_{2,p}(x)| \leq \frac{\log 4 + 6 + E_1}{\log x}.
$$

## Depends on

- [The remainder term in Mertens second theorem (von Mangoldt form)](../part-01/mertens-second-error-mangoldt.md)

## Proof depends on

- [Partial sum of $\frac{\log p}{p}$ upper bound](../part-01/mertens-first-error-prime-le.md)
- [Error term in Mertens' first theorem bounded (prime form)](../part-01/mertens-first-theorem-prime-bounded.md)
- [The remainder term in Mertens first theorem (prime form)](../part-01/mertens-first-error-prime.md)
- [The remainder term in Mertens first theorem (von Mangoldt form)](../part-01/mertens-first-error-mangoldt.md)
- [Partial sum of $\frac{\log p}{p}$ lower bound](../part-01/mertens-first-error-prime-ge.md)
- [Integral form for second error (prime form)](mertens-second-error-prime-eq.md)
- [Partial sum of $\Lambda(d)/d$ lower bound](../part-01/mertens-first-error-mangoldt-ge.md)

## Proof

Similar to Lemma [Integral form for second error (prime form)](mertens-second-error-prime-eq.md).

## Lean

Formalized as [`Mertens.E₂p.abs_le`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.E₂p.abs_le), [`Mertens.E₂p.bound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.E₂p.bound), [`Mertens.E₂p.bound'`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.E₂p.bound').

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
