---
declaration: definition
origin: cited
lean: ProbabilityTheory.condKL
statement: formalized
---

# Conditional Kullback-Leibler divergence

Let $\mu$ be a measure on $\mathcal X$ and $\kappa, \eta : \mathcal X \rightsquigarrow \mathcal Y$ be two kernels. The conditional Kullback-Leibler divergence between $\kappa$ and $\eta$ with respect to $\mu$ is

$$
\begin{aligned}
\operatorname{KL}(\kappa, \eta \mid \mu) = \mu\left[x \mapsto \operatorname{KL}(\kappa(x), \eta(x))\right]
\end{aligned}
$$

if $x \mapsto \operatorname{KL}(\kappa(x), \eta(x))$ is $\mu$-integrable and $+\infty$ otherwise.

## Depends on

- [Kullback-Leibler divergence](def-kl.md)

## Lean

Formalized as [`ProbabilityTheory.condKL`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.condKL).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kl_divergence.tex, line 29](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kl_divergence.tex#L29)
