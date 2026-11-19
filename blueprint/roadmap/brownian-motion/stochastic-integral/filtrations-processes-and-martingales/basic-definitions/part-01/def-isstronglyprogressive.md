---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.IsStronglyProgressive
---

# Progressively measurable

A stochastic process $X$ is said to be progressively measurable with respect to a filtration $\mathcal{F}$ if at each point in time $i$, $X$ restricted to $(-\infty, i] \times \Omega$ is measurable with respect to the product $\sigma$-algebra where the $\sigma$-algebra used for $\Omega$ is $\mathcal{F}_i$.

## Depends on

- [Filtration](def-filtration.md)

## Lean

Formalized as [`MeasureTheory.IsStronglyProgressive`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.IsStronglyProgressive).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 24](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L24)
