---
declaration: definition
origin: cited
lean: ProbabilityTheory.condFDiv
statement: formalized
---

# Conditional f-divergence

Let $f : \mathbb{R} \to \mathbb{R}$, $\mu$ a measure on $\mathcal X$ and $\kappa, \eta : \mathcal X \rightsquigarrow \mathcal Y$ two Markov kernels from $\mathcal X$ to $\mathcal Y$. The conditional f-divergence between $\kappa$ and $\eta$ with respect to $\mu$ is

$$
\begin{aligned}
D_f(\kappa, \eta \mid \mu) = \mu\left[x \mapsto D_f(\kappa(x), \eta(x))\right]
\end{aligned}
$$

if $x \mapsto D_f(\kappa(x), \eta(x))$ is $\mu$-integrable and $+\infty$ otherwise.

## Depends on

Its statement uses no other node that has an article here.

## Lean

Formalized as [`ProbabilityTheory.condFDiv`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.condFDiv).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 391](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L391)
