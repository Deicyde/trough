---
declaration: theorem
origin: cited
lean: ProbabilityTheory.fDiv_comp_le_compProd'
statement: formalized
proof: formalized
---

# fDiv_comp_le_compProd_2

Let $\mu, \nu$ be two finite measures on $\mathcal X$ and let $\kappa, \eta : \mathcal X \rightsquigarrow \mathcal Y$ be two finite kernels. Then $D_f(\kappa \circ \mu, \eta \circ \nu) \le D_f(\mu \otimes \kappa, \nu \otimes \eta)$.

## Depends on

- [f-divergence](../part-01/def-fdiv.md)

## Proof depends on

- [Data-processing](thm-fdiv-data-proc-2.md)

## Proof

$\kappa \circ \mu$ is the composition of $\mu \otimes \kappa$ and the deterministic kernel for the function $(x,y) \mapsto y$. The same applies for $\eta \circ \nu$ and $\nu \otimes \eta$. The result is then an application of the data-processing inequality, Theorem [Data-processing](thm-fdiv-data-proc-2.md).

## Lean

Formalized as [`ProbabilityTheory.fDiv_comp_le_compProd'`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_comp_le_compProd').

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 1253](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L1253)
