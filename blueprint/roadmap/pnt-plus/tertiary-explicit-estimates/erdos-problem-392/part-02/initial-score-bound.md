---
declaration: proposition
origin: cited
lean: Erdos392.Params.initial.score_bound
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/665
---

# initial-score-bound

The initial score is bounded by

$$
n \log(1-1/M)^{-1} + \sum_{p \leq n/L} M \log n + \sum_{p \leq \sqrt{n}} M \log^2 n / \log 2
+ \sum_{n/L < p \leq n} \frac{n}{p} \log \frac{n}{p}
+ \sum_{p \leq L} (M \log n + M L \pi(n)) \log L.
$$

## Depends on

- [params-set](../part-01/params-set.md)
- [score-def](../part-01/score-def.md)
- [initial-factorization-def](../part-01/initial-factorization-def.md)

## Proof depends on

- [waste-def](../part-01/waste-def.md)
- [initial-factorization-large-prime-le](../part-01/initial-factorization-large-prime-le.md)
- [initial-factorization-large-prime-ge](../part-01/initial-factorization-large-prime-ge.md)
- [initial-factorization-medium-prime-le](../part-01/initial-factorization-medium-prime-le.md)
- [initial-factorization-waste](../part-01/initial-factorization-waste.md)
- [initial-factorization-small-prime-le](initial-factorization-small-prime-le.md)
- [balance-def](../part-01/balance-def.md)
- [initial-factorization-small-prime-ge](initial-factorization-small-prime-ge.md)
- [initial-factorization-medium-prime-ge](../part-01/initial-factorization-medium-prime-ge.md)
- [initial-factorization-tiny-prime-ge](initial-factorization-tiny-prime-ge.md)

## Proof

Combine Lemma [initial-factorization-waste](../part-01/initial-factorization-waste.md), Sublemma [initial-factorization-large-prime-le](../part-01/initial-factorization-large-prime-le.md), Sublemma [initial-factorization-large-prime-ge](../part-01/initial-factorization-large-prime-ge.md), Sublemma [initial-factorization-medium-prime-le](../part-01/initial-factorization-medium-prime-le.md), Sublemma [initial-factorization-medium-prime-ge](../part-01/initial-factorization-medium-prime-ge.md), Sublemma [initial-factorization-small-prime-le](initial-factorization-small-prime-le.md), Sublemma [initial-factorization-small-prime-ge](initial-factorization-small-prime-ge.md), and Sublemma [initial-factorization-tiny-prime-ge](initial-factorization-tiny-prime-ge.md), and combine $\log p$ and $\log (n/p)$ to $\log n$.

## Lean

Formalized as [`Erdos392.Params.initial.score_bound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Erdos392.Params.initial.score_bound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Erdos392.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Erdos392.lean)
