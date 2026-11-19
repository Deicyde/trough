---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.IsStable
---

# stable

A class of stochastic processes $P$ is stable if whenever $X$ is in $P$, then for any stopping time $\tau$, the process $X^{\tau}\mathbb{I}_{\tau > 0}$ is also in $P$.

## Depends on

- [Local property](def-locally.md)

## Lean

Formalized as [`ProbabilityTheory.IsStable`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsStable).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 132](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L132)
