---
declaration: lemma
origin: cited
lean: ProbabilityTheory.klDiv_prod_two'
statement: formalized
proof: formalized
---

# kl_prod_two'

Let $\mu_1, \nu_1$ be finite measures on $\mathcal X$ and $\mu_2, \nu_2$ probability measures on $\mathcal{Y}$. Then

$$
\operatorname{KL}(\mu_1\times \mu_2, \nu_1 \times \nu_2) = \operatorname{KL}(\mu_1, \nu_1) + \operatorname{KL}(\mu_2, \nu_2) \mu_1 (\mathcal X) \: .
$$

## Depends on

- [Kullback-Leibler divergence](def-kl.md)

## Proof depends on

- [Chain rule, kernel version](thm-kl-compprod.md)
- [condKL_const](lem-condkl-const.md)

## Proof

Write $\mu_1 \times \mu_2$ and $\nu_1 \times \nu_2$ as composition products of a measure and a constant kernel, then apply the chain rule (Theorem [Chain rule, kernel version](thm-kl-compprod.md)) and Lemma [condKL_const](lem-condkl-const.md).

## Lean

Formalized as [`ProbabilityTheory.klDiv_prod_two'`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.klDiv_prod_two').

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kl_divergence.tex, line 329](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kl_divergence.tex#L329)
