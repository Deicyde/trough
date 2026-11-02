---
declaration: lemma
origin: cited
lean: Erdos392.primeCounting_le_bound
statement: formalized
proof: formalized
---

# primeCounting-le-bound

For all $n \geq 2$, one has

$$
\pi(n) \leq \sqrt{n} + \frac{2n \log 4}{\log n}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

By Chebyshev's bound, $\prod_{p \leq n} p \leq 4^n$, so $\sum_{p \leq n} \log p \leq n \log 4$. The number of primes $p \leq \sqrt{n}$ is trivially at most $\sqrt{n}$. For primes $p > \sqrt{n}$, we have $\log p > \frac{1}{2} \log n$, hence

$$
\bigl(\pi(n) - \pi(\sqrt{n})\bigr) \cdot \tfrac{1}{2} \log n
< \sum_{\sqrt{n} < p \leq n} \log p \leq n \log 4,
$$

giving $\pi(n) - \pi(\sqrt{n}) < \frac{2n \log 4}{\log n}$. Adding $\pi(\sqrt{n}) \leq \sqrt{n}$ yields the result.

## Lean

Formalized as [`Erdos392.primeCounting_le_bound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Erdos392.primeCounting_le_bound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Erdos392.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Erdos392.lean)
