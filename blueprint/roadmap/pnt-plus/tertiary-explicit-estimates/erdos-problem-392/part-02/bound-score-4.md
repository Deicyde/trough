---
declaration: lemma
origin: cited
lean: Erdos392.Params.initial.bound_score_4
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/517
---

# bound-score-4

If $n$ sufficiently large depending on $L, \varepsilon$, then $\sum_{n/L < p \leq n} \frac{n}{p} \log \frac{n}{p} \leq \varepsilon n$.

## Depends on

- [params-set](../part-01/params-set.md)

## Proof depends on

- [primeCounting-is-o-id](primecounting-is-o-id.md)

## Proof

Bound $\frac{n}{p}$ by $L$ and use the prime number theorem (or the Chebyshev bound).

## Lean

Formalized as [`Erdos392.Params.initial.bound_score_4`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Erdos392.Params.initial.bound_score_4).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Erdos392.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Erdos392.lean)
