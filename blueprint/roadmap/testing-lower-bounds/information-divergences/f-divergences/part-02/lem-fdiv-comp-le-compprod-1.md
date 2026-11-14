---
declaration: lemma
origin: cited
lean: ProbabilityTheory.fDiv_comp_le_compProd
statement: formalized
proof: formalized
---

# fDiv_comp_le_compProd_1

Let $\mu, \nu$ be two finite measures on a standard Borel space $\mathcal X$ and let $\kappa, \eta : \mathcal X \rightsquigarrow \mathcal Y$ be two finite kernels. $D_f(\kappa \circ \mu, \eta \circ \nu) \le D_f(\mu \otimes \kappa, \nu \otimes \eta)$

## Depends on

- [f-divergence](../part-01/def-fdiv.md)

## Proof depends on

- [Marginals](thm-fdiv-fst-le-1.md)

## Proof

By definition, $\kappa \circ \mu$ is the marginal of $\mu \otimes \kappa$ (a measure on $\mathcal X \times \mathcal Y$) on $\mathcal Y$, and similarly for the other measure. Hence by Theorem [Marginals](thm-fdiv-fst-le-1.md), $D_f(\kappa \circ \mu, \eta \circ \nu) \le D_f(\mu \otimes \kappa, \nu \otimes \eta)$.

## Lean

Formalized as [`ProbabilityTheory.fDiv_comp_le_compProd`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_comp_le_compProd).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 1031](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L1031)
