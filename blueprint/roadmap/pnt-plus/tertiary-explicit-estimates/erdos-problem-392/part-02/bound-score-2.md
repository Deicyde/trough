---
declaration: lemma
origin: cited
lean: Erdos392.Params.initial.bound_score_2
statement: formalized
proof: formalized
---

# bound-score-2

If $L$ is sufficiently large depending on $M, \varepsilon$, and $n$ sufficiently large depending on $L$, then $\sum_{p \leq n/L} M \log n \leq \varepsilon n$.

## Depends on

- [params-set](../part-01/params-set.md)

## Proof depends on

- [pi-alt](../../../elementary-corollaries/pi-alt.md)

## Proof

Use the prime number theorem (or the Chebyshev bound).

## Lean

Formalized as [`Erdos392.Params.initial.bound_score_2`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Erdos392.Params.initial.bound_score_2).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Erdos392.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/IEANTN/Erdos392.lean)
