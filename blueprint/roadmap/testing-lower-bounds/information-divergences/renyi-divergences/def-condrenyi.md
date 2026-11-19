---
declaration: definition
origin: cited
lean: ProbabilityTheory.condRenyiDiv
statement: formalized
---

# Conditional Rényi divergence

Let $\mu$ be a measure on $\mathcal X$ and $\kappa, \eta : \mathcal X \rightsquigarrow \mathcal Y$ be two kernels. The conditional Rényi divergence of order $\alpha \in (0,+\infty) \backslash \{1\}$ between $\kappa$ and $\eta$ conditionally to $\mu$ is

$$
\begin{aligned}
R_\alpha(\kappa, \eta \mid \mu) =\frac{1}{\alpha - 1} \log (1 + (\alpha - 1) \operatorname{H}_\alpha(\kappa, \eta \mid \mu)) \: .
\end{aligned}
$$

## Depends on

- [Conditional Hellinger $\alpha$-divergence](../hellinger-alpha-divergences/def-condhellingeralpha.md)

## Lean

Formalized as [`ProbabilityTheory.condRenyiDiv`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.condRenyiDiv).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/renyi_divergence.tex, line 130](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/renyi_divergence.tex#L130)
