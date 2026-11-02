---
declaration: corollary
origin: cited
lean: Mertens.E₂Λ.abs_le, Mertens.E₂Λ.bound, Mertens.E₂Λ.bound'
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1318
---

# Bound for second Mertens error (von Mangoldt form)

For any $x \geq 2$, one has

$$
|E_{2,\Lambda}(x)| \leq \frac{\log 4 + 6}{\log x}.
$$

## Depends on

- [The remainder term in Mertens second theorem (von Mangoldt form)](../part-01/mertens-second-error-mangoldt.md)

## Proof depends on

- [The remainder term in Mertens first theorem (von Mangoldt form)](../part-01/mertens-first-error-mangoldt.md)
- [Partial sum of $\Lambda(d)/d$ upper bound](../part-01/mertens-first-error-mangoldt-le.md)
- [Mertens' first theorem (von Mangoldt form)](../part-01/mertens-first-theorem-mangoldt.md)
- [Partial sum of $\Lambda(d)/d$ lower bound](../part-01/mertens-first-error-mangoldt-ge.md)
- [Integral form for second error (von Mangoldt form)](../part-01/mertens-second-error-mangoldt-eq.md)

## Proof

Insert Lemma [Partial sum of $\Lambda(d)/d$ upper bound](../part-01/mertens-first-error-mangoldt-le.md) and Lemma [Partial sum of $\Lambda(d)/d$ lower bound](../part-01/mertens-first-error-mangoldt-ge.md) into Lemma [Integral form for second error (von Mangoldt form)](../part-01/mertens-second-error-mangoldt-eq.md) and use the triangle inequality to obtain the required upper and lower bounds.

## Lean

Formalized as [`Mertens.E₂Λ.abs_le`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.E₂Λ.abs_le), [`Mertens.E₂Λ.bound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.E₂Λ.bound), [`Mertens.E₂Λ.bound'`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.E₂Λ.bound').

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
