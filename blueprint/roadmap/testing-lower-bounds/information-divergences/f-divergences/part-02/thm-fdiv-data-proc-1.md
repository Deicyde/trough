---
declaration: theorem
origin: cited
lean: ProbabilityTheory.fDiv_comp_right_le
statement: formalized
proof: formalized
---

# Data-processing

Let $\mu, \nu$ be two measures on $\mathcal X$ and let $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ be a Markov kernel, where both $\mathcal X$ and $\mathcal Y$ are standard Borel. Then $D_f(\kappa \circ \mu, \kappa \circ \nu) \le D_f(\mu, \nu)$.

## Depends on

- [f-divergence](../part-01/def-fdiv.md)

## Proof depends on

- [fDiv_comp_le_compProd_1](lem-fdiv-comp-le-compprod-1.md)
- [Composition-product with a kernel](thm-fdiv-compprod-left-1.md)

## Proof

By Lemma [fDiv_comp_le_compProd_1](lem-fdiv-comp-le-compprod-1.md), $D_f(\kappa \circ \mu, \kappa \circ \nu) \le D_f(\mu \otimes \kappa, \nu \otimes \kappa)$. Then the latter is equal to $D_f(\mu, \nu)$ by Lemma [Composition-product with a kernel](thm-fdiv-compprod-left-1.md).

## Lean

Formalized as [`ProbabilityTheory.fDiv_comp_right_le`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_comp_right_le).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 1061](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L1061)
