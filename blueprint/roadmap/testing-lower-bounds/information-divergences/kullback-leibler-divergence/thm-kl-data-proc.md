---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: InformationTheory.klDiv_comp_right_le
---

# Data-processing

Let $\mu, \nu$ be two measures on $\mathcal X$ and let $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ be a Markov kernel. Then $\operatorname{KL}(\kappa \circ \mu, \kappa \circ \nu) \le \operatorname{KL}(\mu, \nu)$.

## Depends on

- [Kullback-Leibler divergence](def-kl.md)

## Proof depends on

- [Data-processing](../f-divergences/part-03/thm-fdiv-data-proc-2.md)
- [kl_eq_fDiv](lem-kl-eq-fdiv.md)

## Proof

Apply Theorem [Data-processing](../f-divergences/part-03/thm-fdiv-data-proc-2.md).

## Lean

Formalized as [`InformationTheory.klDiv_comp_right_le`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/InformationTheory.klDiv_comp_right_le).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kl_divergence.tex, line 104](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kl_divergence.tex#L104)
