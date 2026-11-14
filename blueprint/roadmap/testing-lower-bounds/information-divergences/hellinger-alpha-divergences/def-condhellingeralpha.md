---
declaration: definition
origin: cited
lean: ProbabilityTheory.condHellingerDiv
statement: formalized
---

# Conditional Hellinger $\alpha$-divergence

Let $\mu$ be a measure on $\mathcal X$ and $\kappa, \eta : \mathcal X \rightsquigarrow \mathcal Y$ be two kernels. The conditional Hellinger divergence of order $\alpha \in (0,+\infty) \backslash \{1\}$ between $\kappa$ and $\eta$ conditionally to $\mu$ is

$$
\begin{aligned}
\operatorname{H}_\alpha(\kappa, \eta \mid \mu) = D_{f_\alpha}(\kappa, \eta \mid \mu) \: ,
\end{aligned}
$$

for $f_\alpha : x \mapsto \frac{x^{\alpha} - 1}{\alpha - 1}$.

## Depends on

- [Conditional f-divergence](../f-divergences/part-01/def-condfdiv.md)

## Lean

Formalized as [`ProbabilityTheory.condHellingerDiv`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.condHellingerDiv).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/hellinger_alpha.tex, line 93](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/hellinger_alpha.tex#L93)
