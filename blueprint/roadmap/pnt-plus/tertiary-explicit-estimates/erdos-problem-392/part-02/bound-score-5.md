---
declaration: lemma
origin: cited
lean: Erdos392.Params.initial.bound_score_5
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/518
---

# bound-score-5

If $n$ sufficiently large depending on $M, L, \varepsilon$, then $\sum_{p \leq L} (M \log n + M L \pi(n)) \log L \leq \varepsilon n$.

## Depends on

- [params-set](../part-01/params-set.md)

## Proof depends on

- [primeCounting-le-bound](primecounting-le-bound.md)

## Proof

Use the prime number theorem (or the Chebyshev bound).

## Lean

Formalized as [`Erdos392.Params.initial.bound_score_5`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Erdos392.Params.initial.bound_score_5).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Erdos392.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/IEANTN/Erdos392.lean)
