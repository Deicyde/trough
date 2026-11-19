---
declaration: lemma
origin: cited
lean: ProbabilityTheory.chernoffDiv_one
statement: formalized
proof: formalized
---

# chernoff_eq_kl

$C_1(\mu, \nu) = \inf_{\xi \in \mathcal P(\mathcal X)}\max\{\operatorname{KL}(\xi, \mu), \operatorname{KL}(\xi, \nu)\}$ .

## Depends on

- [Chernoff divergence](def-chernoff.md)
- [Kullback-Leibler divergence](../kullback-leibler-divergence/def-kl.md)

## Proof depends on

- [Rényi divergence](../renyi-divergences/def-renyi.md)

## Proof

This is $R_1 = \operatorname{KL}$ (by definition).

## Lean

Formalized as [`ProbabilityTheory.chernoffDiv_one`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.chernoffDiv_one).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/chernoff.tex, line 18](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/chernoff.tex#L18)
