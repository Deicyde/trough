---
declaration: corollary
origin: cited
lean: ProbabilityTheory.fDiv_prod_left
statement: formalized
proof: formalized
---

# fDiv_prod_left_1

Let $\mu, \nu$ be two finite measures on $\mathcal X$ and let $\xi$ be a probability measure on $\mathcal Y$. Then $D_f(\mu \times \xi, \nu \times \xi) = D_f(\mu, \nu)$.

## Depends on

- [f-divergence](../part-01/def-fdiv.md)

## Proof depends on

- [Composition-product with a kernel](thm-fdiv-compprod-left-1.md)

## Proof

Apply Lemma [Composition-product with a kernel](thm-fdiv-compprod-left-1.md) with $\kappa$ the constant kernel with value $\xi$.

## Lean

Formalized as [`ProbabilityTheory.fDiv_prod_left`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_prod_left).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 866](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L866)
