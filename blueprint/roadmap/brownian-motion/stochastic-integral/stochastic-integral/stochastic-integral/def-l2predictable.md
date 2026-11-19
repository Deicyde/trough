---
declaration: definition
origin: cited
lean: ProbabilityTheory.L2Predictable
statement: formalized
---

# L2 space of predictable processes

Let $\mu$ be a measure on $T$ and $P$ a measure on $\Omega$. We denote by $L^2(\mu, P)$ the space $L^2(T \times \Omega, \mathcal{P}, \mu \times P)$, in which $\mathcal{P}$ is the predictable $\sigma$-algebra, and the measure $\mu \times P$ is the restriction of the product measure on $\mathcal{B}(T) \otimes \mathcal{F}$ to $\mathcal{P}$ .

## Depends on

- [Filtration.predictable_le_prod](lem-filtration-predictable-le-prod.md)

## Lean

Formalized as [`ProbabilityTheory.L2Predictable`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.L2Predictable).

## Sources

- [Brownian motion blueprint: chapters/stochastic_integral.tex, line 37](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/stochastic_integral.tex#L37)
