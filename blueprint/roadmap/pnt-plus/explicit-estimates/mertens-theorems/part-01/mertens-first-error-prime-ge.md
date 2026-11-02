---
declaration: corollary
origin: cited
lean: Mertens.E₁Λ.le_E₁p_add_E₁
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1312
---

# Partial sum of $\frac{\log p}{p}$ lower bound

For any $x \geq 1$, one has

$$
E_{1,\Lambda}(x) \leq E_{1,p}(x) + E_1
$$

and thus

$$
E_{1,p}(x) \geq -2 - E_1
$$

where

$$
E_1 := \sum_{p} \frac{\log p}{p(p-1)}.
$$

## Depends on

- [The remainder term in Mertens first theorem (prime form)](mertens-first-error-prime.md)
- [The remainder term in Mertens first theorem (von Mangoldt form)](mertens-first-error-mangoldt.md)

## Proof depends on

- [$E_1$ summable](e1-summable.md)

## Proof

Use the triangle inequality and the geometric series formula to estimate in Lemma Mertens-sum-mangoldt-div-le arising from prime powers.

## Lean

Formalized as [`Mertens.E₁Λ.le_E₁p_add_E₁`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.E₁Λ.le_E₁p_add_E₁).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
