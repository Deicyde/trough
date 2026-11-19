---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.multivariateGaussian
---

# Multivariate Gaussian

The multivariate Gaussian measure on $\mathbb{R}^d$ with mean $m \in \mathbb{R}^d$ and covariance matrix $\Sigma \in \mathbb{R}^{d \times d}$, with $\Sigma$ positive semidefinite, is the pushforward measure of the standard Gaussian measure on $\mathbb{R}^d$ by the map $x \mapsto m + \Sigma^{1/2} x$. We denote this measure by $\mathcal{N}(m, \Sigma)$.

## Depends on

- [Standard Gaussian measure](../part-01/def-stdgaussian.md)

## Lean

Formalized as [`ProbabilityTheory.multivariateGaussian`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.multivariateGaussian).

## Sources

- [Brownian motion blueprint: chapters/gaussian.tex, line 423](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/gaussian.tex#L423)
