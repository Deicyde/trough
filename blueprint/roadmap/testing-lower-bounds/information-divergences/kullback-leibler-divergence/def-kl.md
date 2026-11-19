---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: InformationTheory.klDiv
---

# Kullback-Leibler divergence

Let $\mu, \nu$ be two measures on $\mathcal X$. The Kullback-Leibler divergence between $\mu$ and $\nu$ is

$$
\begin{aligned}
\operatorname{KL}(\mu, \nu) = \mu\left[\log \frac{d \mu}{d \nu}\right]
\end{aligned}
$$

if $\mu \ll \nu$ and $x \mapsto \log \frac{d \mu}{d \nu}(x)$ is $\mu$-integrable and $+\infty$ otherwise.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`InformationTheory.klDiv`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/InformationTheory.klDiv).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kl_divergence.tex, line 3](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kl_divergence.tex#L3)
