---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: InformationTheory.klDiv_self
---

# kl_self

$\operatorname{KL}(\mu, \mu) = 0$.

## Depends on

- [Kullback-Leibler divergence](def-kl.md)

## Proof depends on

- [kl_eq_fDiv](lem-kl-eq-fdiv.md)
- [fDiv_self](../f-divergences/part-01/lem-fdiv-self.md)

## Proof

KL is an f-divergence thanks to Lemma [kl_eq_fDiv](lem-kl-eq-fdiv.md), then apply Lemma [fDiv_self](../f-divergences/part-01/lem-fdiv-self.md).

## Lean

Formalized as [`InformationTheory.klDiv_self`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/InformationTheory.klDiv_self).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kl_divergence.tex, line 60](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kl_divergence.tex#L60)
