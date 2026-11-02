---
declaration: proposition
origin: cited
lean: Erdos392.Params.initial.score
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/519
---

# initial-score

The score of the initial factorization can be taken to be $o(n)$.

## Depends on

- [params-set](../part-01/params-set.md)
- [score-def](../part-01/score-def.md)
- [initial-factorization-def](../part-01/initial-factorization-def.md)

## Proof depends on

- [bound-score-4](bound-score-4.md)
- [bound-score-1](bound-score-1.md)
- [bound-score-2](bound-score-2.md)
- [initial-score-bound](initial-score-bound.md)
- [bound-score-5](bound-score-5.md)
- [bound-score-3](bound-score-3.md)

## Proof

Pick $M$ large depending on $\varepsilon$, then $L$ sufficiently large depending on $M, \varepsilon$, then $n$ sufficiently large depending on $M,L,\varepsilon$, so that the bounds in Sublemma [bound-score-1](bound-score-1.md), Sublemma [bound-score-2](bound-score-2.md), Sublemma [bound-score-3](bound-score-3.md), Sublemma [bound-score-4](bound-score-4.md), and Sublemma [bound-score-5](bound-score-5.md) each contribute at most $(\varepsilon/5) n$. Then use Proposition [initial-score-bound](initial-score-bound.md).

## Lean

Formalized as [`Erdos392.Params.initial.score`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Erdos392.Params.initial.score).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Erdos392.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Erdos392.lean)
