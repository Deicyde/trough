---
declaration: lemma
origin: cited
lean: Mertens.sum_log_le
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1304
---

# Partial sum of logarithm upper bound

For any $x \geq 1$, one has

$$
\sum_{n \leq x} \log n \leq x \log x.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Trivial since $\log n \leq \log x$.

## Lean

Formalized as [`Mertens.sum_log_le`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.sum_log_le).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
