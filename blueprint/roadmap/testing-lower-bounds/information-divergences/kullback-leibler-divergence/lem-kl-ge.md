---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: InformationTheory.mul_log_le_klDiv
---

# kl_ge

Let $\mu, \nu$ be two finite measures on $\mathcal X$. Then $\operatorname{KL}(\mu, \nu) \ge \mu(\mathcal X) \log \frac{\mu(\mathcal X)}{\nu(\mathcal X)}$.

## Depends on

- [Kullback-Leibler divergence](def-kl.md)

## Proof depends on

- [le_fDiv](../f-divergences/part-01/lem-le-fdiv.md)
- [kl_eq_fDiv](lem-kl-eq-fdiv.md)

## Lean

Formalized as [`InformationTheory.mul_log_le_klDiv`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/InformationTheory.mul_log_le_klDiv).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kl_divergence.tex, line 119](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kl_divergence.tex#L119)
