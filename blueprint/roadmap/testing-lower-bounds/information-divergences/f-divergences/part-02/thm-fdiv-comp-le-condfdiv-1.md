---
declaration: theorem
origin: cited
lean: ProbabilityTheory.fDiv_comp_left_le
statement: formalized
proof: formalized
---

# Conditioning increases f-divergence

Let $\mu$ be a finite measure on $\mathcal X$ and let $\kappa, \eta : \mathcal X \rightsquigarrow \mathcal Y$ be two finite kernels. Then $D_f(\kappa \circ \mu, \eta \circ \mu) \le D_f(\mu \otimes \kappa, \mu \otimes \eta) = D_f(\kappa, \eta \mid \mu)$

## Depends on

- [f-divergence](../part-01/def-fdiv.md)
- [Conditional f-divergence](../part-01/def-condfdiv.md)

## Proof depends on

- [fDiv_comp_le_compProd_1](lem-fdiv-comp-le-compprod-1.md)
- [fDiv_compProd_right](lem-fdiv-compprod-right.md)

## Proof

By Lemma [fDiv_comp_le_compProd_1](lem-fdiv-comp-le-compprod-1.md), $D_f(\kappa \circ \mu, \eta \circ \mu) \le D_f(\mu \otimes \kappa, \mu \otimes \eta)$. This is equal to $D_f(\kappa, \eta \mid \mu)$ by Lemma [fDiv_compProd_right](lem-fdiv-compprod-right.md).

## Lean

Formalized as [`ProbabilityTheory.fDiv_comp_left_le`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_comp_left_le).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 1046](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L1046)
