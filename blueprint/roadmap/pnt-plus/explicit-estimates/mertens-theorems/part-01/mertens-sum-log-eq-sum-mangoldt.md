---
declaration: lemma
origin: cited
lean: Mertens.sum_log_eq_sum_mangoldt
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1306
---

# Partial sum of logarithm as sum of $\Lambda(d)/d$

For any real $x$, one has

$$
\sum_{n \leq x} \log n = \sum_{d \leq x} \Lambda(d) \lfloor \frac{x}{d} \rfloor.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We have

$$
\begin{aligned}
\sum_{n \leq x} \log n
&= \sum_{n \leq x} \sum_{d \mid n} \Lambda(d)
= \sum_{d \leq x} \Lambda(d) \sum_{n \leq x, d \mid n} 1
= \sum_{d \leq x} \Lambda(d) \left\lfloor \frac{x}{d} \right\rfloor.
\end{aligned}
$$

## Lean

Formalized as [`Mertens.sum_log_eq_sum_mangoldt`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.sum_log_eq_sum_mangoldt).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
