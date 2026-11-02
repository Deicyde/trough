---
declaration: corollary
origin: cited
lean: Mertens.E₁Λ.le
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1308
---

# Partial sum of $\Lambda(d)/d$ upper bound

For any $x \geq 1$, one has

$$
E_{1,\Lambda}(x) \leq \log 4 + 4.
$$

## Depends on

- [The remainder term in Mertens first theorem (von Mangoldt form)](mertens-first-error-mangoldt.md)

## Proof depends on

- [Partial sum of logarithm upper bound](mertens-sum-log-le.md)
- [Partial sum of logarithm as sum of $\Lambda(d)/d$](mertens-sum-log-eq-sum-mangoldt.md)

## Proof

Insert Lemma [Partial sum of logarithm as sum of $\Lambda(d)/d$](mertens-sum-log-eq-sum-mangoldt.md) into Lemma [Partial sum of logarithm upper bound](mertens-sum-log-le.md) and upper bound $x/d$ by $\lfloor x/d \rfloor + 1$, and use the Mathlib bound $\psi(x) \leq (\log 4 + 4) x$.

## Lean

Formalized as [`Mertens.E₁Λ.le`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.E₁Λ.le).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
