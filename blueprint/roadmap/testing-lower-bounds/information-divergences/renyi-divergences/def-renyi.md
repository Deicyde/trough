---
declaration: definition
origin: cited
lean: ProbabilityTheory.renyiDiv
statement: formalized
---

# Rényi divergence

Let $\mu, \nu$ be two finite measures on $\mathcal X$. The Rényi divergence of order $\alpha \in \mathbb{R}$ between $\mu$ and $\nu$ is

$$
\begin{aligned}
R_\alpha(\mu, \nu) = \left\{
\begin{array}{ll}
- \log \left( \nu\{x \mid \frac{d \mu}{d \nu}(x) > 0\} / \nu(\mathcal X) \right) & \text{for } \alpha = 0
\\
\operatorname{KL}(\mu / \mu(\mathcal X), \nu / \nu(\mathcal X)) & \text{for } \alpha = 1
\\
\frac{1}{\alpha - 1} \log \left( \frac{(1 - \alpha) \nu(\mathcal X) + \alpha \mu(\mathcal X) + (\alpha - 1) \operatorname{H}_\alpha(\mu, \nu)}{\mu(\mathcal X)^\alpha \nu(\mathcal X)^{1 - \alpha}} \right) & \text{for } \alpha \notin \{0, 1\}
\end{array}\right.
\end{aligned}
$$

It is the Rényi divergence of the normalized measures $\mu / \mu(\mathcal X)$ and $\nu / \nu(\mathcal X)$. For $\alpha \notin \{0, 1\}$, the numerator inside the logarithm is $\int \left(\frac{d \mu}{d \nu}\right)^\alpha d\nu$.

## Depends on

- [Kullback-Leibler divergence](../kullback-leibler-divergence/def-kl.md)
- [Hellinger $\alpha$-divergence](../hellinger-alpha-divergences/def-hellingeralpha.md)

## Lean

Formalized as [`ProbabilityTheory.renyiDiv`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.renyiDiv).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/renyi_divergence.tex, line 3](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/renyi_divergence.tex#L3)
