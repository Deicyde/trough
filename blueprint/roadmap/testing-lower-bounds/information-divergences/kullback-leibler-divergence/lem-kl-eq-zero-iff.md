---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: InformationTheory.klDiv_eq_zero_iff
---

# Converse Gibbs' inequality

Let $\mu, \nu$ be two probability measures. Then $\operatorname{KL}(\mu, \nu) = 0$ if and only if $\mu = \nu$.

## Depends on

- [Kullback-Leibler divergence](def-kl.md)

## Proof depends on

- [kl_eq_fDiv](lem-kl-eq-fdiv.md)
- [fDiv_eq_zero_iff](../f-divergences/part-01/lem-fdiv-eq-zero-iff.md)

## Proof

KL is an f-divergence thanks to Lemma [kl_eq_fDiv](lem-kl-eq-fdiv.md), then apply Lemma [fDiv_eq_zero_iff](../f-divergences/part-01/lem-fdiv-eq-zero-iff.md).

## Lean

Formalized as [`InformationTheory.klDiv_eq_zero_iff`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/InformationTheory.klDiv_eq_zero_iff).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kl_divergence.tex, line 146](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kl_divergence.tex#L146)
