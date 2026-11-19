---
declaration: definition
origin: cited
lean: ProbabilityTheory.gaussianProjectiveFamily
statement: formalized
---

# Projective family of the Brownian motion

For $I = \{t_1, \ldots, t_n\}$ a finite subset of $\mathbb{R}_+$, let $P^B_I$ be the multivariate Gaussian measure on $\mathbb{R}^n$ with mean $0$ and covariance matrix $C_{ij} = \min(t_i, t_j)$ for $1 \leq i,j \leq n$. We call the family of measures $P^B_I$ the *projective family of the Brownian motion*.

## Depends on

- [Multivariate Gaussian](../../gaussian-distributions/gaussian-measures/part-02/def-multivariategaussian.md)
- [posSemidef_brownianCov](lem-possemidef-browniancov.md)

## Lean

Formalized as [`ProbabilityTheory.gaussianProjectiveFamily`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.gaussianProjectiveFamily).

## Sources

- [Brownian motion blueprint: chapters/projective_family.tex, line 114](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/projective_family.tex#L114)
