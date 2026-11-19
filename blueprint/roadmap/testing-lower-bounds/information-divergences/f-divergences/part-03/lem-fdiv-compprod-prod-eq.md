---
declaration: lemma
origin: cited
lean: ProbabilityTheory.fDiv_comp_eq_of_fst
statement: formalized
proof: formalized
---

# fDiv_compProd_prod_eq

Let $\mu, \nu$ be two finite measures on $\mathcal X$ and let $\kappa : \mathcal X \rightsquigarrow (\mathcal X \times \mathcal Y)$ be a Markov kernel such that for all $x$, $(\kappa(x))_X = \delta_x$. Then $D_f(\kappa \circ \mu, \kappa \circ \nu) = D_f(\mu, \nu)$.

## Depends on

- [f-divergence](../part-01/def-fdiv.md)

## Proof depends on

- [Data-processing](thm-fdiv-data-proc-2.md)
- [Marginals](thm-fdiv-fst-le-2.md)

## Proof

$D_f(\kappa \circ \mu, \kappa \circ \nu) \le D_f(\mu, \nu)$ by Theorem [Data-processing](thm-fdiv-data-proc-2.md). For the other inequality, remark that $\mu = (\kappa \circ \mu)_X$ (and similarly for $\nu$). Hence by Theorem [Marginals](thm-fdiv-fst-le-2.md) $D_f(\mu, \nu) \le D_f(\kappa \circ \mu, \kappa \circ \nu)$.

## Lean

Formalized as [`ProbabilityTheory.fDiv_comp_eq_of_fst`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_comp_eq_of_fst).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 1319](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L1319)
