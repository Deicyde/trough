---
declaration: definition
origin: cited
lean: ProbabilityTheory.hellingerDiv
statement: formalized
---

# Hellinger $\alpha$-divergence

Let $\mu, \nu$ be two measures on $\mathcal X$. The Hellinger divergence of order $\alpha \in [0,+\infty)$ between $\mu$ and $\nu$ is

$$
\begin{aligned}
\operatorname{H}_\alpha(\mu, \nu) = \left\{
\begin{array}{ll}
\nu \{x \mid \frac{d\mu}{d\nu} (x) = 0\} & \text{for } \alpha = 0 \\
\operatorname{KL}(\mu, \nu) & \text{for } \alpha = 1
\\
D_{f_\alpha}(\mu, \nu) & \text{for } \alpha \in (0,+\infty) \backslash \{1\}
\end{array}\right.
\end{aligned}
$$

with $f_\alpha : x \mapsto \frac{x^{\alpha} - 1}{\alpha - 1}$.

## Depends on

- [Kullback-Leibler divergence](../kullback-leibler-divergence/def-kl.md)
- [f-divergence](../f-divergences/part-01/def-fdiv.md)

## Lean

Formalized as [`ProbabilityTheory.hellingerDiv`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.hellingerDiv).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/hellinger_alpha.tex, line 3](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/hellinger_alpha.tex#L3)
