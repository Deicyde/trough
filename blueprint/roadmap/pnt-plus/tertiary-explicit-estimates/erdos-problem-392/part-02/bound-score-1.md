---
declaration: lemma
origin: cited
lean: Erdos392.Params.initial.bound_score_1
statement: formalized
proof: formalized
---

# bound-score-1

If $M$ is sufficiently large depending on $\varepsilon$, then $n \log(1-1/M)^{-1} \leq \varepsilon n$.

## Depends on

- [params-set](../part-01/params-set.md)

## Proof

Use the fact that $\log(1-1/M)^{-1}$ goes to zero as $M \to \infty$.

## Lean

Formalized as [`Erdos392.Params.initial.bound_score_1`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Erdos392.Params.initial.bound_score_1).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Erdos392.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/IEANTN/Erdos392.lean)
