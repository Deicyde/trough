---
declaration: lemma
origin: cited
lean: ProbabilityTheory.condFDiv_ne_top_iff_fDiv_compProd_ne_top
statement: formalized
proof: formalized
---

# fDiv_compProd_ne_top_iff

Let $\mu$ be a finite measure on $\mathcal X$ and let $\kappa, \eta : \mathcal X \rightsquigarrow \mathcal Y$ be two finite kernels. Then $D_f(\mu \otimes \kappa, \mu \otimes \eta) \ne \infty \iff D_f(\kappa, \eta \mid \mu) \ne \infty$.

## Depends on

- [f-divergence](../part-01/def-fdiv.md)
- [Conditional f-divergence](../part-01/def-condfdiv.md)

## Proof depends on

- [fDiv_compProd_right](lem-fdiv-compprod-right.md)

## Proof

Immediate from Lemma [fDiv_compProd_right](lem-fdiv-compprod-right.md).

## Lean

Formalized as [`ProbabilityTheory.condFDiv_ne_top_iff_fDiv_compProd_ne_top`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.condFDiv_ne_top_iff_fDiv_compProd_ne_top).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 481](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L481)
