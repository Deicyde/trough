---
declaration: theorem
origin: cited
lean: ProbabilityTheory.klDiv_fst_add_condKL
statement: formalized
proof: formalized
---

# Chain rule, product version

Let $\mu, \nu$ be two finite measures on $\mathcal X \times \mathcal Y$, where $\mathcal Y$ is standard Borel. Then $\operatorname{KL}(\mu, \nu) = \operatorname{KL}(\mu_X, \nu_X) + \operatorname{KL}(\mu_{Y|X}, \nu_{Y|X} \mid \mu_X)$.

## Depends on

- [Kullback-Leibler divergence](def-kl.md)
- [Conditional Kullback-Leibler divergence](def-condkl.md)

## Proof depends on

- [Chain rule, kernel version](thm-kl-compprod.md)

## Proof

Write $\mu = \mu_X \otimes \mu_{Y|X}$ and $\nu = \nu_X \otimes \nu_{Y|X}$, then use Theorem [Chain rule, kernel version](thm-kl-compprod.md).

## Lean

Formalized as [`ProbabilityTheory.klDiv_fst_add_condKL`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.klDiv_fst_add_condKL).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kl_divergence.tex, line 314](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kl_divergence.tex#L314)
