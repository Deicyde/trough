---
declaration: definition
origin: cited
lean: ProbabilityTheory.chernoffDiv
statement: formalized
---

# Chernoff divergence

The Chernoff divergence of order $\alpha > 0$ between two measures $\mu$ and $\nu$ on $\mathcal X$ is

$$
\begin{aligned}
C_\alpha(\mu, \nu) = \inf_{\xi \in \mathcal P(\mathcal X)}\max\{R_\alpha(\xi, \mu), R_\alpha(\xi, \nu)\} \: .
\end{aligned}
$$

## Depends on

- [Rényi divergence](../renyi-divergences/def-renyi.md)

## Lean

Formalized as [`ProbabilityTheory.chernoffDiv`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.chernoffDiv).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/chernoff.tex, line 3](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/chernoff.tex#L3)
