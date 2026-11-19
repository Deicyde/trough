---
declaration: theorem
origin: cited
lean: ProbabilityTheory.le_fDiv_compProd'
statement: formalized
proof: formalized
---

# fDiv_le_compProd_2

Let $\mu, \nu$ be two finite measures on $\mathcal X$ and let $\kappa, \eta : \mathcal X \rightsquigarrow \mathcal Y$ be two Markov kernels. Then $D_f(\mu, \nu) \le D_f(\mu \otimes \kappa, \nu \otimes \eta)$.

## Depends on

- [f-divergence](../part-01/def-fdiv.md)

## Proof depends on

- [Data-processing](thm-fdiv-data-proc-2.md)

## Proof

Since $\kappa$ is a Markov kernel, $\mu$ is the composition of $\mu \otimes \kappa$ and the deterministic kernel for the function $(x,y) \mapsto x$. The same applies for $\nu$ and $\nu \otimes \eta$. The result is then an application of the data-processing inequality, Theorem [Data-processing](thm-fdiv-data-proc-2.md).

## Lean

Formalized as [`ProbabilityTheory.le_fDiv_compProd'`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.le_fDiv_compProd').

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 1237](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L1237)
