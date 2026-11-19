---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.stdGaussian
---

# Standard Gaussian measure

Let $(e_1, \ldots, e_d)$ be an orthonormal basis of $E$ and let $\mu$ be the standard Gaussian measure on $\mathbb{R}$. The standard Gaussian measure on $E$ is the pushforward measure of the product measure $\mu \times \ldots \times \mu$ by the map $x \mapsto \sum_{i=1}^d x_i \cdot e_i$.

## Depends on

- [Gaussian law](../../../../../mathlib/overview/probability-theory/random-variables-and-their-laws/gaussian-law.md)

## Lean

Formalized as [`ProbabilityTheory.stdGaussian`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.stdGaussian).

## Sources

- [Brownian motion blueprint: chapters/gaussian.tex, line 304](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/gaussian.tex#L304)
