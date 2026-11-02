---
declaration: corollary
origin: cited
lean: Mertens.E₁Λ.ge
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1307
---

# Partial sum of $\Lambda(d)/d$ lower bound

For any $x \geq 1$, one has

$$
E_{1,\Lambda}(x) \geq - 2.
$$

## Depends on

- [The remainder term in Mertens first theorem (von Mangoldt form)](mertens-first-error-mangoldt.md)

## Proof depends on

- [Partial sum of logarithm lower bound](mertens-sum-log-ge.md)
- [Partial sum of logarithm as sum of $\Lambda(d)/d$](mertens-sum-log-eq-sum-mangoldt.md)

## Proof

Insert Lemma [Partial sum of logarithm as sum of $\Lambda(d)/d$](mertens-sum-log-eq-sum-mangoldt.md) into Lemma [Partial sum of logarithm lower bound](mertens-sum-log-ge.md) and lower bound $x/d$ by $\lfloor x/d \rfloor$.

## Lean

Formalized as [`Mertens.E₁Λ.ge`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.E₁Λ.ge).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
